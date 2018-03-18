+++
draft = false
date="2009-02-16 22:04:20"
title="C#: Object Initializer and The Horse Shoe"
tag=['coding', 'c']
category=['.NET']
+++

The <a href="http://davidhayden.com/blog/dave/archive/2006/12/04/ObjectInitializationExpressions.aspx">object initializer</a> syntax introduced in C# 3.0 makes it easier for us to initialise our objects in one statement but I think we need to remember that they are not <a href="http://en.wikipedia.org/wiki/Named_parameter">named parameters</a> and that there is still a place (a very good one actually) for creating objects from constructors or factory methods.

Unfortunately what I think the cleaner syntax does is encourage us to create objects with half the fields populated and half of them null by default.

When we didn't have the object initializer syntax we would have to set properties on objects like so:


~~~csharp

var foo = new Foo();

var bar = new Bar();
bar.Baz = new Baz();

foo.Bar = bar;
~~~

It takes a lot of extra boiler plate code to achieve this and it looks terrible, hopefully driving us towards using the constructor to initialise our objects.

Object initializers makes it much easier to achieve the same thing but at its worst we end up with code similar to the following which to me <strong>looks a bit like a horse shoe</strong>, an anti pattern in my opinion.


~~~csharp

new Foo 
{ 
	Bar = new Bar 
	{ 
		Baz = new Baz 
		{
			Other = new Other
			{
				Value = "value",
				OtherValue = "otherValue"
			}
		}
	}
}
~~~

I don't think we should write code like this - to me <strong>it's not expressive and it's difficult to understand</strong> why certain fields are set or not set. You end up having to think how this code fits into the bigger picture in order to understand it - extra context which shouldn't be necessary. 

From experience we also end up in the debugger much more frequently than should be the case, trying to work out why certain fields are set. I feel this leads to very implicit code where you have to work out what is going on/where you are in the work flow by checking the state of our objects. 

Of course the problem here is the reliance on properties (i.e. getters/setters) to instantiate our objects rather than object initializer in itself but the new syntax has made it much easier for us to do it.

Certainly there are some times when it's quite nice to have the object initializer syntax but as with most things we need to be careful not to overdo it.
