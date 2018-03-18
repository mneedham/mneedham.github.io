+++
draft = false
date="2013-11-29 19:50:53"
title="Neo4j: What is a node?"
tag=['neo4j']
category=['neo4j']
+++

<p>One of the first things I needed to learn when I started using Neo4j was how to model my domain using nodes and relationships and it wasn't initially obvious to me what things should be nodes.</p>
 

<p>Luckily <a href="https://twitter.com/iansrobinson">Ian Robinson</a> showed me a mini-algorithm which I found helpful for getting started. The steps are as follows:</p>


<ol>
<li>Write out the questions you want to ask</li>
<li>Highlight/underline the nouns</li>
<li>Those are your nodes!</li>
</ol>

<p>This is reasonably similar to the way that we work out what our objects should be when we're doing OO modelling and I thought I'd give it a try on some of the data sets that I've worked with recently:</p>



<ul>
<li>Female <strong>friends</strong> of friends that somebody could go out with</li>
<li><strong>Goals</strong> scored by <strong>Arsenal</strong> <strong>players</strong> in a particular <strong>season</strong></li>
<li><strong>Colleagues</strong> who have similar <strong>skills</strong> to me</li>
<li><strong>Episodes</strong> of a <strong>TV program</strong> that a particular <strong>actor</strong> appeared in</li>
<li><strong>Customers</strong> who would be affected if a piece of <strong>equipment</strong> went in for repair</li>
</ul>

<p>If you're like me and aren't that great at English grammar we can always cheat and get <a href="http://nltk.org/book/ch05.html">NLTK</a> to help us out:</p>



~~~python

>>> nltk.pos_tag(nltk.word_tokenize("Female friends of friends that somebody could go out with"))
[('Female', 'NNP'), ('friends', 'NNS'), ('of', 'IN'), ('friends', 'NNS'), ('that', 'WDT'), ('somebody', 'NN'), ('could', 'MD'), ('go', 'VB'), ('out', 'RP'), ('with', 'IN')]
~~~

<p>That tells us the likely tag for each part of speech in the sentence and we can filter the resulting list so we only see nouns like this:</p>



~~~python

>>> nouns = ['NNS', 'NN', 'NP', 'NNP']
>>> [(word, grammar) for (word, grammar) in nltk.pos_tag(nltk.word_tokenize("Female friends of friends that somebody could go out with")) if grammar in nouns]
[('Female', 'NNP'), ('friends', 'NNS'), ('friends', 'NNS'), ('somebody', 'NN')]
~~~

<p>We can ignore the 'Female' in this sentence (I think it's been picked up as a proper noun because of the capitalisation) which leaves us with 'friends' and 'somebody' In both cases these nouns represent the concept of a person so we'd want to create nodes representing people in this domain.</p>


<p>Let's see how NLTK gets on with our second question:</p>



~~~python

>>> sentence = "Goals scored by Arsenal players in a particular season"
>>> [(word, grammar) for (word, grammar) in nltk.pos_tag(nltk.word_tokenize(sentence)) if grammar in ['NNS', 'NN', 'NP']]
[('Goals', 'NNS'), ('Arsenal', 'NNP'), ('players', 'NNS'), ('season', 'NN')]
~~~

<p>In this case we'd have goals, teams (e.g. Arsenal), players and seasons as our nodes.</p>


<p>Although this is a very rough algorithm for working out what things should be nodes in a graph I think it's a good way to get started.</p>
 

<p>After that the other queries we want to write may lead us to change the model to solve our problem even better.</p>

