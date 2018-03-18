+++
draft = false
date="2011-11-06 21:25:06"
title="Scala: Which implicit conversion is being used?"
tag=['scala']
category=['Scala']
+++

Last week my colleague <a href="http://twitter.com/patforna">Pat</a> created a method which had a parameter which he wanted to make optional so that consumers of the API wouldn't have to provide it if they didn't want to.

We ended up making the method take in an implicit value such that the method signature looked a bit like this:


~~~scala

def foo[T](implicit blah:(String => T)) = {
  println(blah("mark"))
  "foo"
}
~~~

We can call foo with or without an argument:


~~~scala

scala> foo { x => x + " Needham" } 
mark Needham
res16: java.lang.String = foo
~~~


~~~scala

scala> foo 
mark
res17: java.lang.String = foo
~~~

In the second case it seems like the function is defaulting to an identity function of some sorts since the same value we pass to it is getting printed out. 

We figured that it was probably using one of the implicit conversions in <cite>Predef</cite> but weren't sure which one.

I asked about this on the Scala IRC channel and Heikki Vesalainen suggested running <cite>scala</cite> with the '-print' flag to work it out.


~~~scala

scala -print
~~~

The output is pretty verbose but having defined foo as above this is some of the output we get when calling it:


~~~scala

scala> foo
[[syntax trees at end of cleanup]]// Scala source: <console>
package $line2 {
  final object $read extends java.lang.Object with ScalaObject {
    def this(): object $line2.$read = {
      $read.super.this();
      ()
    }
  };
  final object $read$$iw$$iw extends java.lang.Object with ScalaObject {
    private[this] val res0: java.lang.String = _;
    <stable> <accessor> def res0(): java.lang.String = $read$$iw$$iw.this.res0;
    def this(): object $line2.$read$$iw$$iw = {
      $read$$iw$$iw.super.this();
      $read$$iw$$iw.this.res0 = $line1.$read$$iw$$iw.foo(<strong>scala.this.Predef.conforms()</strong>);
      ()
    }
  };
  final object $read$$iw extends java.lang.Object with ScalaObject {
    def this(): object $line2.$read$$iw = {
      $read$$iw.super.this();
      ()
    }
  }
}
~~~

I've highlighted the call to <cite>Predef.conforms()</cite> which is the implicit conversion that's been substituted into 'foo'.

It's defined like so:

<a href="http://www.scala-lang.org/api/current/index.html#scala.Predef$$$less$colon$less">Predef.scala</a> 

~~~scala

implicit def conforms[A]: A <:< A = new (A <:< A) { def apply(x: A) = x }
~~~

I'm not sure where that would be legitimately used but the comments just above it suggest the following:


~~~text

An instance of `A <:< B` witnesses that `A` is a subtype of `B`.
~~~

This is probably a misuse of implcits and we intend to replace the implicit in our code with a default function value but it was interesting investigating where the implicit had come from!
