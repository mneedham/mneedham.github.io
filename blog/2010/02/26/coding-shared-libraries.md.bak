+++
draft = false
date="2010-02-26 00:36:50"
title="Coding: Shared libraries"
tag=['coding']
category=['Coding']
+++

On a few projects that I've worked on one of the things that we've done is create a shared library of objects which can be used across several different projects and while at the time it seemed like a good idea, in hindsight I'm not sure if it's an entirely successful strategy.

I'm quite a fan of not recreating effort which is generally the goal when trying to pull out common code and within one team this seems to be a good approach the majority of the time. 

When it comes to sharing across teams then I think we need to consider the perceived benefits a bit more because it doesn't come without costs.

These are some of the types of code that we've shared previously:

<h3>Domain objects</h3>

I think this is the most dangerous type of code to share because although we often do have the same domain concepts in different projects, it's quite rare that they mean exactly the same thing.

In addition there is an implicit coupling created with our database since we pretty much now have to make sure that our database schema matches up with the current version of that domain object.

Either that or we do have a shared database for all the applications which use that shared domain object in which case we have an even stronger coupling between applications.

We're assuming that the two application have exactly the same domain concept and from my experience quite often that isn't the case - even if there is a concept with the same name it may be <a href="http://dddstepbystep.com/wikis/ddd/bounded-context.aspx">used in different ways</a> or mean something completely different in different applications.

This is quite similar to the problem with having a universal domain model which Dan points out in <a href="http://dannorth.net/classic-soa">his classic SOA article</a>.

In general I don't think it makes sense to share this type of code.

<h3>Test code</h3>

This one seems like it should fairly universally a good idea - after all we often import 3rd party testing libraries so it seems like just sharing some common testing code shouldn't be much different.

One piece of code that we shared was the Selenium bootstrapping code and this approach worked reasonably well until we wanted to adjust the amount of time between each command because commands were being sent to the browser before elements had the chance to load.

Apart from the fact that the other users of the library didn't want anything change with respect to how they used the code we had to go and make the change in another project, build that and then update the reference that we had to the library.

Certainly this process would have been made easier if we'd used something like <a href="http://ant.apache.org/ivy/">Ivy</a> but the amount of duplication of code that we were saving didn't seem worth the hassle it caused so we ended up inlining the code.	

<h3>Infrastructure code</h3>

General infrastructure code e.g. code to handle NHibernate transactions which is quite unlikely to change seems one candidate which can work quite well in a shared library and so far I haven't seen many problems arise from doing this.

I think the key with these bits of reusable code is that we keep them quite small and ensure that they have only one responsibility which will be useful for all the applications.

We eventually ended up slimming down our shared library and the majority of the code that remains in there is solving specific infrastructure type problems which will be the same across any applications using the same technical stack.

<h3>Things to be careful about when sharing code</h3>

One reason that we may share code is so that if there is a change then it only needs to be done in one place.

We need to have a degree of confident that if we put code in a shared library that this is actually the case.

If it's likely that different applications might need shared code to change in different ways then we might not want to make that bit of code shared otherwise we'll just end up with application specific code in a shared library.

From what I've noticed it makes most sense to put code which is unlikely to change and is generic enough to be useful across several applications as is into shared libraries. 

For any other code it might actually be beneficial to accept that there will be some duplication between applications in the same organisation and not try and pull out a common piece.
