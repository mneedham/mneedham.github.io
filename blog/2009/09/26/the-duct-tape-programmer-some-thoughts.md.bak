+++
draft = false
date="2009-09-26 17:16:34"
title="The Duct Tape Programmer: Some thoughts"
tag=['software-development', 'duct-tape-programmer']
category=['Software Development']
+++

I just came across quite an insightful post by Jak Charlton titled '<a href="http://devlicio.us/blogs/casey/archive/2009/09/25/ship-it-or-ship-out.aspx">Ship it or Ship out</a>'  in which he talks about the importance of shipping the software we work on, referring to  Joel's recent post '<a href="http://www.joelonsoftware.com/items/2009/09/23.html">The Duct Tape Programmer</a>'.

<h3>Unit testing</h3>

When I first read Joel's post I didn't really like it because it seems to downplay the role of unit testing when coding, something which I believe is quite important from my experience of software development so far.

What didn't quite make sense to me is that Joel has released the <a href="http://stackoverflow.com/">StackOverflow</a> website and it seems to work reasonably well and from my brief use of it I haven't seen any glaring errors which might indicate a lack of quality.

Having read Jak's post and some of the comments on his post it seems to me that perhaps the situations in which I work and which Joel describes are just different to each other and that neither of our approaches is inherently good or bad. 

FriedBob sums this up quite nicely in the <a href="http://devlicio.us/blogs/casey/archive/2009/09/25/ship-it-or-ship-out.aspx#comments">comments section</a>:

<blockquote>
What it boils down to is that you can't make a blanket statement about an sort of programming practice and say this is the best way every time every situation.

You have to use the best tool and approach for the job, and every situation is different.

You have to find a balance between "duct tape programming", structured tool/framework based coding, code quality, shipping date and maintainability.  Find the right mix, and you won't really have to make any significant sacrifices in any of these areas.
</blockquote>

In the type of work I do we typically have a team with multiple developers working together on something and I think the approach to coding in this environment needs to be slightly different to what it might be if you were working alone for example.

When I'm working alone I often just hack things together because I'm generally learning new things and it's pretty much throwaway code that noone else will ever need to understand.

The problem with this approach comes about when you want to <a href="http://www.markhneedham.com/blog/2009/07/20/coding-quick-feedback/">make changes to the code</a> - if it's been written in a rushed/hacky fashion then it can be really difficult to remember why you did it that way and having unit tests can help in this case.

If the code never needs to be changed then the value of having these tests is reduced to giving us quick feedback on whether or not our code does what we expect it to.

In the projects I work on <strong>we need to change the code all the time and in this case tests are also quite useful for giving us the ability to do this</strong> while providing a degree of confidence that we haven't broken something else.

In fact typically it might be someone other than the original writer of the code who needs to make changes so the tests can also give them some idea of what the code is supposed to be doing. 

When working on code alone this type of knowledge would be in your head. When working on a team we need to find some way of expressing this so that our team mates don't need to talk to us every time they want to make a change to the code.

Since I work on code bases with many other people and we want to frequently change our code as we discover better ways of doing things or the business changes their requirements we need some sort of safety net to allow us to do that - unit tests are part of that safety net.

Perhaps Joel doesn't have any of those and that's why he doesn't need the safety net.

Uncle Bob has also <a href="http://blog.objectmentor.com/articles/2009/09/24/the-duct-tape-programmer">written a post where he addresses this</a> and points out that writing unit tests doesn't necessarily slow us down.

<h3>Business/Developer alignment</h3>

Jak's observation on how the business and developers are fundamentally not aligned is quite astute:

<blockquote>
And we know that better code will be easier to maintain - and developers HATE bug fixing duty, so we want to ensure we don't have to do much of it.

To a developer, the most important factor in any project is Quality, followed by Time (because we know our bosses will be mad if we miss our deadlines), but we are happy to slip Functionality because it matters little to us if a new feature isn't included in the release.
</blockquote>

I've actually observed that while that might be true for some developers, in general there seems to be an almost unspoken desire to get story points on the board instead of taking a bit more time to ensure that the code we write now won't hinder our ability to deliver functionality that we need to write, perhaps as soon as the next iteration.

I've written a <a href="http://www.markhneedham.com/blog/2009/09/16/coding-watch-out-for-mutable-code/">couple of</a> <a href="http://www.markhneedham.com/blog/2009/09/25/tdd-it-makes-you-question-what-youre-doing/">posts</a> recently where I describe the struggle a colleague and I have had working with code that was written in a rushed fashion.

Personally I find myself getting very demotivated when we end up just hacking code together to get it done as quickly as possible and I think Jak is spot on in identifying that the reason for this is that I know the code is going to be more difficult to maintain in the future when we take this approach.

I can certainly see the benefit in hacking some code in if we are near to a release and don't want to risk rewriting a whole chunk of code just to design it well but in normal development time I prefer to take the time to write something that will be reasonably easy to work with in the future.

I think there is some benefit to the business in knowing about this trade off since if we keep on compromising on the quality of what we're writing to get more features in it will eventually become very difficult to add these in a timely manner at which stage we will look quite stupid.

<h3>Overall</h3>
It's quite interesting to hear different opinions on ways to deliver software since everyone seems to do this slightly differently to each other.

Even though I don't think I'll be changing the way I approach software development these posts have certainly made me think more about my favoured approach and why we do the things we do.
