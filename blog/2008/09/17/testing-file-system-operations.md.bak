+++
draft = false
date="2008-09-17 15:48:37"
title="Testing file system operations"
tag=['tdd', 'gateway', 'testing', 'file-system', 'design-patterns']
category=['Testing']
+++

On my previous project one of the areas that we needed to work out how to test was around interaction with the file system.

The decision that we needed to make was whether we should unit test this type of functionality or whether it could just be covered by a functional test.

<h3>To Unit Test</h3>

One of the patterns to use when unit testing things like this is the <a href="http://www.martinfowler.com/eaaCatalog/gateway.html">Gateway pattern</a>. To quote Martin Fowler's Patterns of Enterprise Application Architecture

<blockquote>
[A gateway is] An object that encapsulates access to an external system or resource.
</blockquote>

Therefore we would define an interface with the file operations that we intended to use in our code.


~~~csharp

public interface IFileGateway
{
	bool Exists(string path);
}
~~~

We can then mock/stub this out in a unit test and use an implementation of the gateway in the real application.


~~~csharp

public class FileGateway : IFileGateway
{
    public bool Exists(string path)
    {
        return File.Exists(path);
    }
}
~~~

In this case making the code more testable was remarkably easy. We can test the behaviour of the system without actually having any reliance on the file system which means we can potentially cut time from our test suite.

Additionally we are now shielded from the implementation of how we find out if a file exists. This provides flexibility if in the future files are stored on a cluster rather than a single machine, for example, and we need to have a different implementation of working out if a file exists.

The disadvantage is that we have added another level of abstraction to the system which potentially adds complexity.

<h3>To Functional Test/To Not Test</h3>

The alternative approach is just to test the operation in a functional test or not bother testing this functionality at all.

We could setup some dummy file locations for our test and then do various tests against these. 

This is probably marginally quicker than wrapping the calls to the file system behind an abstraction as suggested above. 

The problem is that this gain in speed is lost by the extra time it would take to run our build - we would now probably test more combinations since this bit of functionality is not covered at a lower level.

We are also now tied to the file system for executing this operation so if we need to change this in the future there may now be multiple places where changes need to be made.

The other option of course is to not bother testing this functionality. The logic behind this approach is that we know that File.Exists works because it is part of the .NET framework, why bother testing it?

While this is true, it is the interaction with our system that we are interested in. We are not actually testing an API implementation - we want to know if a file exists or not. How this is worked out is irrelevant to us.

Clearly we get a gain in speed of development if we don't test things like this - and we can probably make a reasonable attempt at explaining why it's not necessary. As with most things in software the trade off comes later on when we end up with the same problems we would have in just functional testing.

<h3>In Conclusion</h3>

I am not a fan of over engineering things for the sake of it and maybe the Gateway pattern approach to making this unit testable would be seen as that.

I don't believe this is the case. The gains we get from having clearly defined boundaries of where we interact with external resources is invaluable and helps make our code more flexible, maintainable and open to change.
