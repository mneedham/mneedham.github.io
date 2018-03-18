+++
draft = false
date="2012-10-27 20:24:48"
title="Kaggle Digit Recognizer: Mahout Random Forest attempt"
tag=['machine-learning-2']
category=['Machine Learning']
+++

I've written previously about the <a href="http://www.markhneedham.com/blog/2012/10/23/kaggle-digit-recognizer-a-k-means-attempt/">K-means</a> <a href="http://www.markhneedham.com/blog/2012/10/27/kaggle-digit-recognizer-k-means-optimisation-attempt/">approach</a> that <a href="http://twitter.com/jennifersmithco">Jen</a> and I took when trying to solve <a href="http://www.kaggle.com/c/digit-recognizer">Kaggle's Digit Recognizer</a> and having stalled at about 80% accuracy we decided to try one of the algorithms suggested in the <a href="http://www.kaggle.com/c/digit-recognizer/details/tutorial">tutorials section</a> - the <a href="https://www.kaggle.com/wiki/RandomForests">random forest</a>!

We initially used a <a href="https://github.com/eandrejko/random-forests-clj">clojure random forests library</a> but struggled to build the random forest from the training set data in a reasonable amount of time so we switched to <a href="https://cwiki.apache.org/MAHOUT/breiman-example.html">Mahout's version</a> which is based on Leo Breiman's <a href="http://oz.berkeley.edu/users/breiman/randomforest2001.pdf">random forests</a> paper.

There's <a href="http://blog.factual.com/the-wisdom-of-crowds">a really good example explaining how ensembles work on the Factual blog</a> which we found quite useful in helping us understand how random forests are supposed to work.

<blockquote>
One of the most powerful Machine Learning techniques we turn to is ensembling. Ensemble methods build surprisingly strong models out of a collection of weak models called base learners, and typically require far less tuning when compared to models like Support Vector Machines.

Most ensemble methods use decision trees as base learners and many ensembling techniques, like Random Forests and Adaboost, are specific to tree ensembles.
</blockquote>

We were able to adapt the <cite><a href="https://github.com/apache/mahout/blob/trunk/examples/src/main/java/org/apache/mahout/classifier/df/BreimanExample.java">BreimanExample</a></cite> included in the examples section of the Mahout repository to do what we wanted.

To start with we wrote the following code to build the random forest:


~~~java

public class MahoutKaggleDigitRecognizer {
  public static void main(String[] args) throws Exception {
    String descriptor = "L N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N ";
    String[] trainDataValues = fileAsStringArray("data/train.csv");

    Data data = DataLoader.loadData(DataLoader.generateDataset(descriptor, false, trainDataValues), trainDataValues);

    int numberOfTrees = 100;
    DecisionForest forest = buildForest(numberOfTrees, data);
  }

  private static DecisionForest buildForest(int numberOfTrees, Data data) {
    int m = (int) Math.floor(Maths.log(2, data.getDataset().nbAttributes()) + 1);

    DefaultTreeBuilder treeBuilder = new DefaultTreeBuilder();
    treeBuilder.setM(m);

    return new SequentialBuilder(RandomUtils.getRandom(), treeBuilder, data.clone()).build(numberOfTrees);
  }

  private static String[] fileAsStringArray(String file) throws Exception {
    ArrayList<String> list = new ArrayList<String>();

    DataInputStream in = new DataInputStream(new FileInputStream(file));
    BufferedReader br = new BufferedReader(new InputStreamReader(in));

    String strLine;
    br.readLine(); // discard top one (header)
    while ((strLine = br.readLine()) != null) {
      list.add(strLine);
    }

    in.close();
    return list.toArray(new String[list.size()]);
  }
}
~~~

The training data file looks a bit like this:


~~~text

label,pixel0,pixel1,pixel2,pixel3,pixel4,pixel5,pixel6,pixel7,pixel8...,pixel783
1,0,0,0,0,0,0,...,0
0,0,0,0,0,0,0,...,0
~~~

So in this case the label is in the first column which is represented as an <cite>L</cite> in the descriptor and the next 784 columns are the numerical value of the pixels in the image (hence the 784 <cite>N</cite>'s in the descriptor).

We're telling it to create a random forest which contains 100 trees and since we have a finite number of categories that an entry can be classified as we pass <cite>false</cite> as the 2nd argument (regression) of <cite><a href="https://github.com/apache/mahout/blob/trunk/core/src/main/java/org/apache/mahout/classifier/df/data/DataLoader.java#L184">DataLoader.generateDataSet</a></cite>.

The <cite>m</cite> value determines how many attributes (pixel values in this case) are used to construct each tree and supposedly <cite>log<sub>2</sub>(number_of_attributes) + 1</cite> is the optimal value for that!

We then wrote the following code to predict the labels of the test data set:


~~~java

public class MahoutKaggleDigitRecognizer {
  public static void main(String[] args) throws Exception {
    ...
    String[] testDataValues = testFileAsStringArray("data/test.csv");
    Data test = DataLoader.loadData(data.getDataset(), testDataValues);
    Random rng = RandomUtils.getRandom();

    for (int i = 0; i < test.size(); i++) {
    Instance oneSample = test.get(i);

    double classify = forest.classify(test.getDataset(), rng, oneSample);
    int label = data.getDataset().valueOf(0, String.valueOf((int) classify));

    System.out.println("Label: " + label);
  }

  private static String[] testFileAsStringArray(String file) throws Exception {
    ArrayList<String> list = new ArrayList<String>();

    DataInputStream in = new DataInputStream(new FileInputStream(file));
    BufferedReader br = new BufferedReader(new InputStreamReader(in));

    String strLine;
    br.readLine(); // discard top one (header)
    while ((strLine = br.readLine()) != null) {
      list.add("-," + strLine);
    }

    in.close();
    return list.toArray(new String[list.size()]);
  }
}
~~~

There were a couple of things that we found confusing when working out how to do this:

<ol>
<li>The format of the test data needs to be identical to that of the training data which consisted of a label followed by 784 numerical values. Obviously with the test data we don't have a label so Mahout excepts us to pass a '-' where the label would go otherwise it will throw an exception, which explains the '-' on the <cite>list.add</cite> line.</li>
<li>We initially thought the value returned by <cite><a href="https://github.com/apache/mahout/blob/trunk/core/src/main/java/org/apache/mahout/classifier/df/DecisionForest.java#L90">forest.classify</a></cite> was the prediction but in actual fact it's an index which we then need to look up on the data set.</li> 
</ol>

When we ran this algorithm against the test data set with 10 trees we got an accuracy of 83.8%, with 50 trees we got 84.4%, with 100 trees we got 96.28% and with 200 trees we got 96.33% which is where we've currently peaked.

The amount of time it's taking to build the forests as we increase the number of trees is also starting to become a problem so our next step is either to look at a way to parallelise the creation of the forest or do some sort of <a href="http://www.kaggle.com/c/digit-recognizer/forums/t/2308/feature-extraction-technique">feature extraction </a>to try and improve the accuracy.

The <a href="https://github.com/jennifersmith/machinenursery/blob/master/src/main/java/MahoutPlaybox.java">code is on github</a> if you're interested in playing with it or have any suggestions on how to improve it.
