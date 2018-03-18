+++
draft = false
date="2015-03-01 02:36:06"
title="Python: Detecting the speaker in HIMYM using Parts of Speech (POS) tagging"
tag=['python']
category=['Python']
+++

<p>
Over the last couple of weeks I've been experimenting with <a href="http://www.markhneedham.com/blog/2015/02/20/pythonscikit-learn-detecting-which-sentences-in-a-transcript-contain-a-speaker/">different</a> <a href="http://www.markhneedham.com/blog/2015/02/24/pythonnltk-naive-vs-naive-bayes-vs-decision-tree/">classifiers</a> to detect speakers in HIMYM transcripts and in all my attempts so far the only features I've used have been words.
</p>


<p>
This led to classifiers that were overfitted to the training data so I wanted to generalise them by introducing parts of speech of the words in sentences which are more generic.
</p>


<p>
First I changed the function which generates the features for each word to also contain the parts of speech of the previous and next words as well as the word itself:
</p>



~~~python

def pos_features(sentence, sentence_pos, i):
    features = {}

    features["word"] = sentence[i]
    features["word-pos"] = sentence_pos[i][1]

    if i == 0:
        features["prev-word"] = "<START>"
        features["prev-word-pos"] = "<START>"
    else:
        features["prev-word"] = sentence[i-1]
        features["prev-word-pos"] = sentence_pos[i-1][1]

    if i == len(sentence) - 1:
        features["next-word"] = "<END>"
        features["next-word-pos"] = "<END>"
    else:
        features["next-word"] = sentence[i+1]
        features["next-word-pos"] = sentence_pos[i+1][1]

    return features

~~~

<p>
Next we need to tweak our calling code to calculate the parts of speech tags for each sentence and pass it in:
</p>



~~~python

featuresets = []
for tagged_sent in tagged_sents:
    untagged_sent = nltk.tag.untag(tagged_sent)
    sentence_pos = nltk.pos_tag(untagged_sent)
    for i, (word, tag) in enumerate(tagged_sent):
        featuresets.append((pos_features(untagged_sent, sentence_pos, i), tag) )
~~~

<p>
I'm using nltk to do this and although it's <a href="https://honnibal.wordpress.com/2013/09/11/a-good-part-of-speechpos-tagger-in-about-200-lines-of-python/">slower than some alternatives</a>, the data set is small enough that it's not an issue.
</p>


<p>Now it's time to train a Decision Tree with the new features. I created three variants - one with both words and POS; one with only words; one with only POS.</p>


<p>
I took a deep copy of the training/test data sets and then removed the appropriate keys:
</p>



~~~python

def get_rid_of(entry, *keys):
    for key in keys:
        del entry[key]

import copy

# Word based classifier
tmp_train_data = copy.deepcopy(train_data)
for entry, tag in tmp_train_data:
    get_rid_of(entry, 'prev-word-pos', 'word-pos', 'next-word-pos')

tmp_test_data = copy.deepcopy(test_data)
for entry, tag in tmp_test_data:
    get_rid_of(entry, 'prev-word-pos', 'word-pos', 'next-word-pos')

c = nltk.DecisionTreeClassifier.train(tmp_train_data)
c.classify(tmp_test_data)

# POS based classifier
tmp_train_data = copy.deepcopy(train_data)
for entry, tag in tmp_train_data:
    get_rid_of(entry, 'prev-word', 'word', 'next-word')

tmp_test_data = copy.deepcopy(test_data)
for entry, tag in tmp_test_data:
    get_rid_of(entry, 'prev-word', 'word', 'next-word')

c = nltk.DecisionTreeClassifier.train(tmp_train_data)
c.classify(tmp_test_data)
~~~

<p>The <a href="https://github.com/mneedham/neo4j-himym/blob/bae87fb6cea228bcd4ee8b4b406bf18c605c6834/scripts/detect_speaker.py">full code is on my github</a> but these were the results I saw:</p>



~~~bash

$ time python scripts/detect_speaker.py
Classifier              speaker precision    speaker recall    non-speaker precision    non-speaker recall
--------------------  -------------------  ----------------  -----------------------  --------------------
Decision Tree All In             0.911765          0.939394                 0.997602              0.996407
Decision Tree Words              0.911765          0.939394                 0.997602              0.996407
Decision Tree POS                0.90099           0.919192                 0.996804              0.996008
~~~

