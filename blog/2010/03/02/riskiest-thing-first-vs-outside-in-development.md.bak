+++
draft = false
date="2010-03-02 22:49:11"
title="Riskiest thing first vs Outside in development"
tag=['software-development']
category=['Software Development']
+++

I had an interesting conversation with my colleague <a href="http://ilovemartinfowler.com/">David Santoro</a> last week where I described the way that I often pick out the <a href="http://www.markhneedham.com/blog/2009/05/11/tackling-the-risk-early-on-at-a-task-level/">riskiest parts of a story or task</a> and do those first and David pointed out that this approach didn't seem to fit in with the idea of <a href="http://www.infoq.com/presentations/bdd-dan-north">outside in development</a>.

The idea with outside in development as I understand it is that we would look to drive any new functionality from the UI i.e. the outside and work our way inwards through the various layers and probably eventually end up with persistence i.e. the inside. 

In the particular example that were basing our discussion on I described a story that I was working on with my pair where we needed to apply some constraints to certain items in our data set and then display them differently on the UI as a result of that.

We went through the existing domain model to see if there was anything in there that we could make use of, and having realised that there wasn't anything we mapped out the tasks we would need to do to implement this functionality.

The most difficult/tricky task was to handle the data migration as we realised that we would need to add an extra column to one of the tables. We also needed to do the associated Hibernate mapping and the code from the UI and controller level downwards to make use of this.

We did the data migration and associated work first and one we were happy that was working we went and coded from the UI downwards until we reached the persistence layer.

In this situation it seemed like it worked out reasonably well and I couldn't see that we would have ended up with a different solution if we had started off driving through the UI.

In fact we did end up spending most of our time doing the data migration so to me it seemed somewhat justified doing that first since we did run into a couple of problems.

Outside in development in general seems a good thing to me so I'm curious as to whether I'm justifying a sub optimal approach to myself or whether there are some situations where we can vary the approach a bit?
