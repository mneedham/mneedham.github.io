+++
draft = false
date="2015-01-19 00:24:23"
title="Python/NLTK: Finding the most common phrases in How I Met Your Mother"
tag=['python']
category=['Python']
+++

<p>

Following on from <a href="http://www.markhneedham.com/blog/2015/01/10/python-nltkneo4j-analysing-the-transcripts-of-how-i-met-your-mother/">last week's blog post</a> where I found the most popular words in How I met your mother transcripts, in this post we'll have a look at how we can pull out sentences and then phrases from our corpus.

</p>

The first thing I did was tweak the scraping script to pull out the sentences spoken by characters in the transcripts.</p>
 

<p>Each dialogue is separated by two line breaks so we use that as our separator. I also manually skimmed through the transcripts and found out which tags we need to strip out. I ended up with the following:
</p>



~~~python

import csv
import nltk
import re
import bs4

from bs4 import BeautifulSoup, NavigableString
from soupselect import select
from nltk.corpus import stopwords
from collections import Counter
from nltk.tokenize import word_tokenize

episodes_dict = {}

def strip_tags(soup, invalid_tags):
    for tag in invalid_tags:
        for match in soup.findAll(tag):
            match.replaceWithChildren()
    return soup

def extract_sentences(html):
    clean = []
    brs_in_a_row = 0
    temp = ""
    for item in raw_text.contents:
        if item.name == "br":
            brs_in_a_row = brs_in_a_row + 1
        else:
            temp = temp + item
        if brs_in_a_row == 2:
            clean.append(temp)
            temp = ""
            brs_in_a_row = 0
    return clean

speakers = []
with open('data/import/episodes.csv', 'r') as episodes_file, \
     open("data/import/sentences.csv", 'w') as sentences_file:
    reader = csv.reader(episodes_file, delimiter=',')
    reader.next()

    writer = csv.writer(sentences_file, delimiter=',')
    writer.writerow(["SentenceId", "EpisodeId", "Season", "Episode", "Sentence"])
    sentence_id = 1

    for row in reader:
        transcript = open("data/transcripts/S%s-Ep%s" %(row[3], row[1])).read()
        soup = BeautifulSoup(transcript)
        rows = select(soup, "table.tablebg tr td.post-body div.postbody")

        raw_text = rows[0]
        [ad.extract() for ad in select(raw_text, "div.ads-topic")]
        [ad.extract() for ad in select(raw_text, "div.t-foot-links")]
        [ad.extract() for ad in select(raw_text, "hr")]

        for tag in ['strong', 'em', "a"]:
            for match in raw_text.findAll(tag):
                match.replace_with_children()
        print row
        for sentence in [
                item.encode("utf-8").strip()
                for item in extract_sentences(raw_text.contents)
            ]:
            writer.writerow([sentence_id, row[0], row[3], row[1], sentence])
            sentence_id = sentence_id + 1
~~~

<p>
Here's a preview of the sentences CSV file:
</p>



~~~python

$ head -n 10 data/import/sentences.csv
SentenceId,EpisodeId,Season,Episode,Sentence
1,1,1,1,Pilot
2,1,1,1,Scene One
3,1,1,1,[Title: The Year 2030]
4,1,1,1,"Narrator: Kids, I'm going to tell you an incredible story. The story of how I met your mother"
5,1,1,1,Son: Are we being punished for something?
6,1,1,1,Narrator: No
7,1,1,1,"Daughter: Yeah, is this going to take a while?"
8,1,1,1,"Narrator: Yes. (Kids are annoyed) Twenty-five years ago, before I was dad, I had this whole other life."
9,1,1,1,"(Music Plays, Title ""How I Met Your Mother"" appears)"
~~~

<p>
The next step is to iterate through each of those sentences and create some <a href="http://www.nltk.org/_modules/nltk/util.html">n-grams</a> to capture the common phrases in the transcripts.
</p>


<blockquote>
In the fields of computational linguistics and probability, an n-gram is a contiguous sequence of n items from a given sequence of text or speech.
</blockquote>

<p>
Python's <a href="http://www.nltk.org/">nltk</a> library has a function that makes this easy e.g.
</p>



~~~python

>>> import nltk
>>> tokens = nltk.word_tokenize("I want to be in an n gram")
>>> tokens
['I', 'want', 'to', 'be', 'in', 'an', 'n', 'gram']
>>> nltk.util.ngrams(tokens, 2)
[('I', 'want'), ('want', 'to'), ('to', 'be'), ('be', 'in'), ('in', 'an'), ('an', 'n'), ('n', 'gram')]
>>> nltk.util.ngrams(tokens, 3)
[('I', 'want', 'to'), ('want', 'to', 'be'), ('to', 'be', 'in'), ('be', 'in', 'an'), ('in', 'an', 'n'), ('an', 'n', 'gram')]
~~~

<p>
If we do a similar thing of HIMYM transcripts while stripping out the speaker's name - lines are mostly in the form "Speaker:Sentence" - we end up with the following top phrases:
</p>



~~~python

import nltk
import csv
import string
import re

from collections import Counter

non_speaker = re.compile('[A-Za-z]+: (.*)')

def extract_phrases(text, phrase_counter, length):
    for sent in nltk.sent_tokenize(text):
        strip_speaker = non_speaker.match(sent)
        if strip_speaker is not None:
            sent = strip_speaker.group(1)
        words = nltk.word_tokenize(sent)
        for phrase in nltk.util.ngrams(words, length):
            phrase_counter[bphrase] += 1
                
