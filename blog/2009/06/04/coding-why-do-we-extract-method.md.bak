+++
draft = false
date="2009-06-04 20:30:47"
title="Coding: Why do we extract method?"
tag=['coding', 'refactoring', 'extract-method']
category=['Coding']
+++

Ever since I've read <a href="http://www.markhneedham.com/blog/2008/09/15/clean-code-book-review/">Uncle Bob's Clean Code book</a> my approach to coding has been all about the '<a href="http://c2.com/cgi/wiki?ExtractMethod">extract method</a>' refactoring - I pretty much look to extract method as much as I can until I get to the point where extracting another method would result in me just describing the language semantics in the method name.

One of the approaches that I've come across with regards to doing this refactoring is that it's only used when there is duplication of code and we want to reduce that duplication so that it's all in one place and then call that method from two places.

While this is certainly a valuable reason for doing extracting method I think there are other reasons why we would want to do it more frequently than just this.

<h3>Expressing intent</h3>
One of the main reasons we design code in an object oriented way is that it often allows us to describe the intent of our code more clearly than we would be able to it we wrote it with a more procedural approach and I think the same thing applies when extracting methods inside a class.

Quite often when reading code we're interested in knowing a bit more about a class than we can derive from its name but we're not really that interested in all the low level details of its implementation.

If methods have been extracted abstracting all that detail away from us then <strong>we're able to quickly glance at the class and fairly quickly work out what is going on</strong> and then move back to working out what we were actually doing in the first place.

<h3>It makes code easier to read</h3>
A consequence of extracting that detail away is that it makes the code easier to read because <strong>we don't have to hold as much information about what is going on in our head at any one time</strong>.

The aim is to try and ensure that the chunks of code that we extract into a method are all at the same level of abstraction - Neal Ford refers to this as the Single Level of Abstraction Principle (SLAP) in <a href="http://www.markhneedham.com/blog/2008/09/05/the-productive-programmer-book-review/">The Productive Programmer</a>.

We would therefore not have a chunk of code which described some business concept or rule mixed in with a bit of code that was interacting with the database as an extreme example.

I find myself most frequently extracting method when I come across several lines of code doing similar operations, the aim being that when we read the code we don't need to care about each of the individual operations but just the fact that operations are being done.

<h3>It exposes semantic errors</h3>

One benefit which I hadn't actually appreciated until recently is that extracting a method can actually help to <strong>identify areas of code which shouldn't actually be where they are</strong>.

We were recently working on some code around starting up a Selenium session where the 'ResetSeleniumSession' method was doing the following:


~~~csharp

public ISelenium ResetSeleniumSession()
{
	if(Selenium != null)
	{
		Selenium.Stop();
	}
	Selenium = new CustomSelenium(....)
	Selenium.Start()
	Selenium.Open(ApplicationRootUrl);
	Selenium.WindowMaximize();
}
~~~
We didn't think those last two lines belonged in there so we extracted them out so that we could make sure that the opening of the selenium client was still being done in all the places that ResetSeleniumSession was being called:


~~~csharp

public ISelenium ResetSeleniumSession()
{
	...
	Selenium = new CustomSelenium(....)
	Selenium.Start()
	LoadAndMaximise(ApplicationRootUrl);
}
~~~

Later on another colleague passed by and saw us looking at this method and pointed out that it was wrong that we were launching the client from inside this method and had probably been added into that method by mistake!

Maybe that code would have been spotted anyway but it had been like that for a while and I think extracting it out into its own method to make it more obvious was useful for exposing that.

<h3>In Summary</h3>
That's all I can think of for the moment although I'm sure there are more reasons why we'd want to extract method.

From my experience extract method is the most useful refactoring that we can do and it can quickly make a bit of code that seems impossible to understand somewhat readable and it can help keep new code that we write easy for others to understand instead of becoming a legacy mess.
