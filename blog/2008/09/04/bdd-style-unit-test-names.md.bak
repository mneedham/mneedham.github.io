+++
draft = false
date="2008-09-04 00:05:18"
title="BDD style unit test names"
tag=['tdd', 'bdd', 'unit-tests', 'test-driven-development']
category=['Testing']
+++

A <a href="http://www.fuzzylizard.com/archives/2008/09/03/977/">couple</a> <a href="http://sarahtaraporewalla.blogspot.com/2008/08/test-names-go-wild.html">of</a> my colleagues have been posting about how to name your unit tests based on this <a href="http://blog.jayfields.com/2008/05/testing-value-of-test-names.html">original post</a> by Jay Fields.

I think that test names are useful, especially when written in a <a href="http://dannorth.net/introducing-bdd">BDD</a> style expressing what a test is supposed to be doing.  

For example, in a C# NUnit test we might see the following as a test name:


~~~csharp

[Test]
public void ShouldDoSomething()
{
	// Code testing that we're doing something
}
~~~

I write all my tests like this and I'm often asked what the point of the 'Should' is, why not just name it 'DoSomething'. 

For me although it's a subtle change it influences the way that people look at the test. They can look at the test in a much more critical way. 

In the above example someone can look at the test name 'ShouldDoSomething' and then think 'Actually no, it should be doing something else.' The test name and the test contents can then be changed to fit this new understanding of the test. 

I'm with <a href="http://www.fuzzylizard.com/archives/2008/09/03/977/">Chris Johnston</a> who says the following when it comes to naming tests:

<blockquote>
One habit that I picked up on my last project was naming a test after I had written it. While creating the unit test, I would simply name it foo(). Then, once I saw what the code was actually doing, I would go back and rename the test to something appropriate.
</blockquote>

Ideally I want to name the test properly before I write it but sometimes it becomes clear to me exactly what the name should be as I'm writing the test. 

If I'm in this situation I usually just name the test 'ShouldDoSomething' and then by the time I've written it I know what it should actually be doing and I can go back and rename it.

In terms of the general argument over whether we should even have test names, I have only really coded tests in Java and C# so I'm not in a position to comment on whether using a language like Ruby means that they aren't necessary.

For me the test name provides the intention of what you are trying to do, and I like to skim the list of tests in a class - by using Ctrl - F12 and then typing in 'Should' to filter the method list in <a href="http://www.jetbrains.com/resharper/documentation/ReSharper25DefaultKeymap.pdf">Resharper</a> - so that I can see at a high level what is supposed to be happening in that test fixture.

In the world of <a href="http://www.jetbrains.com/idea/">IntelliJ</a> there is also a nice plugin called <a href="http://testdox.codehaus.org/">TestDox</a> which allows you to get a list of your tests nicely indented with spaces.

