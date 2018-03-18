+++
draft = false
date="2011-07-26 22:31:58"
title="Scala: Prettifying test builders with package object"
tag=['scala']
category=['Scala']
+++

We have several different <a href="http://www.natpryce.com/articles/000769.html">test builders</a> in our code base which look roughly like this:


~~~scala

case class FooBuilder(bar : String, baz : String) {
	def build = new Foo(bar, baz)
}
~~~

In our tests we originally used them like this:


~~~scala

class FooPageTest extends Specs with ShouldMatchers {
	it("should let us load a foo") {
		when(databaseHas(FooBuilder(bar = "Bar", baz = "Bazz")))
		// and so on...
	}
}
~~~

This works well but we wanted our tests to only contain domain language and no implementation details.

We therefore started pulling out methods like so:


~~~scala

class FooPageTest extends Specs with ShouldMatchers {
	it("should let us load a foo") {
		when(databaseHas(aFooWithBarAndBaz("Bar", "Bazza")))
		// and so on...
	}

	def aFooWithBarAndBaz(bar:String, baz;String) = FooBuilder(bar = bar, baz = baz)
}
~~~

This was fine to start with but we eventually ended up with 10-12 different variations oh how <cite>Foo</cite> could be constructed, negating the value that the builder pattern provides.

Instead what we can do is use of an alias of <cite>FooBuilder</cite> to achieve something equally readable:


~~~scala

package object TestSugar {
	val aFooWith = FooBuilder
}
~~~

We can then use <cite>aFooWith</cite> like so:


~~~scala

import TestSugar._

class FooPageTest extends Specs with ShouldMatchers {
	it("should let us load a foo") {
		when(databaseHas(aFooWith(bar = "Bar", baz = "Bazza")))
		// and so on...
	}
}
~~~

We could also achieve that by renaming <cite>FooBuilder</cite> to <cite>aFooWith</cite> but that makes it much less discoverable whereas this solution lets us achieve both goals.

The package object approach isn't really needed - we could easily put those vals onto an Object or Class but they don't really seem to belong to any which is why we've gone for this approach.
