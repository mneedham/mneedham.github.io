+++
draft = false
date="2016-07-27 02:45:28"
title="scikit-learn: TF/IDF and cosine similarity for computer science papers"
tag=['python']
category=['Python']
+++

<p>
A couple of months ago I downloaded the meta data for a few thousand computer science papers so that I could try and write a mini recommendation engine to tell me what paper I should read next.
</p>


<p>
Since I don't have any data on which people read each paper a collaborative filtering approach is ruled out, so instead I thought I could try content based filtering instead.
</p>


<p>
Let's quickly check the <a href="https://en.wikipedia.org/wiki/Recommender_system#Content-based_filtering">Wikipedia definition of content based filtering</a>:
</p>



<blockquote>
In a content-based recommender system, keywords are used to describe the items and a user profile is built to indicate the type of item this user likes. 

In other words, these algorithms try to recommend items that are similar to those that a user liked in the past (or is examining in the present).
</blockquote>

<p>
We're going to focus on the finding similar items part of the algorithm and we'll start simple by calculating the similarity of items based on their titles. We'd probably get better results if we used the full text of the papers or at least the abstracts but that data isn't as available.
</p>


<p>
We're going to take the following approach to work out the similarity between any pair of papers:
</p>



~~~text

for each paper:
  generate a TF/IDF vector of the terms in the paper's title
  calculate the cosine similarity of each paper's TF/IDF vector with every other paper's TF/IDF vector
~~~

<p>
This is very easy to do using the Python scikit-learn library and I've actually done the first part of the process while doing some <a href="http://www.markhneedham.com/blog/2015/02/15/pythonscikit-learn-calculating-tfidf-on-how-i-met-your-mother-transcripts/">exploratory analysis of interesting phrases in the TV show How I Met Your Mother</a>.
</p>


<p>
Let's get started. 
</p>


<p>
We've got one file per paper which contains the title of the paper. We first need to iterate through that directory and build an array containing the papers:
</p>



~~~python

import glob

corpus = []
for file in glob.glob("papers/*.txt"):
    with open(file, "r") as paper:
        corpus.append((file, paper.read()))
~~~

<p>
Next we'll build a TF/IDF matrix for each paper:
</p>



~~~python

from sklearn.feature_extraction.text import TfidfVectorizer

tf = TfidfVectorizer(analyzer='word', ngram_range=(1,3), min_df = 0, stop_words = 'english')
tfidf_matrix =  tf.fit_transform([content for file, content in corpus])
~~~

<p>
Next we'll write a function that will find us the top n similar papers based on cosine similarity:
</p>




~~~python

from sklearn.metrics.pairwise import linear_kernel

def find_similar(tfidf_matrix, index, top_n = 5):
    cosine_similarities = linear_kernel(tfidf_matrix[index:index+1], tfidf_matrix).flatten()
    related_docs_indices = [i for i in cosine_similarities.argsort()[::-1] if i != index]
    return [(index, cosine_similarities[index]) for index in related_docs_indices][0:top_n]
~~~

<p>Let's try it out:</p>



~~~python

>>> corpus[1619]
('papers/221215.txt', 'TOTEM: a reliable ordered delivery protocol for interconnected local-area networks')

>>> for index, score in find_similar(tfidf_matrix, 1619):
       print score, corpus[index]

0.917540397202 ('papers/852338.txt', 'A reliable ordered delivery protocol for interconnected local area networks')
0.248736845733 ('papers/800897.txt', 'Interconnection of broadband local area networks')
0.207309089025 ('papers/103726.txt', 'High-speed local area networks and their performance: a survey')
0.204166719869 ('papers/161736.txt', 'High-speed switch scheduling for local-area networks')
0.198514433132 ('papers/627363.txt', 'Algorithms for Distributed Query Processing in Broadcast Local Area Networks')
~~~

<p>It's pretty good for finding duplicate papers!</p>



~~~python

>>> corpus[1599]
('papers/217470.txt', 'A reliable multicast framework for light-weight sessions and application level framing')

>>> for index, score in find_similar(tfidf_matrix, 1599):
       print score, corpus[index]

1.0            ('papers/270863.txt', 'A reliable multicast framework for light-weight sessions and application level framing')
0.139643354066 ('papers/218325.txt', 'The KryptoKnight family of light-weight protocols for authentication and key distribution')
0.134763799612 ('papers/1251445.txt', 'ALMI: an application level multicast infrastructure')
0.117630311817 ('papers/125160.txt', 'Ordered and reliable multicast communication')
0.117630311817 ('papers/128741.txt', 'Ordered and reliable multicast communication')
~~~

<p>But sometimes it identifies duplicates that aren't identical:
</p>



~~~python

>>> corpus[5784]
('papers/RFC2616.txt', 'Hypertext Transfer Protocol -- HTTP/1.1')

>>> for index, score in find_similar(tfidf_matrix, 5784):
       print score, corpus[index]

1.0 ('papers/RFC1945.txt', 'Hypertext Transfer Protocol -- HTTP/1.0')
1.0 ('papers/RFC2068.txt', 'Hypertext Transfer Protocol -- HTTP/1.1')
0.232865694216 ('papers/131844.txt', 'XTP: the Xpress Transfer Protocol')
0.138876842331 ('papers/RFC1866.txt', 'Hypertext Markup Language - 2.0')
0.104775586915 ('papers/760249.txt', 'On the transfer of control between contexts')
~~~

<p>
Having said that, if you were reading and liked the HTTP 1.0 RFC the HTTP 1.1 RFC probably isn't a bad recommendation. 
</p>


<p>There are obviously also some papers that get identified as being similar which aren't. I created <a href="https://github.com/mneedham/computer-science-papers/blob/master/similarities.csv">a CSV file</a> containing 5 similar papers for each paper as long as the similarity is greater than 0.5. You can see <a href="https://github.com/mneedham/computer-science-papers/blob/master/most_similar.py">the script that generates that file</a> on github as well.
</p>


<p>
That's as far as I've got for now but there are a couple of things I'm going to explore next:
</p>


<ul>
<li>How do we know if the similarity suggestions are any good? How do we measure good? Would using a term counting vector work better than TF/IDF?</li>
<li>
Similarity based on abstracts as well as/instead of titles
</li>
</ul>

<p>
<a href="https://github.com/mneedham/computer-science-papers/blob/master/similarity.py">All the code from this post</a> for calculating similarities and writing them to CSV is on github as well so feel free to play around with it.
</p>

