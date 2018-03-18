+++
draft = false
date="2011-09-15 22:21:14"
title="Scala: for comprehensions with Options"
tag=['scala']
category=['Scala']
+++

I've generally avoided using for expressions in Scala because the keyword reminds me of for loops in Java/C# and I want to learn to program in a less imperative way. 

After working with my colleague <a href="http://twitter.com/#!/mushtaqA">Mushtaq</a> I realised that in some cases using for comprehensions can lead to much more readable code.  

An interesting use case where this is the case is when we want to create an object from a bunch of parameters that may or may not be set. i.e. a bunch of options.

For example we might take some input from the user where they have to enter their name but could choose to leave the field blank:  


~~~scala

val maybeFirstName : Option[String] = Some("Mark")
val maybeSurname : Option[String] = None
~~~

We only want to create a <cite>Person</cite> if they have provided both names.

The for comprehension works quite well in allowing us to do this:


~~~scala

case class Person(firstName:String, surname:String)
~~~


~~~scala

scala> for { firstName <- maybeFirstName; surname <- maybeSurname } yield Person(firstName, surname)
res27: Option[Person] = None
~~~

If we set the surname to have a value:


~~~scala

val maybeSurname : Option[String] = Some("Needham")
~~~

Running the same for comprehension will yield a <cite>Person</cite>


~~~scala

scala> for { firstName <- maybeFirstName; surname <- maybeSurname } yield Person(firstName, surname)
res29: Option[Person] = Some(Person(Mark,Needham))
~~~

From what I understand  when we have multiple values assigned using '<-' inside a for comprehension, each value will have <cite>flatMap</cite> called on it except for the last one which will have <cite>map</cite> called instead.

The equivalent code if we didn't use a for comprehension would therefore look like this:


~~~scala

scala> maybeFirstName.flatMap { firstName => maybeSurname.map { surname => Person(firstName, surname) } } 
res43: Option[Person] = Some(Person(Mark,Needham))
~~~

For me the for comprehension expresses intent much better and it seems to excel even more as we add more values to the comprehension.
