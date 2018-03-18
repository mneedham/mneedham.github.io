+++
draft = false
date="2009-06-16 23:37:04"
title="Book Club: Arguments and Results (James Noble)"
tag=['books', 'papers', 'james-noble', 'arguments-and-results']
category=['Book Club']
+++

We restarted our book club again last week by reading <a href="http://www.laputan.org/pub/patterns/noble/noble.pdf">James Noble's Arguments and Results paper</a>, a paper I came across from a <a href="http://blog.objectmentor.com/articles/2009/02/26/10-papers-every-programmer-should-read-at-least-twice">Michael Feathers blog post a few months ago detailing 10 papers that every programmer should read</a>.

We decided to try out the idea of reading papers/individual chapters from books as it allows us to vary the type of stuff we're reading more frequently and is an approach which <a href="http://blog.obiefernandez.com/content/2009/06/agile-design-o-rly.html">Obie seems to be having some success with</a>.

This firs half of paper describes some approaches for detailing with complexity in the arguments that we send to methods and the second half approaches for the results that we get back from methods.

We split the different patterns between us and attempted to come up with examples in code we'd worked on where we'd seen each of the patterns in use.

<h3>Arguments Object</h3>
This pattern is used to simplify a method's signature by grouping up the common arguments and object and changing the method signature to take in this object instead.

The author quotes <a href="http://en.wikipedia.org/wiki/Alan_Perlis">Alan Perlis</a> as saying "If you have a procedure with 10 parameters you probably missed some" which I think best sums up the reason why you would want to do this refactoring.

Another advantage of doing this, which <a href="http://camswords.wordpress.com/">Cam</a> pointed out, is that it may help to bring out domain concepts which weren't explicit before.

The disadvantage of this approach is that we make it more difficult for clients to use our API. I think this was <a href="http://www.markhneedham.com/blog/2009/04/27/coding-weakstrong-apis/#comment-15672">best summed up in a comment on a post I wrote about using weak or strong APIs</a> by 'Eric':

<blockquote>


The choice is between passing (1) what the client probably has on hand already (the pieces) vs. passing (2) what the class demands (a pre-formed object). Which serves the client better and more naturally?

Which brick-and-mortar shop gets more business–the one taking credit cards (already in the customers' hands), or the one demanding cash in some foreign currency (which the customers first have to go get)?

Subordinate the service's convenience to the client's. Accept what a client likely has at the ready. (At the least, offer an overloaded constructor that does so.)

</blockquote>

A simple example from some code I worked on recently involved refactoring a few methods similar to this:


~~~csharp

public void Process(string streetName, string streetNumber, string state) { }
~~~

to:


~~~csharp

public void Process(Address address) { }
~~~

Some other examples which we thought of were:

<ul>
<li>The way that Ruby makes use of hashmaps to pass data into constructors instead of passing in each option individually to a separate parameter</li>
<li><a href="http://www.martinfowler.com/apsupp/spec.pdf">The specification pattern</a>/Query object pattern</li>
</ul>

<h3>Selector Object</h3>
This pattern is used to try and reduce the number of similar methods that exist on an object by creating one method which takes in the original object and an additional 'selector object' argument which is used to determine what exactly we do inside the new method.

The author also describes another way of solving this problem which is to build a small inheritance hierarchy and then make use of the double dispatch pattern to determine which specific method needs to be called.

The advantage of this pattern is that it helps to simplify the API of the object as there is now just one method to call to perform that specific operation.

The disadvantage is that the client of this object needs to do more work to use it although again I feel that this patterns helps to draw out domain concepts and move behaviour to the correct places.

I worked on a project where we did something similar to this although I'm not sure if it's exactly the same:


~~~csharp

public abstract class OurObject 
{
	public abstract void Configure(Configuration configuration)
}

public class ObjectOne : OurObject
{
	public void Configure(Configuration configuration)
	{
		configuration.ConfigureObjectOne(this);
	}
}

public class ObjectTwo : OurObject
{
	public void Configure(Configuration configuration)
	{
		configuration.ConfigureObjectTwo(this);
	}
}
~~~


~~~csharp

public class Configuration
{
	public void ConfigureObjectOne(ObjectOne objectOne)
	{
		// do config stuff
	}	

	public void ConfigureObjectTwo(ObjectTwo objectTwo)
	{
		// do config stuff
	}	
	...
}
~~~

We felt that possibly the <a href="http://en.wikipedia.org/wiki/Composite_pattern">composite pattern</a> might work well especially for the example described in the paper although we didn't come up with any other examples of this pattern on code we'd worked on.

<h3>Curried Object</h3>
This pattern is used to help simplify the arguments that a client needs to send to an object by simplifying that interface through the use of a 'curried object' which takes care of any values that the object needs which the client doesn't need to worry about (these could be arguments which don't really change for example). 

