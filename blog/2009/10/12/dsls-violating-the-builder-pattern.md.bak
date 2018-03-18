+++
draft = false
date="2009-10-12 22:20:16"
title="DSLs: Violating the builder pattern"
tag=['c', 'dsl']
category=['Coding']
+++

I recently came across <a href="http://pragdave.blogs.pragprog.com/pragdave/2008/03/the-language-in.html">an interesting post by Dave Thomas</a> where he discussed several domain specific languages (DSLs) he's come across and suggests that a lot of them seem to be trying too hard to read like the english language instead of focusing on describing a vocabulary for their specific domain

Reading this post reminded me that I fell into this trap earlier in the year while doing some work to create a builder pattern in our code which didn't need to make use of a 'Build' method but instead would make use of <a href="http://www.markhneedham.com/blog/2009/02/22/c-implicit-operator/">C#'s implicit operator to automatically convert the builder to an object at the appropriate moment</a>.

My motivation was to make the code more readable but the code actually ended up being quite misleading for anyone else who came across it.

When someone sees the builder pattern they have an expectation that the method chaining sequence should end with 'Build()' so by using the implicit operator I was essentially breaking a well defined DSL for creating new objects.

To add to our problems, we nearly always use 'var' to describe local variables in our code base so there we times when you couldn't tell if what you had was a 'Foo' or a 'FooBuilder'.

Quite frequently the implicit conversion only happens when the variable is passed into another method or construct which explicitly defines which value is needed.


~~~csharp

[Test]
public void SomeRandomTest()
{	
	var foo = new FooBuilder().Foo("someValue");

	var someFoos = new Foo[] { foo }; 
}	
~~~
In this example 'foo' is only implicitly converted to the type 'Foo' when it is put into the array and its actual type is 'FooBuilder'.

In terms of what I was trying to achieve I created a piece of code that was easier to read but more difficult to understand which means that it's not intention revealing <a href="http://twitter.com/sai_venkat/statuses/4624116366">as my colleague Sai Venkatakrishnan pointed out</a>.

It was an interesting experiment but I think in the future I'll stick with the more obvious approach which is a bit more verbose but a bit more intention revealing as well.
