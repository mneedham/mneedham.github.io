+++
draft = false
date="2009-09-28 00:02:12"
title="Learning from others/Learning yourself"
tag=['learning']
category=['Learning']
+++

Something which has become quite apparent to me recently is that I learn things far more quickly if I try it out myself and make mistakes than if I just rely on someone else's word for it but some more experienced colleagues seem able to use information explained to them fair more effectively and don't necessarily need to go through this process.

While reading through the Dreyfus Model one of the ideas that is suggested is that once people reach the level of 'Proficient' at any given skill then they are able to learn from the experiences of others without needing to experience something themselves.

Andy Hunt sums this up quite nicely in <a href="http://www.markhneedham.com/blog/2008/10/06/pragmatic-learning-and-thinking-book-review/">Pragmatic Learning and Thinking</a> :
<blockquote>
Proﬁcient practitioners make a major breakthrough on the Dreyfus model: they can correct previous poor task performance. They can reﬂect on how they’ve done and revise their approach to perform better the next time. Up until this stage, that sort of self-improvement is simply not available. 

Also, <strong>they can learn from the experience of others. As a proﬁcient practitioner, you can read case studies, listen to water cooler gossip of failed projects, see what others have done, and learn effectively from the story, even though you didn’t participate in it ﬁrsthand</strong>.</blockquote>

If you're not at that level yet it therefore seems to be the case that it's necessary to experience this situations in order to learn effectively.

The trick thing then is to engineer an environment where it is possible to learn but not one where you jeopardise a code base by doing so.

In a way this is what we did with the <a href="http://www.markhneedham.com/blog/2009/09/19/set-based-concurrent-engineering-a-simple-example/">setter/constructor injection problem that I described previously</a> - <a href="http://erik.doernenburg.com/">Erik</a> pointed out the disadvantages that we would get from using constructor injection on a class which many classes derived from but I didn't fully appreciate his concerns and I couldn't picture the problems we would face until we spent a bit of time putting the dependency into the constructor and I was able to see how this dependency would cascade down into the 30 or so sub classes.

Since we were trying out a setter based injection approach alongside the constructor injection based approach in a time boxed exercise we were able to just throw away the constuctor based injection code when we saw that it wasn't quite going to work and so no harm was done to the code base.

I sometimes feel that a similar type of learning is probably going on in other situations as well.

One fairly common area of contention on projects I've worked on is around whether or not we should put stub/mock calls in a setup method in a test fixture.

On a project I worked on a couple of years ago we ran ourselves into a world of pain by putting mock/stub calls there because when we wanted to test a specific interaction in a test there would often be an unexpected failure because of those calls in the setup method. 

It was never entirely obvious what had happened and we would end up wasting a lot of time before we realised what had happend.

As a result of that <a href="http://www.markhneedham.com/blog/2008/12/19/tdd-mock-expectations-in-setup/">I've been pretty much against that approach</a> although I can see why we might want to do this. It becomes very tedious typing out the same setup code in each of our tests.



Abstracting away that common setup into a method or series of methods which we explicitly call in each test provides one way to solve the problem but it takes the test setup one more click away from us when we're analysing test failures so I'm not sure whether it solves all our problems.

My current thinking is that perhaps we can make use of the setup method as long as all the tests defined in that test fixture require exactly the same setup but that as soon as we are writing a test which requires a different setup we need to pull that test out into its own test fixture. 

The problem with this is that we end up splitting our tests based on how they test interaction with a dependency which seems very strange to me.

I still don't have the answer for the best way to solve this problem but I think I know a bit better from having experimented with some ideas than I would have by just listening to someone tell me about their experiences.

From my understanding of the Dreyfus Model, someone who's really good at unit testing wouldn't necessarily need to do this but would instead be able to learn from someone else's experiences just by talking to them about it.

I'm assuming that they would be able to do this because they have a wealth of similar situations to relate your stories to and they can therefore fill in any gaps in the knowledge they have.

I think this aspect of the Dreyfus Model helps identify why just explaining something from your experience rarely seems to be successful - unless the other person is 'Proficient' at the skill in question they won't easily be able to relate your experience to the problem without some experimentation of their own. 

Perhaps there's more to it and I'm way off the mark but this theory at least seems reasonably plausible to me
