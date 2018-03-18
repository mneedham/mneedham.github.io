+++
draft = false
date="2011-07-09 19:54:05"
title="Scala: Traits galore"
tag=['scala', 'traits']
category=['Scala']
+++

We recently came across a problem where we had some logic that we wanted to be used by two classes. 

Our original thought was to pull it up into an abstract class which ended up looking like this:


~~~scala

abstract class SomeArbitraryClass(root:xml.Node) {
  def unrelatedField1:String
  def unrelatedField2:String

  def startPage:String
  def endPage:String
  def pageRange = if(firstPage == lastPage) "page %s".format(firstPage) else "pages %s-%s".format(firstPage, lastPage)
}
~~~

Writing a test *link to scala test* for the page logic helped us to see more clearly that the design was a bit awkward:


~~~scala

class SomeArbitraryClassTest extends Spec with ShouldMatchers {
  it("should format page range") {
    val someArbitraryClass = new SomeArbitraryClass(<empty />) {
      def unrelatedField1 = null
      def unrelatedField2 = null
      def startPage = "1"
      def endPage = "2"
    }

    someArbitraryClass.pageRange should equal("pages 1-2")
  }
}
~~~

It seemed pretty weird to have to pass in an empty XML tag to the class when our test didn't care at all about XML.

Having <cite>unrelatedField1</cite> and <cite>unrelatedField2</cite> as null values further helped us to see that the page stuff is totally unrelated to the rest of this class.

We therefore pulled out a trait just for the three page related functions:


~~~scala

trait PageAware {
  def startPage:String
  def endPage:String
  def pageRange = if(firstPage == lastPage) "page %s".format(firstPage) else "pages %s-%s".format(firstPage, lastPage)
}
~~~

That trait is much more cohesive than the original <cite>Content</cite> class and our new test reflects that:


~~~scala

class PageAwareTest extends Spec with ShouldMatchers {
  it("should format page range") {
    val pageAware = new PageAware() {
      def startPage = "1"
      def endPage = "2"
    }

    pageAware.pageRange should equal("pages 1-2")
  }
}
~~~

And we can pull that trait into the abstract class too:


~~~scala

abstract class SomeArbitraryClass(root:xml.Node) extends PageAware {
  def unrelatedField1:String
  def unrelatedField2:String
}
~~~

I guess we could also just pull in <cite>PageAware</cite> at the sub class level but since all of the sub classes need to be page aware this seems to make sense.

We seem to be pulling out traits quite frequently as they seem to be a really nice way to abstract a group of related functions.

Our design is starting to resemble the <a href="http://www.engineyard.com/blog/2010/let-them-code-cake/">cake layering pattern</a> suggested by Martin Emde as an approach for avoiding ActiveRecord objects becoming cluttered with logic in Rails land.
