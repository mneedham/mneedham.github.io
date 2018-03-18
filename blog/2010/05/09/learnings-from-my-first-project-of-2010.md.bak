+++
draft = false
date="2010-05-09 22:17:57"
title="Learnings from my first project of 2010"
tag=['software-development']
category=['Software Development']
+++

Pat Kua recently wrote <a href="http://www.thekua.com/atwork/2010/03/six-years-at-thoughtworks/">a retrospective of his time working at ThoughtWorks</a> and since I recently finished the first project I've worked on in 2010 I thought it would be interesting to have a look at what I'd learned and observed while working on it.

<h3>"Perfect" code</h3>
I've previously believed that driving for the cleanest code with the least duplication and best structured object oriented design was the way to go but on this project we favoured a simpler design which felt quite procedural in comparison to some of the code bases I've worked on.

I initially felt that this would be a problem but the code was still pretty <strong>easy to change</strong> and everyone on the team was able to understand it without any problem so that seemed to outweigh any other concerns.

<h3>There's always a story to be told</h3>
The client initially had a very stringent change process where if a developer wanted to implement a new feature they would have to get a change request signed off before they were able to check out a branch of the code base to work on it.

This had been changed before I started working there such that Subversion was being used by the development teams although the code still had to go through quite a stringent change management process before it could be released into production.

We didn't really understand why this was the case because it just seemed to make it more difficult to get anything live.

As it turned out that change process was introduced to get around a problem they'd experienced where code was being manually changed in live. This meant that when there was a bug it was difficult to reproduce it since that version of the code wasn't in source control.

Of course there are other ways to achieve this goal but it was interesting that the approach being taken wasn't completely illogical but had been arrived at through a series of steps which did make sense. Dan North talks of the need to have a <a href="http://www.markhneedham.com/blog/2009/04/25/pimp-my-architecture-dan-north/">project shaman</a> who can <strong>tell the story of why certain decisions were made</strong> and the history behind them and it's always useful to have someone who can do that.

<h3>Theory of constraints</h3>
The other interesting thing that I learnt, which is directly linked to the above, is that there is always a constraint within a system and <strong>no matter how much you optimise other parts of your system it won't make any difference to the overall situation</strong>.

In this case no matter how quickly the team was able to code new requirements it didn't make that much difference because there was still quite a big wait at the end pushing the release through the release management system so it could go into production.

We were starting to work on trying to improve this part of the process when I rolled off the project but a lesson for me here is to try and identify where the constraint is in any given system and try and work out how we can address that.
