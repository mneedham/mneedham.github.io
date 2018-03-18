+++
draft = false
date="2009-10-14 23:21:39"
title="Book Club: Working Effectively With Legacy Code - Chapters 1 & 2 (Michael Feathers)"
tag=['book-club']
category=['Book Club']
+++

We've decided to go back to reading a book in our technical book club after a few months of discussing different papers and the chosen book is Michael Feathers' '<a href="http://www.amazon.co.uk/Working-Effectively-Legacy-Robert-Martin/dp/0131177052/ref=sr_1_1?ie=UTF8&s=books&qid=1255440556&sr=8-1">Working Effectively With Legacy Code</a>'.

We started off by reading the first two chapters titled 'Changing Software' and 'Working with Feedback' and these are some of my thoughts and our discussion of the chapters:

<ul>
<li>Early on Feathers talks about the need to change software in order to add features and fix bugs and while it is certainly necessary to make some changes to code in order to do this we discussed <strong>whether there is ever a time that we might look to keep the number of changes we're making to a minimum</strong>.

<a href="http://watchitlater.com/blog/">Tom</a> suggested that if we have good enough tests then we shouldn't be fearful of making changes at any time. I think we'd look to be more careful about making changes around the time of a release because we don't have a lot of time to recover if we make a mistake. Perhaps that only suggests that we don't have good enough tests though!</li>
<li>Something which I've noticed recently is that we often end up with <strong>transitionary refactorings</strong> in our code base which are attempts at refactorings which haven't quite been completed yet. I think this is somewhat inevitable if we are making <a href="http://programmer.97things.oreilly.com/wiki/index.php/The_Boy_Scout_Rule">incremental changes to improve the quality of the code base</a>. 

The problem with this is that it is sometimes it is not obvious where that refactoring is going and if someone other than the original authors has to work with the code then they can easily drive it in a different direction.

While we were discussing this it reminded me of an idea we read in '<a href="http://www.markhneedham.com/blog/2009/07/15/book-club-an-agile-approach-to-a-legacy-system-chris-stevenson-and-andy-pols/">An agile approach to a legacy system</a>'. The authors suggest that whenever there is a big refactoring to make the whole team only works on that until it is completed. It would be interesting to see how well this approach would work with a bigger team.</li>
<li>I really like the definition of unit tests that Feathers uses - <strong>tests that give us 'localised feedback and 'run fast</strong>'. I wrote a post last year <a href="http://www.markhneedham.com/blog/2008/12/04/what-make-a-good-unit-test/">where I tried to break this down further</a> but I think Feathers' guideline is useful to keep in mind when writing these tests. 

It's easy to end up relying on functional tests which undoubtably have their place but don't provide the rapid feedback that we need to work effectively.</li>
<li>We also discussed <strong>the need to think twice before creating a technical debt card or adding a 'TODO' comment</strong> to a piece of code. More often than not these just end up being ignored so it makes sense to check whether you can make the change when you see the problem where possible. 

Evan Bottcher wrote <a href="http://www.markhneedham.com/blog/2009/08/30/coding-the-guilty-bystander/#comment-21880">a cool comment in a previous post I wrote where he describes his experience with TODO comments</a>:

<blockquote>I find TODO comments a symptom of this – a colleague of mine once said that he was annoyed by TODOs, that they're a statement of 'I can't be bothered doing this, I want YOU TODO this".</blockquote>
It's certainly not always possible to fix things immediately but my current thinking is it probably makes sense to note that down somewhere that's not in the code and get back to it as soon as possible. Having said that I was reading <a href="http://programmer.97things.oreilly.com/wiki/index.php/First_Write%2C_Second_Copy%2C_Third_Refactor">Mario Fusco's entry</a> in '<a href="http://programmer.97things.oreilly.com/wiki/index.php/Edited_Contributions">97 things every programmer should know</a>' earlier and he recommends putting 'TODO' comments into the code base to identify areas of code to come back to later. Perhaps it just depends on the team.</li>
<li>I think the following observation is quite astute:

<blockquote>Breaking down a big class into pieces can be pretty involved work unless you do it a couple of times a week. When you do, it becomes routine. You get better at figuring out what can break and what can't, and it is much easier to do.</blockquote>
In addition if we don't do this type of refactoring then those classes increase in size and it becomes even more difficult to do in future.

Tom also pointed out that the more we practice the better we become at identifying good and bad code which allows us to better focus our attention on where we need to make improvements.
</li>
</ul>



