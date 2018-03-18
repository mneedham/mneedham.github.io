+++
draft = false
date="2009-05-12 09:21:13"
title="Debugging: Get to a stage where it works"
tag=['debugging']
category=['Software Development']
+++

When debugging a problem I've learnt far too many times that where possible the most effective approach is to try and get the application back into a state where it does work and then analyse the changes that have resulted in it no longer working as expected.

About 7 or 8 years ago when I used to code PHP at school and university that pretty much was my default approach - I didn't really know how to program well enough to work out how to fix something that was broken so I would always just revert back all the steps I'd done until it worked.

I didn't think it was a particularly good approach at the time - I wasn't using source control so I always used to lose my changes - but looking back at that approach now I think it is one of the most effective ones when debugging.

A recent example of this came when we were trying to work out why our selenium server was no longer being launched when we ran the build locally.

There had been some changes on the files involved but they didn't seem substantial, so my pair and I started looking through the code as it was now and trying to work out what it was doing wrong now.

We didn't really succeed in getting anywhere - there wasn't anything that stood out as being wrong.

Somewhat luckily another colleague happened to come across the code that we were looking at and pointed out something else that seemed strange about what was going on. It turned out that more of the code had been changed that we originally thought.

We went back to the subversion logs and realised that the paths to the selenium jar had been changed to be relative rather than absolute - it was a valid change designed to allow us to run the build for different branches locally - but the relative path wasn't correct and therefore the selenium server was never being started even when the build was run from the trunk.

We had actually been attempting to fix this problem on a branch so we had actually made the problem more difficult for ourselves than it needed to be. Not only was the absolute path not going to work for us but the relative path that we needed was also different as we had checked out the code a level up in the directory structure.

In an attempt to get something working we reverted the changes back to a state where we were able to run the build on the trunk and the selenium server starting working correctly again.

We then had a more stable base to make the changes from. 

The lesson for me here was that if things go wrong it's more effective to get back to a working state as quickly as possible and go from there instead of theorising on what went wrong and trying to fix it that way.