The client now sends its arguments to the 'curried object' which is then sent to the object. 

I've come across the idea of <a href="http://diditwith.net/2008/01/30/WhyILoveFFunctionsFunctionsFunctions.aspx">currying</a> while playing around with F# and in the functional world it seems to be about composing functions together, each of which only takes in one argument. I'm not sure if the author uses such a strict definition as that.

The advantage of this pattern is that it helps to simplify things for the client of the object although we now add in a level of indirection into the code because we send data to the 'curried object' which is actually executed by another example.

I'm not sure whether it's strictly currying but an example which seemed to fit into this pattern is where we make calls to external services which might require some arguments passed to them that the rest of our application doesn't care about. 

We therefore keep this setup inside a 'Gateway' object which the rest of our code interacts with. The 'Gateway' object can then send the external services this data and the data we pass it.

<a href="http://en.wikipedia.org/wiki/Iterator">Iterators</a> are suggested as being the most common use of currying in our code as they shield us from the internals of how the data is stored.

<h3>Result Object</h3>
This pattern is used to allow us to keep the results of potentially expensive operations so that we don't need to make several of these expensive calls to get the data that we want.

The advantage of doing this is that we are able to make out code more efficient although the client needs to do more work to get the data they care about out of the returned object.

An example of this could be if we are making a call across the network to get some data. If there are three pieces of data that we want then it makes more sense to get all this data in one 'result object' 
instead of making individual calls for the data.

I think this pattern is also useful in situations where there are multiple outcomes from an operation and we want to signify this in the result we return. 

An example of where this might be useful could be if we want to know whether a call was successful or not and if it wasn't then we want details about the way in which it failed. This could easily be modeled in a result object.

I'm not sure whether an Option/Maybe in functional programming could be considered to be a result object - they do return more information than other data types do although this isn't for performance purposes.

<h3>Future Object</h3>
This pattern is used when we want to perform an expensive operation and do something else while we wait for that operation to return - effectively we want to asynchronously process a result and then probably call a callback when it's done.

This pattern is useful when we want to go and get some data via a network call but we don't want to freeze up the user interface while we're doing that. I think this pattern is probably more applicable for client side applications than on the web where the typical approach I've seen is to block the use from doing anything while an operation is being executed. Perhaps something like Gmail does make use of this pattern though, I'm not sure.

The concurrency aspects should be taken care of by the 'future object' in this pattern meaning that the future object will be more complicated than other code. 

<a href="http://www.infoq.com/articles/pickering-fsharp-async">F# asynchronous work flows</a> certainly seem to be an example of this pattern whereby we make use of other threads to make network calls or put data into a database before returning results to the main thread when they're done.

<h3>Lazy Object</h3>
This pattern is used when we want to return a result but we don't know whether or not that method will actually be called - we therefore only get the data when the method is actually called.

The advantage of this is that we don't get data unnecessarily although it can be difficult to debug since we don't know exactly when the data is going to be fetched.

An example of this is Hibernate which by <a href="http://docs.jboss.org/hibernate/stable/core/reference/en/html/performance.html">default lazy loads</a> our data. If we later on try to access some data inside an aggregate root then we need to ensure that we have a Hibernate session open so that it is able to go and fetch the data for us.

F# also has a 'lazy' keyword which we can use to create lazy values which are only evaluated when specifically called:


~~~ocaml

let foo value = 
    printfn "%d" value
    value > 10
    
let fooBar = lazy foo 10    

> fooBar.Force();;
10
false
~~~

<a href="http://dotnetperls.com/lazy-linq-queries">LINQ in C#</a> also makes use of lazy evaluation.

<h3>In Summary</h3>
I think this is a really interesting paper and it was the first one that caught my eye from briefly skimming through the 10 that Michael Feathers listed. 

I found it quite difficult explaining some of the patterns so if anything doesn't make sense or you can think of a better way describing a pattern then please let me know.

Book club wise it was good to get to discuss what I'd read as others always come up with ideas that you hadn't thought of and we had some interesting discussions.

Next time we are reading '<a href="http://www.mockobjects.com/book/readability.html">The Readability of Tests</a>' from Steve Freeman and Nat Pryce's upcoming book '<a href="http://www.mockobjects.com/book/index.html">Growing Object Oriented Software, guided by tests</a>'.
