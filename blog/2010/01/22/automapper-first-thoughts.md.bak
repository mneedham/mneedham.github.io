+++
draft = false
date="2010-01-22 23:21:56"
title="Automapper: First thoughts"
tag=['automapper']
category=['.NET']
+++

I came across Jimmy Bogard's <a href="http://www.codeplex.com/AutoMapper">Automapper</a> library a while ago but hadn't had the opportunity to try it out on a project until this week.

The problem we wanted to solve was relatively simple. 

We had a domain object and we wanted to create a copy of that with one of the fields changed and all of the ids cleared from the object and any objects contained within it so that we could persist the new web of objects to the database.

We had a structure a bit like this:


~~~csharp

public class Foo 
{
	public Bar Bar { get; set; }
	public Baz Baz { get; set; }
}
~~~

And wanted to create a copy of this object while changing one of the values on Baz:


~~~csharp

Mapper.CreateMap<Foo, Foo>().ForMember(x => x.Id, opts => opts.Ignore());
Mapper.CreateMap<Bar, Bar>().ForMember(x => x.Id, opts => opts.Ignore());
Mapper.CreateMap<Baz, Baz>()
      .ForMember(x => x.Id, opts => opts.Ignore())
      .ForMember(x => x.SomeProperty, opts => opts.MapFrom(source => someNewValue));
~~~

It works really well although it took me a little while to realise that the 'Mapper' class was keeping track of what we'd set up via its methods internally.

<a href="http://www.lostechies.com/blogs/jimmy_bogard/archive/2009/12/23/automapper-dsl-design-post-mortem.aspx">Jimmy refers to this as the static gateway pattern</a> which seems a little similar to the way that Rhino Mocks keeps track of expectations from what I remember from <a href="http://www.markhneedham.com/blog/2009/07/28/reading-code-rhino-mocks/">reading some of the code</a>.

In general though I've got more used to expression builder style DSLs so it was interesting to see one which has been done with a different approach. 

The next thing we had to work out was where that mapping code should go. 

Since it's completely about 'Foo' I originally thought it should go inside Foo on a static method which we could use to clone the object perhaps with an API like this:


~~~csharp

public Foo CloneWith(string someNewValue)
{
	// mapping code in here
}
~~~

The problem with that is that it means we have a static dependency in our domain model and from reading <a href="http://alistair.cockburn.us/Hexagonal+architecture">Alistair Cockburn's Hexagonal Architecture article</a> I've come to believe that we should try to ensure that objects in our domain model don't have dependencies on anyone else.

An alternative might be to have it on the object and then create an interface which represents the ability to clone Foo:


~~~csharp

public Foo CloneWith(string someNewValue, ICanCloneAFoo fooCloner)
{
	return fooCloner.Clone();
}
~~~

The mapping code would then go on the implementer of 'ICanCloneAFoo'. The discussions we had around this reminded me of <a href="http://www.markhneedham.com/blog/2009/02/09/oop-what-does-an-objects-responsibility-entail/">a post I wrote about a year ago</a> and the solution we decided to use was the same. We put the mapping code onto a mapper object.

It's not a bad solution as it follows the convention that's been done for other mapping problems in the code although as <a href="http://twitter.com/mikewagg">Mike</a> pointed out, the code to clone the object is not as discoverable as it would be if it was on the object itself.

In that mapper we're still calling the Automapper code directly which I think is fine although I'm not sure whether we're quite adhering to the idea of wrapping 3rd party libraries, as suggested in <a href="http://www.amazon.com/gp/product/0321503627?ie=UTF8&tag=marneesblo-20&linkCode=as2&camp=1789&creative=390957&creativeASIN=0321503627">Growing Object Oriented Software</a>, and not allowing them to bleed into our code base. 

It seems like in the case doing that might lead to more problems than it would solve.
