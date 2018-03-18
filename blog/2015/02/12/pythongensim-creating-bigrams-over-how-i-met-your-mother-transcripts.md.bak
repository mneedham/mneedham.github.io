+++
draft = false
date="2015-02-12 23:45:03"
title="Python/gensim: Creating bigrams over How I met your mother transcripts"
tag=['python']
category=['Python']
+++

<p>As part of my continued playing around with How I met your mother transcripts I wanted to identify plot arcs and as a first step I wrote some code using the <a href="https://radimrehurek.com/gensim/">gensim</a> and <a href="http://www.nltk.org/">nltk</a> libraries to identify bigrams (two word phrases).
</p>


<p>
There's an <a href="http://radimrehurek.com/gensim/models/phrases.html#module-gensim.models.phrases">easy to follow tutorial in the gensim docs</a> showing how to go about this but I needed to do a couple of extra steps to get my text data from a CSV file into the structure gensim expects.
</p>


<p>Let's first remind ourselves what the <a href="https://github.com/mneedham/neo4j-himym/blob/master/data/import/sentences.csv">sentences CSV file</a> looks like:</p>



~~~bash

$ head -n 15 data/import/sentences.csv  | tail
5,1,1,1,Son: Are we being punished for something?
6,1,1,1,Narrator: No
7,1,1,1,"Daughter: Yeah, is this going to take a while?"
8,1,1,1,"Narrator: Yes. (Kids are annoyed) Twenty-five years ago, before I was dad, I had this whole other life."
9,1,1,1,"(Music Plays, Title ""How I Met Your Mother"" appears)"
10,1,1,1,"Narrator: It was way back in 2005. I was twenty-seven just starting to make it as an architect and living in New York with my friend Marshall, my best friend from college. My life was good and then Uncle Marshall went and screwed the whole thing up."
11,1,1,1,Marshall: (Opens ring) Will you marry me.
12,1,1,1,"Ted: Yes, perfect! And then you're engaged, you pop the champagne! You drink a toast! You have s*x on the kitchen floor... Don't have s*x on our kitchen floor."
13,1,1,1,"Marshall: Got it. Thanks for helping me plan this out, Ted."
14,1,1,1,"Ted: Dude, are you kidding? It's you and Lily! I've been there for all the big moments of you and Lily. The night you met. Your first date... other first things."
~~~

<p>
We need to transform those sentences into an array of words for each line and feed it into gensim's <cite>models.Phrase</cite> object:
</p>



~~~python

import nltk
import csv
import string
from gensim.models import Phrases
from gensim.models import Word2Vec
from nltk.corpus import stopwords

sentences = []
bigram = Phrases()
with open("data/import/sentences.csv", "r") as sentencesfile:
    reader = csv.reader(sentencesfile, delimiter = ",")
    reader.next()
    for row in reader:
        sentence = [word.decode("utf-8")
                    for word in nltk.word_tokenize(row[4].lower())
                    if word not in string.punctuation]
        sentences.append(sentence)
        bigram.add_vocab([sentence])
~~~

<p>
We're used nltk's <cite>word_tokezine</cite> function to create our array of words and then we've got a clause to make sure we remove any words which are punctuation otherwise they will dominate our phrases.
</p>


<p>We can take a quick peek at some of the phrases that have been created like so:</p>



~~~python

>>> list(bigram[sentences])[:5]
[[u'pilot'], [u'scene', u'one'], [u'title', u'the', u'year_2030'], [u'narrator_kids', u'i', u"'m", u'going', u'to', u'tell', u'you', u'an_incredible', u'story.', u'the', u'story', u'of', u'how', u'i', u'met_your', u'mother'], [u'son', u'are', u'we', u'being', u'punished', u'for', u'something']]
~~~

<p>gensim uses an underscore character to indicate when it's joined two words together and in this sample we've got three phrases - 'narrator_kids', 'met_you' and 'an_incredible'.
</p>


<p>We can now populate a Counter with our phrases and their counts and find out the most common phrases. One thing to note is that I've chosen to get rid of stopwords at this point rather than earlier because I didn't want to generate 'false bigrams' where there was actually a stop word sitting in between.</p>



~~~python

bigram_counter = Counter()
for key in bigram.vocab.keys():
    if key not in stopwords.words("english"):
        if len(key.split("_")) > 1:
            bigram_counter[key] += bigram.vocab[key]