phrase_counter = Counter()

with open("data/import/sentences.csv", "r") as sentencesfile:
    reader = csv.reader(sentencesfile, delimiter=",")
    reader.next()
    for sentence in reader:
        extract_phrases(sentence[4], phrase_counter, 3)

most_common_phrases = phrase_counter.most_common(50)
for k,v in most_common_phrases:
    print '{0: <5}'.format(v), k
~~~

<p>And if we run that:</p>



~~~bash

$ python extract_phrases.py
1123  (',', 'I', "'m")
1099  ('I', 'do', "n't")
1005  (',', 'it', "'s")
535   ('I', 'ca', "n't")
523   ('I', "'m", 'not')
507   ('I', 'mean', ',')
507   (',', 'you', "'re")
459   (',', 'that', "'s")
458   ('2030', ')', ':')
454   ('(', '2030', ')')
453   ('Ted', '(', '2030')
449   ('I', "'m", 'sorry')
...
247   ('I', 'have', 'to')
247   ('No', ',', 'I')
246   ("'s", 'gon', 'na')
241   (',', 'I', "'ll")
229   ('I', "'m", 'going')
226   ('do', "n't", 'want')
226   ('It', "'s", 'not')
~~~

<p>I noticed that quite a few of the phrases had punctuation in so my next step was to get rid of any of the phrases that had any punctuation in. I updated <cite>extract_phrases</cite> like so:</p>



~~~python

def extract_phrases(text, phrase_counter, length):
    for sent in nltk.sent_tokenize(text):
        strip_speaker = non_speaker.match(sent)
        if strip_speaker is not None:
            sent = strip_speaker.group(1)
        words = nltk.word_tokenize(sent)
        for phrase in nltk.util.ngrams(words, length):
            if all(word not in string.punctuation for word in phrase):
                phrase_counter[phrase] += 1
~~~

<p>
Let's run it again:
</p>



~~~bash

$ python extract_phrases.py
1099  ('I', 'do', "n't")
535   ('I', 'ca', "n't")
523   ('I', "'m", 'not')
449   ('I', "'m", 'sorry')
414   ('do', "n't", 'know')
383   ('Ted', 'from', '2030')
338   ("'m", 'gon', 'na')
334   ('I', "'m", 'gon')
300   ('gon', 'na', 'be')
279   ('END', 'OF', 'FLASHBACK')
267   ("'re", 'gon', 'na')
...
155   ('It', "'s", 'just')
151   ('at', 'the', 'bar')
150   ('a', 'lot', 'of')
147   ("'re", 'going', 'to')
144   ('I', 'have', 'a')
142   ('I', "'m", 'so')
138   ('do', "n't", 'have')
137   ('I', 'think', 'I')
136   ('not', 'gon', 'na')
136   ('I', 'can', 'not')
135   ('and', 'I', "'m")
~~~

<p>Next I wanted to display each phrase as a string rather than a tuple which was <a href="http://stackoverflow.com/questions/21948019/python-untokenize-a-sentence">more difficult than I expected</a>. I ended up with the following function which almost does the job:</p>



~~~python

def untokenize(ngram):
    tokens = list(ngram)
    return "".join([" "+i if not i.startswith("'") and \
                             i not in string.punctuation and \
                             i != "n't"
                          else i for i in tokens]).strip()
~~~

<p>I updated <cite>extract_phrases</cite> to use that function:</p>



~~~python

def extract_phrases(text, phrase_counter, length):
    for sent in nltk.sent_tokenize(text):
        strip_speaker = non_speaker.match(sent)
        if strip_speaker is not None:
            sent = strip_speaker.group(1)
        words = nltk.word_tokenize(sent)
        for phrase in nltk.util.ngrams(words, length):
            if all(word not in string.punctuation for word in phrase):
                phrase_counter[untokenize(phrase)] += 1
~~~

<p>Let's go again:</p>



~~~bash

$ python extract_phrases.py
1099  I don't
535   I can't
523   I'm not
449   I'm sorry
414   don't know
383   Ted from 2030
338   'm gon na
334   I'm gon
300   gon na be
279   END OF FLASHBACK
...
151   at the bar
150   a lot of
147   're going to
144   I have a
142   I'm so
138   don't have
137   I think I
136   not gon na
136   I can not
135   and I'm
~~~

<p>
These were some of the interesting things that stood out for me and deserve further digging into:
</p>


<ul>
<li>
A lot of the most popular phrases begin with 'I' - it would be interesting to filter those sentences to find the general sentiment.
</li>
<li>The 'untokenize' function struggles to reconstruct the slang phrase 'gonna' into a single word.</li>
<li>'Ted from 2030' is actually a speaker which doesn't follow the expected regex pattern and so wasn't filtered out.</li>
<li>
'END OF FLASHBACK' shows quite high up and pulling out those flashbacks would probably be an interesting feature to extract to see which episodes reference each other.
</li>
<li>'Marshall and Lily' and 'Lily and Marshall' show up on the list - it would be interesting to explore the frequency of pairs of other characters.</li>
</ul>

<p>The <a href="https://github.com/mneedham/neo4j-himym">code is all on github</a> if you want to play with it.</p>

