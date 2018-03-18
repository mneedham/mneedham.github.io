+++
draft = false
date="2009-10-23 00:08:10"
title="Coding: The primitive obsession"
tag=['coding']
category=['Coding']
+++

I recently came across an interesting post by Naresh Jain where he details a discussion at the <a href="http://sdtconf.com/">SDTConf 2009</a> about the <a href="http://blogs.agilefaqs.com/2009/10/19/biggest-stinkers/">code smells that hurt people the most</a>. 

Naresh describes the 'primitive obsession' anti pattern as being the crux of poor design:

<blockquote>
I would argue that I’ve seen code which does not have much duplication but its very difficult to understand what’s going on. Hence I claim, “only if the code had better abstractions it would be a lot easier to understand and evolve the code”. Also when you try to eliminate duplicate code, at one level, there is no literal code duplication, but there is conceptual duplication and creating a high order abstraction is an effective way to solve the problem. Hence I conclude that looking back, <strong>Primitive Obsession is at the crux of poor design. a.k.a Biggest Stinker</strong>.
</blockquote>

When I first read this post I thought Naresh was only talking about primitives such as strings, integers, decimals and so on but after discussing this pattern at today's <a href="http://www.markhneedham.com/blog/category/book-club/">book club</a> <a href="http://watchitlater.com/blog/">Tom</a> pointed out that the problem might also be defined as '<strong>describing high level domain concepts with low level types</strong>'.

I've noticed that this pattern in code often seems to happen when we have abstractions in our code which are very generic and don't express the domain very clearly.

I think the reason people code in this way comes from a desire to minimise the amount of code being written - as I understand it the theory is that if we write less code then it will be more maintainable.

I really like the way <a href="http://intwoplacesatonce.com/">Dave Cameron</a> describes the disadvantages of doing this in <a href="http://blogs.agilefaqs.com/2009/10/19/biggest-stinkers/#comment-20408408">a comment on Naresh's post</a>:

<blockquote>
Naresh, I agree strongly with your assertion that we need *better* abstractions. Eliminating duplication by introduction a mediocre abstraction leads to pain. Removing duplication and parceling it up in an awkward way can make it more difficult to see a more elegant abstraction later. The short-term benefit of eliminating duplication leads to a long-term pain of awkward design.
</blockquote>

The other motivator behind this style of coding is to try and create classes which are really reusable. 

<a href="http://www.udidahan.com/2009/06/07/the-fallacy-of-reuse/">Udi Dahan explains why this often doesn't work</a> but the problem that I see from this attempt at writing reusable code is that it will get reused in places where the concept doesn't quite make sense. 

As a result of this we end up writing a lot of very hacky code to try and make it fit.

The most frequent offender seems to be the creation of collections of things which we then query to find specific items elsewhere in the code. More often that not we'll also perform some custom logic on that particular item. 

At its most extreme we might extract each of the items in a collection and make use of them separately. This somewhat defeats the purpose of the collection.

When this happens it often seems to me that what we actually have is a series of attributes of an object rather than a collection.

While discussing why this type of coding happens it was pointed out that it's much easier to make use of the primitives than to spend the time looking for a helpful abstraction - I think this is an example of <a href="http://www.markhneedham.com/blog/2009/07/21/good-lazy-and-bad-lazy/">bad laziness</a>. 

We might be spending less effort now writing the code but it will be more difficult for anyone else who reads it in future which is not a good trade off.

Another similar pattern I've seen quite frequently is where we <a href="http://www.markhneedham.com/blog/2009/07/24/wrapping-collections-inheritance-vs-composition/">extend one of the classes in the collection API with our 'domain concept</a>'. 

While this seems better than just passing around a collection the problem is that any clients of our class have access to any of the methods of the collections API we extend which provides more flexibility than we would like and can lead to our object being in an unexpected state if those methods get used.

<h3>In summary</h3>
I think the way to solve this problem comes down to spending more time thinking about our domain and the best way to model it and discussing this regularly with other people on the team.

That way I believe our knowledge of how the system actually works will be more explicit in the code which will make it easier for people to understand the code base.
