+++
draft = false
date="2009-10-04 16:59:29"
title="Coding: Rules of thumb"
tag=['software-development']
category=['Coding']
+++

I recently came across <a href="http://ayende.com/Blog/archive/2009/09/28/even-tests-has-got-to-justify-themselves.aspx">a post by Ayende where he talks about the need for tests to justify themselves</a> and describes his approach to testing which doesn't involved TDDing all the code he writes.

While this approach clearly works well for Ayende I really like the following comment by Alex Simkin:

<blockquote>
Anyway, this post should be marked MA (Mature Audience Only), so younger programmers wont use excuse to not write unit tests because Ayende doesn't do it.
</blockquote>

This reminds me of a conversation I was having with a few colleagues a while ago where we were discussing whether we should look to test drive absolutely everything that we write or whether we should make that decision on a case by case basis.

Personally, I don't yet have the experience to be able to tell when it's appropriate not to drive code (excluding <a href="http://www.thekua.com/atwork/2008/02/if-you-do-test-driven-development-all-the-time-youre-doing-something-wrong/">spiking</a>) and pretty much every time that I've decided something was 'too easy' to test drive I've managed to make a mistake and not realised it until much later than would have been the case with a test driven approach.

I'm finding that this applies to more than just testing though and it seems that where an approach is known to reduce a lot of potential pain then it might be useful to favour that approach unless we find an intriguing reason not to.

Thinking along those lines I think it makes sense to follow some 'rules of thumb' and not break them unless we absolutely have to.

Some rules of thumb which I've come across are:

<ul>
<li>Don't put anything into the session</li>
<li>Don't put getters onto objects - make all code adhere to the <a href="http://www.pragprog.com/articles/tell-dont-ask">tell don't ask</a> principle</li>
<li>Write production code test first</li>
<li>Write classes which adhere to the single responsibility principle</li>
<li>Favour composition over inheritance</li>
<li>Favour constructor injection over setter injection</li>
</ul>

Given a situation where I want to reuse some code and I know that I could choose between doing it with composition or inheritance I wouldn't consider this a 50-50 choice but instead would look to use composition unless it became really difficult to do this and inheritance was clearly the answer in which case I would use that.

Obviously these 'rules of thumb' might be a bit restrictive for people at the higher levels of skill of the <a href="http://www.markhneedham.com/blog/2009/07/18/book-club-the-dreyfus-model-stuart-and-hubert-dreyfus/">Dreyfus model</a> and I imagine that even with people with less experience they could be quite dangerous if applied too literally. 

I wonder whether being dogmatic about a few rules of thumb would be more or less dangerous than making decisions not to follow a useful practice because you mistakenly believe you have the ability to tell whether or not it applies in a given situation?

Corey Haines wrote <a href="http://programmingtour.blogspot.com/2009/10/on-term-pragmatic.html">a really good post where he talks about the misuse of the word 'pragmatic'</a> which seems to address this area although he comes to a slightly different conclusion: 

<blockquote>
This is a common thing that I hear from software developers: they have a little bit of experience, think that they understand something to the point where they can make their own decisions on what it means to 'be pragmatic.' Often times, people use the term 'pragmatic' as a way to hide a lack of skill and experience. Or, sometimes, it is used in ignorance: someone doesn't realize that they don't understand something well enough. Usually, though, it is brought to play when someone is justifying cutting corners on something...this can come back later to bite you in the ass. 

Think your 9 months of trying TDD makes you an expert, someone who can suddenly decide when it is 'pragmatic' to not design your system with TDD. Or, don't even worry about designing your system with TDD, just talk about automated testing. 

Are you being 'pragmatic' about automated testing, skipping it things you don't know how to do or are hard?
</blockquote>

Typically when people try to justify a shortcut this is exactly the way they will justify it. The irony is that quite often much suffering is gained from that decision so it wasn't really that pragmatic after all.

I realise that there <a href="http://scottcreynolds.com/archive/2009/09/29/601.aspx">aren't really any rules for software development that we can follow all the time</a> and expect to gain success with but it does seem that some approaches have already been proven to be more effective than others so it might be useful to make use of them.
