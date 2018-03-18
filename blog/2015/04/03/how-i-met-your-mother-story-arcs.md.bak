+++
draft = false
date="2015-04-03 23:31:33"
title="How I met your mother: Story arcs"
tag=['machine-learning-2']
category=['Machine Learning']
+++

<p>
After weeks of playing around with various algorithms to extract story arcs in How I met your mother I've come to the conclusion that I don't yet have the skills to completely automate this process so I'm going to change my approach.
</p>


<p>
The new plan is to treat the outputs of the algorithms as suggestions for possible themes but then have a manual step where I extract what I think are interesting themes in the series.
</p>


<p>
A theme can consist of a single word or a phrase and the idea is that once a story arc is identified we'll search over the corpus and find the episodes where that phrase occurs.
</p>


<p>We can then generate a CSV file of (story arc) -> (episodeId), store that into our HIMYM graph and use the story arc as another factor for episode similarity.</p>


<p>I ended up with the following script to work out <a href="https://raw.githubusercontent.com/mneedham/neo4j-himym/master/data/import/sentences.csv">which episodes contained a story arc</a>:</p>



~~~bash

#!/bin/bash

find_term() {
  arc=${1}
  searchTerm=${2}
  episodes=$(grep --color -iE "${searchTerm}" data/import/sentences.csv | awk -F"," '{ print $2  }' | sort | uniq)
  for episode in ${episodes}; do
    echo ${arc},${episode}
  done
}

find_term "Bro Code" "bro code"
find_term "Legendary" "legen(.*)ary"
find_term "Slutty Pumpkin" "slutty pumpkin"
find_term "Magician's Code" "magician's code"
find_term "Thanksgiving" "thanksgiving"
find_term "The Playbook" "playbook"
find_term "Slap Bet" "slap bet"
find_term "Wrestlers and Robots" "wrestlers"
find_term "Robin Sparkles" "sparkles"
find_term "Blue French Horn" "blue french horn"
find_term "Olive Theory" "olive"
find_term "Thank You Linus" "thank you, linus"
find_term "Have you met...?" "have you met"
find_term "Laser Tag" "laser tag"
find_term "Goliath National Bank" "goliath national bank"
find_term "Challenge Accepted" "challenge accepted"
find_term "Best Man" "best man"
~~~

<p>
If we run this script we'll see something like the following:
</p>



~~~bash

$ ./scripts/arcs.sh
Bro Code,14
Bro Code,155
Bro Code,170
Bro Code,188
Bro Code,201
Bro Code,61
Bro Code,64
Legendary,117
Legendary,120
Legendary,122
Legendary,136
Legendary,137
Legendary,15
Legendary,152
Legendary,157
Legendary,162
Legendary,171
...
Best Man,208
Best Man,30
Best Man,32
Best Man,41
Best Man,42
~~~

<p>
I pulled out these themes by eyeballing the output of the following scripts:
</p>


<ul>
<li>
<a href="https://github.com/mneedham/neo4j-himym/blob/master/scripts/scikit_ngram.py">TF/IDF</a> - calculates TF/IDF scores for ngrams. This helps find important themes in the context of a single episode. I then did some manual searching to see how many of those themes existed in other episodes
</li>
<li><a href="https://github.com/mneedham/neo4j-himym/blob/master/scripts/tfidf_special.py">Weighted Term Frequency</a> - this returns a weighted term frequency for ngrams of different lengths. The weights are determined by the <a href="http://www.markhneedham.com/blog/2015/03/30/python-creating-a-skewed-random-discrete-distribution/">skewed random discrete distribution I wrote about earlier in the week</a>. I ran it with different skews and ngram lengths.</li>

<li>
<a href="https://github.com/mneedham/topic-modelling-mallet/blob/master/ner.py">Named entity extraction</a> - this pulls out any phrases that are named entities. It mostly pulled out names of people (which I used as a stop word list in some other algorithms) but also revealed a couple of themes.
</li>
<li>
<a href="https://github.com/mneedham/topic-modelling-mallet/blob/master/train_himym.sh">Topic modelling</a> - I used <a href="http://mallet.cs.umass.edu/">mallet</a> to extract topics across the corpus. Most of them didn't make much sense to me but there were a few which identified themes that I recognised.
</li>
</ul>

<p>
I can't remember off the top of my head if any obvious themes have been missed so if you know HIMYM better than me let me know and I'll try and work out why those didn't surface.
</p>


<p>
Next I want to see how these scripts fare against some other TV shows and see how quickly I can extract themes for those. It'd also be cool if I can make the whole process a bit more automated.
</p>

