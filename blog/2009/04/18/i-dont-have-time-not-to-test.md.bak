+++
draft = false
date="2009-04-18 09:25:17"
title="I don't have time not to test!"
tag=['testing']
category=['Testing']
+++

I recently read a blog post by Joshua Lockwood where he spoke of some people who claim they <a href="http://www.lostechies.com/blogs/joshua_lockwood/archive/2009/04/13/quot-i-don-t-have-time-to-test-quot.aspx">don't have time to test</a>.

Learning the TDD approach to writing code has been one of best things that I've learnt over the last few years - before I worked at ThoughtWorks I didn't know how to do it and the only way I could verify whether something worked was to load up the application and manually check it.

It was severely painful and on one particular occasion I managed to put some code with a bug into production because I didn't know all the places that making that code change would impact.

It's not a good way of working and I'm glad I've been given the opportunity to work with people who have showed me a better way.

My experience pretty much matches a comment made by <a href="http://www.lostechies.com/members/chrismissal/default.aspx">Chris Missal</a> on the post where he pointed out that you are going to test your code anyway so you might as well automate that test!

<blockquote>
"You're already testing with the debugger, TestPage1.aspx, or whatever... Just save that code and automate it!"
</blockquote>

I've just spent the last 2 hours doing some <a href="http://www.markhneedham.com/blog/2009/04/18/f-refactoring-that-little-twitter-application-into-objects/">refactoring on an F# twitter application I'm working on</a> and because I didn't write any tests it's been a very painful experience indeed.

Every time I make a change I have to copy all the code into F# interactive, run the code and then manually make sure that I haven't broken anything.

I've been doing this in fairly small steps - make one change then run it - but <strong>the cycle time is still much greater than it would be if I had just put some tests around the code in the first place</strong>.

I think we should be looking to test more than just the 'complex code' as well - there have been numerous occasions when I've put the logic for a conditional statement the wrong way around and a test has come to the rescue.

It pretty much applies to all the languages that I've worked in and if we can't see how to easily create an automated test for a bit of code then <a href="http://www.markhneedham.com/blog/2008/11/30/tdd-if-its-hard-to-test-reflect-on-your-approach/">it's a sign that we're doing something wrong</a> and we might want to take a look at that!
