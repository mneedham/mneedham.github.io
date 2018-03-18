+++
draft = false
date="2009-01-10 14:04:57"
title="Finding the value in fixing technical debt"
tag=['software-development']
category=['Software Development']
+++

<a href="http://www.martinfowler.com/bliki/TechnicalDebt.html">Technical debt</a> is a term coined by Martin Fowler which we tend to use on our projects to describe a number of different situations on projects as <a href="http://iancartwright.com/blog/2009/01/five-kinds-of-technical-debt.html">Ian Cartwright points out</a> in his post on the subject.

Ian covers it in more detail, but to summarise my understanding of what technical debt actually is:

<blockquote>
Technical debt is where we know that something we choose not to take care of now is going to affect us in the future.
</blockquote>

The latter part of the sentence is interesting because it is somewhat subjective. There are clearly different levels of what 'affect us' means. 

<h3>Phantom Debt</h3>

The most interesting area of this is around the area of what Ian describes as Phantom debt.

<blockquote>
This is 'technical debt' as invoked by a developer who has decided they don't like part of the code base and hence want to rewrite it. Technical Debt certainly sounds better than 'egotistical refactoring session' ;-)
</blockquote>

Since reading Uncle Bob's <a href="http://www.markhneedham.com/blog/2008/09/15/clean-code-book-review/">Clean Code</a> I've become a bit fanatical in my approach to trying to make code as readable as possible, mainly by extracting code into methods which describe what is going on.

Whenever I come across code that doesn't make sense to me I try to <a href="http://www.industriallogic.com/xp/refactoring/composeMethod.html">break it into methods</a> which make it easier for me to understand and hopefully easier for the next person to read to.

I don't think that's technical debt in the typical sense because it is difficult to put a value on how that is going to hurt us in the future - I am only trying to make my life easier the next time I come across this piece of code. The problem is that it is <a href="http://www.markhneedham.com/blog/2008/12/02/what-are-your-personal-practices/">my opinion</a> that structuring code in this way is preferable. I have certainly worked with people who consider it overkill.

The benefits of handling this type of 'debt' are not as great as taking care of a concurrency issue which could cause the application to work in a non deterministic way when handling a high number of users for example. On the other hand the amount of time to fix it is much less.

Clearly if I went through the whole code base and applied this refactoring everywhere that would not be adding value so my approach tends to be that I'll only refactor if I'm working with that particular piece of code and its current state is hindering my ability to do so.

This is fairly similar to the advice I have been given around the best approach to getting tests around legacy code - only put tests around that code when you have to work with that particular piece of code otherwise you'll be there all day.

<h3>Looking at the value we're adding</h3>

There is a bit of balance between making the code perfect and adding value to the customer.

One of the ideas of lean is that we should always look at the value that we are adding to the customer and in removing some kinds of technical debt I suppose we are not actually adding tangible value. I don't think it's completely wasted time though because we are (hopefully) helping to reduce the time wasted trying to read difficult to understand code, making debugging easier etc.

It's definitely a tricky balance to find though.
