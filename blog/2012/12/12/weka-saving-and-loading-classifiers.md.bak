+++
draft = false
date="2012-12-12 00:04:42"
title="Weka: Saving and loading classifiers"
tag=['machine-learning-2', 'weka']
category=['Machine Learning']
+++

<p>In our continued machine learning travels <a href="https://twitter.com/jennifersmithco">Jen</a> and I have been building some classifiers using <a href="http://www.cs.waikato.ac.nz/ml/weka/">Weka</a> and one thing we wanted to do was save the classifier and then reuse it later.</p>


<p>There is <a href="http://weka.wikispaces.com/Saving+and+loading+models">documentation</a> for how to do this from the command line but we're doing everything programatically and wanted to be able to save our classifiers from Java code.</p>


<p>As it turns out it's not too tricky when you know which classes to call and saving a classifier to a file is as simple as this:</p>



~~~java

MultilayerPerceptron classifier = new MultilayerPerceptron();
classifier.buildClassifier(instances); // instances gets passed in from elsewhere

Debug.saveToFile("/path/to/weka-neural-network", classifier);
~~~

<p>If we want to load that classifier up we can make use of the <cite><a href="http://weka.sourceforge.net/doc.dev/weka/classifiers/misc/SerializedClassifier.html">SerializedClassifier</a><cite> class like so:</p>



~~~java

SerializedClassifier classifier = new SerializedClassifier();
classifier.setModelFile(new File("/path/to/weka-neural-network"));
~~~

<p><a href="http://www.youtube.com/watch?v=Hl545RF6dXA">Simples</a>!</p>

