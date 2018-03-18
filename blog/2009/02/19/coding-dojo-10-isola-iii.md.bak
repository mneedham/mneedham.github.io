+++
draft = false
date="2009-02-19 23:09:33"
title="Coding Dojo #10: Isola III"
tag=['coding-dojo']
category=['Coding Dojo']
+++

In our latest coding dojo we continued working on <a href="http://bitbucket.org/codingdojosydney/isola">Isola</a> with a focus on adding functionality following on from <a href="http://www.markhneedham.com/blog/2009/02/12/coding-dojo-9-refactoring-isola/">last week's refactoring effort</a>.

<h3>The Format</h3>

We used the <a href="http://codingdojo.org/cgi-bin/wiki.pl?RandoriKata">Randori</a> approach with four people participating for the whole session.

<h3>What We Learnt</h3>

<ul>
<li>Our real aim for this session was to try and get the code into a state where we could reject an invalid move i.e. a move to a square that wasn't adjacent to the one the player was currently on. As we still had the whole board represented as a string this proved to be quite tricky but we eventually came up with an approach which <a href="http://bitbucket.org/codingdojosydney/isola/src/c024ba6f708b/src/main/java/gn/isola/game/IsolaBoard.java">calculated the difference between the last and current moves</a> and was able to tell us whether or not it was valid. This didn't cover diagonal moves, however. We found it pretty difficult to drive this functionality due to the way the board was represented.</li>
<li>What I've found surprising is how long we've been able to get away with having the board represented like this. Ideally we would have it represented in a structure that made it easy for us to make changes. This would require quite a <strong>big refactoring effort</strong> which we shied away from, I think due to the fact that we would be working without a green bar for quite a while during the refactoring. It wasn't obvious to me how we could refactor the code in small steps.</li>
<li><a href="http://blog.halvard.skogsrud.com/">Halvard</a> pointed out that while we don't want to do Big Design Up Front, what we did in the first week of Isola was No Design Up Front which was equally harmful. Finding a happy medium i.e. <strong>Enough Design Up Front</strong> is necessary to avoid the problems we have run into here.</li>
</ul>

<h3>For next time</h3>

<ul>
<li>We're planning to try and implement Isola in Javascript next week. Most of the Dojo regulars are working with Javascript on their projects so it makes sense to give it a go.</li>
</ul>
