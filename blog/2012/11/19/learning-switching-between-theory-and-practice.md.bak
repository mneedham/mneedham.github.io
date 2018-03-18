+++
draft = false
date="2012-11-19 13:31:49"
title="Learning: Switching between theory and practice"
tag=['learning']
category=['Learning', 'Machine Learning']
+++

In one of my first ever blog posts I wrote about the differences I'd experienced <a href="http://www.markhneedham.com/blog/2008/02/09/learning-theory-first/">in learning the theory about a topic and then seeing it in practice</a>. 

The way I remember learning at school and university was that you learn all the theory first and then put it into practice but I typically don't find myself doing this whenever I learn something new.

I spent a bit of time over the weekend learning more about neural networks as my colleague <a href="https://twitter.com/jennifersmithco">Jen Smith</a> suggested <a href="https://twitter.com/JenniferSmithCo/status/269167128672890880">this might be a more effective technique for getting a higher accuracy score</a>  on the <a href="http://www.kaggle.com/c/digit-recognizer">Kaggle Digit Recogniser</a> problem.

I first came across neural networks during <a href="https://www.coursera.org/course/ml">Machine Learning Class</a> about a year ago but I didn't put any of that knowledge into practice and as a result it's mostly been forgotten so my first step was to go back and watch the videos again.

Having got a high level understanding of how they work I thought I'd try and find a Neural Networks implementation in <a href="http://mahout.apache.org/">Mahout</a> since Jen and I have been hacking with that so I have a reasonable level of familiarity with it.

I could only find people talking about writing an implementation rather than any suggestion that there was one so I turned to google and came across <a href="https://github.com/nickewing/netz">netz</a> - a Clojure implementation of neural networks.

On its project page there were links to several 'production ready' Java frameworks for building neural networks including <a href="http://neuroph.sourceforge.net/documentation.html">neuroph</a>, <a href="http://www.heatonresearch.com/encog">encog</a> and <a href="http://leenissen.dk/fann/wp/">FANN</a>.

I spent a few hours playing around with some of the encog examples and trying to see whether or not we'd be able to plug the Digit Recogniser problem into it.

To refresh, the digit recogniser problem is a <strong>multi class classification problem</strong> where we train a classifier with series of 784 pixel brightness values where we know which digit they refer to.

We should then be able to feed it any new set of 784 pixel brightness values and it will tell us which digit that is most likely to be.

I realised that the <a href="https://github.com/mneedham/encog-examples-3.1.0/blob/master/src/main/java/org/encog/examples/neural/gui/ocr/OCR.java">OCR encog example</a> wouldn't quite work because it assumed that you'd only have one training example for each class!

<blockquote>
<a href="https://github.com/encog/encog-java-core/blob/master/src/main/java/org/encog/neural/som/training/clustercopy/SOMClusterCopyTraining.java">SOMClusterCopyTraining.java</a>

* For now, this trainer will only work if you have equal or fewer training elements 

* to the number of output neurons.
</blockquote>

I was pretty sure that I didn't want to have 40,000 output neurons but I thought I better switch back to theory and make sure I understood how neural networks were supposed to work by reading the slides from an <a href="http://www2.econ.iastate.edu/tesfatsi/NeuralNetworks.CheungCannonNotes.pdf">introductory talk</a>.

Now that I've read those I'm ready to go back into the practical side again and try and build up a network a bit more manually than I imagined the previous time by using the <a href="https://github.com/encog/encog-java-core/blob/master/src/main/java/org/encog/neural/networks/BasicNetwork.java">BasicNetwork</a> class.

I'm sure as I do that I'll have to switch back to theory again and read a bit more, then code a bit more and so the cycle goes on!
