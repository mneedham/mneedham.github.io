+++
draft = false
date="2009-04-08 05:43:43"
title="Coding: Passing booleans into methods"
tag=['coding']
category=['Coding']
+++

In a post I wrote a couple of days ago about <a href="http://www.markhneedham.com/blog/2009/04/05/coding-criticising-without-context/">understanding the context of a piece of code before criticising it</a>, one of the examples that I used of a time when it seems fine to break a rule was passing a boolean into a method to determine whether or not to show an editable version of a control on the page.

Chatting with <a href="http://pilchardfriendly.wordpress.com/">Nick</a> about this yesterday it became clear to me that I've missed one important reason why you'd not want to pass a boolean into a method.

The first reason I hate passing booleans around is that it usually means <strong>we are controlling the path code should take inside a method</strong> rather than just calling the appropriate method ourself.

The following type code is not that unusual to see:


~~~csharp

public void SomeMethod(bool someBoolean) 
{
	if(someBoolean) 
	{
		// doThis
	}
	else
	{
		// doThat		
	}
}
~~~

The client of this method knows what it wants to happen so why not just have two methods, like so:


~~~csharp

public void DoThis() 
{
}
~~~


~~~csharp

public void DoThat() 
{
}
~~~

In the specific case I was referring to in the post we had a HtmlHelper (ASP.NET MVC) method called DropDownOrReadOnly which either rendered a drop down with options for a user to select or just displayed the option they had previously selected if they were an existing user.

The boolean in this case was a property on the model which indicated whether or not the user had the ability to change these options or not.

It was therefore a case of doing an if statement in the aspx page or inside the helper. Initially we went for putting it in the aspx page but they started to look so messy we moved it into the helper.

Now what I totally didn't see in this example until Nick pointed it out is that where we are passing in a boolean to this method, what we really want is an object which defines a strategy for how we render the control - we can delegate the decision for whether to display a drop down or read only version of the control.

Instead of passing in a boolean we could end up with something like this:


~~~csharp

public abstract class EditMode
{
    public static readonly EditMode Editable = new Editable();
    public static readonly EditMode ReadOnly = new ReadOnly();

    public abstract void RenderFieldWith(HtmlHelper htmlHelper);
}
~~~


~~~csharp

public class Editable : EditMode
{
    public override void RenderFieldWith(HtmlHelper htmlHelper)
    {
        htmlHelper.Label(...);
    }
}
~~~


~~~csharp

public class ReadOnly : EditMode
{
    public override void RenderFieldWith(HtmlHelper htmlHelper)
    {
        htmlHelper.DropDownList(...);
    }
}
~~~

We've added the 'Label' method to HtmlHelper as an extension method for the sake of the above example. I'm sure the API for EditMode can be done better but that's the basic idea.

We could then use it like this:


~~~csharp

public static class HtmlHelperExtensions
{
    public static void DropDownOrReadOnly(this HtmlHelper htmlHelper, EditMode editMode)
    {
        editMode.Render(htmlHelper);
    }
}
~~~

Again I've simplified the API to show the idea of delegating responsibility for how we render the control to the EditMode. Nick has written more about this idea in a post about <a href="http://pilchardfriendly.wordpress.com/2009/04/06/refactoring-to-law-of-demeter/">refactoring to the law of demeter</a>.

The final reason that passing booleans around is not a great idea is that when you read the code it's not immediately obvious what's going on - <strong>the API is not expressible at all</strong>.

If we compare


~~~csharp

HtmlHelper.DropDownOrReadOnly(true)
~~~

with


~~~csharp

HtmlHelper.DropDownOrReadOnly(EditMode.ReadOnly)
~~~

I think it's clear that with the second approach it's <a href="http://www.markhneedham.com/blog/2009/03/18/coding-make-it-obvious/">much easier</a> for someone coming into the code to understand what is going on.


