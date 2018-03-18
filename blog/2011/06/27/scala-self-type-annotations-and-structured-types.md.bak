+++
draft = false
date="2011-06-27 23:21:56"
title="Scala: Self type annotations and structured types"
tag=['scala']
category=['Scala']
+++

A few days ago I <a href="http://twitter.com/markhneedham/status/84025938903437312">tweeted that I didn't really see the point in structured types in Scala</a>...

<blockquote>
Not sure I understand where you would use structural types in #scala instead of defining a method on a trait <a href="http://bit.ly/jgiW7b">http://bit.ly/jgiW7b</a>
</blockquote>

...but today my colleague Uday came up with a cool way of combining <a href="http://programming-scala.labs.oreilly.com/ch12.html#SelfTypeAnnotations">self type annotations</a> with structured types inside a trait we defined.

We had some code duplicated across two classes which looked roughly like this:


~~~scala

class OnePageType {
  lazy val peopleNodes = root \\ "SomeNode" \ "SomeSubNode" \ "People" \ "Person"
  private def fullName(personName: Node): String = // code to build person's name

  lazy val people: String = peopleNodes.map(fullName).mkString(", ")
}
~~~


~~~scala

class AnotherPageType {
  lazy val peopleNodes = root \\ "OtherNode" \ "OtherSubNode" \ "People" \ "Person"
  private def fullName(personName: Node): String = // code to build person's name

  lazy val people: String = peopleNodes.map(fullName).mkString(", ")
}
~~~

The first line is different but the other two are identical because the data is stored in exactly the same format once we get down to that level.

Since We want to keep the XPathish queries as descriptive as possible so that we don't accidentally end up pulling the wrong elements onto the page, making those a bit looser wasn't an option in this case.

Instead we pulled out a trait like so:


~~~scala

trait People {
  self: {val peopleNodes: NodeSeq} =>

  private def fullName(personName: Node): String = // code to build person's name

  lazy val people: String = peopleNodes.map(fullName).mkString(", ")
}
~~~

Which we include in the classes like this:


~~~scala

class OnePageType extends People {}
class AnotherPageType extends People {}
~~~

What we're done on line 2 of the <cite>People</cite> trait is to define a self annotation which says that we need a val of <cite>peopleNodes</cite> to be present on the classes in which the trait is mixed.

If a val of <cite>peopleNodes</cite> doesn't exist then the class won't compile!

In this case the structure type works quite well because we wouldn't really want to pull out <cite>peopleNodes</cite> into a trait just to reference it as a self type annotation.