for key, counts in bigram_counter.most_common(20):
    print '{0: <20} {1}'.format(key.encode("utf-8"), counts)

i_'m                 4607
it_'s                4288
you_'re              2659
do_n't               2436
that_'s              2044
in_the               1696
gon_na               1576
you_know             1497
i_do                 1464
this_is              1407
and_i                1389
want_to              1071
it_was               1053
on_the               1052
at_the               1035
we_'re               1033
i_was                1018
of_the               1014
ca_n't               1010
are_you              994
~~~

<p>Most of the phrases aren't really that interesting and I had better luck feeding the phrases into a Word2Vec model and repeating the exercise:
</p>



~~~python

bigram_model = Word2Vec(bigram[sentences], size=100)
bigram_model_counter = Counter()
for key in bigram_model.vocab.keys():
    if key not in stopwords.words("english"):
        if len(key.split("_")) > 1:
            bigram_model_counter[key] += bigram_model.vocab[key].count

for key, counts in bigram_model_counter.most_common(50):
    print '{0: <20} {1}'.format(key.encode("utf-8"), counts)

do_n't               2436
gon_na               1576
ca_n't               1010
did_n't              704
come_on              499
end_of               460
kind_of              396
from_2030            394
my_god               360
they_'re             351
'm_sorry             349
does_n't             341
end_flashback        327
all_right            308
've_been             303
'll_be               301
of_course            289
a_lot                284
right_now            279
new_york             270
look_at              265
trying_to            238
tell_me              196
a_few                195
've_got              189
wo_n't               174
so_much              172
got_ta               168
each_other           166
my_life              157
talking_about        157
talk_about           154
what_happened        151
at_least             141
oh_god               138
wan_na               129
supposed_to          126
give_me              124
last_night           121
my_dad               120
more_than            119
met_your             115
excuse_me            112
part_of              110
phone_rings          109
get_married          107
looks_like           105
'm_sorry.            104
said_``              101
~~~

<p>The first 20 phrases or so aren't particularly interesting although we do have 'new_york' in there which is good as that's where the show is set. If we go further we'll notice phrases like 'my_dad', 'get_married' and 'last_night' which may all explain interesting parts of the plot.</p>


<p>Having the data in the Word2Vec model allows us to do some other fun queries too. e.g.</p>



~~~python

>>> bigram_model.most_similar(['marshall', 'lily'], ['ted'], topn=10)
[(u'robin', 0.5474381446838379), (u'go_ahead', 0.5138797760009766), (u'zoey', 0.505358874797821), (u'karen', 0.48617005348205566), (u'cootes', 0.4757827818393707), (u'then', 0.45426881313323975), (u'lewis', 0.4510520100593567), (u'natalie.', 0.45070385932922363), (u'vo', 0.4189065098762512), (u'players', 0.4149518311023712)]

>>> bigram_model.similarity("ted", "robin")
0.51928683064927905

>>> bigram_model.similarity("barney", "robin")
0.62980405583219112

>>> bigram_model.most_similar(positive=['getting_married'])
[(u'so_glad', 0.780311107635498), (u'kidding', 0.7683225274085999), (u'awake', 0.7682262659072876), (u'lunch.', 0.7591195702552795), (u'ready.', 0.7372316718101501), (u'single.', 0.7350872755050659), (u'excited_about', 0.725479006767273), (u'swamped', 0.7252731323242188), (u'boyfriends', 0.7127221822738647), (u'believe_this.', 0.71015864610672)]

>>> bigram_model.most_similar(positive=['my_dad'])
[(u'my_mom', 0.7994954586029053), (u'somebody', 0.7758427262306213), (u'easier', 0.7305313944816589), (u'hot.', 0.7282992601394653), (u'pregnant.', 0.7103987336158752), (u'nobody', 0.7059557437896729), (u'himself.', 0.7046393156051636), (u'physically', 0.7044381499290466), (u'young_lady', 0.69412761926651), (u'at_bernie', 0.682607889175415)]
~~~

<p>
I'm not quite at the stage where I can automatically pull out the results of a gensim model and do something with it but it is helping me to see some of the main themes in the show.
</p>


<p>Next up I'll try out trigrams and then TF/IDF over the bigrams to see which are the most important on a per episode basis. I also need to dig into Word2Vec to figure out why it comes up with different top phrases than the Phrases model.</p>

