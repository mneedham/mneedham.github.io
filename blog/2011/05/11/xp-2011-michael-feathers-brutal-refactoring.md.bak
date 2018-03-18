+++
draft = false
date="2011-05-11 13:35:42"
title="XP 2011: Michael Feathers - Brutal Refactoring"
tag=['xp2011']
category=['XP 2011']
+++

The second session that I attended at XP 2011 was Michael Feathers' tutorial 'Brutal Refactoring' where he talked through some of the things that he's learned since he finished writing '<a href="http://www.amazon.com/Working-Effectively-Legacy-Michael-Feathers/dp/0131177052/ref=sr_1_1?ie=UTF8&qid=1305116318&sr=8-1">Working Effectively With Legacy Code</a>'.

I've found some of Michael's recent blog posts about <a href="http://michaelfeathers.typepad.com/michael_feathers_blog/2011/01/measuring-the-closure-of-code.html">analysing the data in our code repositories</a>  quite interesting to read and part of this tutorial was based on the research he's done in that area.

<h4>Clean code vs Understandable code</h4>

The session started off discussing the difference between <a href="http://www.amazon.com/Clean-Code-Handbook-Software-Craftsmanship/dp/0132350882/ref=sr_1_2?ie=UTF8&qid=1305116318&sr=8-2">clean code</a> and understandable code.

Feathers gave a definition of clean code as code which is simple and has no hidden surprises and suggested that this is quite a high bar to try to obtain.

Understandable code on the other hand is about the amount of thinking that we need to do in order to understand a piece of code and can be a more achievable goal.

He also pointed out that it would be very rare us to take a code base and refactor the whole thing and that we should get used to having our code bases in a state where not every part of it is perfect.

<h4>Behavioural economics</h4>

Next we discussed behavioural economics where Feathers suggested that the 'incentives' structure of programming leads to code ending up in a bad state

i.e. It's much easier/less time consuming for people to add code to an existing method or to an existing class rather than creating a new method or class.

The main reason for that is the difficulty in choosing a name for those methods/classes rather than the mechanical complexity of doing so in a text editor.

Feathers suggested there are probably also things that we don't know about ourselves and the way we program.

<h4>The shape of code</h4>

Next we covered the shape of code in systems and the research that Feathers has been doing and has written a few blog posts about.

Feathers suggested that most code bases will follow a power curve whereby most files are hardly changed at all but there will be a small number of files which get changed a lot.

I tried this out on a couple of code bases that I've worked on and noticed the same trend.

Feathers showed a graph with code churn on one axis and code complexity on the other and suggested that we really need to focus our refactoring efforts on code which is changed frequently and is complex!

When chatting afterwards Feathers suggested that it would be interesting to look at the way that certain classes increased in complexity over time and see whether we could map those changes to events that happened to the code base.

<h4>Finding the design</h4>
Feathers talked about the idea of grouping together clumps of code to try and see if they make sense as a domain concept.

For example if three parameters seem to be being used together throughout the code base then perhaps it means that those 3 parameters together mean something.

He described it as an inside out way of deriving domain concepts as we're working from what we already have in the code and seeing if it makes sense rather than deriving code from domain concepts.

<h4>Rapid scratch refactoring</h4>

I'd previously read about scratch refactoring in Working Effectively With Legacy Code, where the idea is that we start refactoring code to how we want it to be without worrying about it actually working, and Feathers gave an example of doing this on a piece of code.

The most interesting thing about this for me was that he did the refactoring in notepad rather than in the IDE.

He said this was because the IDE's compile warnings were distracting from the goal of the exercise which is to understand how we could improve the code.

<h4>Deciding upon architectural rules</h4>

Feathers said that when he first starts working with a team he gets people to explain to him how the system works and that as a side effect of doing this exercise they start to see ways that it could be simplified.

My colleague Pat Kua <a href="http://www.thekua.com/atwork/2007/07/onboarding-strategy-visible-architecture/">talks about something similar in his on boarding series</a> and one of the benefits of <a href="http://www.markhneedham.com/blog/2009/10/21/the-effect-of-adding-new-people-to-project-teams/">adding new people to teams</a> is that we end up having these discussions.

It helps to have a shared understanding of what the system is so that people will know where to put things.

We could do this by stating some rules about the way code will be designed e.g. receivers will never talk to repositories.

This seems somehow related to a recent observation of mine that it's much easier to work when we have to do so within some sort of constraints rather than having free reign to do whatever we want.

<h4>Systemic concerns</h4>
Feathers gave an example of a place where he'd worked where an upstream team decided to lock down a service they were providing by using the Java 'final' keyword on their methods so that those methods couldn't be overridden.

He pointed out that although we can use languages to enforce certain things people will find ways around them which in this case meant that the downstream team created another class wrapping the service which did what they wanted.

He also observed that the code around hard boundaries is likely to be very messy.

We also covered some other topics such as wrapping global variables/singletons in classes and passing those classes around the system and the idea of putting hypotheses/assertions into production code.

Pat's <a href="http://www.thekua.com/atwork/2011/05/notes-from-michael-feathers-brutal-refactoring/">also written some notes about this session on his blog</a>.
