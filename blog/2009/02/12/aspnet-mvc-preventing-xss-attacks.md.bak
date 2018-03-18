+++
draft = false
date="2009-02-12 22:47:30"
title="ASP.NET MVC: Preventing XSS attacks"
tag=['aspnet', 'mvc']
category=['.NET']
+++

<a href="http://en.wikipedia.org/wiki/Cross-site_scripting">XSS</a>(Cross site scripting) attacks on websites seem to be quite popular these days but luckily if you're working with the ASP.NET MVC framework Steve Sanderson has written a <a href="http://blog.codeville.net/2007/12/19/aspnet-mvc-prevent-xss-with-automatic-html-encoding/">great post on how to protect yourself from this</a>.

The solution Steve details works the opposite way to other solutions I have heard for this problem - we assume that everything that goes to the browser needs to be HTML encoded unless otherwise stated.

The benefit of this approach is that when we add new things to our page in the future we don't need to worry that we might have inadvertently reintroduced a security problem.

<h3>Excluding aspx code from being encoded </h3>

After setting up the encoding we came up against the problem of how to exclude HTML that we are generating from our aspx templates that we don't want HTML encoded.

This was a particular problem with our use of the HtmlHelper and UrlHelper provided with the framework.  

Since the majority of the methods we use are extension methods on these classes we didn't find it that easy to work out how to proxy those calls (we couldn't just override the methods since they aren't actually on HtmlHelper!) to our own RawHtmlHelper which could cast the result to RawHtml and therefore allow it to be rendered by the page.

The aim was to minimise the amount of things that we had to change. The worst case solution would be to have to go through all our aspx files and change every call to a Helper method to a new encoded version of the same method.

Luckily the <a href="">new</a> keyword comes to the rescue and allows us to hack around the problem.

We hooked into the page lifecycle to create a new version of the Html property which returned our RawHtmlHelper.


~~~csharp

public class BaseViewPage<TModel> : ViewPage<TModel> where TModel = class
{
	public override void InitHelpers() 
	{
		base.Html = new RawHtmlHelper(..);
		base.Url = new RawUrlHelper(...);
	}

	public new RawHtmlHelper Html 
	{
		get { return (RawHtmlHelper) base.Html; }
	}
}
~~~


~~~csharp

public class RawHtmlHelper : HtmlHelper 
{
	public RawHtml TextBox(string name, object value)
	{
		return (RawHtml) ((HtmlHelper)this).TextBox(name, value);
	}
}
~~~

In our aspx page we don't need to make any changes to our code in order for it to now use the RawHtmlHelper method instead of the HtmlHelper method. 


~~~text

<%= Html.TextBox("name", "value") %>
~~~

The only other change was to make each of our aspx code behind classes inherit from BaseViewPage so that they receive the new Html property.

<h3>Overall</h3>

There is way too much casting for my liking in this solution but I'm not sure if a better solution exists other than creating our own version of the helper methods named 'RawTextBox', 'RawRadioButton' and so on. 

The amount of work with that approach would be almost the same except if we have used the original HtmlHelper anywhere then we need to go and change all those too - exactly the problem we were trying to solve with the above solution.
