+++
draft = false
date="2011-09-25 10:24:20"
title="Scala: Replacing a trait with a fake one for testing"
tag=['scala']
category=['Scala']
+++

We recently wanted to replace a trait mixed into one of our classes with a fake version to make it easier to test but forgot how exactly to do that!

The class is roughly like this:


~~~scala

trait Foo { def foo : String = "real foo" } 
class Mark extends Foo {}
~~~

We originally tried to replace it like this:


~~~scala

trait BrokenFakeFoo { def foo : String = "broken fake foo" }
val m = new Mark with BrokenFakeFoo
~~~


~~~text

error: overriding method foo in trait Foo of type => String;
 method foo in trait BrokenFakeFoo of type => String needs `override' modifier
       val m = new Mark with BrokenFakeFoo
~~~

If <cite>m</cite> compiled it would have two versions of <cite>foo</cite> but it wouldn't know which one to use, hence the error message.

Attempt two was this:


~~~scala

trait BrokenFakeFoo { override def foo : String = "broken fake foo" }
~~~


~~~text

error: method foo overrides nothing
       trait BrokenFakeFoo { override def foo : String = "broken fake foo" }
~~~

As <a href="https://github.com/uday-rayala">Uday</a> pointed out, what we actually need to do is make our fake trait extend the original one and then override the method.


~~~scala

trait FakeFoo extends Foo { override def foo : String = "fake foo" }
val m = new Mark with FakeFoo
~~~


~~~text

m.foo
> res5: String = fake foo
~~~

Since <cite>FakeFoo</cite> is the right most of the traits mixed into <cite>Mark</cite> its <cite>foo</cite> method will be used over the <cite>Foo</cite> one mixed into <cite>Mark</cite> on its class definition.
