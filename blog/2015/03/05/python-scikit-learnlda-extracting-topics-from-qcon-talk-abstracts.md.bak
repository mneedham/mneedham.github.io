+++
draft = false
date="2015-03-05 08:52:22"
title="Python: scikit-learn/lda: Extracting topics from QCon talk abstracts"
tag=['python']
category=['Machine Learning', 'Python']
+++

<p>
Following on from <a href="http://blog.bruggen.com/2015/02/the-qcon-graph.html">Rik van Bruggen's blog post on a QCon graph he's created</a> ahead of <a href="http://qconlondon.com/schedule">this week's conference</a>, I was curious whether we could extract any interesting relationships between talks based on their abstracts.
</p>


<p>
Talks are already grouped by their hosting track but there's likely to be some overlap in topics even for talks on different tracks. 
I therefore wanted to extract topics and connect each talk to the topic that describes it best.
</p>


<p>
My first attempt was following <a href="http://scikit-learn.org/stable/auto_examples/applications/topics_extraction_with_nmf.html">an example which uses Non-Negative Matrix factorization</a> which worked very well for extracting topics but didn't seem to provide an obvious way to work out how to link those topics to individual talks. 
</p>


<p>
Instead I ended up looking at the <a href="https://pypi.python.org/pypi/lda">lda library</a> which uses Latent Dirichlet Allocation and allowed me to achieve both goals.
</p>


<p>
I already had some code to run TF/IDF over each of the talks so I thought I'd be able to feed the matrix output from that into the LDA function. This is what I started with:
</p>



~~~python

import csv

from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.decomposition import NMF
from collections import defaultdict
from bs4 import BeautifulSoup, NavigableString
from soupselect import select

def uri_to_file_name(uri):
    return uri.replace("/", "-")

sessions = {}
with open("data/sessions.csv", "r") as sessions_file:
    reader = csv.reader(sessions_file, delimiter = ",")
    reader.next() # header
    for row in reader:
        session_id = int(row[0])
        filename = "data/sessions/" + uri_to_file_name(row[4])
        page = open(filename).read()
        soup = BeautifulSoup(page)
        abstract = select(soup, "div.brenham-main-content p")
        if abstract:
            sessions[session_id] = {"abstract" : abstract[0].text, "title": row[3] }
        else:
            abstract = select(soup, "div.pane-content p")
            sessions[session_id] = {"abstract" : abstract[0].text, "title": row[3] }

corpus = []
titles = []
for id, session in sorted(sessions.iteritems(), key=lambda t: int(t[0])):
    corpus.append(session["abstract"])
    titles.append(session["title"])

n_topics = 15
n_top_words = 50
n_features = 6000

vectorizer = TfidfVectorizer(analyzer='word', ngram_range=(1,1), min_df = 0, stop_words = 'english')
matrix =  vectorizer.fit_transform(corpus)
feature_names = vectorizer.get_feature_names()

import lda
import numpy as np

vocab = feature_names

model = lda.LDA(n_topics=20, n_iter=500, random_state=1)
model.fit(matrix)
topic_word = model.topic_word_
n_top_words = 20

for i, topic_dist in enumerate(topic_word):
    topic_words = np.array(vocab)[np.argsort(topic_dist)][:-n_top_words:-1]
    print('Topic {}: {}'.format(i, ' '.join(topic_words)))
~~~

<p>And if we run it?</p>



~~~bash

