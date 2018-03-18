+++
draft = false
date="2009-09-19 02:24:11"
title="Set Based Concurrent Engineering: A simple example"
tag=['lean', 'concurrent-set-based-engineering']
category=['Lean']
+++

One of my favourite ideas that I came across while reading the Poppendieck's <a href="http://www.markhneedham.com/blog/2008/12/20/lean-software-development-book-review/">Lean Software Development</a> is  set based concurrent engineering which encourages us to keep our options open with regards to the solution to a problem  until we absolutely need to decide on an approach after which we probably can't easily change that decision so we will most likely stick with it.

I like the idea but on the projects I've worked on we often seem to take a more point based approach - there will be some discussion up front on the potential solutions to a problem and eventually one of them will be considered to be the best solution and we go and implement that one.

Last week we were doing more work on getting an authenticated user into our system and on this occasion we were trying to work out the best way to get some of the user's details into our 'Service' base class so that we could send down the user's SAML token with specific requests.

We identified two solutions to do this - inject the user into the Service through a constructor or inject it via a property.

A colleague and I were in favour of the constructor based approach since it results in us creating an object which has all its dependencies ready at creation.

<a href="http://erik.doernenburg.com/">Erik</a> and another colleague favoured the introduction of setter injection in this case since we could just add that to the top level abstract class and avoid the problem that we would have with constructor injection whereby every sub class would need to have that constructor defined.  


~~~csharp

public abstract class Service
{
	public Service(User user)
	{
	
	}
}

public class SomeService : Service
{
	public SomeService(User user) : base(user) { }
	// every sub class of Service would need this constructor
}
~~~

We decided to try out both of these solutions concurrently for a time boxed period and then go with the one which looked like it was working out better.

While pursuing the constructor based approach we actually ran into a problem trying to resolve the services - it seems to be a bug in Unity Container version 1.2 which <a href="http://unity.codeplex.com/WorkItem/View.aspx?WorkItemId=3696">doesn't allow you to use parameters in the constructor of a type which is being intercepted by a 'VirtualMethodInterceptor'</a> which we are making use of for caching some service requests.

We spent a bit of time trying to debug this to work out what was going on but the code eventually fails when trying to emit some IL code.

I tried the latest version of the container out separately and it seemed to work correctly for the same situation so I think the bug has been fixed now.

By this time the time box was up and my other colleague had got further with the setter based approach than we had managed to get so we decided to go with that approach instead.

I think it was still an interesting approach to take as we learnt a bit more about how the container works and we got to see the trade off that we would be making if we used constructor injection between keeping our objects 'pure' and creating a lot of boiler plate code to create the constructor for each new service class - we went through about 30 classes putting the new constructor in!

