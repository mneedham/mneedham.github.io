+++
draft = false
date="2011-11-01 00:58:45"
title="Scala: Option.isDefined as the new null check"
tag=['scala']
category=['Scala']
+++

One cool thing about using Scala on my current project is that we don't have nulls anywhere in our code, instead when something may or may not be there we make use of the Option type.

Unfortunately what we've (heavily contributed by me) ended up with in our code base is repeated use of the <cite><a href="http://www.scala-lang.org/api/rc/scala/Option.html">isDefined</a></cite> method whenever we want to make a decision depending on whether or not the option is populated.

For example the following is quite common:


~~~scala

case class Foo(val bar:String)
val foo : Option[Foo] = Some(Foo("mark"))
~~~


~~~scala

> val bar = if(foo.isDefined) Some(foo.get.bar) else None
bar: Option[String] = Some(mark)
~~~

We can actually get rid of the if statement by making use of <cite>collect</cite> instead:


~~~scala

> val bar = foo.collect { case f => f.bar } 
bar: Option[String] = Some(mark)
~~~

And if foo is <cite>None</cite>:


~~~scala

> val foo : Option[Foo] = None
> val bar = foo.collect { case f => f.bar } 
bar: Option[String] = None
~~~

The code is now simpler and as long as you understand <cite>collect</cite> then it's easier to understand as well.

Another quite common example would be something like this:


~~~scala

case class Foo(val bar:Option[String])
~~~


~~~scala

> val foos = List(Foo(Some("mark")), Foo(None), Foo(Some("needham")))
foos: List[Foo] = List(Foo(Some(mark)), Foo(None), Foo(Some(needham)))
~~~


~~~scala

> foos.filter(_.bar.isDefined).map(_.bar.get + " awesome")
res23: List[java.lang.String] = List(mark awesome, needham awesome)
~~~

Which we can simplify down to:


~~~scala

foos.collect { case Foo(Some(bar)) => bar + " awesome" }
~~~

When I was playing around with F# a couple of years ago I learnt that wherever possible I should try and keep chaining functions together rather than breaking the code up into conditionals and I think the same applies here.

There are loads of methods available on <cite><a href="http://www.scala-lang.org/api/rc/scala/collection/TraversableLike.html">TraversableLike</a></cite> to help us achieve this.
