+++
draft = false
date="2009-11-10 06:33:22"
title="Legacy Code: Sensing"
tag=['legacy-code', 'michael-feathers']
category=['Coding']
+++

In '<a href="http://www.amazon.com/gp/product/0131177052?ie=UTF8&tag=marneesblo-20&linkCode=as2&camp=1789&creative=390957&creativeASIN=0131177052">Working Effectively With Legacy Code</a>' Michael Feathers describes two reasons for wanting to break dependencies in our code - to allow <a href="http://www.markhneedham.com/blog/2009/10/20/book-club-working-effectively-with-legacy-code-chapters-34-5-michael-feathers/">separation and sensing</a>.

The former describes the need to get a piece of code into a test harness while the latter describes the need to assert whether that piece of code is doing what we want it to.

On the projects I've worked on we've tended to run into problems with the latter more frequently and Matt and I actually ran into this problem when we were <a href="http://www.markhneedham.com/blog/2009/10/18/coding-role-based-interfaces/">refactoring some code into a role based interface approach</a>.

We started with the following code:


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
 
	private IContent BuildContent()
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

The 'BuildContent' method is the one that we're really interested in here but it's a private method on the controller so we currently don't have an easy way to assert that it's being created correctly.

In order to test that functionality more easily we decided to make the method public so we could just call it directly. 

We wanted to do this so that we could write some tests around this bit of functionality before we refactored it so that we could be sure we hadn't broken the way it worked while doing so.

As <a href="http://hamletdarcy.blogspot.com/2009/06/forgotten-refactorings.html">Hamlet D'Arcy points out, if we're going to call it refactoring then we need to make sure that we're protected by tests</a>. Otherwise we're just changing stuff.


~~~csharp

[Test]
public void ShouldCreateContent()
{
	var someRepository = MockRepository.CreateMock<ISomeRepository>();

	var controller = new BusinessType1Controller(someRepository);

	someRepository.Expect(s => s.GetBusinessType1Message()).Return("someValue");

	var content = controller.BuildContent();

	// and so on	
}
~~~

We did the same for the other business types as well.

I normally don't like making private methods public but we didn't intend to checkin our code until the refactoring was complete at which point the method would be made private again. 

The code ended up something like this:


~~~csharp

public class BusinessType1Controller : ApplicationController
{
	public override IContent CreateContent()
	{
		return new BusinessType1Content(someRepository);
	}
}
~~~


~~~csharp

public class BusinessType1Content : IContent
{
	private readonly ISomeRepository someRepository;

	public BusinessType1Content(ISomeRepository someRepository)
	{
		this.someRepository = someRepository;
	}

	public string GetMessage()
	{
		// this would be a different repository call for other business types
		return someRepository. GetBusinessType1Message();
	}
}
~~~

We were able to create a test against the business types directly instead of having to write a test against the controller:


~~~csharp

[Test]
public void ShouldCreateContent()
{
	var someRepository = MockRepository.CreateMock<ISomeRepository>();

	var content = new Content(someRepository);

	someRepository.Expect(s => s.GetBusinessType1Message()).Return("someValue");

	var message = controller.GetMessage();

	// and so on	
}
~~~

Having got these new tests passing the ones we'd written against 'BuildContent' now also worked and since they were effectively testing the same thing we were able to get rid of them and make 'BuildContent' private again.

Despite the fact that I was initially reluctant to expose the 'BuildContent' method this approach seemed to work out reasonably well.

An alternative approach would have been to create a test only ApplicationController and then create a method on that which called the 'OnActionExecuting' method.

We've done that to test some other things and it would have allowed us to test the creation of 'Content' in a more roundabout way without needing to make 'BuildContent' public.

The additional effort involved in doing that for not much gain means that given a similar situation in the future I'd probably use just make the method public again!
