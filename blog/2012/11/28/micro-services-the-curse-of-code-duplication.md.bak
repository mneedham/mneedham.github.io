+++
draft = false
date="2012-11-28 08:11:04"
title="Micro Services: The curse of code 'duplication'"
tag=['software-development']
category=['Micro Services']
+++

A common approach we've been taking on some of the applications I've worked on recently is to decompose the system we're building into smaller <a href="http://2012.33degree.org/talk/show/67">micro services</a> which are independently deployable and communicate with each other over HTTP.

An advantage of decomposing systems like that is that we could have separate teams working on each service and then make use of a <a href="http://martinfowler.com/articles/consumerDrivenContracts.html">consumer driven contract</a> as a way of ensuring the contract between them is correct.

Often what actually happens is that we have one team working on all of the services which can lead to the a mentality where we treat start treating the comunication between services as if it's happening in process.

One of the earliest lessons I learnt when writing code is that you should <a href="http://en.wikipedia.org/wiki/Don't_repeat_yourself">avoid repeating yourself</a> in code - if you have two identical bits of code then look to extract that into a method somewhere and then call it from both locations.

This lesson often ends up getting applied across micro service boundaries when we have the same team working on both sides.

For example if we have a customer that we're sending between two services then in Java land we might create a <cite>CustomerDTO</cite> in both services to marshall JSON to/from the wire.

We now have two versions of the 'same' object although that isn't necessarily the case because the client might not actually care about some of the fields that get sent because its definition of a customer is different than the provider's.

Nevertheless if we're used to being able to working with tools like <a href="http://www.jetbrains.com/idea/">IntelliJ</a> which let us make a change and see it reflected everywhere we'll end up driving towards a design where the <cite>CustomerDTO</cite> is shared between the services.

This can be done via a JAR dependency or using something like <a href="http://git-scm.com/book/en/Git-Tools-Submodules">git sub modules</a> but in both cases we've now coupled the two services on their shared message format.

I think the 'duplication' thing might be less of an issue if you're using a language like Clojure where you could work with maps/lists without transforming them into objects but I haven't built anything web related with Clojure so I'm not sure.

As I understand it when we go down the micro services route we're trading off the ease of working with everything in one process/solution for the benefits of being able to deploy, scale and maintain parts of it independently.

Perhaps the problem I've described is just about getting used to this trade off rather than holding onto the idea that we can still treat it as a single application.

I'd be curious to hear others' experiences but I've seen this same pattern happen two or three times so I imagine it may well be common.
