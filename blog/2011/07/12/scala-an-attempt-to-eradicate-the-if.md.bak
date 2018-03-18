+++
draft = false
date="2011-07-12 22:50:40"
title="Scala: An attempt to eradicate the if"
tag=['scala']
category=['Scala']
+++

In a <a href="http://www.markhneedham.com/blog/2011/07/09/scala-traits-galore/">previous post</a> I included a code sample where we were formatting a page range differently depending on whether the start page and end pages were the same.

The code looked like this:


~~~scala

trait PageAware {
  def startPage:String
  def endPage:String
  def pageRange = if(firstPage == lastPage) "page %s".format(firstPage) else "pages %s-%s".format(firstPage, lastPage)
}
~~~

Looking at the if statement on the last line we were curious whether it would be possible to get rid of it and replace it with something else.

In Java we could use the ternary operator:


~~~java

public class PageAware {
  public String pageRange() {
    return (firstPage == lastPage) ? String.format("page %s", firstPage) : String.format("pages %s-%s", firstPage, lastPage)
  }
}
~~~

The if/else statement in Scala is supposed to replace that as far as I understand but I think the ternary operator looks neater.

Beyond defining that we played around with some potential alternatives.

We could use a <cite>Map</cite> to store the true and false values as keys:


~~~scala

trait PageAware {
  def pageRange = Map(true -> "page %s", false -> "pages %s-%s")(firstPage == lastPage).format(firstPage, lastPage)
}
~~~

<a href="http://twitter.com/#!/uday_rayala">Uday</a> came up with a pattern matching solution which looks like this:


~~~scala

trait PageAware {
  def pageRange = ((firstPage, lastPage) match { case (`firstPage`, `firstPage`) => "page %s" case _ => "pages %s-%s"}).format(firstPage, lastPage)
}
~~~

Unfortunately both of these solutions are significantly less readable than the if/else one so it seems like this is one of the situations where it doesn't actually make sense to get rid of it.
