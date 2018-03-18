+++
draft = false
date="2010-05-06 23:36:26"
title="F#: My current coding approach"
tag=['f']
category=['F#']
+++

I spent a bit of time over the weekend coding <a href="http://code.google.com/p/yetanotherbuilder/">a simple generic builder for test objects</a> in F# and I noticed that although there were similarity with the ways I drive code in C# or Java my approach didn't seem to be exactly the same.

I've previously written about the importance of <a href="http://www.markhneedham.com/blog/2009/07/20/coding-quick-feedback/">getting quick feedback</a> when programming and how I believe that this can often be achieved faster by using the REPL rather than unit testing.

<h3>Still driving from the outside in</h3>

This time I decided to apply some of my recent learnings on <a href="http://www.markhneedham.com/blog/2010/04/18/coding-another-outside-in-example/">the value of</a> <a href="http://www.markhneedham.com/blog/2010/03/02/riskiest-thing-first-vs-outside-in-development/">driving from the outside in</a> so I started by writing an acceptance test which described the fluent interface of the code at a high level.

I want to use the builder from C# code so I was driving the code from C# tests:

~~~csharp

[Test]
public void ShouldCreateAFoo()
{
	var foo = Build.A<Foo>().Build();

	Assert.That(foo.Bar, Is.EqualTo("Bar"));
}
~~~

I wrote enough code to make that test compile at which stage the test was failing with a null reference exception because I hadn't instantiated 'Foo' yet.

At this stage if I was coding in C# I would probably work out what object I needed to create to do that and then I would write a test directly against that object and then write the code to make that pass.

In this case I didn't do that but instead I had a rough idea of the functions that I needed to glue together to get that test to pass. I just wrote those functions and combined them together without writing any tests against those individual functions. 

I extended my initial test to cover all the different types that are being used by the objects in our code base and then I added the code to make the new type pass.

<h3>Approach to learning an API</h3>

Since it's reflection code and I don't know those APIs that well I spent a bit of time tinkering in the REPL until I knew which methods I needed to call.

If I was writing C# then I'd have probably spent less time trying out different methods and more time reading through the list of available methods before choosing the one that I wanted.

I wrote quite messy code initially until I had the first test passing and then I went back and tidied it up so that it was a bit more readable.

At this stage <a href="http://code.google.com/p/yetanotherbuilder/source/browse/yab/TypeHelper.fs">common functions</a> started to reveal themselves and it made sense to have some unit tests directly against those as documentation if nothing else. The tests were all immediately green so those bits of code weren't test driven at that level.

<h3>Do we need really granular tests in F#?</h3>

My overall feeling at the moment is that while it's useful to have tests around code written in F#, we don't need to go as granular with our tests as we might do in C#.

Due to the conciseness of the language it's often so obvious that the code written is correct that I don't think tests at the functional level would add that much value. Equally I'm not necessarily convinced that the design would be any different if the individual functions were test driven.

I found the high level test gave me enough protection for any changes that I wanted to make and it did protect me a couple of times when I made breaking changes.

Having said all that, I'm still only writing toy code so it would be interesting to see if my approach would be any different if I was working on an F# application with a team of other developers.
