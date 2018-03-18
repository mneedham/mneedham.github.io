+++
draft = false
date="2009-07-21 23:10:20"
title="Good Lazy and Bad Lazy"
tag=['software-development']
category=['Software Development']
+++

One of the things I remember picking up from reading <a href="http://www.pragprog.com/the-pragmatic-programmer">The Pragmatic Programmer</a> is that developers need to be lazy in order to find better ways to solve problems and I came across a post by Philipp Lensson from a few years ago where he also suggests <a href="http://blogoscoped.com/archive/2005-08-24-n14.html">good developers are lazy and dumb</a>.

Something which I've come to realise more recently is that it's not necessarily true that being lazy as a developer is always a good thing - it depends in what way you are being lazy because there are certainly good and bad ways in which you can express your laziness!

I think bad laziness is often linked to the <strong>path of least resistance</strong> and is where we just take the easiest route to solving our problem without necessarily considering whether that solution fits in with the way the code is being written or the problems that we might have later as a result of our approach.

I've noticed (by doing most of them!) that there are some fairly common ways that we can fall into this trap:

<ul>
<li>Adding setters to a class when we have some extra data that we want to put inside that class instead of taking the time to either change the constructor to take in the new data or considering if we now need to create a new class to better represent the system. The problem here is that we end up with objects that may be half initialised which makes them <a href="http://www.markhneedham.com/blog/2009/05/23/coding-setters-reduce-trust/">really difficult to work with later on</a>.</li>
<li>Wanting to change some code which has problems with it and instead of following the <a href="http://www.informit.com/articles/article.aspx?p=1235624&seqNum=6">boy scout rule</a> and leaving it in a better state than we found it in we hack in our fix and then get out of there as quickly as possible. A colleague of mine likens this to fixing a broken window with duct tape instead of properly fixing the underlying problem. </li>
<li><a href="http://iancartwright.com/blog/2009/04/test-code-is-just-code.html">Copying and pasting test code</a> instead of writing each one individually and noticing any duplication from this process and then taking steps to remove this. I'm still unsure what the best way is to write tests which are <a href="http://www.markhneedham.com/blog/2009/04/13/tdd-balancing-dryness-and-readability/">both readable and remove duplication</a> but copying and pasting entire tests is certainly not the way to go.</li>
<li>Writing tests which make use of expectations and then not calling the 'Verify' method to ensure that those expectations are called - the test is now not even testing what it's supposed to be testing</li>
</ul>

I'm sure there are more but these are just some of the ones that come to mind.

In most of these cases the laziness actually comes from not really spending a lot of time thinking about what we are actually trying to do - we just picked the simplest approach that came to mind.

On the other hand if we take the time to think when we have problems to solve we can still come up with ways to be lazy but do so in a positive way.

I think the key to good lazy is that we get <strong>longer term benefits from this laziness</strong> as compared to bad lazy where we might get some immediate benefits but will probably suffer later on as a result of that.

<ul>
<li>Automating the startup of a service that our build depends on because we don't want to have to remember to keep turning it on by ourself manually.</li>
<li>Extracting common code out into methods so that we don't have to keep duplicating the same code. This approach is also useful for helping to reduce the complexity we need to deal with in each method which allows us pay less attention when browsing the code.</li>
<li>Extracting small classes when we see a class getting too big so that we can test the logic more easily without having to write dozens of lines of code just to get the class into a state where assertions can be made against it. </li>
<li>Writing automated tests to get <a href="http://www.markhneedham.com/blog/2009/07/20/coding-quick-feedback/">quick feedback</a> so that we don't have to launch the application and then click through all the screens to get to the place that we want to test.</li>
</ul>

Again I'm sure there are more of these and I'm still striving to make sure that when I'm lazy it's in the second category rather than the first.
