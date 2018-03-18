+++
draft = false
date="2009-04-16 18:20:50"
title="Coding Dojo #12: F#"
tag=['coding-dojo', 'f']
category=['Coding Dojo', 'F#']
+++

In our latest coding dojo we worked on trying to port some of the functionality of some <a href="http://bitbucket.org/codingdojosydney/to_fsharp/src/tip/Chaos/">C# 1.0 brain models</a>, and in particular one around simulating <a href="http://en.wikipedia.org/wiki/Logistic_map">chaos behaviour</a>, that <a href="http://www.twitter.com/davcamer">Dave</a> worked on at university.

<h3>The Format</h3>

This was more of an experimental dojo since everyone was fairly new to F# so we didn't rotate the pair at the keyboard as frequently as possible. 

<h3>What We Learnt</h3>

<ul>
<li>The aim of the session was to try and put some unit tests around the C# code and then try and replace that code with an F# version of it piece by piece. We created an F# project in the same solution as the C# one and then managed to hook up the C# and F# projects, referencing the C# one from the F# one, with some success although the references did seem to get slightly confused at times. The support from the IDE isn't really there yet so it can be a bit tricky at times.</li>
<li>We were using the <a href="http://codebetter.com/blogs/matthew.podwysocki/archive/2008/04/25/xunit-net-goes-1-0-and-unit-testing-f.aspx">XUnit.NET framework</a> to unit test our code - this seems like a useful framework for testing F# code since it doesn't require so much setup to get a simple test working. We can just annotate a function with the 'Fact' annotation and we're good to go. One thing to be careful about is to make sure that you are actually creating functions to be evaluated by the test runner and not having the tests evaluated immediately and therefore not being picked up by the runner. For a while I had written a test similar to this and it wasn't being picked up:


~~~text

[<Fact>] let should_do_something = Assert.AreEqual(2,2)
~~~

The type of 'should_do_something" is 'unit' and as I understand it gets evaluated immediately. What we really want to do though is create a function (with type 'unit -> unit') which can be evaluated later on:


~~~text

[<Fact>] let should_do_something() = Assert.AreEqual(2,2)
~~~

The brackets are important, something that I hadn't appreciated. We were generally running the test by directly calling the test runner from the command line - we couldn't quite work out how to hook everything up inside Visual Studio.</li>
<li>I'm not sure if we went exactly to <a href="http://www.amazon.co.uk/Working-Effectively-Legacy-Robert-Martin/dp/0131177052/ref=sr_1_1?ie=UTF8&s=books&qid=1239830214&sr=8-1">the book</a> with our refactoring of the code to make it testable - the method on the class doing the work was private so we made it public - but it helped to get us moving. We were able to then replace this with an F# function while verifying that the output was still the same. As I mentioned on <a href="http://www.markhneedham.com/blog/2009/04/13/f-a-day-of-writing-a-little-twitter-application/">my post about the little twitter application I'm working on</a>, I'm intrigued as to how we should structure code in F#. Apparently <a href="http://forum.codecall.net/programming-news/10523-object-oriented-f-creating-classes.html">the answer is as objects</a> but I'm interested how the design would differ from one done in a predominantly OO as opposed to functional language.</li>
</ul>

<h3>For next time</h3>

<ul>
<li>I'm really enjoying playing around with F# - it's definitely interesting learning a different approach to programming than I'm used to - so we might continue working on that next time around. If not then we need to find another game to model! </li>
</ul>
