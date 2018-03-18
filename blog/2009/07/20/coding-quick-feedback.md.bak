+++
draft = false
date="2009-07-20 21:10:12"
title="Coding: Quick feedback"
tag=['coding', 'quick-feedback']
category=['Coding']
+++

One of the most important things to achieve if we are to get any sort of productivity when writing code is to find ways to get the quickest feedback possible.

My general default stance with respect to this has always been to TDD code although I've found when coding in F# that I'm not actually sure what the overall best way to get quick feedback is.

This is partly because I haven't been able to find a way to run tests easily from inside Visual Studio but also partly because even when you do this the code for the whole project needs to be recompiled before the tests can be run which takes time.

I often just load functions into F# interactive and then manually test them in there with a couple of values. If the results are what I expect then I move on. 

By doing this I'm getting <strong>feedback that the code works</strong> for the inputs that I've tried but I'm not getting <strong>feedback that I haven't broken some old functionality</strong> with my changes which has <a href="http://twitter.com/markhneedham/status/2703773959">happened a couple of times now</a>.

I'm coming to the conclusion that when I really am just testing out a small function it is quite valuable to be able to make use of F# interactive to play around with this code and quickly know if it is working but once I start composing several different functions together in the REPL and end up in trial and error mode then it might be more effective to write a unit test to help out. 

There are certainly other occasions where we can get quicker feedback by other means, and my colleague <a href="http://www.thekua.com/atwork/2008/02/if-you-do-test-driven-development-all-the-time-youre-doing-something-wrong/">Pat Kua wrote a post last year where he pointed out that you don't always need to use TDD</a> - it depends what type of code you're writing. 

When you're spiking or working in experimentation mode as he refers to it TDD won't be as effective and if you try to use TDD you will probably end up very frustrated because it will slow down your ability to get the type of feedback that you want.

When we are spiking we are looking for <strong>feedback on whether the approach we are trying out will actually work</strong>  and the quickest way to find this out is often just to hack some code together and not spend a great deal of time worrying about the quality of what we're writing.

Kent Beck recently wrote about the <a href="http://www.threeriversinstitute.org/blog/?p=187">trade off between the amount of time it takes to write an automated test and the feedback it gives you</a> giving an example when developing JUnit Max of a time when his feedback cycle was quicker by not writing the test since it would take several hours to work out how to do so.

While Kent Beck probably has the experience to make this sort of trade off call fairly accurately others may need to be more careful about doing this.

When I first started coding my way of working out whether something worked was to launch the application and check that way. 

That often does provide quicker immediate feedback than working out how to write a test but if we make a change to our code and want to know if it still works we need to launch the application again to find out. We frequently end up having to do this cycle multiple times since we always make mistakes and have to go back and correct these.

I think the current popularity of javascript heavy applications is leading us into the trap of thinking that we don't need to write automated tests to cover this functionality since we can just verify it works by launching the application - sadly the number of bugs that creep in when we take this approach is quite substantial so <strong>any initial speed gains are cancelled out by the re-work we need to do later</strong>.

Another interesting area where we need to get feedback quickly is at the points at which we integrate with external systems. 

An example of this on a project I worked on was that we had logic in our application which relied on the value returned from a service layer dependency. 

We got caught out by this value changing and breaking our application so after this we put in an integration test which specifically tested for that value and therefore allowed us to know earlier on if there had been a breaking change made.

These are just some of the areas that I've come across where there are different ways that we can get feedback and we need to make <a href="http://www.markhneedham.com/blog/2009/03/02/trade-offs-some-thoughts/">trade offs</a> to work out which is the best way for our given situation.
