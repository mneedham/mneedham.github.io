+++
draft = false
date="2012-05-22 10:26:49"
title="Scala/Haskell: A simple example of type classes"
tag=['scala', 'haskell']
category=['Scala', 'Haskell']
+++

I never really understood type classes when I was working with Scala but I recently came across <a href="http://marakana.com/s/scala_typeclasses,1117/index.html">a video where Dan Rosen explains them pretty well</a>. 

Since the last time I worked in Scala I've been playing around with Haskell where type classes are much more common - for example if we want to compare two values we need to make sure that their type extends the 'Eq' type class.

<a href="http://learnyouahaskell.com/making-our-own-types-and-typeclasses">Learn Me a Haskell's chapter on type classes</a> defines them like so:

<blockquote>
Typeclasses are like interfaces. 

A typeclass defines some behaviour (like comparing for equality, comparing for ordering, enumeration) and then types that can behave in that way are made instances of that typeclass. 

The behaviour of typeclasses is achieved by defining functions or just type declarations that we then implement. So when we say that a type is an instance of a typeclass, we mean that we can use the functions that the typeclass defines with that type.
</blockquote>

In that chapter we then go on <a href="http://learnyouahaskell.com/making-our-own-types-and-typeclasses#a-yes-no-typeclass">to create a 'YesNo' type class</a> which defines Boolean semantics for all different types. 

We start by defining the type class like so:


~~~haskell

class YesNo a where
  yesno :: a -> Bool
~~~

Any type which extends that type class can call this 'yesno' function and find out the truthyness of its value.

e.g.


~~~haskell

instance YesNo Int where
  yesno 0 = False
  yesno _ = True
~~~

If we call that:


~~~haskell

> yesno (0 :: Int)
False

> yesno (1 :: Int)
True
~~~

We get the expected result, but if we try to call it for a type which hasn't defined an instance of 'YesNo':


~~~haskell

> yesno "mark"

    No instance for (YesNo [Char])
      arising from a use of `yesno'
    Possible fix: add an instance declaration for (YesNo [Char])
    In the expression: yesno "mark"
    In an equation for `it': it = yesno "mark"
~~~

In Scala we can use traits and implicits to achieve the same effect. First we define the 'YesNo' trait:


~~~scala

trait YesNo[A] {
  def yesno(value:A) : Boolean
}
~~~

Then we define an implicit value in a companion object which creates an instance of the 'YesNo' type class for Ints:


~~~scala

object YesNo {
  implicit val intYesNo = new YesNo[Int] { 
    def yesno(value:Int) = 
      value match { case 0 => false;  case _ => true } }
}
~~~

We then need to call our 'yesno' function and the idea is that if we've defined a type class instance for the type we call it with it will return us a boolean value and if not then we'll get a compilation error.


~~~scala

object YesNoWriter {
  def write[A](value:A)(implicit  conv: YesNo[A]) : Boolean = {
    conv.yesno(value)
  }
}
~~~

If we call that:


~~~text

> YesNoWriter.write(1)
res1: Boolean = true

> YesNoWriter.write(0)
res2: Boolean = false
~~~

It works as expected, but if we try to call it with a type which wasn't defined for the 'YesNo' type class we run into trouble:


~~~text

> YesNoWriter.write("mark")
:10: error: could not find implicit value for parameter conv: YesNo[java.lang.String]
       YesNoWriter.write("mark")
~~~

We can also define YesNoWriter like this by making use of <a href="http://stackoverflow.com/questions/3855595/scala-identifier-implicitly">context bounds</a>:


~~~scala

object YesNoWriter {
  def write[A:YesNo](value:A) : Boolean = {
    implicitly[YesNo[A]].yesno(value)
  }
}
~~~

I think this pattern is preferred when we might just be tunnelling the implicit parameter through to another method but we can still use it here and use the 'implicitly' method to get access to the implicit value.


I'm still not entirely sure about the use of implicits but in this case they provide another way to implement polymorphism without having to use inheritance. 

<a href="http://marakana.com/s/scala_typeclasses,1117/index.html">Dan Rosen goes into much more detail about type classes and implicits</a> and I <a href="http://www.markhneedham.com/blog/2011/07/19/scala-rolling-with-implicit/">wrote about how we were using them on a project I worked on last year in an earlier blog post</a> if you want to learn more.
