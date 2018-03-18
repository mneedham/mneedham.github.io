+++
draft = false
date="2012-11-29 17:09:29"
title="Kaggle Digit Recognizer: Weka AdaBoost attempt"
tag=['machine-learning-2', 'kaggle']
category=['Machine Learning']
+++

In our latest attempt at <a href="http://www.kaggle.com/c/digit-recognizer">Kaggle's Digit Recognizer</a> <a href="http://twitter.com/jennifersmithco">Jen</a> and I decided to try out <a href="http://en.wikipedia.org/wiki/Boosting_(machine_learning)">boosting</a> on our random forest algorithm, an approach that Jen had come across in a talk at the <a href="http://clojure-conj.org/">Clojure Conj</a>.

We couldn't find any documentation that it was possible to apply boosting to Mahout's random forest algorithm but we knew it was possible with <a href="http://www.cs.waikato.ac.nz/ml/weka/">Weka</a> so we decided to use that instead!

As I understand it the way that boosting works in the context of random forests is that each of the trees in the forest will be assigned a weight based on how accurately it's able to classify the data set and these weights are then used in the voting stage.

There's a more detailed explanation of the algorithm in <a href="http://e-research.csm.vu.edu.au/files/xu/04634231.pdf">this paper</a>.

We had the following code to train the random forest:


~~~java

public class WekaAdaBoostRandomForest {
    public static void main(String[] args) {
        FastVector attributes = attributes();

        Instances instances = new Instances("digit recognizer", attributes, 40000);
        instances.setClassIndex(0);

        String[] trainingDataValues = KaggleInputReader.fileAsStringArray("data/train.csv");

        for (String trainingDataValue : trainingDataValues) {
            Instance instance = createInstance(trainingDataValue);
            instances.add(instance);
        }

        Classifier classifier = buildClassifier(instances);
    }

    private static Classifier buildClassifier(Instances instances) throws Exception {
        RandomForest randomForest = new RandomForest();
        randomForest.setNumTrees(200);

        MultiBoostAB multiBoostAB = new MultiBoostAB();
        multiBoostAB.setClassifier(randomForest);
        multiBoostAB.buildClassifier(instances);
        return multiBoostAB;
    }

    private static FastVector attributes() {
        FastVector attributes = new FastVector();
        attributes.addElement(digit());

        for (int i = 0; i <= 783; i++) {
            attributes.addElement(new Attribute("pixel" + i));
        }

        return attributes;
    }

    private static Attribute digit() {
        FastVector possibleClasses = new FastVector(10);
        possibleClasses.addElement("0");
        possibleClasses.addElement("1");
        possibleClasses.addElement("2");
        possibleClasses.addElement("3");
        possibleClasses.addElement("4");
        possibleClasses.addElement("5");
        possibleClasses.addElement("6");
        possibleClasses.addElement("7");
        possibleClasses.addElement("8");
        possibleClasses.addElement("9");
        return new Attribute("label", possibleClasses, 0);

    }

}
~~~

The code in the <cite>KaggleInputReader</cite> is used to process the CSV file and is the same as that included <a href="http://www.markhneedham.com/blog/2012/10/27/kaggle-digit-recognizer-mahout-random-forest-attempt/">in a previous post</a> so I won't bother including it in this post.

The Weka API is slightly different to the Mahout one in that we have to tell it the names of all the labels that a combination of features belong to whereas with Mahout it seems to work it out for you.

Wf use the <cite>RandomForest</cite> class to build up our trees and then wrap it in the <cite>MultiBoostAB</cite> class to apply the boosting. There is another class we could use to do this called <cite>AdaBoostM1</cite> but they both seem to give similar results so we stuck with this one.

Once we'd trained the classifier up we ran it against our test data set like so:


~~~java

public class WekaAdaBoostRandomForest {
    public static void main(String[] args) {
        ...
        String[] testDataValues = KaggleInputReader.fileAsStringArray("data/test.csv");


        FileWriter fileWriter = new FileWriter("weka-attempts/out-" + System.currentTimeMillis() + ".txt");
        PrintWriter out = new PrintWriter(fileWriter);
        for (String testDataValue : testDataValues) {
            Iteration iterate = iterate(testDataValue, classifier, instances);
            out.println((int) iterate.getPrediction());
            System.out.println("Actual: " + iterate.getActual() + ", Prediction: " + iterate.getPrediction());
        }
        out.close();
    }
   
    private static Iteration iterate(String testDataValue, Classifier classifier, Instances instances) throws Exception {
        Instance predictMe = createTestDataBasedInstanceToPredict(testDataValue, instances);
        double prediction = classifier.classifyInstance(predictMe);

        return new Iteration(new Double(testDataValue.split(",")[0]), prediction);
    }

    private static Instance createTestDataBasedInstanceToPredict(String testDataValue, Instances instances) {
        String[] columns = testDataValue.split(",");
        Instance instance = new Instance(785);

        for (int i = 0; i < columns.length; i++) {
            instance.setValue(new Attribute("pixel" + i, i+1), new Double(columns[i]));
        }

        instance.setDataset(instances);
        return instance;
    }
}
~~~

We got an accuracy of 96.529% with this code which is 0.2% higher than we managed with the Mahout Random forest without any boosting. The <a href="https://github.com/jennifersmith/machinenursery/blob/master/src/main/java/WekaPlaybox.java">full code for this solution is on github</a> as always!

We still haven't managed to get an accuracy higher than the default solution provided by Kaggle so any suggestions about what else to try are welcome!

We've been playing around with neural networks using <a href="http://www.heatonresearch.com/encog">encog</a> but they seem a bit magical and the moment and it's difficult to work out why they don't work when you don't get the result you expect!
