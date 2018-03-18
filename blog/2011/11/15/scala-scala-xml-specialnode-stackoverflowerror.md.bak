+++
draft = false
date="2011-11-15 00:26:46"
title="Scala: scala.xml.SpecialNode: StackOverFlowError"
tag=['scala']
category=['Scala']
+++

We have some code in our application where we parse reasonably complex XML structures and then sometimes choose to get rid of certain elements from the structure.

When we wanted to get rid of an element we replaced that element with a <cite><a href="http://www.scala-lang.org/api/current/scala/xml/SpecialNode.html">SpecialNode</a></cite>:


~~~scala

val emptyNode = new scala.xml.SpecialNode() {
  def buildString(sb:StringBuilder) = new StringBuilder()
  def label = null
}
~~~

Unfortunately when you call #text on the node it results in the following exception which we only found out today:


~~~scala

> emptyNode.text

java.lang.StackOverflowError
	at scala.xml.NodeSeq$$anonfun$text$1.apply(NodeSeq.scala:152)
	at scala.collection.TraversableLike$$anonfun$map$1.apply(TraversableLike.scala:194)
	at scala.collection.TraversableLike$$anonfun$map$1.apply(TraversableLike.scala:194)
	at scala.collection.Iterator$class.foreach(Iterator.scala:652)
	at scala.collection.LinearSeqLike$$anon$1.foreach(LinearSeqLike.scala:50)
	at scala.collection.IterableLike$class.foreach(IterableLike.scala:73)
	at scala.xml.NodeSeq.foreach(NodeSeq.scala:43)
	at scala.collection.TraversableLike$class.map(TraversableLike.scala:194)
	at scala.xml.NodeSeq.map(NodeSeq.scala:43)
	at scala.xml.NodeSeq.text(NodeSeq.scala:152)
	at scala.xml.Node.text(Node.scala:200)
~~~

The way to get around that problem is to override the text method so it returns empty:


~~~scala

val emptyNode = new scala.xml.SpecialNode() {
  def buildString(sb:StringBuilder) = new StringBuilder()
  def label = null
  override def text = ""
}
~~~


~~~scala

> emptyNode.text
res1: String = ""
~~~

It took a seriously long time for us to track down what was going on and that bit of code wasn't unit tested.

#fail
