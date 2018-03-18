+++
draft = false
date="2009-01-22 23:02:15"
title="Coding Dojo #7: Retlang/Hamcrest .NET attempt"
tag=['coding-dojo']
category=['Coding Dojo']
+++

We ran a sort of coding dojo/playing around session which started with us looking at the .NET concurrency library, <a href="http://code.google.com/p/retlang/">Retlang</a>, and ended with an attempt to write <a href="http://code.google.com/p/hamcrest/">Hamcrest</a> style assertions in C#. 

<h3>The Format</h3>
We had the same setup as for our normal coding dojos with two people at the keyboard although we didn't rotate as aggressively as normal. 

<h3>What We Learnt</h3>

<ul>
<li>We started off having a look at a concurrency problem in <a href="http://confluence.public.thoughtworks.org/display/CCNET/Welcome+to+CruiseControl.NET">Cruise Control .NET</a> which <a href="">Dave Cameron</a> recently fixed. The intention was to try and take one of the cases of multi threading and replace it with a message based approach using the Retlang library.  </li>
<li>As I understand it, you can have <strong>any number of subscribers</strong> subscribe to any channel using Retlang which is different to the Erlang approach whereby only one subscriber would be allowed. A bit of experimentation also suggests that subscribers need to be subscribed to a channel at the time a message is published in order to receive it. </li>
<li>
We started off with an initial test case but got sidetracked in trying to work out how to make the assertion syntax a bit nicer. The original assertion read like the examples on the website in that we check the state of a ManualResetEvent so that we know whether or not a message was received by a subscriber.

The assertion read like this:


~~~csharp

var gotMessage = new ManualResetEvent(false);
...
Assert.IsTrue(gotMessage.WaitOne(2000, false));
~~~

We initially worked this to read like so:


~~~csharp

AssertThat(gotMessage, HasTrippedWithin(2.Seconds());
~~~

AssertThat and HasTrippedWithin were local methods and Seconds was an extension method. It's pretty nice but the problem is that we can't reuse this code easily in other test classes and keep the readability.

C# doesn't have Java's ability to import static methods so we would need to reference the class which the AssertThat method and HasTrippedWithin methods reside on directly either by having every test case extend it or by explicitly referencing it when we use the methods.</li>
<li>A bit more playing around with extension methods and trying to work out a good way to write Matchers led us to the following syntax:


~~~csharp

gotMessage.Should(Be.TrippedWithin(2.Seconds());
~~~

We also considered putting a Verify extension method on object so that a test case could have a series of different matchers to be evaluated.


~~~csharp

this.Verify(
	gotMessage.Is().TrippedWithin(2.Seconds())
);
~~~

For some reason we need to use the 'this' keyword in order to access an extension method defined on object - I don't really understand why as I thought classes implicitly extended object, meaning the following should be possible:


~~~csharp

Verify(gotMessage.Is().TrippedWithin(2.Seconds()));
~~~

</li>
<li>I think the way that our tests fail and the way that they report this failure is vital for getting the most out of TDD so I'd be interested to know of any ideas people have with regards to this. The thing that makes Hamcrest so good is not just the fluent syntax but the error messages that you receive when tests fail - it's very clear where the problem lies when a test fails, there is rarely a need to get out the debugger in complete confusion as to why the test failed.</li>

</ul>



<h3>Next Time</h3>

<ul>
<li>I think we may make a return to coding some OO problems again next week - I'm not convinced that we are getting the most out of the Dojo sessions learning something which is new to the majority of people taking part.
</ul>
