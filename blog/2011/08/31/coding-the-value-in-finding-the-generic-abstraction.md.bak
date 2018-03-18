+++
draft = false
date="2011-08-31 06:49:48"
title="Coding: The value in finding the generic abstraction"
tag=['coding']
category=['Coding']
+++

I recently worked on adding the meta data section for each of the different document types that it serves which involved showing 15-20 pieces of data for each document type.

There are around 4-5 document types and although the meta data for each document type is similar it's not exactly the same!

When we got to the second document type it wasn't obvious where the abstraction was so we went for the copy/paste approach to see if it would be any easier to see the commonality if we put the two templates side by side.

We saw some duplication in the way that we were building up each individual piece of meta data but couldn't see any higher abstraction.

We eventually got through all the document types and hadn't really found a clean solution to the problem.

I wanted to spend some time playing around the code to see if I could find one but <a href="http://duncan-cragg.org/blog/">Duncan</a> pointed out that it was important to consider that refactoring in the bigger context of the application.

Even if we did find a really nice design it's probably not going to give us any benefit since we've covered most of the document types and there will maybe be just one that we have to add the meta data section for.

The return on investment for finding a clean generic abstraction won't be very high in this case.

In another part of our application we need to make it possible for the use to do <a href="http://en.wikipedia.org/wiki/Faceted_search">faceted search</a> but it hasn't been decided what the final list of facets to search on will be.

It therefore needs to be very easy to make it possible to search on a new facet and include details about that facet in all search results.

We spent a couple of days about 5/6 weeks ago working out how to model that bit of code so that it would be really easy to add a new facet since we knew that there would be more coming in future.

When that time eventually came last week it took just 2 or 3 lines of code to get the new facet up and running.

In this case spending the time to find the generic abstraction had a good return on investment.

I sometimes find it difficult to know exactly which bits of code we should invest a lot of time in because there are always loads of places where improvements can be made.

Analysing <strong>whether there's going to be a future return on investment</strong> from cleaning it up/finding the abstraction seems to be a useful thing to do.

Of course the return on investment I'm talking about here relates to the speed at which we can add future functionality.

I guess another return on investment could be reducing the time it takes to understand a piece of code if it's likely to be read frequently.
