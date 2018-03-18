+++
draft = false
date="2009-09-14 23:49:07"
title="Scala: The '_=' mixed identifier"
tag=['scala']
category=['Scala']
+++

I've been playing around with Scala a bit and in particular following some of the code examples from <a href="http://www.codecommit.com/blog/scala/scala-for-java-refugees-part-5">Daniel Spiewak's 'Scala for Java Refugees' article on Traits and Types</a>.

One thing that I got a bit confused about in one of the examples was the use of the '_' at the end of one of the function definitions:

~~~scala

class MyContainer[T] {
  private var obj:T = null

  def value = obj
  def value_=(v:T) = obj = v
}

val cont = new MyContainer[String]
cont.value = "Daniel"

println(cont.value)
~~~
From my limited understanding of the language the '_' (or placeholder syntax) is often passed to functions when we only want to partially apply the function to its arguments but when you use it in that context there's usually a space between the function name and the '_' so it wasn't being used like that.

From <a href="http://www.artima.com/shop/programming_in_scala">Programming in Scala</a>:
<blockquote>Remember that you need to leave a space between the function name and the underscore, because otherwise the compiler will think you are referring to a different symbol, such as for example, a method named println_, which likely does not exist.</blockquote>
In this example we were able to make use of 'value' without using the '_' though so clearly this was some other syntax I was unaware of.

I came across the idea that it might be linked to '<a href="http://www.scala-lang.org/docu/files/api/scala/util/DynamicVariable.html">DynamicVariable</a>' but I think that it's just a coincidence that 'DynamicVariable' happens to define a function called 'value_' since the code described above doesn't mention 'DynamicVariable' anywhere.

Eventually <a href="http://twitter.com/wgren/statuses/3979169229">Lars Westergren set me back on track by pointing out that what's being described is a mixed identifier</a> which is a much simpler explanation than what I'd been thinking!

In this case the mixed identifier is 'value_=' which defines an assignment operator which takes in a value 'v' of type 'T' and then assigns it to 'obj'.

It seems quite similar to the way we would use properties in C#.

I'm still finding having so many '=' on the same line to be a bit confusing at the moment so I'd  probably rewrite that function like this so it's easier for me to understand:

~~~scala

def value_=(v:T) = { obj = v }
~~~

<a href="http://twitter.com/channingwalton">Channing Walton</a> also linked me to <a href="http://www.naildrivin5.com/scalatour/wiki_pages/ScalaProperties">a post which explains how Scala properties work</a>. 
