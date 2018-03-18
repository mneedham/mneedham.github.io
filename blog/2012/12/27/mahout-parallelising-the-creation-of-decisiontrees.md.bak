+++
draft = false
date="2012-12-27 00:08:01"
title="Mahout: Parallelising the creation of DecisionTrees"
tag=['machine-learning-2', 'mahout']
category=['Machine Learning']
+++

<p>A couple of months ago I wrote a <a href="http://www.markhneedham.com/blog/2012/10/27/kaggle-digit-recognizer-mahout-random-forest-attempt/">blog post</a> describing our use of <a href="http://mahout.apache.org/">Mahout</a> random forests for the <a href="http://www.kaggle.com/c/digit-recognizer">Kaggle Digit Recogniser Problem</a> and after seeing how long it took to create forests with 500+ trees I wanted to see if this could be sped up by parallelising the process.</p>


<p>From looking at the <cite><a href="https://github.com/apache/mahout/blob/trunk/core/src/main/java/org/apache/mahout/classifier/df/DecisionForest.java">DecisionTree</a></cite> it seemed like it should be possible to create lots of small forests and then combine them together.</p>


<p>After unsuccessfully trying to achieve this by directly using <cite>DecisionForest</cite> I decided to just copy all the code from that class into <a href="https://github.com/jennifersmith/machinenursery/blob/master/src/main/java/MultiDecisionForest.java">my own version</a> which allowed me to achieve this.</p>


<p>The code to build up the forest ends up looking like this:</p>



~~~java

List<Node> trees = new ArrayList<Node>();

MultiDecisionForest forest = MultiDecisionForest.load(new Configuration(), new Path("/path/to/mahout-tree"));
trees.addAll(forest.getTrees());

MultiDecisionForest forest = new MultiDecisionForest(trees);
~~~

<p>We can then use <cite>forest</cite> to classify values in a test data set and it seems to work reasonably well.</p>


<p>I wanted to try and avoid putting any threading code in so I made use of <a href="http://www.gnu.org/software/parallel/">GNU parallel</a> which is available on Mac OS X with a <cite>brew install parallel</cite> and on Ubuntu by <a href="http://askubuntu.com/questions/12764/where-do-i-get-a-package-for-gnu-parallel">adding the following repository</a> to <cite>/etc/apt/sources.list</cite>…</p>



~~~text

deb http://ppa.launchpad.net/ieltonf/ppa/ubuntu oneiric main 
deb-src http://ppa.launchpad.net/ieltonf/ppa/ubuntu oneiric main 
~~~

<p>…followed by a <cite>apt-get update</cite> and <cite>apt-get install parallel</cite>.</p>


<p>I then wrote a script to parallelise the creation of the forests:</p>


<em><a href="https://github.com/jennifersmith/machinenursery/blob/master/parallel-forests.sh">parallelise-forests.sh</a></em>

~~~text

#!/bin/bash 

start=`date`
startTime=`date '+%s'`
numberOfRuns=$1

seq 1 ${numberOfRuns} | parallel -P 8 "./build-forest.sh"

end=`date`
endTime=`date '+%s'`

echo "Started: ${start}"
echo "Finished: ${end}"
echo "Took: " $(expr $endTime - $startTime)
~~~

<em><a href="https://github.com/jennifersmith/machinenursery/blob/master/build-forest.sh">build-forest.sh</a></em>

~~~sh

#!/bin/bash

java -Xmx1024m -cp target/machinenursery-1.0.0-SNAPSHOT-standalone.jar main.java.MahoutPlaybox
~~~

<p>It should be possible to achieve this by using the parallel option in <cite>xargs</cite> but unfortunately I wasn't able to achieve the same success with that command.</p>


<p>I <a href="http://stackoverflow.com/questions/2791069/how-to-use-parallel-execution-in-a-shell-script">hadn't come across</a> the <cite>seq</cite> command until today but it works quite well here for allowing us to specify how many times we want to call the script.</p>


<p>I was probably able to achieve about a 30% speed increase when running this on my Air. There was a greater increase running on a high CPU AWS instance although for some reason some of the jobs seemed to get killed and I couldn't figure out why.</p>


<p>Sadly even with a new classifier with a massive number of trees I didn't see an improvement over the <a href="http://www.markhneedham.com/blog/2012/11/29/kaggle-digit-recognizer-weka-adaboost-attempt/">Weka random forest using AdaBoost</a> which I wrote about a month ago. We had an accuracy of 96.282% here compared to 96.529% with the Weka version.</p>

