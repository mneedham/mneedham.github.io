+++
draft = false
date="2010-08-12 18:59:54"
title="One idea at a time"
tag=['coaching-2']
category=['ThoughtWorks University']
+++

One thing I noticed while pairing with some of the <a href="http://www.thoughtworks.com/thoughtworks-university">ThoughtWorks University</a> guys a few weeks ago is that I had an almost overwhelming urge to show them all sorts of coding techniques that I've learned, probably to the point where it'd be more confusing than helpful.

<a href="http://jkwerner2.wordpress.com/">JK</a> pointed out that it's more effective to bite your tongue and just focus on one idea at a time which is something that the authors of <a href="http://www.amazon.com/Agile-Coaching-Rachel-Davies/dp/1934356433/ref=sr_1_1?ie=UTF8&s=books&qid=1281621756&sr=8-1-spell">Agile Coaching</a> touch on briefly at the beginning of the book:

<blockquote>
You're probably itching to get started, but where do you get started? There's no right place. The simplest approach is to pick one thing and jump in. 
</blockquote>

For example one story I joined involved adding a new feature which touched all layers of the application from the view through the service layer and to the database.

My favoured approach is to start from the UI and work out what we actually need to develop by starting from what the user will actually see i.e. outside in development.

The approach that had been taken on the story meant that the API of one of the services was being driven out straight from a service test rather than coming for a need for that method from the controller.

The reason I prefer to <a href="http://www.markhneedham.com/blog/2010/04/18/coding-another-outside-in-example/">drive out a story from the outside in</a> is that we don't have to try and imagine the way someone might want to use an object - we already know because we've written the consumer code for that method already.

While learning how to drive from the outside in is a useful skill, in this case the main skill that we were trying to encourage was test driven development and getting the grads used to the red - green - refactor cycle and so on.

Although it would have made our lives easier to stop and go and write the code for the controller which needed the service first, I think it would have been quite confusing to leave the service in a half completed state and move off to work on something else.

We therefore kept on working on the service code while trying to imagine exactly how it would be used by the controller. 

While this wasn't the optimal way to develop this piece of code and perhaps took longer overall I think it was a more useful approach to take in this situation and is one I'd take again given similar circumstances.
