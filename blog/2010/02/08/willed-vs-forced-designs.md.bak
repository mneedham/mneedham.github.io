+++
draft = false
date="2010-02-08 22:48:05"
title="Willed vs Forced designs"
tag=['coding']
category=['Coding']
+++

I came across an interesting post that Roy Osherove wrote a few months ago where he talks about '<a href="http://weblogs.asp.net/rosherove/archive/2009/11/12/test-driven-design-willed-vs-forced-designs.aspx">Willed vs Forced Designs</a>' and some common arguments that people give for not using TypeMock on their projects.

I'm not really a fan of the TypeMock approach to dealing with dependencies in tests because it seems to avoid the fact that the code is probably bad in the first place if we have to resort to using some of the approaches it encourages.

Having said that Roy makes the following point which I think is quite accurate:

<blockquote>
You let an automated tool (rhino mocks, Moq etc..) tell you when your design is OK or not. That point alone should go against anything ALT.NET has ever stood for, doesn’t it? If you need a tool to tell you what is good or bad design, then you are doing it wrong. 
</blockquote>

While it is true that it's useful to be able to know for ourselves whether our code is drifting into territory where it's become way too complicated, I think it is useful to have the tests as a reminder that this is becoming the case.

It's quite easy when you have a delivery deadline and are under pressure to stop being as observant about the quality of what you're coding and to rush to complete our particular task.

In these situations it can be useful to be restricted by our framework to the extent that the pain we'll feel in trying to test our code will act as an indicator that we're doing something wrong.

What I found interesting when reading Roy's post is that the arguments sound sounds quite similar to the discussion a couple of years ago with respect to whether using Mockito instead of jMock was bad because <a href="http://dannorth.net/2008/09/the-end-of-endotesting#comment-17523">it hides design problems that you have with dependencies</a>. Steve Freeman wrote the following comment on Dan's post:

<blockquote>
But, it also became clear that he wrote Mockito to address some weak design and coding habits in his project and that the existing mocking frameworks were doing exactly their job of forcing them into the open. How a team should respond to that feedback is an interesting question.

In the meantime, I’ve found that I /can/ teach using the existing frameworks if I concentrate on what they were intended for: focusing on the relationships between collaborating objects. I’ve seen quite a few students light up when they get the point. In fact, the syntactic noise in jMock really helps to bring this out, whereas it’s easy for it to get lost with easymock and mockito.
</blockquote> 

In this case I definitely prefer the style of mocking that we get with Mockito over jMock even though I've worked on code bases where we've created objects with way too many dependencies and haven't felt the pain as much because the framework is so easy to use.

I can't think of a compelling argument for why this is different to the TypeMock vs other mocking frameworks argument. It seems to be a similar argument around dependencies in our code.

The other thing I'm intrigued about is whether the choice of framework should be in some way linked to the level of skill of the people who are going to use it.

If someone is a Dreyfus Model novice with respect to object oriented design then it would make much more sense to use a tool which makes it really obvious that they're doing something wrong. In that case using a perhaps more limited tool would just be a quick feedback mechanism.

Once we have a bit more skill then it would seem more appropriate to use the more powerful tool which we have the ability to abuse but hopefully now have the experience to know when we can and cannot get away with doing so.

In the end the argument seems quite similar to ones I've often heard about <a href="http://en.citizendium.org/wiki/Ruby_programming_language">programming in Ruby</a> and whether or not we should give programmers powerful language features because they're liable to hang themselves.

In conclusion I'm thinking that perhaps TypeMock in experienced hands isn't such a bad thing and could actually be useful in some select situations but would probably be quite a dangerous tool for someone new to the whole unit testing game.
