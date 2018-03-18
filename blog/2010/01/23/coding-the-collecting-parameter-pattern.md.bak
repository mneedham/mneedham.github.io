+++
draft = false
date="2010-01-23 14:45:59"
title="Coding: The collecting parameter pattern"
tag=['coding']
category=['Coding']
+++

The <a href="http://www.industriallogic.com/xp/refactoring/accumulationToCollection.html">collecting parameter pattern</a> is one of my favourite ones when used well but I've noticed recently that it can lead to quit misleading APIs as well.

One way that we used it quite effectively was when <a href="http://www.markhneedham.com/blog/2009/03/10/oo-micro-types/">getting objects to render themselves to a ViewData container</a> which was then used to populate the view. 


~~~csharp

public class Micro {
	private string micro;
 
	public Micro(string micro) {
		this.micro = micro;
	}
 
	public void renderTo(ViewData viewData) {
		viewData.add(micro);
	}
}
~~~

I think it's quite obvious from the method name what it does and we can easily test this method by checking on the contents of the value passed in after the method's been executed.

The problem I've noticed with this pattern is when the method isn't so explicit about what it's doing or where a method is using a collecting parameter as well as returning a value.

For example:


~~~csharp

public SomeModel GetModel(ViewData viewData) 
{
	viewdata["someKey"] = "someValue;
	// do some other stuff

	return new SomeModel(...); 
}
~~~

It's not entirely obvious from reading the method signature that it would be mutating the 'ViewData' that's been passed in. I would actually expect that 'SomeModel' is being constructed from 'ViewData' if I just read the method signature in isolation. It's almost like it's following the collecting parameter pattern by accident. 

In a way I find that API as misleading as ones which make use of an 'out' parameter to allow multiple values to be returned - it doesn't do what you expect, its <strong>intent is not clear</strong>.

Since I've started playing around with functional programming languages I've become more keen on the idea that functions take in inputs and return outputs and this pattern goes against that idea by encouraging mutation of state.

It seems to me that for the most part writing functions which return a value and don't do anything else reveal their intent more and for the less frequent occasions where we want to keep encapsulation but still find out some data about an object the collecting parameter pattern works pretty well. It should be used sparingly though.
