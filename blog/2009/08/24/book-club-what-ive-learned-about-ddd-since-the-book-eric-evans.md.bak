+++
draft = false
date="2009-08-24 18:20:33"
title="Book Club: What I've learned about DDD since the book (Eric Evans)"
tag=['book-club']
category=['Book Club']
+++

This week book club became video club as we discussed Eric Evans' QCon London presentation '<a href="http://www.infoq.com/presentations/ddd-eric-evans">What I've learned about DDD since the book</a>'.

I was lucky enough to be able to <a href="http://www.markhneedham.com/blog/2009/03/13/qcon-london-2009-what-ive-learned-about-ddd-since-the-book-eric-evans/">attend this presentation live</a> and we previously ran a book club where I briefly summarised what I'd learnt but this gave everyone else an opportunity to see it first hand.

There are some of my thoughts and our discussion of the presentation:

<ul>
<li>We spent a lot of time discussing domain events - one of the new ideas which Evans had observed since publishing the book - and <a href="http://lizdouglass.wordpress.com/">Liz</a> pointed out that <strong>a domain event often exists where there is some sort of interaction between objects which doesn't seem to belong on either object</strong>.

The example Liz gave is where there is an accident between two cars and we realise that there should be a Collision object to describe what's happened.  <a href="http://intwoplacesatonce.com/">Dave</a> pointed out that <a href="http://book.git-scm.com/1_the_git_object_model.html">commits in Git</a> could be another example of a domain event. 

We discussed some domain events which we had noticed in code bases we had worked on. 

One system I worked on had the concept of transactions to describe interactions between different accounts. They were also used to <a href="http://www.markhneedham.com/blog/2008/08/27/handling-balances-in-systems/">calculate the balance</a> of an account at any time in preference to keeping the balance of each account updated in real time.

The balance on the account would still be updated at the end of each day such that we would only need to make use of transactions since the last update to calculate a balance.</li>
<li>What really stood out for me in our discussion is how a lot of the concepts that Eric Evans talks about are designed to make us <strong>explicitly state what we are doing in our code</strong>.

We have domain events for describing what happens in the domain, we try to define bounded contexts so we know what the object model means in specific areas of the code, we identify a core domain so we can spend our time on the most important code and so on.

Dave  described this as <strong>conscious coding</strong> in that it makes us think very carefully about what we're coding rather than just coding without real analysis and probably writing code which isn't as useful as it could be.</li>
<li>I'm still not sure that I really get what the <strong>core domain</strong> means but Dave described it as 'If we stripped out all the other code in our system except for the core domain we would still be able to build something around that' which actually has the side effect of pointing out that we need to ensure that this code is completely decoupled from any implementation details of the current way we are using it.

For example if we are currently writing a website and it is decided that we need to be able to display our content on a mobile phone, we should still be able to make use of the same core domain code to do that fairly easily.</li>
<li>The section of the talk about the <strong>big ball of mud and the green house</strong> was also very interesting and Raphael Speyer came up with the analogy of only letting code from outside the green house inside if it had been hosed down and all the mud removed so that we can ensure that out important code is of comparable quality.

If I understand correctly the core domain is the code that should reside in that metaphorical green house and we will spend a lot of time on its modeling so that it will be easy to change in the future.

By contrast the modeling of the code outside the green house is not as important - a lot of the time the code out there is 'just data' and we want to display that data to users with minimal effort in modeling it in our code since we don't get a great deal of value from doing so.</li>
</ul>
