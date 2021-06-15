#Requirements
import requests
from time import sleep, time
from datetime import datetime
import pandas as pd

#Twitter credential.
import AppCred


# Create own TwitterAPI class to ease snowballing for everyone.

# Correspondance with Twitter API lead developer saying that rate limit is best done using the http-header instead of calling
# the rate limit endpoint: https://twittercommunity.com/t/rate-limit-status-does-not-update/155138
# Might be a good note for the SDS-basecamp, where we learn to use the endpoint.

# had to rewrite alot of code so the TwitterAPI class' rate limit error handling is a bit messy

#Define error type to be used in TwitterAPI-class.
class RateLimitError(Exception):
    def __init__(self, Remaining = None, Limit = None, ResetTime = None,*args, **kwargs):
        self.Remaining = ResetTime
        self.Limit = ResetTime
        self.ResetTime = ResetTime 


class TwitterAPI():
    '''Twitter API: A class to shuffle through a list of bearer token to circumvent twitter api rate limits.
    Bearer tokens should be passed as a list '''
        
    def __init__(self, 
                 bearer_tokens : 'list of bearer tokens for twitter api (authontication procedure)'
                 ):
        
        if type(bearer_tokens) == list:
            self.tokens = bearer_tokens
        elif type(bearer_tokens) == str:
            self.tokens = [bearer_tokens]
        
        self.headers = [{"Authorization": f"Bearer {token}"} for token in self.tokens]
        self._current_header_in_use = 0
        self._wait_time = [0 for token in self.tokens] #To contain epoch time to all api calls or 0 if they all are available 

    ################################# REQUEST TWITTER API USING "REQUESTS" LIBRARY #################################

    def connect_to_endpoint(self, url, headers = None):
        if headers == None: headers = self.headers[self._current_header_in_use]
        response = requests.request("GET", url, headers = headers)
        if response.status_code == 429:
            raise RateLimitError(ResetTime = response.headers['x-rate-limit-reset'])
        elif response.status_code != 200:
            raise Exception(
                f"""Requested url: {url},
                    Request returned an error: {response.status_code} {response.text},
                    """)
        return response.json()
    
    ################################## ERROR HANDLING #############################################

    #Find rate limits that has been used #not used any more
    def rate_limit_use(self, header = None):
        if header == None: header = self.headers[self._current_header_in_use]
        header = header
        path = "https://api.twitter.com/1.1/application/rate_limit_status.json?"
        rate_limit = self.connect_to_endpoint(path, header)
        rate_limits_used = {}
        for x in rate_limit['resources']:
            for y in rate_limit['resources'][x]:
                if rate_limit['resources'][x][y]['limit'] != rate_limit['resources'][x][y]['remaining']:
                    rate_limits_used.update({y : rate_limit['resources'][x][y]})
        return rate_limits_used

    #Find the rate limits that are 0  #not used any more
    def rate_limit_exhausted(self, header = None):
        d = self.rate_limit_use(header)
        rate_limit_exhausted = {k : d[k] for k in d if d[k]['remaining'] == 0}
        return rate_limit_exhausted

    #Find the waiting time until all rate limits has been recovered  #not used any more
    def rate_limit_recovery_time_max(self, header = None):
        dic = self.rate_limit_exhausted(header)
        if bool(dic): 
            epoch_time_max = max([dic[x]['reset'] for x in dic])
        else:
            epoch_time_max = 0
        return epoch_time_max

    ######## HELPER FUNCTION #########
    def rate_limit_sleep(self, header=None):
        timestamp_ready = min(self._wait_time)
        seconds_to_wait, minutes_to_wait = timestamp_ready - time(), round((timestamp_ready - time())/60,2)
        time_to_resume = datetime.fromtimestamp(timestamp_ready).strftime("%d/%m/%Y %H:%M:%S")

        print(f"""
        Rate in question: {self.rate_limit_exhausted(header)} 
        Waiting {minutes_to_wait} minutes before retrying ({time_to_resume})
        """)
        sleep(seconds_to_wait)

    
    ################# LOOP ERROR HANDLING AND API REQUEST OVER BEARER TOKEN LIST #####################

    def update_wait_times(self, ResetTime):
        
        self._wait_time[self._current_header_in_use] = float(ResetTime)
        self._wait_time = [0 if 0 > (x - time()) else x for x in self._wait_time ]

    def connect_to_endpoint_loop(self, url):     
        while True:
            try: 
                json_response = self.connect_to_endpoint(url, headers = self.headers[self._current_header_in_use])
                break
            except RateLimitError as r:
                self.update_wait_times(r.ResetTime)
                print(f'RateLimitError, trying to change header.')
                if 0 in self._wait_time:
                    self._current_header_in_use = self._wait_time.index(0)
                    print(f'Succesfull. Changing to bearer token with index {self._current_header_in_use}')
                    continue
                else:
                    print('Looped through all available bearer tokens - rate limit error is encountered.')
                    self.rate_limit_sleep()
                    continue
        return json_response

    ##CONNECT TO ENDPOINT LOOP OVER PAGES OF RESULTS FROM CONSTRUCTED URLS  

    def connect_to_endpoint_pagenation(self, url_input, max_results = 1000):
    
        #Input and output
        tokens = ['next_token','previous_token']
        url = url_input
        json_response_gross = []
        
        i = 1 #enumerator
        
        while True:    
            json_response = self.connect_to_endpoint_loop(url)

            #IF THERE ARE PAGEING TOKENS:
        
            if any(t in json_response['meta'] for t in tokens):
                try:
                    json_response_gross.extend(json_response['data'])
                except:
                    json_response_gross.extend(json_response)
                print(f'GET request succesfull ({i}/x): {url}')            
                if 'next_token' not in json_response['meta']:
                    break
                else:
                    token = json_response['meta']['next_token']
                    url = f"{url_input}&pagination_token={token}"
                    i += 1
            #IF THERE ARE NO NEXT/PREVIOUS TOKENS RESULTS ARE ON ONE PAGE AND THE WHILE LOOP IS BROKEN.
            else:
                try:
                    json_response_gross.extend(json_response['data'])
                except:
                    json_response_gross.extend(json_response)
                print(f'GET request succesfull : {url}')
                break

        return json_response_gross
  
    ################################## URL CONSTRUCTORS  ##############################################
  
    #GET metadata on specific user from either user name or user id
    def url_lookup_user(self, usernames = None, ids = None):
        if ids != None: 
            id_or_user_name = f"{ids}?"
        else:
            id_or_user_name = f"by?usernames={usernames}"    
        
        user_fields = ""
        url = f"https://api.twitter.com/2/users/{id_or_user_name}&{user_fields}"
        return url

    #GET data on users following user id in question
    def url_get_following(self, user_id):
        # find all metadata (possible userfields, expansions etc.) that can be returned here: 
        # https://developer.twitter.com/en/docs/twitter-api/users/follows/api-reference/get-users-id-following
        user_fields = "user.fields=public_metrics,location,description,verified,created_at"
        return f"https://api.twitter.com/2/users/{user_id}/following?max_results=1000&{user_fields}"


    #GET data on a user's followers 
    def url_get_followers(self, user_id):
        # find all metadata (possible userfields, expansions etc.) that can be returned here: 
        # https://developer.twitter.com/en/docs/twitter-api/users/follows/api-reference/get-users-id-following
        user_fields = "user.fields=public_metrics,location,description,verified,created_at"
        return f"https://api.twitter.com/2/users/{user_id}/followers?max_results=1000&{user_fields}"



    ####################################################################################################
    ################################### PROJECT SPECIFIC METHODS #######################################
    ####################################################################################################

    ########## RETURNS A DICTIONARY WITH THE PEOPLE THAT FOLLOWS A USER

    def find_user_network(self, username, method = 'following' , max_results = 1000):        
        
        #find user 
        url_user_lookup = self.url_lookup_user(username)
        user = self.connect_to_endpoint(url_user_lookup)
        user_id = user['data'][0]['id']

        #construct relevant API        
        if method == 'following':
            url_call = self.url_get_following(user_id)
        elif method == 'followers':
            url_call = self.url_get_followers(user_id)

        return self.connect_to_endpoint_pagenation(url_call, max_results)

    ####### SNOWBALL SAMPLING ########

    def snowball(self, seeds: list, depth, regex_pattern_filter = '(?i)Wind(?!ow)'):
        #initiate variables
        all_balls_list = []
        all_results = []
        current_ball_results = []
        
        #first ball is the seed, which is NOT filtered with regex pattern.
        current_ball = seeds
        
        for depth_level in range(depth + 1):      
            
            for v,x in enumerate(current_ball):
                print(f'{v+1} out of {len(current_ball)} users. Username: {x}')
                try:
                    json_response_list = self.find_user_network(x, max_results=1000)
                    for y in json_response_list:
                        y['followed_by'] = x
                        y['ball_depth'] = depth_level
                        y['regex_pattern_filter_to_create_ball'] = regex_pattern_filter
                except:
                    json_response_list = []

                #store results
                current_ball_results.extend(json_response_list)

            #store results
            all_results.extend(current_ball_results)
            #list to contain users that has been scraped
            all_balls_list.extend(current_ball)
            df_to_ball = pd.DataFrame(current_ball_results)
    
            current_ball = list(set(df_to_ball['username'].loc[(df_to_ball['description'].str.contains(regex_pattern_filter)) | 
                                                            (df_to_ball['username'].str.contains(regex_pattern_filter))]))
            current_ball = [x for x in current_ball if x not in all_balls_list]

        return all_results

if __name__ == "__main__":
    api = TwitterAPI(AppCred.BEARER_TOKENS)
    # api.find_following_of_user('windwatchorg')
    results_snowball = api.snowball(['windwatchorg'], 2, regex_pattern_filter = '(?i)Wind(?!ow)')
    df = pd.DataFrame(results_snowball)
    df.to_pickle('data/results') 