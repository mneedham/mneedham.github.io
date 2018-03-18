+++
draft = false
date="2015-02-15 15:56:09"
title="Python/scikit-learn: Calculating TF/IDF on How I met your mother transcripts"
tag=['python']
category=['Python']
+++

<p>
Over the past few weeks I've been playing around with various NLP techniques to find interesting insights into How I met your mother from its transcripts and one technique that kept coming up is TF/IDF.</p>


<p>The <a href="http://en.wikipedia.org/wiki/Tf%E2%80%93idf">Wikipedia definition</a> reads like this:</p>


<blockquote>
<strong>tf–idf</strong>, short for <strong>term frequency–inverse document frequency</strong>, is a numerical statistic that is intended to reflect how important a word is to a document in a collection or corpus.

It is often used as a weighting factor in information retrieval and text mining. 

The tf-idf value increases proportionally to the number of times a word appears in the document, but is offset by the frequency of the word in the corpus, which helps to adjust for the fact that some words appear more frequently in general.
</blockquote>

<p>
I wanted to generate a <a href="http://en.wikipedia.org/wiki/Tf%E2%80%93idf">TF/IDF</a> representation of phrases used in the hope that it would reveal some common themes used in the show.
</p>



<p>
Python's <a href="http://scikit-learn.org/stable/">scikit-learn</a> library gives you two ways to generate the TF/IDF representation:
</p>


<ol>
<li>Generate a matrix of token/phrase counts from a collection of text documents using <cite><a href="http://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html">CountVectorizer</a></cite> and feed it to <cite><a href="http://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfTransformer.html#sklearn.feature_extraction.text.TfidfTransformer.fit_transform">TfidfTransformer</a></cite> to generate the TF/IDF representation.
</li>
<li>
Feed the collection of text documents directly to <cite><a href="http://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html">TfidfVectorizer</a></cite> and go straight to the TF/IDF representation skipping the middle man.

</li>
</ol>

<p>
I started out using the first approach and hadn't quite got it working when I realised there was a much easier way!
</p>


<p>I have a collection of <a href="https://github.com/mneedham/neo4j-himym/blob/master/data/import/sentences.csv">sentences in a CSV file</a> so the first step is to convert those into a list of documents:</p>



~~~python

from collections import defaultdict
import csv

episodes = defaultdict(list)
with open("data/import/sentences.csv", "r") as sentences_file:
    reader = csv.reader(sentences_file, delimiter=',')
    reader.next()
    for row in reader:
        episodes[row[1]].append(row[4])

for episode_id, text in episodes.iteritems():
    episodes[episode_id] = "".join(text)

corpus = []
for id, episode in sorted(episodes.iteritems(), key=lambda t: int(t[0])):
    corpus.append(episode)
~~~

<p><cite>corpus</cite> contains 208 entries (1 per episode), each of which is a string containing the transcript of that episode. Next it's time to train our TF/IDF model which is only a few lines of code:
</p>



~~~python

from sklearn.feature_extraction.text import TfidfVectorizer
tf = TfidfVectorizer(analyzer='word', ngram_range=(1,3), min_df = 0, stop_words = 'english')
~~~

<p>
The most interesting parameter here is <cite>ngram_range</cite> - we're telling it to generate 2 and 3 word phrases along with the single words from the corpus.
</p>


<p>e.g. if we had the sentence "Python is cool" we'd end up with 6 phrases - 'Python', 'is', 'cool', 'Python is', 'Python is cool' and 'is cool'.

<p>
Let's execute the model against our corpus:
</p>



~~~python

tfidf_matrix =  tf.fit_transform(corpus)
feature_names = tf.get_feature_names() 
>>> len(feature_names)
498254

>>> feature_names[50:70]
[u'00 does sound', u'00 don', u'00 don buy', u'00 dressed', u'00 dressed blond', u'00 drunkenly', u'00 drunkenly slurred', u'00 fair', u'00 fair tonight', u'00 fall', u'00 fall foliage', u'00 far', u'00 far impossible', u'00 fart', u'00 fart sure', u'00 friends', u'00 friends singing', u'00 getting', u'00 getting guys', u'00 god']
~~~

<p>
So we're got nearly 500,000 phrases and if we look at <cite>tfidf_matrix</cite> we'd expect it to be a 208 x 498254 matrix - one row per episode, one column per phrase:
</p>



~~~python

>>> tfidf_matrix
<208x498254 sparse matrix of type '<type 'numpy.float64'>'
	with 740396 stored elements in Compressed Sparse Row format>
~~~

<p>
This is what we've got although under the covers it's using a sparse representation to save space. Let's convert the matrix to dense format to explore further and find out why:
</p>



~~~python

dense = tfidf_matrix.todense()
>>> len(dense[0].tolist()[0])
498254
~~~

<p>
What I've printed out here is the size of one row of the matrix which contains the TF/IDF score for every phrase in our corpus for the 1st episode of How I met your mother. A lot of those phrases won't have happened in the 1st episode so let's filter those out:
</p>



~~~python

episode = dense[0].tolist()[0]
phrase_scores = [pair for pair in zip(range(0, len(episode)), episode) if pair[1] > 0]

>>> len(phrase_scores)
4823
~~~