Topic 0: zoosk faced exposing expression external externally extra extraordinary extreme extremes face facebook facilitates faster factor factors fail failed failure
Topic 1: zoosk faced exposing expression external externally extra extraordinary extreme extremes face facebook facilitates faster factor factors fail failed failure
Topic 2: zoosk faced exposing expression external externally extra extraordinary extreme extremes face facebook facilitates faster factor factors fail failed failure
Topic 3: zoosk faced exposing expression external externally extra extraordinary extreme extremes face facebook facilitates faster factor factors fail failed failure
Topic 4: zoosk faced exposing expression external externally extra extraordinary extreme extremes face facebook facilitates faster factor factors fail failed failure
Topic 5: zoosk faced exposing expression external externally extra extraordinary extreme extremes face facebook facilitates faster factor factors fail failed failure
Topic 6: zoosk faced exposing expression external externally extra extraordinary extreme extremes face facebook facilitates faster factor factors fail failed failure
Topic 7: zoosk faced exposing expression external externally extra extraordinary extreme extremes face facebook facilitates faster factor factors fail failed failure
Topic 8: zoosk faced exposing expression external externally extra extraordinary extreme extremes face facebook facilitates faster factor factors fail failed failure
Topic 9: 10 faced exposing expression external externally extra extraordinary extreme extremes face facebook facilitates faster factor factors fail failed failure
Topic 10: zoosk faced exposing expression external externally extra extraordinary extreme extremes face facebook facilitates faster factor factors fail failed failure
Topic 11: zoosk faced exposing expression external externally extra extraordinary extreme extremes face facebook facilitates faster factor factors fail failed failure
Topic 12: zoosk faced exposing expression external externally extra extraordinary extreme extremes face facebook facilitates faster factor factors fail failed failure
Topic 13: zoosk faced exposing expression external externally extra extraordinary extreme extremes face facebook facilitates faster factor factors fail failed failure
Topic 14: zoosk faced exposing expression external externally extra extraordinary extreme extremes face facebook facilitates faster factor factors fail failed failure
Topic 15: zoosk faced exposing expression external externally extra extraordinary extreme extremes face facebook facilitates faster factor factors fail failed failure
Topic 16: zoosk faced exposing expression external externally extra extraordinary extreme extremes face facebook facilitates faster factor factors fail failed failure
Topic 17: zoosk faced exposing expression external externally extra extraordinary extreme extremes face facebook facilitates faster factor factors fail failed failure
Topic 18: zoosk faced exposing expression external externally extra extraordinary extreme extremes face facebook facilitates faster factor factors fail failed failure
Topic 19: zoosk faced exposing expression external externally extra extraordinary extreme extremes face facebook facilitates faster factor factors fail failed failure
~~~

<p>As you can see, every topic has the same set of words which isn't what we want. Let's switch out our TF/IDF vectorizer for a simpler count based one:
</p>



~~~python

vectorizer = CountVectorizer(analyzer='word', ngram_range=(1,1), min_df = 0, stop_words = 'english')
~~~

<p>The rest of the code stays the same and these are the topics that get extracted:
</p>



~~~bash

Topic 0: time people company did writing real way used let cassandra soundcloud successful know web organization audio lives swift stuck
Topic 1: process development delivery platform developer continuous testing rapidly deployment implementing release demonstrate paas advice hard light predictable radically introduce
Topic 2: way open space kind people change meetings ll lead powerful practice times everyday simple qconlondon organization unconference track extraordinary
Topic 3: apache apis processing open spark distributed leading making environments solr cases brooklyn components existing ingestion contributing data target evolved
Topic 4: management million effective cost halo gameplay player billion ad catastrophic store microsoft final music influence information launch research purchased
Topic 5: product look like use talk problems working analysis projects challenges 2011 functionality useful spread business deep inside happens sensemaker
Topic 6: ll computers started principles free focus face smaller atlas control uses products avoid computing ground billions mean volume consistently
Topic 7: code end users developers just application way line apps mobile features sites hours issues applications write faster game better
Topic 8: ve development teams use things world like time learned lessons think methods multiple story say customer developer experiences organisations
Topic 9: software building docker built challenges monitoring gilt application discuss solution decision talk download source center critical decisions bintray customers
Topic 10: years infrastructure tools language different service lot devops talk adoption scala popular clojure advantages introduced effectively looking wasn includes
Topic 11: high does latency session requirements functional performance real world questions problem second engineering patterns gravity explain discuss expected time
Topic 12: business make build technology technologies help trying developers parts want interfaces small best centres implementations critical moo databases going
Topic 13: need design systems large driven scale software applications slow protocol change needs approach gets new contracts solutions complicated distributed
Topic 14: architecture service micro architectures increasing talk microservices order market value values new present presents services scalable trading practices today
Topic 15: java using fast robovm lmax ios presentation really jvm native best exchange azul hardware started project slowdowns goal bring
Topic 16: data services using traditional create ways support uk large user person complex systems production impact art organizations accessing mirage
Topic 17: agile team experience don work doing processes based key reach extra defined pressure machines nightmare practices learn goals guidance
Topic 18: internet new devices programming things iot big number deliver day connected performing growing got state thing provided times automated
Topic 19: cloud including deploy session api government security culture software type attack techniques environment digital secure microservice better creation interaction
~~~

