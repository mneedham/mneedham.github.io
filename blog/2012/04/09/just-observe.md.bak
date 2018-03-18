+++
draft = false
date="2012-04-09 22:45:07"
title="Just Observe"
tag=['software-development']
category=['Software Development']
+++

One of the most common instincts of a developer when starting on a new team is to look at the way the application has been designed and find ways that it can be done differently.

Most often 'differently' means that a pattern used in a previous project will be favoured and while I think it's good to make use of experience that we've gained, we do miss out on some learning if we write every application the same way.

Therefore, unless I see a decision being made which is clearly going to lead to disaster later on, I now prefer to observe the approach being taken and understand its advantages and disadvantages before making a judgement.

A few years Jay Fields wrote a post titled '<a href="http://blog.jayfields.com/2009/03/kill-your-darlings.html">Kill Your Darlings</a>' where he suggested the following:

<blockquote>
You always gain by allowing someone to show you an alternative solution. If someone wants to solve a problem in a different way, there are several gains to be had. If their way is inferior, you have an opportunity to mentor a team-mate. 

If their way is equally elegant, you've gained another solution, or point of view that may be superior in the future. If their way is superior you learn something new and the codebase improves. 

In exchange for these gains you only need to give up time. Time is valuable, but it's also well spent on improving the ability of a team-mate or your personal ability.
</blockquote>

He was talking in a slightly different context but it seems equally applicable here.

One example from the current project I'm working on is that we're not using an ORM tool but instead mapping from database queries to domain objects manually.

This is being done partly to get around the query optimisation problems we can end up with when using tools like Hibernate but it also means that we design our domain code properly and don't get tempted to make it match the database structure.

I initially thought that it was a strange decision to write code to do mapping when you have a tool to do it for you but it hasn't been as bad as I'd imagined although the data access code is pretty messy.

On the positive side we can directly measure the performance of each query, make the necessary tweaks, and then re-measure the performance much more easily this way.

The application is read only so we wouldn't have got to use the full 'CRUD' repertoire that Hibernate provides anyway.

It might not be the right choice for the next application that I work on but I'm glad I got the chance to see what an application written without an ORM looks like.

Just observe!
