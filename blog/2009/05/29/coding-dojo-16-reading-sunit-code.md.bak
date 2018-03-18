+++
draft = false
date="2009-05-29 09:23:19"
title="Coding Dojo #16: Reading SUnit code"
tag=['coding-dojo', 'smalltalk', 'sunit']
category=['Coding Dojo']
+++

Continuing on from <a href="http://www.markhneedham.com/blog/2009/05/21/coding-dojo-15-smalltalk/">last week's look at Smalltalk</a>, in our latest coding dojo we spent some time investigating the <a href="http://sunit.sourceforge.net/">SUnit testing framework</a>, how we would use it to write some tests and looking at how it actually works.

<h3>The Format</h3>

We had 3 people for the dojo this week and the majority was spent looking at the code on a big screen and trying to understand between us what was going on. We only had the dojo for about 90 minutes this week. Normally we go for around 3 hours.

<h3>What We Learnt</h3>

<ul>
<li>An interesting thing which I noticed during this session was the idea of <a href="http://www.mactech.com/articles/frameworks/8_2/Protocol_Evins.html">protocols</a> which are used to organise a set of methods that a class' instance respond to. I think these are intended more for humans than for the computer which I think is a really cool idea - I am strongly of the belief that programming languages provide a mechanism for <a href="http://olabini.com/blog/2009/05/communication-over-implementation/">communicating our intent with ourselves and with the other people on our team</a>.</li>
<li>As a result of looking at the description of the 'initialize-release' protocol for Object I became intrigued about the way that objects are removed by the garbage collection. We weren't able to find out exactly how Visual Works does garbage collection but I learnt a little bit about <a href="http://www.exept.de:8080/doc/online/english/programming/GC.html">the way that garbage collection works</a> in general using three different approaches - mark and sweep, copying collector and reference count.</li>
<li>Another thing which I found interesting was the way that Smalltalk handles exceptions - we came across this when looking at how XUnit handles passing and failing test cases. Since Smalltalk only has messages and objects there is no explicit of an exception so as I understand it objects have the ability to respond to an error signal being sent to them.

(TestResult runCase:aTestCase)

~~~smalltalk

	| testCasePassed |
	testCasePassed := [[aTestCase runCase.
	true]
		sunitOn: self class failure
		do:
			[:signal | 
			self failures add: aTestCase.
			signal sunitExitWith: false]]
		sunitOn: self class error
		do:
			[:signal | 
			self errors add: aTestCase.
			signal sunitExitWith: false].
	testCasePassed ifTrue: [self passed add: aTestCase]
~~~

The above is the code block we spent a bit of time looking at which I think in C# world would look a bit like this:


~~~csharp

try 
{
	aTestCase.runCase()
}
catch(FailureException) 
{
	this.Failures.Add(aTestCase);
}
catch(ErrorException)
{
	this.Errors.Add(aTestCase);
}
this.Passed.Add(aTestCase);
~~~

It seems easier to understand to me having exceptions as a language construct but I haven't done much Smalltalk so maybe that's just a preference for what's familiar.</li>
<li>It took us a bit of Googling to work out how to start the SUnit TestRunner in VisualWorks but the way to do it eventually turned out to be quite simple. Typing the following code into the workspace window does it:


~~~smalltalk

TestRunner open
~~~
</li>
</ul>

<h3>For next time</h3>

<ul>
<li>If we continue in Smalltalk world for another week then we'll probably play around with <a href="http://sunit.sourceforge.net/">SUnit</a> a bit more and perhaps get onto <a href="http://www.seaside.st/">seaside</a>. If not then we'll be back to the Java modeling I imagine.</li>
</ul>