<p>
Some of the groupings seem to make sense e.g. Topic 11 contains words related to high performance code with low latency; Topic 15 covers Java, the JVM and other related words; but others are more difficult to decipher</p>
 

<p>e.g. both Topic 14 and Topic 19 talk about micro services but the latter mentions 'government' and 'security' so perhaps the talks linked to that topic come at micro services from a different angle altogether.
</p>


<p>
Next let's see which topics a talk is most likely to be about. We'll look at the first ten:</p>



~~~python

doc_topic = model.doc_topic_
for i in range(0, 10):
    print("{} (top topic: {})".format(titles[i], doc_topic[i].argmax()))
    print(doc_topic[i].argsort()[::-1][:3])

To the Moon (top topic: 8)
[ 8  0 11]
Evolutionary Architecture and Micro-Services - A Match Enabled by Continuous Delivery (top topic: 14)
[14 19 16]
How SoundCloud uses Cassandra (top topic: 0)
[0 6 5]
DevOps and the Need for Speed (top topic: 18)
[18  5 16]
Neuro-diversity and agile (top topic: 7)
[17  7  2]
Java 8 in Anger (top topic: 7)
[ 7 15 12]
APIs that Change Lifestyles (top topic: 9)
[ 9  6 19]
Elasticsearch powers the Citizen Advice Bureau (CAB) to monitor trends in society before they become issues (top topic: 16)
[16 12 19]
Architecture Open Space (top topic: 2)
[ 2 19 18]
Don’t let Data Gravity crush your infrastructure (top topic: 11)
[11 16  3]
~~~

<p>
So our third talk on the list 'How SoundCloud uses Cassandra' does end up being tagged with topic 0 which mentions SoundCloud so that's good!
</p>



~~~text

Topic 0: time people company did writing real way used let cassandra soundcloud successful know web organization audio lives swift stuck
~~~

<p>It's next two topics are 5 & 6 which contain the following words...</p>



~~~text

Topic 5: product look like use talk problems working analysis projects challenges 2011 functionality useful spread business deep inside happens sensemaker
Topic 6: ll computers started principles free focus face smaller atlas control uses products avoid computing ground billions mean volume consistently
~~~

<p>...which are not as intuitive. What about Java 8 in Anger? It's been tagged with topics 7, 15 and 12:</p>



~~~text

Topic 7: code end users developers just application way line apps mobile features sites hours issues applications write faster game better
Topic 15: java using fast robovm lmax ios presentation really jvm native best exchange azul hardware started project slowdowns goal bring
Topic 12: business make build technology technologies help trying developers parts want interfaces small best centres implementations critical moo databases going
~~~

<p>
15 makes sense since that mentions Java and perhaps 12 and 7 do as well as they both mention developers.
</p>


<p>
So while the topics pulled out are not horrendous I don't think they're particularly useful yet either. These are some of the areas I need to do some more research around:
</p>


<ul>
<li>
How do you measure the success of topic modelling? I've been eyeballing the output of the algorithm but I imagine there's an automated way to do that.
</li>
<li>How do you determine the right number of topics? I found <a href="http://blog.cigrainger.com/2014/07/lda-number.html#fn:fn-1">an article written by Christophe Grainger</a> which explains a way of doing that which I need to look at in more detail.</li>
<li>
It feels like I would be able to pull out better topics if I had an ontology of computer science/software words and then ran the words through that to derive topics.
</li>
<li>
Another approach suggested by <a href="https://twitter.com/mesirii">Michael</a> is to find the most popular words using the <cite>CountVectorizer</cite> and tag talks with those instead.
</li>
</ul>

<p>
If you have any suggestions let me know. The <a href="https://github.com/mneedham/neo4j-qcon/blob/master/topics.py">full code is on github</a> if you want to play around with it.
</p>

