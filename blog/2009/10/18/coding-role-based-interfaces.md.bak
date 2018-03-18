+++
draft = false
date="2009-10-18 20:33:39"
title="Coding: Role based interfaces"
tag=['coding']
category=['Coding']
+++

I've <a href="http://www.mockobjects.com/files/usingmocksandtests.pdf">read a bit about role based interfaces</a> but I've never really quite understood how the idea could be applied into our code - this week my colleague Matt Dunn has been teaching me.

We had a requirement to show some content on every page of the website we're working on. The content would be slightly different depending on which business process you're doing.

Our first solution made use of an already defined 'BusinessType' property which allowed us to work out which content we needed to create. 


~~~csharp

public class ApplicationController : Controller
{
	public string BusinessType
	{
		get { return GetType().Replace("Controller", ""); }
	}

	public override void OnActionExecuting(ActionExecutingContext context) 
	{
    		base.OnActionExecuting(context);
		ViewData["SomeViewDataKey"] = CreateThatViewDataStuff();
	}

	private ViewDataStuff CreateThatViewDataStuff()
	{
		return new ViewDataStuff 
		{
			Content = BuildContent()
			// and so on
		};
	}

	private Content BuildContent()
	{
		if(BusinessType == "BusinessType1")
		{
			return CreateContentForBusinessType1();
		}
		else if(BusinessType == "BusinessType2")
		{
			return CreateContentForBusinessType2();
		}
		else
		{
			return CreateContentForEveryOtherBusinessType();
		}
	}
}
~~~


~~~csharp

public class BusinessType1Controller : ApplicationController { }
public class BusinessType2Controller : ApplicationController { }
~~~

The problem is that it's really hacky, way too much is going on in the ApplicationController and every time we have a business type which has different content we have to add to the mess.

We decided to make use of polymorphism to make the solution a bit cleaner and my initial thought was that we could just create a 'CreateContent' method on the ApplicationController and then override that if necessary in the other controllers. 

Matt suggested that we should take this a step further and define that method as part of an interface called 'IContentFactory'. 

With this approach we would then be able to just pass a reference to that interface into the 'ViewDataStuff' class which can delegate to the 'IContentFactory' when the content is requested. 

In this case in the 'CreateContent' methods we were making network calls to retrieve data so it allowed us to <a href="http://www.markhneedham.com/blog/2009/09/02/coding-reduce-fields-delay-calculations/">delay these calls until strictly necessary</a>.



~~~csharp

public class ApplicationController : Controller, IContentFactory
{
	public override void OnActionExecuting(ActionExecutingContext context) 
	{
    		base.OnActionExecuting(context);
		ViewData["SomeViewDataKey"] = CreateThatViewDataStuff();
	}

	private ViewDataStuff CreateThatViewDataStuff()
	{
		return new ViewDataStuff(this) 
		{
			// and so on
		};
	}

	public virtual Content CreateContent()
	{
		return new Content(...);
	}
}
~~~


~~~csharp

public class BusinessType1Controller : ApplicationController
{
	public override Content CreateContent()
	{
		// creates the Content object slightly differently.
		return new Content(...); 
	}
}
~~~


~~~csharp

public class ViewDataStuff
{
	private readonly IContentFactory content;

	public ViewDataStuff(IContentFactory content)
	{
		this.content = content;
	}

	public Content Content 
	{
		get { return content.CreateContent(); }
	}
}
~~~

We thought about using <a href="http://www.testingreflections.com/node/view/7234">Udi Dahan's naming notation for interfaces</a> but the factory pattern is quite well known so it seemed like we might creation more confusion by doing that.

I think it'd be interesting to see what we'd have come up with if we'd test driven this code rather than refactored it into this pattern.

Overall though it seems quite neat as an approach and the next time we came across some similar code I was able to introduce a role based interface having been taught how to do it by Matt on this one.
