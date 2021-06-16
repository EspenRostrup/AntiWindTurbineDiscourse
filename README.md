# Opposition to wind turbines
By Alexander Jorge, Kajsa Rosenblad, Snorre Moltzau and Espen Rostrup

Character count: 60,852 characters.  
We think that the readability is best when using GitHub, so we encourage the user to read the paper at [www.github.com/EspenRostrup/AntiWindTurbineDiscourse/](https://github.com/EspenRostrup/AntiWindTurbineDiscourse/).

### Table of contents
Name indicates responsibility. As a note to the examinators we believe that the effort was equally distributed between group members.

1. [Introduction (Digital Methods)](#introduction) - Collective  
1.1 [Data ethical considerations](#data-ethics) - Collective  
2. [Netnography (Digital Methods)](#netnography) - Espen  
2.1 [Account of practices](#account-of-practice) - Kajsa  
2.2 [Discussion](#22) - Snorre  
3. [Network (Digital Methods)](#network) - Alexander  
3.1 [Selecting the seeds](#31) - Espen  
3.2 [Analysis of the network from the snowball sampling](#32) - Kajsa    
3.3 [Discussion](#33) - Snorre  
4. [Collection and preprocessing of tweets (Digital Methods and ASDSII)](#data-collection) - Alexander  
4.1 [Description of final tweet sample](#final-sample) - Espen  
5. [Content Analysis: Manual coding and semantic networks (Digital Methods)](#content-analysis) - Kajsa    
6. [Topic modelling (ASDSII)](#topic-modelling) - Snorre  
6.1 [hSBM implementation](#hsbm) - Alexander  
6.2 [LDA implementation](#lda) - Espen  
6.3 [Discussion](#asds-discussion) - Kajsa  
7. [Methodological reflections (Digital Methods)](#reflections) - Collective   
7.1 [Summing up: Mapping out anti-wind turbine resistance online](#summing-up) - Collective    
7.2 [Methodological reflections](#reflections) - Collective  
  
[Sources](#sources)  
[Notes](#notes)  
[Appendix](#appendix)  

<a id="introduction"></a>
## 1. Introduction (Digital Methods)
<div class=text-justify>
As the acknowledgment of climate change increases, so does the demand for greener energy sources. Amongst such sources, wind turbines stand out both literally and figuratively. The arguments levelled against wind turbines are many: Fear of a destroyed view; Scepticism towards their energy efficacy; or fears of silent hazards such as microplastic and low-frequency noises. There is a heavy leniency in prior research to focus on local, area specific resistance, often referring to it as a “Not in my backyard” (NIMBY) stance (eg. Hagget, 2008 & Wolsink, 2005). This prominence of local resistance focus is enhanced by the fact that studies often center around specific cases (eg. Baxter et al, 2013) as it facilitates the acquisition of accurate data.

This study addresses a lacuna on the topic of wind turbine opposition by investigating both commonly used online data sources as well as applying a variety of both qualitative and quantitative methods, for the comparisons it allows us to make, but also to draw insights between methods. Our approach is inspired by Munk insofar as it combines qualitative and quantitative methods (2019). Additionally, in the paper by Borch et al. (2020) such methods are applied on this specific topic as they attempt to map out wind-power controversies in Danish Facebook groups.

Firstly, a qualitative netnographic campaign will be conducted in order to gain a broad understanding of the field.This includes an immersion journal, a network analysis and a content analysis. The immersion journal is done both in a more traditional way (inspired by Kozinets, 2019) and with a Miro board, allowing us to pedagogically visualise our discoveries. We will also map the semi-symbolic relations between actors in an analogue network. The quantitative part of this report is conducted on Twitter by scraping tweets from a demarcated population. We will conduct a comparative topic modelling analysis, using both a hierarchical Stochastic Block Model (hSBM) and a Latent Dirichlet Analysis (LDA).The idea is thus to attempt to map the anti wind discourse online as well as conduct a methodological investigation and comparison.


This leads us to ask the following explorative research questions:

- Which topics can be observed from the online anti-wind turbine discourse? 
- On which platforms do which actors participate?
- In which way do the insights from the different qualitative and quantitative methods overlap, and in which way do they differ from each other?

To answer these questions we apply various interconnected digital methods. Our research strategy is outlined in the flow chart in [Figure 1](#methods). The figure appears deterministic even though our process of choosing the relevant methods and applying the methods was more iterative following the ideas of Laura K. Nelson’s Computational Grounded Theory (2017) revisited by Bang Carlsen and Ralund (2020). We constantly balanced finding patterns in the digital traces using both qualitative deep reading and explorative computational tools, which aided our understanding of the roles of methods as such, as well the topic at hand.

<a id="methods"> </a>
#### Figure 1: The flow of digital methods applied in the paper
![methods](https://github.com/EspenRostrup/AntiWindTurbineDiscourse/blob/main/visualisations/method-map.svg)  
_Source: Author's own illustration_

Using the logic of the double-funnel process as outlined in Kozinets (2019) we approached the research question using netnography, noting down our findings in an immersion journal ([Appendix 4](#appendix-4)). Thereafter we focused our netnography on Twitter profiles globally and Facebook groups in Scandinavia investigating how the relevant actors behaved online. We openly coded the netnography findings from the Facebook groups across the countries to identify emerging patterns in discourse (see [Appendix 4](#appendix-4) for the codes). The twitter netnography was used to identify relevant seeds for automatically collecting a network of relevant actors using snowball sampling. A part of this actor network was scrutinised further by collecting samples of their tweets and analysing them using both computational and manual methods. We sum up our findings by discussing a manually constructed symbolic network. 

<a id="data-ethics"></a>
### 1.1 Data ethical considerations

In the public curation of the data and in the corpus construction some ethical issues were considered. A balancing of transparency and anonymity must be maintained and considered throughout (see Herschel & Miori (2017) for an elaboration on data ethics). The seeds used for the Twitter dataset were not anonymous and as such, indirectly, neither are the accounts sampled from them, which we report in this paper below. We have chosen to only include specific account names in this report in the visualisation of the network. These data points are not hydrated though and we only scrutinize twitter profiles that are either of a public or organisational character. 
Other ethical considerations we have made include preventing the coder (when coding manual tweets) from seeing any information besides the text itself, including personal information about the account. Similar considerations were taken in the curation of the Facebook dataset, which consisted of data from wind turbine resistance groups. No individuals have been mentioned at all and the groups mentioned were big enough for anything extracted to not be traceable. Our immersion journal contains more private information and is not made public for that reason.
 We structured our files from our netnography which will be outlined below in a single online repository (as suggested by Kozinets (2019)). This repository and all our shared work was stored on a OneDrive Sharepoint in accordance with the data guidelines of the University of Copenhagen and to comply with the general data protection regulation (GDPR).

<a id="netnography"></a>
## 2. Netnography (Digital Methods)
<a id="account-of-practice"></a>
### 2.1 Account of practice

In the initial phase of the netnography the scope included Facebook, Twitter and a wider online search including blogs, forums and informational websites. We decided to consider the anti wind turbine discourse in three countries, namely Denmark, Norway, and Sweden. The results of our netnographic campaign is noted in the structured version of the two different types of immersion journals we kept which is attached in [Appendix 4](#appendix-4). A screenshot of the two types of  are displayed in respectively [Figure 2](#Figure-2) and [Figure 3](#Figure-3). 

In terms of curating and writing data we use a simplified version of Kozinet’s immersion journal. We do not seek an explanation to what Kozinet terms ‘cultural causality’; instead the aim is reflecting on what we find in a systematic way (2019, p. 133). Still, we also find Kozinets four data operations: (1) reconnoitering, (2) recording, (3) researching, and (4) reflecting to be useful for our approach. For our data operations we did open coding of the content with links, dates of collection and inferred a code for later use in manual coding of other material. It was an interactive, collaborative process that led to a structured dataset with information about search ‘tag’ histories, countries, type and collection methods for each query or datapoint we found.

#### Figure 2: The structured Immersion Journal
<a id="Figure-2"> </a>
![Figure 2](https://i.imgur.com/FSpNOIq.png)  
_Source: [Appendix 4b](#appendix-4)_

Furthermore our way of operationalising reconnoitering was through Miro, an online visual collaboration platform for teamwork, and this became an important part of our internal exchange of information sharing our netnographic experience beyond the spreadsheets. In this sense we were mapping our datascape to create critical notes. Recording various aspects of screenshots was done both in the structured immersion journal and on the Miro-board journal. Researcher notes were made as comments in the immersion journal. In this manner we have mapped a multitude of processes that occurred during our research. This visual and reflexive approach later became an integral part of our scouting, selecting and sharing for a focused netnographic exploration as well as rendering key elements of our research (Kozinets, 2019).

#### Figure 3: Screenshot of Miro-board detailing various processes related to our netnography
<a id="Figure-3"> </a>
![Figure 3](https://i.imgur.com/LJf5VLM.png)
_Source: [Appendix 4a](#appendix-4)_

Our emotional engagement strategy within the ethnographic campaign was to join public Facebook groups to get a steady stream of related content from the data sites (Kozinets, 2019. In addition to this a two-hour video interview was conducted with a moderator from one of the largest Facebook groups following an open format, accompanied by an interview guide with ‘broad questions’ as suggested by Kozinets (2019) ([Appendix 3](#appendix-3), Interview Guide).

Most Facebook groups were open groups, although some were closed and permission to join was asked (and granted in every case). Closed groups with less than 100 members were excluded. By simply observing the in-group communication a lot of insights were gained that both facilitated the future coding as well as validated Facebook as a legitimate source of data.


<a id="22"></a>
### 2.2 Discussion

Comparing the countries we find that the largest wind turbine resistance movement online appeared to be in Norway on Facebook. The largest resistance group we found was called _Motvind_, and the group has a sister group active in Sweden that goes by the same name (Motvind Sweden) as well as subgroups such as ‘Motvind Norrmogen’<sup>[1](#f1)</sup> In addition to this, Motvind runs a large group on Facebook called: “Nei til naturødeleggende vindkraft i Norge”. Observations from the immersion journal ([Appendix 4](#appendix-4)) show different creative ways of protesting. One example of resistance present across countries is the lighting of bonfires on mountain tops in both Norway and Sweden. 

Facebook allows for closed and public groups where people easily can find people that share opinions or general interests. This allows for an arguably more local discussion around certain topics than on for example Twitter where such groups do not exist. For instance the danish anti wind turbine group “NEJ TAK til vindmøller i Udklit Fjerritslev” [No thank you to wind turbines in Udklit Fjerritslev] is a public group that a Facebook user easily can find searching for e.g. ”Udklit Fjerritslev” or “vindmøller” (wind turbines). 

Furthermore, it became clear from our netnographic campaign that the scandinavian anti-wind turbine actors are not as active on Twitter as they are on Facebook. For example, on the 5th of June 2021, the group ‘Motvind Norge’ (Motvind Norway) had more than 50,000 members on Facebook while ‘Motvind Norge’ has roughly 400 followers on Twitter.

However, there are many more general anti-wind turbine Twitter users internationally (e.g. @StopTheseThings, @WindWatchOrg, @no2wind, @alabamawind) which we also discovered during our netnographic campaign. These accounts follow each other to share their opposition towards wind turbines across borders, and are actively sharing their opinions on Twitter. 

These considerations in regards to platform differences are important for the conclusions and research questions that can meaningfully be posed when using digital platforms as the object of study, as outlined in Venturini et al. (2018). We started off wanting to discuss arguments against wind turbines in Scandinavia, which can be found on Facebook, but the actors who would be expressing these arguments are not as present on Twitter as they are on Facebook. Using Twitter as the platform from which to draw conclusions should have the platform specificities in mind. 

Due to the lack of Twitter activity within the Scandinavian anti-wind turbine movement, we decided to change our focus to a global focus. With the insights from the immersion into the Scandinavian movement on Facebook we will commence building a Twitter data set that contains anti-wind turbine actors and their discourse in English. 

<a id="network"></a>
## 3. Network Analysis (Digital Methods)

In this section we describe and motivate our data sampling strategy as it pertains to Twitter. Our goal is to construct a network of users that is representative of the anti wind turbine resistance movement on Twitter, which we will analyse further by extracting their tweets. We create this network as a “following” network of a central actor within global wind turbine resistance, by snowballing on the profiles that the “seed” (the central actor) follows. Using graph tools and theory we find that the resulting network distinguishes two groups of actors; a group of actors advocating towards more wind energy and a group of actors advocating against wind energy. For the purpose of investigating the anti wind turbine discourse we argue that it is sufficient to only look at the followers of the seed in order to map out key topics in the anti-wind turbine discourse which narrows our network of actors dramatically.

We rely on snowballing to construct the following-network. This approach to data collection in mapping out wind turbine discourse is inspired by Borch et al. (2020), where all available hyperlinks on three specific anti and pro danish wind energy sites were collected through snowball sampling. However, it is worth noting that, contrary to our automatic snowballing, Munk performed this manually.

We deploy our snowball sampling strategy in the following 2-step approach:

1. We find the profiles that a (set of) seed(s) follows 
2. We only select users who have the term “wind”<sup>[2](#f2)</sup> in either their twitter profile description or in their profile’s username (twitter handle) and use these twitter profiles as new seeds. 

This leads to an iterative 2-step process, repeated four times yielding a network consisting of 974,275 edges and 557,214 nodes out of which only 1,034 are used as seeds. In a later stage we will prune this network.
<a id="31"></a>
### 3.1 Selecting the seeds

The onset of this snowball sampling approach is the seed(s). We collated our netnography, mapping out important actors and filtering out non-English seeds. Later, we checked whether the actors were on twitter. We chose to filter out accounts with less than a thousand followers due to ethical considerations since we planned to delve deep into the followers and followings of the seed. We have displayed the list of potential seeds below in [Table 1](#table1). 


<a id="table1"> </a>
#### Table 1: List of seeds
| Country   | Twitter Name                 | Following | Followers |
| --------- | ---------------------------- | --------- | --------- |
| Australia | Stop These Things            | 27,100    | 24,900    |
| US/Global | National Wind Watch          | 528       | 1,942     |
| Ireland   | windawareireland             | 791       | 1,005     |
| Canada    | Wind Concerns Ontario        | 882       | 1,323     |
| US        | Bill Heller                  | 1,690     | 2,365     |
| Scotland  | S.W.A.T                      | 1,246     | 2,702     |
| Scotland  | Wind\_Energy's\_Absurd       | 401       | 1,604     |
| US        | Barbara Durkin               | 4,061     | 5,225     |
| Ireland   | Gweebarra Conservation Group | 2,810     | 1,516     |  

_Source: [Appendix 4b](#appendix-4)_

We found that an iterative approach to map out the network would be beneficial; starting with one seed and expanding with other seeds after evaluating the resulting network by exploring parts of the twitter users in the network. We decided to use the National Wind Watch as a preliminary seed since the organisation had appeared frequently in our initial netnography and appeared to have a geographical spread of users that the profile followed (see figure 4). We quickly found that all the seeds listed in [Table 1](#table1) were included in the resulting network, which, due to its size and apparent diversity, was deemed to be fit for our analysis.

<a id="32"></a>
### 3.2 Analysis of the network from the snowball sampling

The resulting seeds of the first of our snowball sampling iterations are displayed in [Figure 4a](#figure-4a). The figure displays the 238 profiles and their twitter handles. We have chosen not to filter out the names of the profiles since these profile names are easily obtained by entering the followings of the National Wind Watch. 


#### Figure 4a: The profiles that The National Wind Watch follows filtered by the word “wind”

<a id="figure-4a"> </a>
![figure-4a](https://github.com/EspenRostrup/AntiWindTurbineDiscourse/blob/main/visualisations/1st_degree_network.svg)  
_Source: Data collection as done with code in [Appendix 1a](appendix-1) and pruning code in [Appendix 1b](appendix-1)_

Expanding the network by iterating three more times using these new users as seeds yields a messier set of actors. In order to meaningfully analyse the network we chose to remove users that were followed by less than three users in the entire (non-filtered) network. Furthermore, we decided to only look at (potential) seeds in the network i.e. profiles that has the word wind in either their twitter description or twitter The resulting network has 3,873 nodes, 56,502 edges and is displayed in [Figure 4b](#Figure-4b). The network is constructed in the graph software Gephi and a ForceAtlas2 algorithm is deployed to spatialise the nodes and edges (Jacomy, et al., 2014). <sup>[3](#f3)</sup>


#### Figure 4b: Network of twitter users related to "wind"

<a id="Figure-4b"> </a>
![Figure 4b](https://github.com/EspenRostrup/AntiWindTurbineDiscourse/blob/main/visualisations/full_network_indegree_gt_2_only_wind.svg)  
_Source: Data collection as done with code in [Appendix 1a](appendix-1) and pruning code in [Appendix 1b](appendix-1)_

The 1st degree users are the users from [Figure 4a](#figure-4a). Note that the 3rd degree users do not have any outgoing edges i.e. they do not follow anyone in this network. Since we completed four iterations of our data collection process (outlined in the beginning of this section) the identified would-be seeds from the fourth iteration are never actually used as seeds, which is why the network is not complete. 

By analysing the constellations in the network by both eyeballing the clustered nodes in the network, the clustering is a feature of the ForceAtlas2, and also by calculating the modularity (Blondel et al., 2008) with different resolutions (Lambiotte et al., 2009) we are able to detect some meaningful communities in our network.<sup>[4](#f4)</sup> We have marked smaller communities with stippled lines and coloured the two large communities in red and green. 

First, there are two communities that have nothing to do with wind energy, namely the “Lake Windermere” and “Windsor” communities. We have chosen to show these communities in this report since it reveals the vulnerability of the “filter by word” approach we have taken to indicate whether a twitter profile is relevant for the wind turbine discourse.<sup>[5](#f1)</sup>

Second, there are two large communities that in general contain respectively proponents of and opponents to wind energy (or wind turbines). We find the accuracy of the clustering noteworthy; assortative mixing with few nodes bridging the communities seems to be a good way to describe the network structure. To highlight this structure we show a network in [Figure 4c](#Figure-4c) of actors with more than 70 followers within the entire network. 

Third, within the proponent and opponent clusters there are language clusters, since the word “wind” means the same in both Dutch and German. We will filter out non-anglophone accounts by using a pre-trained classifier to identify the primary language of a twitter account (and the language of a tweet) which we will elaborate on in the section on [collection and preprocessing of tweets](#data-collection).

#### Figure 4c: Subsample of the wind turbine network of twitter users (node indegree greater than 70)

<a id="Figure-4c"> </a>
![Figure 4c](https://github.com/EspenRostrup/AntiWindTurbineDiscourse/blob/main/visualisations/full_network_indegree_gt_70_only_wind.svg)  
_Source: Data collection as done with code in [Appendix 1a](appendix-1) and pruning code in [Appendix 1b](appendix-1)_

<a id="33"></a>
### 3.3 Discussion

Our paper’s goal is to map and understand the discourse of the opposition to wind turbines on social media, as well as explore and combine different qualitative and quantitative methodological approaches. With this goal in mind we have created a follower network to depict relevant actors in the wind turbine debate on twitter. Since Twitter is a large social media platform it would be impossible for us to exhaust the entirety of twitter users that are relevant. However, seeing how the network develops using the iterative snowball approach we argue that we have mapped out at least a significant part of the opposition to wind turbines. This argument is made on the basis of “3rd” degree users being primarily either unrelated to wind turbine discourse or being wind turbine proponents. We could be concerned that the wind turbine opposition is divided on twitter in multiple disjoint partitions and that the community displayed in [Figure 4b](#Figure-4b) is just one of these partitions. We do not believe that to be the case since our list of possible seeds in table 1 above was collected before constructing the network across independent researchers and they are all included in the network. 

Due to time constraints we are only exploring the 1st degree users tweets from [Figure 4a](#figure-4a), which are all exclusively connected to the anti wind turbine community as seen in [Figure 4b](#Figure-4b). In our further discovery of the network. A more rigorous approach would have been to include the 2nd degree users that also were related to the wind turbine opposition community or at least to check whether tweets from this subpopulation 2nd degree users are different in nature to the tweets by the 1st degree users. Furthermore the geographical spread of the 1st degree users is wide enough for us to be sure that it is not a local sub-population of opposition to wind turbines. The geographical spread can be seen in [Figure 5](Figure-5). It is an interactive figure and can be accessed at [rostrup.nu/interactive_twitter_user_map.html](http://rostrup.nu/interactive_twitter_user_map.html).

#### Figure 5: Geographical location of twitter users in the network presented in [Figure 4b](Figure-4b)  
<a id="Figure-5"> </a>
![Figure-5](https://i.imgur.com/PPacdlC.png)
_Note: The geographical location is obtained using the [Google Maps Geocoding](https://developers.google.com/maps/documentation/geocoding/overview) API. The location of a user is taken from the user's profile description. A lot of users have non-geographical locations (or no location at all) in their description which the API might pass as a location. We have only included results where the location is of either the type “political” (which contains countries, cities, administrative regions and more) or “natural_feature”. See [the API documentation](https://developers.google.com/maps/documentation/places/web-service/supported_types) for more specific information about the types. The interactive figure can be seen [here](http://rostrup.nu/interactive_twitter_user_map.html).
Source: Code in [Appendix 1b](appendix-1)_

<a id='data-collection'></a>
## 4. Collection and preprocessing of tweets (Digital Methods and ASDSII)  

Kozinets’ five S’s on how to collect social media data (_Simplifying_ your RQ to a consistent set of search terms, _searching_ for terms on different sites and platforms, _scouting_ and filtering where to retrieve data from, _selecting_ data sets and data, and lastly, _saving_ that data (2019)) quickly gave us some difficulties, since we had a hard time identifying search terms or hashtags that were used by people to signal that they were discussing wind turbine resistance. For example #wind also returned tweets about the weather. Concerns about the precision and recall of using search terms were raised, since we risked getting a lot of noise if we focused too much on collecting tweets based on terms or hashtags that are also used to discuss other topics. Instead, we decided to focus on the users that are also part of our actor network. Caliandro writes about _crowds_ as affective gatherings of people that express themselves in cohesion (2017). He also discusses the process of self-categorisation and representation that occurs on online platforms. This concept seemed useful to us, as we decided to collect the tweets from the 1st degree of our network outlined above. Making it explicit that your account is dedicated to “wind” in some way is a form of self-representation, and a signal that you strive to reach out to a demarcated crowd of twitter users. Limiting our sample this way, we also hoped to get as many true positive tweets as possible, since it is likely that these accounts tweet more about wind turbine resistance than accounts that do not use the term “wind” to categorise themselves. However, this sample of users might also be too demarcated, and we risk having considerable false negatives as well, where users who tweet a lot about wind turbine resistance are not included in our final sample. 

Pre-processing is an important step of any project dealing with text data, as the steps followed have a real impact on the results of subsequent analyses (Denny & Spirling, 2018). Following the pre-processing steps outlined in the aforementioned paper, we lowercase our tweets, remove usernames, urls, digits and punctuation. The network of 1st degree users are not all tweeters tweeting in english. To simplify the content analysis we only proceed to handle english tweets.

We identify the tweet languages using the _FastText _text classification tool (Joulin et al., 2016a, 2016b) which, according to Toftrup et al (2021), is the current standard for language identification (together with _langid.py_ tool). We use a pretrained model to identify the languages of the tweets that are openly available from the FastText webpage (FastText, 2021) without any finetuning or retraining due to the lack of language identified tweets that could help tune the model. The model is pretrained on data from Wikipedia, Tatoeba and SETimes. The model’s output layer contains 176 units; the estimated probabilities of the language of a given input string being one of 176 languages. We classify a tweet as being the language with the largest probability score. We concatenate all the tweets by a user to investigate the user’s primary tweeting languages. Some of the twitter users are bilingual with English as their second or first language. To handle this, we only classify a tweet as English if it is

1. a tweet by an author that is classified as English and
2. the tweet itself is classified as English or if the largest probability score of the language estimated is less than 0.5. 

The parameter choice of 0.5 was a result of a manual inspection of the probability scores of random samples of tweets. 

Using only tweets classified as English we proceed to remove stop words and lemmatise the tweets using the NLTK WordNetLemmatiszer ("NLTK 3.6.2 documentation", 2021). We opt for lemmatisation in favour of stemming because it has been shown that reducing a word to its dictionary form, or a _lemma_, produces more precise and useful results. (Balakrishnan & Ethel, 2014)

We tokenise the tweets to lists of single words (unigrams) as a consequence of the bag-of-word approach we are going to take when estimating our topic model. To preserve the context and meaning of neighboring words in this bag-of-words approach, we include bi-grams in our corpus (or “bag” so to speak). For example, the words “wind” and “farm” seen next to each other in a sentence means something different than these two words seen separately. By creating bi-grams, and combining these with the original unigrams, we end up analysing the words “wind”, “farm” as well as “wind_farm”, which takes the immediate context of the words into account (Denny & Spirling, 2018). 

We choose to remove the least frequent words from the corpus, which we operationalise as words that occur less than five times in the whole corpus. Since we are interested in patterns across our corpus of tweets, words that occur very infrequently will not aid our interpretations. In addition, removing words has the practical utility of reducing the size of our vocabulary, which aids further processing.

<a id='final-sample'></a>
### 4.1 Description of final tweet sample 

We thus ended up collecting a bounded, topic- and user-restricted non-probability sample of 250 000 tweets from 238 users (Rafail, 2018).

From these tweets, we drew a stratified random sample of English language tweets. We stratified the random sampling to ensure that we did not accidentally get a random sample with tweets from only a few, very active users. After removing empty tweets, which were present as a consequence of the pre-processing, the final sample we used in for our content analysis and topic models consisted of 48,059 tweets, tweeted by 172 users. In the topic model section we will use two datasets based on the 48,059 tweets: an aggregated dataset, where tweets have been concatenated on a user level, resulting in a corpus of 172 documents and an unaggregated sample where the individual tweets are the documents.

In the non-aggregated sample the average number of tokens per document and tweet is 16.91 including both unigrams and bigrams and the average number of tweets per user is 279.38. In the aggregated sample, this average is 4,725.71. In Figure 6 we have plotted the most frequent tokens in our dataset. Zipf’s law, the inverse relationship between the rank of a word by frequency and the frequency of the word seems to hold in the way our text corpus is generated. This is in line with Gerlach et al.’s (2018) argument of the document generating process in general is closer to following a Zipfian distribution rather than the Dirichlet distribution. The implications of this argument will be elaborated below.


#### Figure 6: Tokens that appears more than a 1,000 times in our data set

<a id="Figure 6"> </a>
![](https://i.imgur.com/AMdFdOv.png)  
_Source: Code in [Appendix 1d](#appendix-1)_

<a id="content-analysis"></a>
## 5. Content Analysis 


<a id='51'></a>
### 5.1 Manual coding of tweets

The first step of our immersion into the final sample of tweets was that we conducted a manual coding of the content, where we tried to assign meaningful labels, or codes to the themes we identified in the tweets. The aim was for us to understand the way these actors make sense of their advocacy, and also provide us with a qualitative thematic mapping of this “meta-site” (Airoldi, 2018), which we would later triangulate to our quantitative topic models, as well as to the results of our netnographic campaign. 

Coding as an analytical practice has been criticised for being overly reductionist and at risk of imposing meaning where there is none (Lee & Martin, 2014). A genuine understanding of a phenomena, so the story goes, can not and should not be simplistic or quantifiable. Yet, we agree with Lee and Martin’s view, that to be able to approach a science of culture, a certain degree of labelling and simplification is needed, in the same way a map is a simplified representation of the physical space. 

Again following Kozinets, our content analysis of the tweets consisted of _collating_ the tweets, _coding_ them with meaningful labels, a subsequent _combining_ of labels, _counting_ instances and _charting _or visualisation of the results. We started by openly coding 15 unique tweets and 15 common tweets. The approach mimicked that of the open coding of the immersion journal. However, we were more immersed into the netnographic field at this stage of the analytic process, which likely influenced the way we coded the tweets. As researchers, we are inevitably bringing our experiences and knowledge gained from previous stages of the analysis into the process, and this could have resulted in us seeing themes and topics that were not truly manifest in the tweets, simply because we had a hunch of what the tweet or the actor tweeting was implying. This is why, at this stage, we coded the same tweets, to enable discussions about what kind of themes we saw in which tweets. 

Once we coded the tweets, we discussed our findings. A lot of themes were also present in our immersion journal, but we also identified some new ones, for example the mentioning of legal processes. We coded the tweets in quite a similar way, and the discussion about the themes in the tweets helped us gain a common understanding of them. 

The codes from the twitter sample were combined with the codes from the immersion journal, to create a final codebook (see [appendix 5](#appendix-5)). The codebook included a code, a description of the code, an example tweet, instructions on how to code the tweet (mostly binary categories of the theme being present or not), and a hypernym clustering the codes into wider themes. In addition, a coding scheme was created using Google Forms, to simplify the coding of tweets. The first code in the scheme filtered out whether the tweet was relevant or not, which in our case meant that the tweet was about wind power. At the end of the coding scheme there was an option to leave a comment on any difficulties or uncertainties that came up while coding the tweets. 

To ensure that everyone agreed on how to code the final codes, we coded a sample of 20 tweets together. This made us realise certain codes required further clarification, and allowed us to adapt both the codebook and the scheme before commencing the actual coding process. We did not calculate inter-coder reliability, but when we were qualitatively satisfied with our agreement, we proceeded to code tweets independently.

Our final coding consisted of a subset of 250 random tweets out of which 49.6% were coded as relevant (N = 124), 9.6% were unclear, and the remaining tweets were not relevant. As we strived to get a sample with as many true positive tweets as possible, it appears we also got a lot of false positives, resulting in a precision issue which influences the future claims we can make about our data. 

The uncertainties of coding mostly pertained to the lack of context. As an example: 

_“I wouldn't want to live beside them, but who would?”_ 

This tweet could be about wind turbines, but it could also be about something else. In these cases, we refrained from coding the tweet as relevant, since we did not wish to over-analyse our content.

[Figure 7](#Figure-7) displays the count of how many times each code occurred in the tweets. 

#### Figure 7: Count of code types in the manual coding
<a id="Figure-7"> </a>
![Figure_7](https://i.imgur.com/kDCLd97.png)  
_Note: “cfa” stands for “call for action”
Source: Code in [Appendix 1f](appendix-1)_ 

The mention of a specific geographical area was the most common occurrence, followed by mentioning politics/governance and the wind industry. The referencing of a source was also notably present in the sample. There are some codes, such as the mentioning of wildlife and nature, that we expected to occur more often, but that were largely absent in the sample. 

Differentiating between the tweets that do and do not mention a specific geographic location, notable differences are that the mentioning of legal processes and nature occur more frequently when a location is specified. Not surprisingly, tweets that focus on a geographic area also tend to have a focus on the community, as is evident in [Figure 8.](#Figure-8)

#### Figure 8: Filter on geographic location. (Note: “cfa” stands for “call for action”)

<a id="Figure-8"> </a>
![Figure-8](https://i.imgur.com/CnnYSo4.png)  
_Source: [Appendix 1f](#appendix-1)_

<a id='52'></a>
### 5.2 Semantic Network Analysis
To move deeper into the themes and the content in our tweets, we decided to conduct a semantic network analysis by drawing on studies such as the one produced by Decuypere (2019). In this article Decuypere validates the choice of a visual network when exploring social phenomena such as this study aims to do. In addition, Drieger (2013) provides further argumentation for the value of semantic networks as a means to maintain explorative functionality whilst also bringing the analysis closer to the ground. As the design of this study aims to satisfy both these aspects (exploration and grounding) this seemed like a natural next step of our research.

We randomly sampled 5000 pre-processed tweets. Using the python library networkx, we generated a network graph, which consisted of more than 9000 nodes and 180 000 edges. As a first filter, we decided to only include words in the network that occurred more than 50 times in the sample. This resulted in a vocabulary of more than 100 words. On a first inspection, this seemed to capture a lot of relevant words, but there was still some noise in the data. The semantic network was also still very opaque, and difficult to navigate. Next, we manually inspected the vocabulary and filtered out words that occurred often in the sample, but that did not aid in our thematic interpretation of the tweets as this included words such as “though” and “July”. We also decided to remove the words “wind”, “turbine” and “farm” which we expected to occur a lot in the sample. We also decided to filter the graph to only include edges that had a weight >= 3. The resulting semantic network can be seen below in [Figure 9](Figure-9). The networks were created with Gephi, using the Force Atlas 2 algorithm. 

#### Figure 9: Semantic network with select words
<a id="Figure-9"> </a>
![Figure_9](https://i.imgur.com/aWP0n3G.png)  
_Source: Data collection as done with code in [Appendix 1e](appendix-1)_

This rendered a graph that clustered on energy and power, but where “community”, “new” and “green” also took centre stage. Around it we see words like “government”, “people” and “community”, but also specific locations like Ontario and Ireland. Words that are connected with reasons for resistance identified in our netnography also occurred in the network, such as “noise” , “health” and “bird”. A cluster of words which could relate community actions, such as “meeting”, “help” and “support” can also be identified, which offers an interesting nuance to the overall lack of clear “calls for action” in our manual coding of the tweets.

To get a more granular understanding of our tweets, we decided to focus on the codes that appeared as being important from our content analysis and our immersion journal, namely the different levels of actors. We created a new edge-list filtered on the words “industry”, “community” and “government”. This meant that the words in the resulting network needed to be connected to at least one of these three actors. The resulting semantic network is shown in [Figure 10](Figure-10). 

#### Figure 10: Semantic network centred on actors

<a id="Figure-10"> </a>
![Figure_10](https://i.imgur.com/L8MmOt6.png)  
_Source: Data collection as done with code in [Appendix 1e](appendix-1)_

Again, words like “wind”, “turbine” and “farm” are central to the network, together with Ontario. The recurrence of Ontario as a geographical location is an interesting finding, as we had not encountered Ontario as a place with a particularly strong wind-turbine resistance movement during our netnography.
What is also interesting is that the network shows that the classic arguments against wind power, here captured in the words “subsidy”, “noise”, “health” and “bird”, are indeed orbiting the “industry” node. It thus seems that the critique on Twitter is directed towards the wind power industry, and not the government. 

The manual coding of tweets as well as our semantic network lead us to draw three main conclusions. First of all, the classical reasons for resisting wind turbines, such as wanting to protect wildlife or human health concerns, were largely absent when we coded and counted themes in our tweets and when we set up the semantic network. In fact, the only reference to wildlife found in the semantic network was the word “bird”. Secondly, and as a contrast to this absence, the focus of the tweets seemed to be on the community, or the geographic location of resistance. This traces back to online self-representation mentioned in Caliandro (2018) but with an interesting twist. Not only are the users in our sample signalling that they belong to a crowd resisting wind turbines (by including the word “wind” in their username or bio) - they also seem to emphasise and bring the physical geographical space into the digital space. To use Airoldi’s language, the physical site of resistance is brought onto the “meta-site” that is Twitter (2018). Lastly, and with a more methodological focus, we found that the iterative process of reflecting on our netnographic campaign and immersion journal (which was largely based on Facebook data) to be deeply rewarding and useful in the construction of our codebook for the content analysis.


<a id="topic-modelling"></a>
## 6. Topic modelling 
In this section we will enhance our understanding of the anti-wind turbine discourse by quantitatively assessing patterns in a twitter corpus collected on wind turbine opposition. These quantitative patterns will primarily be evaluated in a qualitative, heuristic fashion since the patterns are created to improve our understanding of the anti-wind turbine discourse; the mathematical patterns are interesting through their ability to reflect actual socio-symbolic patterns. This is in line with Ramage et al.'s sentiment: “topic models must find what we know there is” (n.d., p.2 ), so we expect the emerging patterns to be comparable to the patterns from our semantic network and manual coding of the tweets previously in the paper. 

Using topic models to explore and understand socio-symbolic patterns in text corpora is used widely (see e.g., Fuhse et al 2020). We consider two topic models in our pursuit of retrieving interpretable topics from our text corpora, namely the Latent Dirichlet Allocation (LDA) model (Blei et al., 2012), which is a Bayesian probabilistic topic model, and the hierarchical Stochastic Block Model (hSBM) which uses community detection in networks of words and documents to identify the topics (Gerlach et al., 2018). 

Both topic models use a bag-of-words approach to the quantification of the text corpora. For a document, in our case a tweet, the order of the words does not matter. To investigate whether the topic model better reflects the sentiment of the tweets if the order of the words is accounted for, we will use both unigram tokens (singular word-tokens) and bigram tokens (a bigram token is the concatenation of two words in succession) in the topic estimation. 

Following Blei et al. (2012) Latent Dirichlet Allocation can be described by the process by which words and documents are generated; namely that they are drawn from a fixed set of topics with different word distributions. In the hSBM framework, the distributional assumption is relaxed and the hSBM does not include any fixed hyperparameters when estimating the topical nature of the corpora (Gerlach et al., 2018). As such, the number of topics is a feature of the corpus rather than being a (hyper)parameter that we tune. Since the use of hSBM is limited in comparison to the LDA<sup>[6](#f6)</sup>, the practical implementation and visualization of LDA-topic estimation is more developed, which allows for easier exploration of the LDA topics. We will proceed to compare the two models.

<a id="hsbm"> </a>
### 6.1 hSBM implementation

Using the implementation of the hSBM by Gerlach, Peixoto & Altmann (2018), we conducted the hSBM twice; once with the sample of single tweets, and once on the sample aggregated by user, which, we will from now on refer to as the hSBM model and hSBM-U model respectively (U for user).<sup>[7](#f7)</sup>

The hSBM model returned 289 topics. For each word-group on the first level in the hierarchy, we retrieved the 10 most common words per group. Loosely following the procedure in Mimno et al. (2011), the researchers reflected on and mapped out concerns with topics based on four criteria: The (il)logical chain of words (for example “wind” -> “farm” -> “animal”); the presence of “intruder” words in otherwise interpretable topics; the seeming randomness of words in the topic; and lastly, whether the topics are balanced, or if very topic specific words get combined with very generic words. By manually sifting through the remaining 98 topics, we ended up selecting 15 topics. (See [appendix 6](#appendix-6) for a full list of topics.)

 


<a id="table2"> </a>
#### Table 2: hSBM Model
| Topic | Words                                                                                                                    | Interpretation               |
| ----- | ------------------------------------------------------------------------------------------------------------------------ | ---------------------------- |
| 1     | home, resident, family, concern, near, due, setback, km, within, safety                                                  | Distance to turbines (Nimby) |
| 2     | ireland, windfarms, landscape, tourism, northern, ruin, blight, inappropriate, tourist, rural\_ireland                   | Tourism/aesthetic concerns   |
| 3     | tax, credit, break, tax\_credit, production, senate, oklahoma, corporation, incentive, rep                               | Financial                    |
| 4     | energy, sector, fiasco, energy\_plan, energy\_future, new\_energy, repeal, energy\_firm, energy\_scam, energy\_push      | Scam/fiasco                  |
| 5     | protest, page, service, join, protecting, starting, presentation, signed, moor, nowind                                   | Action/protest               |
| 6     | subsidy, money, cut, taxpayer, paid, consumer, produce, spent, bank, payment                                             | Financial                    |
| 7     | noise, turbine\_noise, complaint, regulation, operator, ministry, noise\_complaint, staff, testing, vibration            | Noise pollution              |
| 8     | infrasound, low, sleep, pollution, neighbour, owner, heart, frequency, farm\_noise, noise\_pollution                     | Noise pollution              |
| 9     | health, impact, study, effect, living, dr, adverse, health\_effect, adverse\_health, health\_impact                      | Health concerns              |
| 10    | project, appeal, wind\_project, north, hearing, approval, lawsuit, approved, turbine\_project, final                     | Legal                        |
| 11    | offshore, offshore\_wind, blade, turbine\_blade, toxic, throw, foot, coast, whale, landfill                              | Offshore concerns            |
| 12    | community, local, hill, opposition, local\_community, bribery, community\_say, local\_wind, protect\_community           | Community resistance         |
| 13    | planning, application, refused, permission, granted, windfarm\_planning, laois, planning\_application, grant, actonfacts | Planning /refusal  of plan   |
| 14    | bird, bat, killing, killed, population, slaughter, bird\_bat, extinction, mortality, collision                           | Wildlife                     |
| 15    | eagle, kill, specie, endangered, golden, nest, raptor, threatened, bald, endangered\_specie                              | Wildlife                     |  

 _Source: Topics in [Appendix 6](#appendix-6). Code in [Appendix 1g](#appendix-1)_

The hSBM-U model on the other hand, returned 558 topics. We repeated the process of investigating the topics from the first level of the hierarchy, and manually sifted through the remaining 77 topics. 15 particularly poignant topics are displayed in [Table 3](#table3).


<a id="table3"> </a>
#### Table 3: hSBM-U Model
| Topic | Words                                                                                                                                                   | Interpretation               |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------- |
| 1     | government, policy, global, target, energy\_policy, warming, sea, west, fear, planet                                                                    | Global warming               |
| 2     | Plan, news, impact, public, area, development, proposed, decision, land, near                                                                           | Distance to turbines (Nimby) |
| 3     | money, renewables, tax, said, grid, question, comment, benefit, clean, number                                                                           | Financial                    |
| 4     | bill, appeal, offshore, letter, offshore\_wind, watch, blade, farmer, eagle, giant                                                                      | Offshore concerns            |
| 5     | co, gas, emission, nuclear, billion, scam, set, economic, science, promise                                                                              | Energy mix                   |
| 6     | local, thanks, please, stop, help, council, support, meeting, protect, fact                                                                             | Community resistance         |
| 7     | irish, guideline, permission, granted, laois, high\_court, updated, ltd, kildare, offaly                                                                | Legal                        |
| 8     | landscape, beautiful, bog, hill, objection, mountain, river, tourism, join, countryside                                                                 | Tourism/aesthetic concerns   |
| 9     | study, infrasound, forced, pollution, nuisance, inside, quiet, frequency, noise\_pollution, starting                                                    | Noise pollution              |
| 10    | noise, community, house, night, cause, air, heard, daily, tonight, morning                                                                              | Noise pollution              |
| 11    | windfarm, planning, windfarms, application, refused, planning\_application, object, refusal, height, campaigner                                         | Planning/refusal of plan     |
| 12    | turbine\_noise, plant, citizen, property, bat, wind\_developer, island, regulation, mass, endangered                                                    | Noise pollution/wildlife     |
| 13    | politician, listen, community\_group, exist, subsidise, m, turbine\_group, danish, commitment, enough\_wind                                             | Community resistance         |
| 14    | windfarm\_planning, actonfacts, output\_low, ireland\_windfarm, windfails, mystery, wind\_output, planning\_actonfacts, ancillary, development\_donegal | Efficiency                   |
| 15    | ge, group\_ge, twip, ge\_twip, delivering, group\_call, save\_wind, politician\_save, call\_politician, turbine\_delivering                             | Industry (GE in particular)  |  

 _Source: Topics in [Appendix 6](#appendix-6). Code in [Appendix 1g](#appendix-1)_

The analysis of the hSBM models has three main conclusions. First of all, many of the topics we reflected on being absent in our manual coding of tweets and the semantic network turned out to form distinct topics in the hSBM output. Notable examples are the topics that clearly cluster around human health concerns and aesthetic concerns. In fact, this topic added an additional nuance to the aesthetic concern argument that we had not noticed before - namely the relation to tourism. Second, and this is based on our experience of sifting through the topics, the hSBM model was easier to interpret than the hSBM-U topics. This is interesting because a critique that is often leveled against topic models is that they function worse on short text data. Lastly, both models returned a lot of noise and low-quality topics (Mimno et al., 2011). 


<a id="lda"> </a>
### 6.2 LDA implementation

Jónson and Stolee write in their paper that, even though the LDA is a popular tool to use when evaluating patterns in text data, it might not perform as well on very short text data (2016). They compare the performance of the LDA against other ways of identifying patterns in text, and also measure the model’s performance on a sample of individual tweets against tweets aggregated by the user that tweeted them. The intuition behind this is that by aggregating tweets into “psuedo-documents” authored by the same user, the amount of word co-occurrences within this psuedo-document will also increase.

Taking inspiration from their approach, we will compare the performance of the LDA to our hSBM models, on single tweets as well as sets of tweets aggregated by users. These two LDA’s will be referred to as the LDA and the LDA-U model respectively. Following Jónson and Stolee, the following hyperparameter settings for the LDA were evaluated (for a setting of ”K” topics): α={1/K, 10/K, 50/K, 100/K, 250/K}, β={0.001, 0.01, 0.1, 0.5, 1.0}. In their paper, the values of K were evaluated from the set {10, 50, 100, 200}. However, we also wanted to see how well our LDA performed with the number of topics generated from our two estimated hSBMs. Our hSBM generated 289 topics, which is why our final set of K’s for the LDA will be {10, 50, 100, 200, 300}. We decided not to include the number of topics from the hSBM-U model, since the human interpretation of this number of topics had previously proved to be both more time consuming and complex than rewarding. The α and ꞵ values encode some form of prior assumptions of the distribution of words and topics in the sample. α represents the document-topic density, and the ꞵ the topic-word density. Generally speaking, and assuming a symmetrical Dirichlet distribution, a high α hyperparameter implies that the documents contain more similar topic contents. Similarly, high ꞵ values implies that each topic contains more similar words ("LDA Alpha and Beta Parameters - The Intuition", 2021). We have no a priori beliefs about the concentration of topics or words, and we are thus interested in using these hyper parameters to tune our model. 

One common way of evaluating topic models is to measure the log-likelihood of a test-set. However, this measure of perplexity or, how “surprised” the model is when seeing new data, has been shown not to correlate strongly with human judgement of what constitutes a topic. Instead, we have opted to evaluate our models using coherence values, which measures the degree of semantic similarity between words within a topic. Coherence values help distinguish between topics that are interpretable, and those that are mere artifacts of statistical inference (Syed & Spruit, 2017). These values infer the coherence of topics by analysing the differences/similarities between ”top” words within a topic. (Jónson & Stolee 2016). We will use the C_v coherence value, which uses normalized pointwise mutual information (NPMI) and cosine similarity to evaluate the semantic similarity of words within a given topic. (Röder et al., 2015). The coherence values run from 0 to 1, where 1 would indicate perfect coherence. However, it is important to remember that there is no clear cut objective way to measure the performance of LDA models; there are only different heuristics that ultimately will be the product of the researcher’s choices and particular needs. Yet, we decided to experiment with the coherence values of models with different hyperparameters, as an analytical exercise and to see how the resulting topics compared against the topics of the hSBM models.

The model was first evaluated only on the number of topics, while not modifying α’s and ꞵ’s, and holding passes and iterations constant at 10 and 100 respectively to limit the computational power needed to optimise the parameters. Out of the topics we tried, 300 topics returned the highest coherence score of 0.684. As is evident in [Figure 11](#Figure-11), the coherence values were still increasing in the amount of topics but displayed diminishing marginal gains in the coherence score.

<a id="Figure-11"> </a>
#### Figure 11: LDA Model - Coherence scores by number of topics
![](https://i.imgur.com/aw4FFU2.png)

_Source: Code in [Appendix 1g](#appendix-1)_

We proceeded to finetune the α and ꞵ hyperparameters of the LDA with K = 300. This choice of topic count, K, was selected because of its high coherence value and because it is close to the 289 topics that the hSBM generated. The finetuning of the hyperparameters is shown in [Figure 12](#Figure-12).

<a id="Figure-12"> </a>
#### Figure 12: LDA model - Finetuning coherence values
![](https://i.imgur.com/MpbbZCF.png)  
_Source: Code in [Appendix 1g](#appendix-1)_

Interestingly, the coherence values radically decrease as the ꞵ gets higher, but stays similar at different levels of α-parameter values. Using higher ꞵ values implicates an initial prior distribution where words within topics are more similar to each other, which in our case does not produce as coherent topics. The highest coherence value was found at K = 300, α = 0.333333 and β=0.001, CV = 0.686. 

The 300 topics generated in the final LDA model displayed many of the flaws outlined in Mimno (2011). In fact, it was difficult to find topics that were semantically coherent. Randomness and intruder words were an issue, as well as unbalanced topics. The randomness could be a consequence of the many tweets that are included in the topic model which are unrelated to wind as described in the content analysis above. For more indepth research we suggest efforts into filtering out tweets unrelated to wind turbine discourse. 

For the reader to explore the 300 topics themselves, we have uploaded an interactive visualisation of the 300 topics at [www.rostrup.nu/index.html](http://www.rostrup.nu/index.html) which was created using a python wrapper for the LDAvis-package (Sievert and Shirley, 2012). A screenshot from the site is presented in [Figure 13](#Figure-13).<sup>[8](#f8)</sup> 

<a id="Figure-13"> </a>
#### Figure 13: Dynamic visualisation of fitting an LDA model to an anti wind turbine Twitter corpus
![Figure 13](https://i.imgur.com/FwHYduU.png)  
_Source: Code in [Appendix 1g](#appendix-1)_

A takeaway from the figure could be to remove the more frequent tokens in the data set (the ones in [figure 6](#Figure-6)). The more frequent tokens in the corpus have a high estimated frequency within all the topics which convolutes more interesting semantic interpretations with trivial insights e.g. the word wind is in a lot of the tweets. The first component (the x-axis) of the intertopic PCA captures only the estimated conditional distribution of the word wind (increasing from left to right).

We proceeded to select 15 topics that were still analytically interesting.


<a id="table4"> </a>
#### Table 4: Selection of 15 topics from an LDA model with 300 topics.

| Topic | Words                                                                                                             | Interpretation            |
| ----- | ----------------------------------------------------------------------------------------------------------------- | ------------------------- |
| 1     | wildlife, land\_wind, specie, killing, endangered, kerry, cancel, desecration, environmental\_cost, appears       | Wildlife                  |
| 2     | planning, area, permission, planning\_permission, month, shame, rural\_ireland, nightmare, wealthy, show\_support | Planning/permissions      |
| 3     | effect, adverse, health\_effect, useless, blocked, mine, tom, laurie, unbearable, eventually                      | Health effects            |
| 4     | renewable, renewable\_energy, proposed, humanity, target, battle, proposed\_wind, blight, energy\_target, retweet | Renewable energy          |
| 5     | industry, wind\_industry, finding, wind, apply, associated, reach, subsidised\_wind, joe, furious                 | Industry                  |
| 6     | level, nuisance, noise\_level, dependence\_fossil, killed, noise\_nuisance, noise\_wind, chinese, magazine, funny | Noise pollution           |
| 7     | noise, turbine\_noise, complaint, result, share, aware, noise\_complaint, animal, seriously, saturday             | Noise pollution           |
| 8     | study, many, move, required, sick, alternative, many\_people, complete, hurt, health\_study                       | Health studies            |
| 9     | eagle, death, protection, nice, rural\_ontario, based, fed, administration, bald, investing                       | Wildlife                  |
| 10    | scottish, high, scottish\_government, onshore, onshore\_wind, border, high\_court, wall, democracy, suicide       | Onshore wind              |
| 11    | resident, site, km, turbine\_site, sleep, early, mind, notice, nreap, within\_km                                  | Distance to wind turbines |
| 12    | bird, rule, appeal, bat, there, summer, inquiry, bird\_bat, windfarm\_plan, fox                                   | Wildlife                  |
| 13    | making, wind, profit, hot, reject, difference, nimby, impact\_industrial, bullshit, signalling                    | Industry/nimby            |
| 14    | developer, evidence, court, wind\_developer, might, fair, supreme, supreme\_court, voting, ignoring               | Legal                     |
| 15    | action, low, frequency ,low\_frequency, monday, april, frequency\_noise, draft, annual, session                   | Noise pollution           |  

 _Source: Topics in [Appendix 6](#appendix-6). Code in [Appendix 1g](#appendix-1)_


To briefly summarise the findings of the LDA model, after manually (and quite laboriously) filtering through the 300 topics, the qualitatively most interpretable and analytically useful topics that emerged from the data concerned noise pollution and to some extent, wildlife. However, most of these 15 topics still contain a lot of noise. For example, the third topic included the names “Tom” and “Laurie”, which we find hard to account for. Judging the performance of an LDA based on the coherence values might not be the best way to go, since these 300 topics might on some statistical level be coherent - to the human eye, they are not. 

Moving on to the user aggregated LDA-U model, we quickly noticed that the sequence of K’s that were tested radically decreased the coherence value of the models as seen in [Figure 14](#Figure-14).

#### Figure 14: LDA-U - Coherence values by number of topics
<a id="Figure-14"> </a>
![](https://i.imgur.com/lQVaQWo.png)  
_Source: Code in [Appendix 1g](#appendix-1)_

We decided to experiment with lowering the number of topics and instead tried K = {10-19}. The coherence was at its highest at 15 topics (Cv = 0.537) as shown in [Figure 15](#Figure-15). We thus proceeded to finetune the model with K = 15. 

<a id="Figure-15"> </a>
#### Figure 15: LDA-U - Coherence values by number of topics - a smaller interval of topics
![](https://i.imgur.com/VPUySPT.png)  
_Source: Code in [Appendix 1g](#appendix-1)_

The finetuning of the LDA-U model is displayed below. The model with the highest coherent scores was found at 15 topics with the parameter values α = 16.667 and β=0.5, CV = 0.554 ([Figure 16](#Figure-16)).

<a id="Figure-16"> </a>
#### Figure 16: LDA-U - Finetuning coherence values
![Figure 16](https://i.imgur.com/iw9FbN8.png)  
_Source: Code in [Appendix 1g](#appendix-1)_

The final set of 15 topics that emerged from the fine-tuned LDA-U model as well as our attempts at interpreting them are displayed in [Table 5]('table5') below.

<a id="table5"> </a>
#### Table 5: Final 15 topics from fine-tuned LDA-U model

| Topic | Words                                                                                                              | Interpretation     |
| ----- | ------------------------------------------------------------------------------------------------------------------ | ------------------ |
| 1     | ireland, abp, eirgrid, pylon, solar, waterford, developer, renewables, moneypoint, wind\_developer                 | Ireland/developer  |
| 2     | post, tax, state, county, industrial\_wind, board, cape, ptc, trump, credit                                        | Financial          |
| 3     | ontario, turbine\_noise, study, green\_energy, windturbines, environment, rural, impact, falmouth, appeal          | Canada             |
| 4     | onpoli, ontario, rural, climate, liberal, rural\_ontario, really, canada, cant, thing                              | Canada             |
| 5     | scotland, scottish, salmon, wild, park, windfarms, national, landscape, objection, wild\_land                      | Scotland/nature    |
| 6     | ireland, waterford, element, laois, done, co, money, question, irish, element\_power                               | Ireland            |
| 7     | solar, australia, wind\_amp, amp\_solar, renewable\_energy, price, climate, wind\_industry, nuclear, renewables    | Australia/solar    |
| 8     | thanks\_following, post, forever, edf, u\_facebook, following, remaining, lost, good\_news, abandon                | Spam               |
| 9     | windfarms, donegal, ireland, irish, yet, till, guideline, court, windfarm\_planning, thats                         | Ireland            |
| 10    | latest, link, follow, among, via, week, follower, popular, tweet, yorkshire                                        | Spam               |
| 11    | county, offshore, state, offshore\_wind, proposed, board, solar, town, renewable\_energy, wind\_project            | Offshore           |
| 12    | climate, week, follower, warming, global, climate\_change, eu, last\_week, gas, scientist                          | Climate change     |
| 13    | checked, automatically, followed, person, one\_person, unfollowed, donegal, ireland, wildlife, bog                 | Spam/Ireland       |
| 14    | policy, fossil, fuel, emission, scotland, electricity, climate, impact, still, money                               | Emissions/Scotland |
| 15    | ge, group\_ge, twip, ge\_twip, community\_group, politician, delivering, group\_call, save\_wind, politician\_save | Community          |  

 _Source: Topics in [Appendix 6](#appendix-6). Code in [Appendix 1g](#appendix-1)_

The topics from the LDA-U were qualitatively more difficult to interpret than the topics from the LDA model - but there were also only 15 of them, while the LDA model had 300 topics out of which 15 were somewhat interpretable. In the end, the only themes we could confidently assign to the LDA-U topics had to do with geographical location. The topics were unbalanced (see for example topic 14 that has the words “thats” “yet” and “still” in them, and random (see for example topic 8). It also strikes us as peculiar that the best coherence value was found at 15 topics, when the hSBM-U model generated more than 500 topics for the same data set. 


<a id="asds-discussion"> </a>
### 6.3 Discussion

To wrap up this comparison, both between the hSBM and the LDA, as well as on analysing single tweets and user aggregated documents, we would like to highlight four things. First of all, in their paper, Jónson and Stolee also found that the models they compared to the LDA (although they did not use hSBM) all outperformed the LDA, even when the text data was aggregated per user (2016). This seems to be the case in our study as well, where the hSBM generated less noisy topics, as well as having the advantage that it does not require any tuning of hyperparameters. 

Second, aggregating data per user did not qualitatively aid our analysis of the tweets. This again echoes the findings in Jónson and Stolee, where they also point out that the metadata that is needed to meaningfully aggregate text data might not always be available, which means that this approach will not always be feasible (2016). 

Thirdly, the results from these topic models meaningfully feed into the more qualitative manual content analysis we conducted on a subsample of the tweets. The topics that were more or less absent in the qualitative analysis, such as concerns about noise pollution, took centre stage in this analysis. The sheer amount of tweets that we were able to process also brought interesting nuances to the table, such as the connection between tourism and aesthetic concerns, which we had not documented before.

Lastly, a clear limitation of our analysis was the sampling and pre-processing of our data. As noted in section [2.1](#21), we had a precision issue since only around half of the tweets were manually coded as being relevant to our inquiry. We for example discovered there were some instances of automatically generated tweets about how many followers an account had gained or lost in a week. However, we decided to leave them in the sample. These tweets ended up forming topics of their own, which of course are uninformative to our analysis. Pre-processing wise, we failed to exclude the most used words. The topics thus ended up being qualitatively similar to each other and included a lot of the same words, even though there were of course notable differences. Denny and Spirling (2018) were right in saying pre-processing matters, and in future analyses, we would do this more thoroughly. 

<a id="reflections"></a>
## 7. Discussion of results and methodological contributions

In a study conducted by Munk (2014), investigating the full discourse of wind turbines, both pro and against, we can see a beneficial interplay between qualitative and quantitative methods as conducted in this study. In our case, we acknowledge the fact that a series of oppositional monologues does not constitute a comprehensive discourse. However, as discussed by Aitken (2009), focusing on opposition does not remove value from the results, nor does it invalidate any methodological arguments that are applied. Aitken criticises common misconceptions or dogmatic assumptions pertaining to the opposition. These assumptions risk biasing the results of studies thus misrepresenting opposition. Diversifying methods reduces reliance on single methods that may be afflicted by such biases. 

<a id="summing-up"> </a>
### 7.1 Summing up: Mapping out anti-wind turbine resistance online

We will start by addressing our first two research questions,

- Which topics can be observed from the online anti-wind turbine discourse? 
- On which platforms do which actors participate?

In an attempt to provide an overview of the actors who participate in the anti-wind turbine discourse, we implemented what Campagnolo (2020) calls a situational map. This is one way to represent connections among what may appear unrelated organisational settings across "different generations of discourse production" (Campagnolo, 2020 p.40).

<a id="Figure-17"> </a>
#### Figure 17: Situational map
![](https://i.imgur.com/Y3ugxWC.png)  
_Source: Author's own creation._

In the situational map we depict the socio-symbolic relations between actors. The automated Twitter network [section 3](#network) is represented in the upper left corner of the map, while the Facebook groups identified during the netnographic campaign (section 2) are represented in the right corner. The other actors were identified both in our Twitter dataset as well as during our immersion. Even though the wider analysis has focused on the wind turbine resistance movement, this movement does not exist in a vacuum. It relates to and is influenced by other types of actors. Campagnolo writes that “the situation per se becomes the ultimate unit of analysis”, which is what we aim to illustrate here (2020)

Elaborating further on the difference between platforms, Venturini et al. make a point about the adequacy of the data source in relation to the object of study (2018), which is questionable in our case. As we moved across platforms, we tried to make compatible operationalisations of our RQs, yet we have to acknowledge that we are at risk of comparing apples to pears. Not only do we compare across platforms - the exploration of Facebook was done in a Scandinavian context while the Twitter data set was sampled from English speaking tweets (see flowchart). Nonetheless, the exploration of Scandinavian Facebook groups during our netnographic campaign actually did quite accurately spill over onto our international Twitter data set, which is an interesting finding. There seems to be a discourse that is shared between these actors. An interesting comparison could also be made to Meelen et al. (2019) who investigated how virtual communities can influence and support socio-technical transitions formed around electric vehicles. In our case however, it is not a question of a unified discourse of socio-technical support, but a somewhat unified discourse of socio-technical resistance.

Delving into said discourse, there is a quite natural comparison to be made between the manual content analysis, the semantic network and the topic models. All three methods aim to simplify and establish patterns across cultural phenomena, like a map is a simplification of geographical space, to use the language of Lee and Martin (2015). Our strive to codify and make interpretable the large amounts of text data we had retrieved on twitter had us move across this continuum of methods, reaching from the manual content analysis (which was researcher led), to the semantic network (which was computer assisted, but with a clear involvement from the researchers) to the computer-led topic models, (where the LDA requires the researcher to determine hyperparameters while the hSBM is unsupervised).

Analytically, these different approaches complimented and informed each other, and aided us in triangulating the results of our initial netnographic campaign. One clear example of this is that some of the reasons for resistance that we had identified early on in the project, such as protection of wildlife, seemed largely absent in our manual content analysis, as well as our semantic network. This theme surfaced prominently in our topic models however. It is also worth noting the tourism aspect of the aesthetic critique that emerged from the topic models, as this was not something that was identified using more qualitative methods. Had we not conducted the topic models, it would have gone unnoticed. Reiterating Munk (2019), the methods complimented each other.

Summing up, we find that the wind turbine resistance discourse is fragmented. The reasons for resistance are plentiful, as well as the geographical areas where the movements are based. This made us reflect on the possibility that we may not have included all sub-parts of the discourse, even though we made efforts to analyse the movement across platforms. From a democratic perspective, it is essential to allow for voices being heard from all over a country; academic focus on one platform or political bottlenecking of another may have grave consequences. Lastly, we believe the popular focus on NIMBY as an explanation or merely as an observable phenomena in this topic is a bad heuristic which risks reducing valid arguments to mere selfishness. This conclusion is in line with the conclusions of Devine-Wright and Aitken. Additionally, Devine-Wright (2004) raises more valuable criticism to the field's perceptions of the opposition, taking a sceptical stance towards the cliningin on to NIMBY arguments often posed.

For future studies it would also be worth considering inter-risk framing contests inspired by Blok et al (nd.) between the risks presented by the resistance movement or in a comparative perspective of industrialised sustainable transition and on-the-ground environmental concerns. 

<a id="reflections"> </a>
### 7.2 Methodological reflections 

At the start of this paper, we also asked: 

> In what way do the insights from the different qualitative and quantitative methods overlap, and in what way do they differ from each other?

We would like to highlight two main insights. 

Our first point of reflection concerns the notion of computational grounded theory (Nelson 2020, Bang Carlsen & Ralund, 2021). A critique that is often levelled against manual content analysis is that human coders are biased and unreliable, and that unsupervised quantitative topic models would by default produce more objective results, since there is very little human involvement. Bang Carlsen & Ralund (2021) posit that this distinction between methods can be unfruitful, and a _computer assisted_ approach, where the researcher has an active involvement with the results of the models, ended up being useful in our case. The results our topic models produced would not hold up to scrutiny or be analytically useful if they were stand-alone, since they were filled with noise and randomness. Only by actively involving ourselves with the topics could they contribute to our understanding of the wind turbine resistance discourse. 

A second point of reflection which arose from our qual-quant investigation was that we have better insights into _why_ something might appear absent from a data site. For example, if we would have blindly analysed Twitter data, we might have concluded that wind turbine resistance does not exist in Scandinavia, even though it certainly does, just on another platform. Similarly, since Facebook data is arguably not as readily available as Twitter data, we might have decided not to venture on to that platform at all, if we did not use the analytically more appropriate qualitative digital methods. Had we begun our analysis with a more sequential viewpoint starting with Twitter data we might have identified Ireland, Scotland and Ontario and then proceeded to attempt a qualitative analysis of these. This may have neglected the sizable wind resistance communities in Denmark, Norway and Sweden present on Facebook. Social media data is arguably multifarious, as such data validity and sampling, _or simplicity/difficulty of access in our case_, cannot be the only way to measure how good or suitable data is (Brooker et al., 2016; Marres & Gerlitz, 2016). 

To summarise, the methods (just like the platforms we analysed) have different affordances that lend themselves more or less useful depending on what is under investigation. For an exploratory inquiry like ours, using both qualitative and quantitative methods proved to be incredibly useful, at different stages of the process. Importantly, we never blindly trusted any of the methods we used to analyse this phenomena; rather we were constantly contrasting them against the other methods we utilised, which we think validated our understanding of the phenomena.

One hindrance that this study must acknowledge that it experiences is that of the classic anthropological _meaning problem_, eloquently postulated by Malinowski (1922). Lingering still through reiteration and rediscovery, scholars such as Munk (2019) very much keeps the awareness of the problem alive when he considers its implications in modern academia in his paper on quali-quantitative analysis. The meaning problem does share resemblance to issues widely discussed in other fields such as the symbol grounding problem from cognitive science that we describe as _“the issue with trying to learn Danish from merely a Danish-to-Danish lexicon”_. Furthermore, Munk discusses mixed methods approaches to at least address this issue within our report. Our study incorporates what Munk has dubbed a _complementary_ style of mixing the methods, drawing from each, the strengths of the respective analyses. 

<a id="sources"></a>
 
## Sources

Airoldi, M. (2018). Ethnography and the digital fields of social media. _International Journal Of Social Research Methodology_, _21_(6), 661-673. doi: 10.1080/13645579.2018.1465622

Aitken, M. (2010). Why we still don’t understand the social aspects of wind power: A critique of key assumptions within the literature. _Energy Policy_, _38_(4), 1834-1841. doi: 10.1016/j.enpol.2009.11.060

Balakrishnan, V., & Ethel, L. (2014). Stemming and Lemmatization: A Comparison of Retrieval Performances. Lecture Notes On Software Engineering, 2(3), 262-267. doi: 10.7763/lnse.2014.v2.134

Bang Carlsen, H., & Ralund, S. (2021) Computational grounded theory revisited: from computer lead to computer assisted text analysis. _Big Data And Society_.

Baxter, J., Morzaria, R., & Hirsch, R. (2013). A case-control study of support/opposition to wind turbines: Perceptions of health risk, economic benefits, and community conflict. _Energy Policy_, _61_, 931-943. doi: 10.1016/j.enpol.2013.06.050

Blei, D. (2012). Probabilistic topic models. _Communications Of The ACM_, _55_(4), 77-84. doi: 10.1145/2133806.2133826

Blondel, V.D., Guillaume, J., Lambiotte, R., & Lefebvre, E. (2008). Fast unfolding of communities in largenetworks. _Journal of Statistical Mechanics: Theory and Experiment,10_, P10008.

Borch, K., Munk, A., & Dahlgaard, V. (2020). Mapping wind-power controversies on social media: Facebook as a powerful mobilizer of local resistance. _Energy Policy_, _138_, 111223. doi: 10.1016/j.enpol.2019.111223

Caliandro, A. (2017). Digital Methods for Ethnography: Analytical Concepts for Ethnographers Exploring Social Media Environments. _Journal Of Contemporary Ethnography_, 089124161770296. doi: 10.1177/0891241617702960

Campagnolo, G. (2020). The Analogue Mapping. _Social Data Science Xennials_, 35-50. doi: 10.1007/978-3-030-60358-8_3

Decuypere, M. (2019). Visual Network Analysis: a qualitative method for researching sociomaterial practice. _Qualitative Research_, _20_(1), 73-90. doi: 10.1177/1468794118816613

Denny, M., & Spirling, A. (2018). Text Preprocessing For Unsupervised Learning: Why It Matters, When It Misleads, And What To Do About It. _Political Analysis_, _26_(2), 168-189. doi: 10.1017/pan.2017.44

Devine-Wright, P. (2005). Beyond NIMBYism: towards an integrated framework for understanding public perceptions of wind energy. _Wind Energy_, _8_(2), 125-139. doi: 10.1002/we.124

Drieger, P. (2013). Semantic Network Analysis as a Method for Visual Text Analytics. _Procedia - Social And Behavioral Sciences_, _79_, 4-17. doi: 10.1016/j.sbspro.2013.05.053

FastText, 2021, https://fasttext.cc/docs/en/language-identification.html 

Fuhse, J., Stuhler, O., Riebling, J., Martin, J.L. (2020) Relating social and symbolic relations in quantitative text analysis. A study of parliamentary discourse in the Weimar Republic, Poetics, Volume 78, 101363, doi: 10.1016/j.poetic.2019.04.004 .

Gerlach, M., Peixoto, T., & Altmann, E. (2018). A network approach to topic models. _Science Advances_, _4_(7), eaaq1360. doi: 10.1126/sciadv.aaq1360

Gerlach, M. (2021). hSBM_Topicmodel. Retrieved 15 June 2021, from[ https://github.com/martingerlach/hSBM_Topicmodel](https://github.com/martingerlach/hSBM_Topicmodel)

Haggett, C. (2008). Over the Sea and Far Away? A Consideration of the Planning, Politics and Public Perception of Offshore Wind Farms. _Journal Of Environmental Policy & Planning_, _10_(3), 289-306. doi: 10.1080/15239080802242787

Herschel, R., & Miori, V. (2017). Ethics & Big Data. _Technology In Society_, _49_, 31-36. doi: 10.1016/j.techsoc.2017.03.003

Jacomy, M., Venturini, T., Heymann, S., & Bastian, M. (2014). ForceAtlas2, a Continuous Graph Layout Algorithm for Handy Network Visualization Designed for the Gephi Software. _Plos ONE_, _9_(6), e98679. doi: 10.1371/journal.pone.0098679

Jónsson, E. Stolee, J. (2016). An Evaluation of Topic Modelling Techniques for Twitter.

Joulin, A., Grave, E., Bojanowski, P., & Mikolov, T. (2016a). Bag of Tricks for Efficient Text Classification. arXiv preprint arXiv:1607.01759.

Joulin, A., Grave, E., Bojanowski, P., Douze, M., Jégou, H., & Mikolov, T. (2016b). FastText.zip: Compressing text classification models. arXiv preprint arXiv:1612.03651.

Kozinets, R. (2019). _Netnography_ (3rd ed.). SAGE.

Lambiotte, R. Delvenne, J., & Barahona, M. (2009). Laplacian Dynamics and Multiscale Modular Structure in Networks. _arXiv_. _1_. 

LDA Alpha and Beta Parameters - The Intuition. (2021). Retrieved 15 June 2021, from https://www.thoughtvector.io/blog/lda-alpha-and-beta-parameters-the-intuition/

Lee, M., & Martin, J. (2014). Coding, counting and cultural cartography. _American Journal Of Cultural Sociology_, _3_(1), 1-33. doi: 10.1057/ajcs.2014.13

Malinowski, B. (1922). _Argonauts of the western Pacific_. London (etc.): Routledge & Sons.

Mimno, D., Talley, E., Leenders, M., M. Wallach, H., & McCallum, A. (2011). Optimizing Semantic Coherence in Topic Models. In _Proceedings of the 2011 Conference on Empirical Methods in Natural Language Processing_ (pp. 262-272). Edinburgh, Scotland: Association for Computational Linguistics. Retrieved from[ http://dirichlet.net/pdf/mimno11optimizing.pdf](http://dirichlet.net/pdf/mimno11optimizing.pdf)

Munk, A. (2014). Mapping wind energy controversies online: introduction to methods and datasets. Available at SSRN 2595287.

Munk, A. (2019). Four Styles of Quali-Quantitative Analysis. _Nordicom Review_, _40_(s1), 159-176. doi: 10.2478/nor-2019-0020

Nelson, L. (2020). Computational Grounded Theory: A Methodological Framework. _Sociological Methods & Research_, _49_(1), 3-42. doi: 10.1177/0049124117729703

NLTK 3.6.2 documentation. (2021). Retrieved 15 June 2021, from[ https://www.nltk.org/_modules/nltk/stem/wordnet.html](https://www.nltk.org/_modules/nltk/stem/wordnet.html)

Pedersen, L.. (2020) “Vindkraftmotstander Sultestreiker.” NRK, NRK, 17 June 2020, www.nrk.no/osloogviken/vindkraftmotstander-sultestreiker-1.15056109.

Rafail, P. (2017). Nonprobability Sampling and Twitter. _Social Science Computer Review_, _36_(2), 195-211. doi: 10.1177/0894439317709431

Ramage, D., Rosen, E., Chuang, J., D. Manning, C., & A. McFarland, D. Topic Modeling for the Social Sciences, 2. Retrieved from[ http://users.umiacs.umd.edu/~jbg/nips_tm_workshop/23.pdf](http://users.umiacs.umd.edu/~jbg/nips_tm_workshop/23.pdf)

Röder, M., Both, A., & Hinneburg, A. (2015). Exploring the Space of Topic Coherence Measures. In _WSDM_. Shanghai.

Solberg, E. (2020). “Limte Seg Fast i Protest Mot Vindkraft.” Radio Haugaland, 24 Sept. 2020, radioh.no/limte-seg-fast-i-protest-mot-vindkraft/. 

Syed, S., & Spruit, M. (2017). Full-Text or Abstract? Examining Topic Coherence Scores Using Latent Dirichlet Allocation. _2017 IEEE International Conference On Data Science And Advanced Analytics (DSAA)_. doi: 10.1109/dsaa.2017.61

Terman, R. (2017). Islamophobia and Media Portrayals of Muslim Women: A Computational Text Analysis of US News Coverage. _International Studies Quarterly_, _61_(3), 489-502. doi: 10.1093/isq/sqx051

Toftrup, Mads, Søren Asger Sørensen, Manuel R. Ciosici, Ira Assent (2021). A reproduction of Apple's bi-directional LSTM models for language identification in short strings. In Proceedings of the 16th Conference of the European Chapter of the Association for Computational Linguistics: Student Research Workshop (pp. 36–42). Association for Computational Linguistics.

Wolsink, M. (2006). Invalid theory impedes our understanding: a critique on the persistence of the language of NIMBY. _Transactions Of The Institute Of British Geographers_, _31_(1), 85-91. doi: 10.1111/j.1475-5661.2006.00191.x

<a id="appendix"></a>
## Appendix
<a id="appendix-1"></a>
### Appendix 1 - Code

Appendix 1a - Collecting actors using snowball sampling: [https://github.com/EspenRostrup/AntiWindTurbineDiscourse/TwitterNetworkCollectionScript.py](https://github.com/EspenRostrup/AntiWindTurbineDiscourse/TwitterNetworkCollectionScript.py) 

Appendix 1b - Network visualisation and collection of GPS-coordinates:

[https://github.com/EspenRostrup/AntiWindTurbineDiscourse/blob/main/NetworkVisualisation.ipynb](https://github.com/EspenRostrup/AntiWindTurbineDiscourse/blob/main/NetworkVisualisation.ipynb) 

Appendix 1c - Collecting tweets from actors:

[https://github.com/EspenRostrup/AntiWindTurbineDiscourse/blob/main/tweepy_collection.ipynb](https://github.com/EspenRostrup/AntiWindTurbineDiscourse/blob/main/tweepy_collection.ipynb) 

Appendix 1d - Identifying tweet language (and preprocessing):

[https://github.com/EspenRostrup/AntiWindTurbineDiscourse/blob/main/TweetLanguageDetection.ipynb](https://github.com/EspenRostrup/AntiWindTurbineDiscourse/blob/main/TweetLanguageDetection.ipynb) 

Appendix 1e - Semantic network analysis (and preprocessing):

[https://github.com/EspenRostrup/AntiWindTurbineDiscourse/blob/main/semantic_networks.ipynb](https://github.com/EspenRostrup/AntiWindTurbineDiscourse/blob/main/semantic_networks.ipynb) 

Appendix 1f - Visualisation of manual code of tweets:

[https://github.com/EspenRostrup/AntiWindTurbineDiscourse/blob/main/Content%20analysis.ipynb](https://github.com/EspenRostrup/AntiWindTurbineDiscourse/blob/main/Content%20analysis.ipynb) 

Appendix 1g - Topic modelling, HSBM and LDA (code built in Collab): [https://github.com/EspenRostrup/AntiWindTurbineDiscourse/blob/main/HSBM_LDA_turbines.ipynb](https://github.com/EspenRostrup/AntiWindTurbineDiscourse/blob/main/HSBM_LDA_turbines.ipynb) 





<a id="appendix-2"></a>
### Appendix 2 - Twitter network with a computed modularity with a resolution of 1.0. 

Note: Colors are identified communities; there are 6 in total in this network. The modularity score is 0.544 which roughly indicates that there are more edges between nodes within a given community than one would expect at random (the value 0). If the score is less than zero there are less edges between nodes in a community than we would expect at random.


<a id="appendix-3"></a>
### Appendix 3 - Interview guide

#### Semi-structured interview

Inform about the master’s project. We are studying wind resistance in the nordics on Twitter and on Facebook. Within this scope we have been observing a few groups on Facebook and analysing Twitter data.



1. How did you get involved in the resistance against wind turbines? 

2. Could you tell me the story of your involvement in this resistance movement? 

3. When did you join the group? 

4. When did you become a moderator? 

5. Could you tell me about how the group has developed over time?





<a id="appendix-4"></a>
### Appendix 4 - Immersion journal

Appendix 4a - Miro board: [https://miro.com/app/board/o9J_lGIOU7k=/](https://miro.com/app/board/o9J_lGIOU7k=/) 

Appendix 4b - Excel spreadsheet - requires login - only people from “KU organisation” can get access: [https://alumni.sharepoint.com/:x:/s/UCPH_Turbinefanclub/ES9FzKiXEBpCuMPotY2s3lYBQy5Mm2kMBGnwXr_Yu2FMBg?e=9UeQpb](https://alumni.sharepoint.com/:x:/s/UCPH_Turbinefanclub/ES9FzKiXEBpCuMPotY2s3lYBQy5Mm2kMBGnwXr_Yu2FMBg?e=9UeQpb) 


<!-- Footnotes themselves at the bottom. -->


<a id="appendix-5"></a>
### Appendix 5 - Codebook for manual content analysis

Full list can be accessed on [Github.](https://github.com/EspenRostrup/AntiWindTurbineDiscourse/blob/main/Codebook.xlsx)

<a id="appendix-5"></a>
### Appendix 6 - Full list of topics from hSBM and LDA models
Full list can be accessed on [Github.](https://github.com/EspenRostrup/AntiWindTurbineDiscourse/blob/main/final_topics-2.xlsx)


<a id="notes"></a>
## Notes

 <a id = "f1"> </a>
[^1]: Norrmogen is a lake in Sweden and the group pertains to local anti wind discussions.  
 <a id = "f2"> </a>  
[^2]: We also remove users where the word “wind” is a part of the word “window” by using the regex-pattern `(?i)wind(?!ow)`  
 <a id = "f3"> </a>  
[^3]: We have imposed some more “gravity” on the nodes in the smaller clusters to contain the graph in a readable format. The clusters labeled “The city of Windsor” and “Lake Windermere” are, when the ForceAtlas2 algorithm is deployed, far away from the two big clusters of nodes.  
 <a id = "f4"> </a>  
[^4]: See [Appendix 2](#appendix-2) for the network in [Figure 4b](#Figure-4b) colored by computed communities using a greedy modularity algorithm.  
 <a id = "f5"> </a>  
[^5]: Investigating the larger network including the profiles with an in-degree (followers in the network) smaller or equal to 3, indicates more cities with the word wind in it e.g. Swindon and the wind surfing community is also emerging in the larger network.   
 <a id = "f6"> </a>
[^6]: For instance the search query “latent Dirichlet allocation” on GitHub reveals 881 code repositories and in comparison the query “hierarchical stochastic block model” returns only one repository.  
 <a id = "f7"> </a>
[^7]: For source code see Github repository (Gerlach, 2021).
 <a id = "f8"> </a>
[^8]: There are a lot of metrics in the visualisation and a PCA of intertopic distance (the Shannon-Jensen distance is used), which we due to time and space constraints cannot go into. There are references in the visualisation that explains the metrics for the interested reader.
