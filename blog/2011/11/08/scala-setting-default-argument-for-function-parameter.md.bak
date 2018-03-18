+++
draft = false
date="2011-11-08 22:46:47"
title="Scala: Setting default argument for function parameter"
tag=['scala']
category=['Scala']
+++

Yesterday I wrote about a problem we've been having with <a href="http://www.markhneedham.com/blog/2011/11/06/scala-which-implicit-conversion-is-being-used/">trying to work out how to default a function parameter that we have in one of our methods</a>.

Our current version of the code defines the function parameter as implicit which means that if it isn't passed in it defaults to <cite><a href="http://www.scala-lang.org/api/current/index.html#scala.Predef$$$less$colon$less">Predef.conforms()</a></cite>:


~~~scala

def foo[T](bar: String)(implicit blah:(String => T)) = { 
  println(blah(bar)); 
  bar 
}
~~~

It's not entirely clear just from reading the code where the implicit value is coming from so we want to try and make the code a bit more expressive.

The way we wanted to do this was by making 'blah' have a default value rather than making it implicit.

Our equivalent to <cite>Predef.conforms()</cite> is the <cite><a href="http://stackoverflow.com/questions/1797502/is-there-a-scala-identity-function">identity</a></cite> function and our first attempt at defaulting the parameter looked like this:


~~~scala

def foo[T](bar: String, blah:(String => T) = identity _) = { 
  println(blah(bar)); 
  bar 
}
~~~

Unfortunately when we try to use that function without providing the second argument we get the following exception:


~~~text

scala> foo("mark")
<console>:18: error: polymorphic expression cannot be instantiated to expected type;
 found   : [T](Nothing) => Nothing
 required: (String) => ?
Error occurred in an application involving default arguments.
       foo("mark")
~~~

From what I understand the compiler is unable to infer the type of the input parameter, a problem we can fix by explicitly specifying that:


~~~scala

def foo[T](bar: String, blah:(String => T) = identity[String] _) = { println(blah(bar)); bar }
~~~

We can then either choose to provide a function:


~~~scala

scala> foo("mark", _ + "needham")
markneedham
res17: String = mark
~~~

...or not:


~~~scala

scala> foo("mark")
mark
res16: String = mark
~~~

This solves the problem for this simple example but an interesting problem that we then ran into is that we actually had overloaded versions of the method in question and only one overload is allowed to specify default arguments <a href="http://www.scala-lang.org/sites/default/files/sids/rytz/Mon,%202009-11-09,%2017:29/named-args.pdf">as per the spec</a>.

Each overload actually takes in different parameter types so one way to get around this problem would be to make some of the parameters optional and then default them to None.

At the moment we've ended up leaving the implicit conversion in because the change is a bit bigger in nature than antiticpated.