<p>
There are just under 5000 phrases used in this episode, roughly 1% of the phrases in the whole corpus.
The sparse matrix makes a bit more sense - if scipy used a dense matrix representation there'd be 493,000 entries with no score which becomes more significant as the number of documents increases.
</p>


<p>
Next we'll sort the phrases by score in descending order to find the most interesting phrases for the first episode of How I met your mother:
</p>



~~~python

>>> sorted(phrase_scores, key=lambda t: t[1] * -1)[:5]
[(419207, 0.2625177493269755), (312591, 0.19571419072701732), (267538, 0.15551468983363487), (490429, 0.15227880637176266), (356632, 0.1304175242341549)]
~~~

<p>
The first value in each tuple is the phrase's position in our initial vector and also corresponds to the phrase's position in <cite>feature_names</cite> which allows us to map the scores back to phrases. Let's look up a couple of phrases:
</p>



~~~python

>>> feature_names[419207]
u'ted'
>>> feature_names[312591]
u'olives'
>>> feature_names[356632]
u'robin'
~~~

<p>
Let's automate that lookup:
</p>



~~~python

sorted_phrase_scores = sorted(phrase_scores, key=lambda t: t[1] * -1)
for phrase, score in [(feature_names[word_id], score) for (word_id, score) in sorted_phrase_scores][:20]:
   print('{0: <20} {1}'.format(phrase, score))

ted                  0.262517749327
olives               0.195714190727
marshall             0.155514689834
yasmine              0.152278806372
robin                0.130417524234
barney               0.124411751867
lily                 0.122924977859
signal               0.103793246466
goanna               0.0981379875009
scene                0.0953423604123
cut                  0.0917336653574
narrator             0.0864622981985
flashback            0.078295921554
flashback date       0.0702825260177
ranjit               0.0693927691559
flashback date robin 0.0585687716814
ted yasmine          0.0585687716814
carl                 0.0582101172888
eye patch            0.0543650529797
lebanese             0.0543650529797
~~~

<p>
We see all the main characters names which aren't that interested - perhaps they should be part of the stop list - but 'olives' which is where the olive theory is first mentioned. I thought olives came up more often but a quick search for the term suggests it isn't mentioned again until Episode 9 in Season 9:
</p>



~~~bash

$ grep -rni --color "olives" data/import/sentences.csv | cut -d, -f 2,3,4 | sort | uniq -c
  16 1,1,1
   3 193,9,9
~~~

<p>'yasmine' is also an interesting phrase in this episode but she's never mentioned again:</p>



~~~bash

$ grep -h -rni --color "yasmine" data/import/sentences.csv
49:48,1,1,1,"Barney: (Taps a woman names Yasmine) Hi, have you met Ted? (Leaves and watches from a distance)."
50:49,1,1,1,"Ted: (To Yasmine) Hi, I'm Ted."
51:50,1,1,1,Yasmine: Yasmine.
53:52,1,1,1,"Yasmine: Thanks, It's Lebanese."
65:64,1,1,1,"[Cut to the bar, Ted is chatting with Yasmine]"
67:66,1,1,1,Yasmine: So do you think you'll ever get married?
68:67,1,1,1,"Ted: Well maybe eventually. Some fall day. Possibly in Central Park. Simple ceremony, we'll write our own vows. But--eh--no DJ, people will dance. I'm not going to worry about it! Damn it, why did Marshall have to get engaged? (Yasmine laughs) Yeah, nothing hotter than a guy planning out his own imaginary wedding, huh?"
69:68,1,1,1,"Yasmine: Actually, I think it's cute."
79:78,1,1,1,"Lily: You are unbelievable, Marshall. No-(Scene splits in half and shows both Lily and Marshall on top arguing and Ted and Yasmine on the bottom mingling)"
82:81,1,1,1,Ted: (To Yasmine) you wanna go out sometime?
85:84,1,1,1,[Cut to Scene with Ted and Yasmine at bar]
86:85,1,1,1,Yasmine: I'm sorry; Carl's my boyfriend (points to bartender)
~~~

<p>
It would be interesting to filter out the phrases which don't occur in any other episode and see what insights we get from doing that. For now though we'll extract phrases for all episodes and write to CSV so we can explore more easily:
</p>



~~~python

with open("data/import/tfidf_scikit.csv", "w") as file:
    writer = csv.writer(file, delimiter=",")
    writer.writerow(["EpisodeId", "Phrase", "Score"])

    doc_id = 0
    for doc in tfidf_matrix.todense():
        print "Document %d" %(doc_id)
        word_id = 0
        for score in doc.tolist()[0]:
            if score > 0:
                word = feature_names[word_id]
                writer.writerow([doc_id+1, word.encode("utf-8"), score])
            word_id +=1
        doc_id +=1
~~~

<p>
And finally a quick look at the contents of the CSV:
</p>



~~~bash

$ tail -n 10 data/import/tfidf_scikit.csv
208,york apparently laughs,0.012174304095213192
208,york aren,0.012174304095213192
208,york aren supposed,0.012174304095213192
208,young,0.013397275854758335
208,young ladies,0.012174304095213192
208,young ladies need,0.012174304095213192
208,young man,0.008437685963000223
208,young man game,0.012174304095213192
208,young stupid,0.011506395106658192
208,young stupid sighs,0.012174304095213192
~~~
