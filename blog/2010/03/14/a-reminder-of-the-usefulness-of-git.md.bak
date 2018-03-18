+++
draft = false
date="2010-03-14 00:45:34"
title="A reminder of the usefulness of Git"
tag=['git', 'dscm']
category=['Software Development']
+++

Despite the fact that none of the projects that I've worked on have used <a href="http://git-scm.com/">Git</a> or <a href="http://mercurial.selenic.com/">Mercurial</a> as the team's main repository I keep forgetting how useful those tools can be even if they're just being used locally.

I ran into a problem when trying to work out why a Rhino Mocks expectation wasn't working as I expected last week having refactored a bit of code to include a constructor.

I wanted to include the Rhino Mocks source code in our solution before and after the refactoring and step through the code to see what was different in the way the expectations were being setup.

My initial thought was that I could just check out the repository again in another folder and then include the Rhino Mocks source code there and step through it but unfortunately we have all the projects set up to deploy to IIS so Visual Studio wanted me to adjust all those settings in order to load the solution in the new checkout location.

I probably could have gone and turned off that setting but it seemed a bit too much effort and I realised that I could easily use Git to help me solve the problem.

I took a patch of the changes I'd made and then reverted the code before checking it into a local Git repository.

I updated the solution to include the <a href="http://www.ayende.com/projects/rhino-mocks.aspx">Rhino Mocks</a> code and then created a branch called 'refactoringChanges' so that I could then apply the patch that I'd created with my changes.

It was then really easy to switch back between the two branches and see the differences in the way that the Rhino Mocks was working internally.

The actual problem eventually turned out to be the way that the code calls Castle DynamicProxy but I didn't get the chance to look further into it - we had learnt enough to know how we could get around the problem.

I'm in the process of including the source code for all the 3rd party libraries that we use in the solution on a separate Git branch that I can switch to when I want to debug through that code.

Sometimes I end up having to close down Visual Studio and re-open the solution when I switch to and from that branch but apart from that it seems to work reasonably well so far.
