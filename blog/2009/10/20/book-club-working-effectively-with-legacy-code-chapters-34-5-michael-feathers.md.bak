+++
draft = false
date="2009-10-20 07:01:37"
title="Book Club: Working Effectively With Legacy Code - Chapters 3,4 & 5 (Michael Feathers)"
tag=['book-club']
category=['Book Club']
+++

In our latest technical book club we discussed chapters 3,4 and 5 of Michael Feathers' '<a href="http://www.amazon.co.uk/Working-Effectively-Legacy-Robert-Martin/dp/0131177052/ref=sr_1_1?ie=UTF8&s=books&qid=1255440556&sr=8-1">Working Effectively With Legacy Code</a>' - 'Sensing and Separation', 'The Seam Model' and 'Tools'.

These are some of my thoughts from our discussion of these chapters:

<ul>
<li>Feathers suggests two reasons why we break dependencies when trying to get tests in place - <strong>sensing and separation</strong>. The former involves the breaking of dependencies in order to get access to the values computed in our code and the latter is necessary so that we can get our code into a test harness to start with.

In my time coding professionally I have experienced difficulties with the former than the latter. I have certainly written code which is bordering impossible to test but it seems like maybe writing code which is difficult to sense against is less problematic than code which we struggle to get into a test harness.</li>
<li>I really like the idea of <a href="http://www.markhneedham.com/blog/2009/06/21/seams-some-thoughts/">seams</a> and <a href="http://www.markhneedham.com/blog/2009/08/19/impersonators-finding-the-enabling-point/">enabling points</a> to describe how we can alter the way that our code works by making changes in other places. 

Most of the enabling points in the code I've worked on are object seams but Halvard and I did make use of a link seam when we wanted to override the behaviour of a specific class in a 3rd party library. We were able to do this by including our own class with the same class signature earlier in the application's class path.

Ahrum described a time when he had to do something similar to get rid of some noisy warning messages which one of the dependencies was emitting. He was able to verify that nothing important was going on in that particular class before overriding the behaviour with the same trick.</li>
<li><a href="http://intwoplacesatonce.com/">Dave</a> pointed out that it's useful to remember that <strong>a test is also a client of an object</strong> in particular reference to Feathers pointing out that software doesn't seem to be designed to be easily testable. From what I've seen the best way to make code easily testable is to design in that testability when we're writing it. It's <a href="http://www.markhneedham.com/blog/2008/11/28/tdd-suffering-from-testing-last/">much more difficult and time consuming to try and do that later on</a>.</li>
<li>We had some discussion around big tests in terms of the <strong>size of test fixtures and individual tests</strong>. The consensus seemed to be that when we have an important class where we care a lot about the edge cases then we'll probably write a large number of tests. On the other hand if our individual test methods are big - which usually means there's lots of setup required - then it might indicate that a method or class is doing too much. </li>
<li>The problems in code that these two chapters come generally happen because we are doing too much in single classes instead of separating the responsibilities. Ahrum pointed out that if we had lots of small classes we would have to solve the problem about how to organise these classes effectively instead.

On the projects I've worked on we tend to end up with packages which contain a huge number of classes but I haven't noticed it as being particularly painful so far. Ahrum suggested an alternative approach to grouping objects by the layer they reside in would be to group them by feature instead. I haven't done this before but it'd be interesting to see if it would make it easier to manage our code.</li>
</ul>
