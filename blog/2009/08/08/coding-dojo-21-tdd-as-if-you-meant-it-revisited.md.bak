+++
draft = false
date="2009-08-08 23:50:49"
title="Coding Dojo #21: TDD as if you meant it revisited"
tag=['coding-dojo']
category=['Coding Dojo']
+++

In this weeks dojo we decided to revisit the "TDD as if you meant it' exercise originally invented by Keith Braithwaite for the Software Craftsmanship Conference but recently <a href="http://gojko.net/2009/08/02/tdd-as-if-you-meant-it-revisited/">tried out at the Alt.NET UK Conference in London</a>. 

The idea was to write code for 'tic tac toe' or 'naughts and crosses' and we were following these requirements:

<ul><li>a game is over when all fields are taken</li>
<li>a game is over when all fields in a column are taken by a player</li>
<li>a game is over when all fields in a row are taken by a player</li>
<li>a game is over when all fields in a diagonal are taken by a player</li>
<li>a player can take a field if not already taken</li>
<li>players take turns taking fields until the game is over</li>
</ul>


The <a href="http://openspacecode.googlecode.com/svn/trunk/src/2009-08-01%20London/TddAsIfYouMeanIt/">code from Alt.NET UK is available on Google Code</a> and what I found quite interesting is that the solutions are really quite different to each other. 

Our <a href="http://bitbucket.org/codingdojosydney/tic_tac_toe_as_if_you_mean_it/src/tip/src/org/thoughtworks/dojo/awesome/NaughtsAndToesTest.java">code is up on bitbucket</a> and again it is quite different to the other approaches.

<h3>The Format</h3>

For most of this week's dojo <a href="http://intwoplacesatonce.com/">Dave</a> and I just worked together on the problem although a colleague did come and join us for the last half an hour or so. We were just pairing on a Mac.

<h3>What We Learnt</h3>

<ul>
<li>We coded in Java in <a href="http://www.eclipse.org/">eclipse</a> which I haven't used for about a year and I was really surprised at how rapid the feedback cycle was. We seemed to be able to write a test and have it failing within seconds which is brilliant and just the way it should be whereas I've got used to a much slower feedback loop when using Visual Studio.</li>
<li>We noticed as we did <a href="http://www.markhneedham.com/blog/2009/05/15/coding-dojo-14-rock-scissors-paper-tdd-as-if-you-meant-it/">the previous</a> <a href="http://www.markhneedham.com/blog/2009/04/30/coding-dojo-13-tdd-as-if-you-meant-it/">times</a> when we did this exercise that you <strong>notice objects in the code that you wouldn't normally have noticed</strong> if we hadn't been writing all the implementation details in the test first. 

The 'Square' object was one which neither I nor Dave had expected to exist. We had imagined that code would end up on the 'Game' object and interestingly just before our colleague joined us we had drifted from the rules of the exercise and actually written the outline of a method on the game object to satisfy the 5th acceptance criteria 'a player can take a field if not already taken'.

Luckily we undid that and it became obvious that the new code should be on an object of its own so that's what we did.</li>
<li>The code we have at the moment has everything implemented just using booleans which felt really weird when we were writing the code but seemed to be the simplest thing to do to meet the acceptance criteria.

We discussed this at the time and it seemed that any alternative approach where we didn't do this would end up with us writing a really big test (perhaps with players making moves), therefore meaning the feedback cycle would be really slow.</li>
</ul>

<h3>For next time</h3>

<ul>
<li>I think it would probably be quite interesting to try out this type of exercise and commit to either Git or Mercurial after each of the small steps so that we could see the story of the code more clearly afterwards.</li>
<li>During our <a href="http://www.markhneedham.com/blog/2009/07/11/continuous-integration-community-college-discussion/">discussion on Continuous Integration a few weeks ago</a> it was suggested that we could some sessions on parallelising tests and writing impersonators during one of our coding dojos so we might look at doing that next time around. </li>
</ul>



