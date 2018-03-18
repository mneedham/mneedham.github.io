+++
draft = false
date="2012-02-05 21:40:33"
title="Scala: Converting a scala collection to java.util.List"
tag=['scala']
category=['Scala']
+++

I've been playing around a little with <a href="https://github.com/jiminoc/goose">Goose</a> - a library for extracting the main body of text from web pages - and I thought I'd try converting some of the code to be more scala-esque in style.

The API of the various classes/methods is designed so it's interoperable with Java code but in order to use functions like map/filter we need the collection to be a Scala one.

That's achieved by importing 'scala.collections.JavaConversions._' which will apply an implicit conversion to convert the Java collection into a Scala one.

I needed to go back to the Java one again which can be achieved with the following code:


~~~scala

import scala.collection.JavaConversions._

val javaCollection = seqAsJavaList(Seq("abc"))
~~~

I also used that function in the <a href="https://github.com/mneedham/goose/blob/94da6fffc30db17a0a7e2060a46fc3317420a83e/src/main/scala/com/gravity/goose/text/StopWords.scala">StopWords.scala</a> object in Goose.

There are a load of other functions available in <a href="https://github.com/scala/scala/blob/master/src/library/scala/collection/JavaConversions.scala">JavaConversions</a> as well for going to a Dictionary, Map, Set and so on.
