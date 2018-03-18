+++
draft = false
date="2009-05-15 07:39:57"
title="Coding Dojo #14: Rock, Scissors, Paper - TDD as if you meant it "
tag=['coding-dojo']
category=['Coding Dojo']
+++

We decided to have a second week of following Keith Braithwaite's '<a href="http://www.parlezuml.com/softwarecraftsmanship/sessions/tdd_as_if_you_meant_it.htm">TDD as if you meant it</a>' exercise which he led at the <a href="http://www.parlezuml.com/softwarecraftsmanship/index.htm">Software Craftsmanship Conference</a>.

Our <a href="http://www.markhneedham.com/blog/2009/04/30/coding-dojo-13-tdd-as-if-you-meant-it/">attempt a fortnight ago</a> was around implementing a Flash Message interceptor, to hook into the Spring framework but this week was focused more around modeling, the goal being to model a game of <a href="http://en.wikipedia.org/wiki/Rock-paper-scissors">Rock, Paper, Scissors</a>.

The code is available on our <a href="http://bitbucket.org/codingdojosydney/rockscissorspaper/src/"> bitbucket repository</a>.

<h3>The Format</h3>

We used the <a href="http://codingdojo.org/cgi-bin/wiki.pl?RandoriKata">Randori</a> approach with four people participating for the whole session.

<h3>What We Learnt</h3>

<ul>
<li>It was interesting trying to work out what should be the first test that we should write - <strong>the instinct for me was to think about about the different objects that we would need to model</strong> a game but <a href="http://blog.halvard.skogsrud.com/">Halvard</a> suggested it would be simpler to start off with a <a href="http://bitbucket.org/codingdojosydney/rockscissorspaper/src/tip/test/rsp/RockScissorsPaperUnitTest.java">test where rock should beat scissors</a>. What I also found interesting was that we edited and then ran this test at least 3 times, adding more test setup and then implementation details each time. It felt much more iterative than the normal TDD approach where much more time would be spent up front writing the test before writing the code to make it past.</li>
<li>One thing <a href="http://pilchardfriendly.wordpress.com/">Nick</a> was helping us to drive was <strong>'safe refactoring'</strong> when refactoring various parts of the code. The idea here was to try and drive the refactorings from the IDE without having to do too much of it manually which can lead to mistakes. We also tried to keep the code compiling the whole time while keeping the time that the tests were failing to a minimum.

For example we started off with rock as a string and our goal was to get it to be Throw.ROCK as it is on the repository. 

<ul>
<li>
We started off by making "rock" a constant.</li>
<li>We then introduced the enums by converting from the strings to enums using Throw.valueOf("rock")</li>
<li>Then the twoPlayerRsp method that took an enum was called from the old one that took a string</li>
<li>Finally we updated the tests to call the enum method directly and removed the old twoPlayerRsp that took the string.</li></ul>

This type of refactoring proved to be a bit harder when trying to refactor the return result of the twoPlayerRsp method since you cannot overload on return types in Java. There was therefore a little bit of time when we couldn't compile the code while doing this refactoring.

It felt quite slow refactoring this way but I think this style of refactoring was new to most people so we would probably get quicker at it from doing it a few times. The fact that we are more certain that we haven't broken anything while refactoring this way makes it a useful approach from my point of view.
</li>
</ul>

<h3>For next time</h3>

<ul>
<li>An idea that <a href="http://fragmental.tw/">Phil</a> and I were discussing was running an open dojo where anyone who wants to come is welcome. At the moment we've had it as an internal dojo but if anyone is interested in coming to code with us then let me know by replying to this post or <a href="http://twitter.com/markhneedham">messaging me on twitter</a>. We normally run the dojo on Wednesday nights for a couple of hours in the ThoughtWorks Sydney office.</li>
<li>We've used the Randori approach for the <a href="http://www.markhneedham.com/blog/category/coding-dojo/">majority of our dojos so far</a> and while I think it works really well I'm interested in seeing what other setups we can try. I've been reading about the <a href="http://codeache.blogspot.com/2008/10/coding-rumors-or-uberdojo.html">Uber/Ultra Dojo on Hugo Corbucci's blog</a> so either of those might be something that we try out in one session.</li>
<li>Another quite interesting idea that was suggested to me by <a href="http://dannorth.net">Dan North</a> is to make a commit to Mercurial after each pair's go at the computer so that you have a history of how the code has progressed through the session - I think this would probably be quite interesting to read and maybe more useful than just having the code as it was when the session finished.</li>
</ul>