<p>
There's still not much in it - the POS one has slightly more false positives and false positives when classifying speakers but on other runs it performed better.
</p>


<p>
If we take a look at the decision tree that's been built for the POS one we can see that it's all about POS now as you'd expect:
</p>



~~~python

>>> print(c.pseudocode(depth=2))
if next-word-pos == '$': return False
if next-word-pos == "''": return False
if next-word-pos == ',': return False
if next-word-pos == '-NONE-': return False
if next-word-pos == '.': return False
if next-word-pos == ':':
  if prev-word-pos == ',': return False
  if prev-word-pos == '.': return False
  if prev-word-pos == ':': return False
  if prev-word-pos == '<START>': return True
  if prev-word-pos == 'CC': return False
  if prev-word-pos == 'CD': return False
  if prev-word-pos == 'DT': return False
  if prev-word-pos == 'IN': return False
  if prev-word-pos == 'JJ': return False
  if prev-word-pos == 'JJS': return False
  if prev-word-pos == 'MD': return False
  if prev-word-pos == 'NN': return False
  if prev-word-pos == 'NNP': return False
  if prev-word-pos == 'NNS': return False
  if prev-word-pos == 'POS': return False
  if prev-word-pos == 'PRP': return False
  if prev-word-pos == 'PRP$': return False
  if prev-word-pos == 'RB': return False
  if prev-word-pos == 'RP': return False
  if prev-word-pos == 'TO': return False
  if prev-word-pos == 'VB': return False
  if prev-word-pos == 'VBD': return False
  if prev-word-pos == 'VBG': return False
  if prev-word-pos == 'VBN': return True
  if prev-word-pos == 'VBP': return False
  if prev-word-pos == 'VBZ': return False
if next-word-pos == '<END>': return False
if next-word-pos == 'CC': return False
if next-word-pos == 'CD':
  if word-pos == '$': return False
  if word-pos == ',': return False
  if word-pos == ':': return True
  if word-pos == 'CD': return True
  if word-pos == 'DT': return False
  if word-pos == 'IN': return False
  if word-pos == 'JJ': return False
  if word-pos == 'JJR': return False
  if word-pos == 'JJS': return False
  if word-pos == 'NN': return False
  if word-pos == 'NNP': return False
  if word-pos == 'PRP$': return False
  if word-pos == 'RB': return False
  if word-pos == 'VB': return False
  if word-pos == 'VBD': return False
  if word-pos == 'VBG': return False
  if word-pos == 'VBN': return False
  if word-pos == 'VBP': return False
  if word-pos == 'VBZ': return False
  if word-pos == 'WDT': return False
  if word-pos == '``': return False
if next-word-pos == 'DT': return False
if next-word-pos == 'EX': return False
if next-word-pos == 'IN': return False
if next-word-pos == 'JJ': return False
if next-word-pos == 'JJR': return False
if next-word-pos == 'JJS': return False
if next-word-pos == 'MD': return False
if next-word-pos == 'NN': return False
if next-word-pos == 'NNP': return False
if next-word-pos == 'NNPS': return False
if next-word-pos == 'NNS': return False
if next-word-pos == 'PDT': return False
if next-word-pos == 'POS': return False
if next-word-pos == 'PRP': return False
if next-word-pos == 'PRP$': return False
if next-word-pos == 'RB': return False
if next-word-pos == 'RBR': return False
if next-word-pos == 'RBS': return False
if next-word-pos == 'RP': return False
if next-word-pos == 'TO': return False
if next-word-pos == 'UH': return False
if next-word-pos == 'VB': return False
if next-word-pos == 'VBD': return False
if next-word-pos == 'VBG': return False
if next-word-pos == 'VBN': return False
if next-word-pos == 'VBP': return False
if next-word-pos == 'VBZ': return False
if next-word-pos == 'WDT': return False
if next-word-pos == 'WP': return False
if next-word-pos == 'WRB': return False
if next-word-pos == '``': return False
~~~

<p>
I like that it's identified the '<speaker>:<sentence>' pattern:</p>



~~~python

if next-word-pos == ':':
  ...
  if prev-word-pos == '<START>': return True
~~~

<p>
Next I need to drill into the types of sentence structures that it's failing on and work out some features that can handle those. I still need to see how well a random forest of decision trees would as well.
</p>

