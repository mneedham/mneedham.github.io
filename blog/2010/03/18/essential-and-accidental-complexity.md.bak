+++
draft = false
date="2010-03-18 23:21:55"
title="Essential and accidental complexity"
tag=['software-development']
category=['Software Development']
+++

I've been reading Neal Ford's <a href="http://www.ibm.com/developerworks/views/java/libraryview.jsp?search_by=evolutionary+architecture+emergent+design:">series of articles on Evolutionary architecture and emergent design</a> and in the one about '<a href="http://www.ibm.com/developerworks/java/library/j-eaed1/index.html">Investigating architecture and design</a>' he discusses Essential and accidental complexity which I've previously read about in Neal's book, '<a href="http://www.markhneedham.com/blog/2008/09/05/the-productive-programmer-book-review/">The Productive Programmer</a>'.

Neal defines these terms like so:

<blockquote>
<strong>Essential complexity</strong> is the core of the problem we have to solve, and it consists of the parts of the software that are legitimately difficult problems. Most software problems contain some complexity.
</blockquote> 

<blockquote>
<strong>Accidental complexity</strong> is all the stuff that doesn’t necessarily relate directly to the solution, but that we have to deal with anyway.
</blockquote>

I find it interesting to consider where the line is for when something becomes essential complexity and when it's accidental complexity although Neal suggests that there's a spectrum between these two definitions upon which a piece of complexity sit.

I recently read 37 signals book '<a href="http://www.markhneedham.com/blog/2010/03/08/getting-real-book-review/">Getting real</a>' and one of the things that really stood out for me was the idea of keeping an application simple and writing less software wherever possible.

I'm intrigued as to where this would fit in with respect to essential and accidental complexity because quite often we end up implementing features which aren't part of the application's core value but do add some value yet become way more complicated than anyone would have originally imagined. 

Quite often these won't be the first features played in a release because they're not considered top priority and therefore when they are played the amount of analysis done on their potential impact is often less and as we implement these features they end up pervading across the application and increasing its overall complexity.

Another thing that often happens is that we start developing these features, complicating the code base as we go, before the business eventually decides that it's not worth the time that it's taking.

By this time the complexity has spread across the code and it's quite difficult to get rid of it cleanly.

What typically seems to happen is that some of it will just end up staying around in the code base pretty much unused and confusing people who come across it and don't understand what it's being used for.

If we were coming from the angle of Domain Driven Design then we might say that any complexity in the core domain of our application is essential and we should expect that complexity to exist.

On the other hand perhaps we should be more strict about what complexity is actually essential and try and ensure that only complexity around the absolutely vital features is allowed and look to compromise on simpler solutions for features which play a more supporting role.

If we were to follow a definition along these lines then I think we would recognise that there is actually quite a lot of accidental complexity in our applications because although some complex features do contribute to the solution it probably causes more pain than the value that it adds.

The take away for me is that we should be aware that this type of accidental complexity can creep into our applications and make sure that the business knows the trade offs we are making by implementing these types of features.
