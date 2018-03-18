+++
draft = false
date="2012-10-27 22:03:30"
title="Mahout: Using a saved Random Forest/DecisionTree"
tag=['machine-learning-2', 'mahout']
category=['Machine Learning']
+++

One of the things that I wanted to do while <a href="http://www.markhneedham.com/blog/2012/10/27/kaggle-digit-recognizer-mahout-random-forest-attempt/">playing around with random forests</a> using <a href="http://mahout.apache.org/">Mahout</a> was to save the random forest and then use use it again which is something Mahout does cater for.

It was actually much easier to do this than I'd expected and assuming that we already have a <cite><a href="https://github.com/apache/mahout/blob/trunk/core/src/main/java/org/apache/mahout/classifier/df/DecisionForest.java">DecisionForest</a></cite> built we'd just need the following code to save it to disc:


~~~java

int numberOfTrees = 1;
Data data = loadData(...);
DecisionForest forest = buildForest(numberOfTrees, data);

String path = "saved-trees/" + numberOfTrees + "-trees.txt";
DataOutputStream dos = new DataOutputStream(new FileOutputStream(path));

forest.write(dos);
~~~

When I was looking through the API for how to load that file back into memory again it seemed like all the public methods required you to be using Hadoop in some way which I thought was going to be a problem as I'm not using it.

For example the signature for <cite>DecisionForest.load</cite> reads like this:


~~~java

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;

public static DecisionForest load(Configuration conf, Path forestPath) throws IOException { }
~~~

As it turns out though you can just pass an empty configuration and a normal file system path and the forest shall be loaded:


~~~java

int numberOfTrees = 1;

Configuration config = new Configuration();
Path path = new Path("saved-trees/" + numberOfTrees + "-trees.txt");
DecisionForest forest = DecisionForest.load(config, path);
~~~

Much easier than expected!
