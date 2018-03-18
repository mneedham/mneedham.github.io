+++
draft = false
date="2011-07-23 11:57:44"
title="Scala: Companion Objects"
tag=['scala']
category=['Scala']
+++

One of the language features available to us in Scala which I think is having a big impact in helping us to make our code base easier to follow is the <a href="http://daily-scala.blogspot.com/2009/09/companion-object.html">companion object</a>.

We've been using companion objects quite liberally in our code base to define factory methods for our classes.

As I mentioned in a previous post <a href="http://www.markhneedham.com/blog/2011/06/26/coding-light-weight-wrapper-vs-serialisationdeserialisation/">a lot of our objects are acting as wrappers around XML documents</a> and we've been pushing some of the data extraction from the XML into companion objects so that our classes can take in non XML values.

This means we can test the data extraction against the companion object and then create simpler tests against any other logic in the object because we don't have to create XML documents in each of our tests.

The following is an example of a <cite>Foo</cite> object being constructed with data from an XML document:


~~~scala

object Foo {
   def apply(element: Node) = {
    val bar = element.attribute("bar").get.head.text
    val baz = (element \\ "baz").text
    new Foo(bar, baz)
  }
}	
~~~

There is also some other logic around how a collection of <cite>Foos</cite> should be ordered and by using the companion object to parse the XML we can create a test with appropriate <cite>bar</cite> and <cite>baz</cite> values to test that.


~~~scala

case class Foo(bar: String, baz:String) extends Ordered[Foo] {
   def compare(that: Foo) = {
     // logic to compare Foos
   }
}
~~~

Before we had the companion object we were putting the logic to create <cite>Foo</cite> inside the object where it is created from which increased the complexity of that object and made it more difficult for people to read.

We've also been using this approach to build up <a href="http://code.google.com/p/selenium/wiki/PageObjects">page objects</a> representing sub sections of a page in our Web Driver tests and it seems to work quite nicely there as well.
