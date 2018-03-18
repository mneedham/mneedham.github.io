+++
draft = false
date="2012-11-24 19:43:32"
title="A first failed attempt at Natural Language Processing"
tag=['machine-learning-2']
category=['Machine Learning']
+++

One of the things I find fascinating about dating websites is that the profiles of people are almost identical so I thought it would be an interesting exercise to grab some of the free text that people write about themselves and prove the similarity.

I'd been talking to <a href="https://twitter.com/mattb">Matt Biddulph</a> about some Natural Language Processing (NLP) stuff he'd been working on and he wrote up a <a href="https://gist.github.com/3888345">bunch of libraries, articles and books that he'd found useful</a>. 

I started out by plugging the text into one of the many NLP libraries that Matt listed with the vague idea that it would come back with something useful. 

I'm not sure exactly what I was expecting the result to be but after 5/6 hours of playing around with different libraries I'd got nowhere and parked the problem not really knowing where I'd gone wrong.

Last week I came across a paper titled "<a href="http://people.cs.umass.edu/~brun/pubs/pubs/Kiddon11.pdf">That’s What She Said: Double Entendre Identiﬁcation</a>" whose authors wanted to work out when a sentence could legitimately be followed by the phrase "that's what she said".

While the subject matter is a bit risque I found that reading about the way the authors went about solving their problem was very interesting and it allowed me to see some mistakes I'd made.

<h4>Vague problem statement</h4>
Unfortunately I didn't do a good job of working out exactly what problem I wanted to solve - my problem statement was too general. 

In the paper the authors narrowed down their problem space by focusing on a specific set of words which are typically used as double entendres and then worked out the sentence structure that the targeted sentences were likely to have.

Instead of defining my problem more specifically I plugged the text into <a href="http://mallet.cs.umass.edu/topics-devel.php">Mallet</a>, <a href="http://mvnrepository.com/artifact/edu.washington.cs.knowitall/morpha-stemmer">morpha-stemmer</a> and <a href="https://github.com/louismullie/stanford-core-nlp">Stanford Core NLP</a> and tried to cluster the most popular words.

That didn't really work because people use slightly different words to describe the same thing so I ended up looking at <a href="http://www.yawni.org/wiki/Main/WhatsWordNet">Yawni</a> - a wrapper around <a href="http://wordnet.princeton.edu/">WordNet</a> which groups sets of words into cognitive synonyms. 

In hindsight a more successful approach might have been to find the common words that people tend to use in these types of profiles and then work from there.

<h4>No Theory</h4>

I recently wrote about how I've been <a href="http://www.markhneedham.com/blog/2012/11/19/learning-switching-between-theory-and-practice/">learning about neural networks by switching in between theory and practice</a> but with NLP I didn't bother reading any of the theory and thought I could get away with plugging some data into one of the libraries.

I now realise that was a mistake as I didn't know what to do when the libraries didn't work as I'd hoped because I wasn't sure what they were supposed to be doing in the first place!

My next step should probably be to understand <a href="http://en.wikipedia.org/wiki/Vector_space_model">how text gets converted into vectors</a>, then move onto <a href="http://en.wikipedia.org/wiki/Tf%E2%80%93idf">tf-idf</a> and see if I have a better idea of how to solve my problem.
