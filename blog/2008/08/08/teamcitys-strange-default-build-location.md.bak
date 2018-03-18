+++
draft = false
date="2008-08-08 19:52:50"
title="TeamCity's strange default build location"
tag=['team-city', 'jetbrains', 'continuous-integration', 'build']
category=['Build']
+++

We've been using <a href="http://www.jetbrains.com/teamcity/">TeamCity</a> on my current project and it's proven to be fairly impressive in general.

We're running quite a few different builds which have dependencies on each other and it's been pretty much one click on the web admin tool to get that set up.

One thing that had me really confused is the default location it chooses to build from. The problem is that it seems to change arbitrarily, with the folder name it builds in being calculated from a VSC hash (not sure quite how that's worked out but there we go).

I had (naively) assumed that the default build location would always stay the same and was therefore referencing this location from our build script. Turns out it can change whenever it feels like it!

Our 15:38 build was built to c:/TeamCity/Agent/c734523aedrte but our 15:40 build was built to c:/TeamCity/Agent/d6420ghi2.

Cue much confusion as I repeatedly looked at the first folder trying desperately to work out why nothing was being checked out. Eventually, more by fluke than skill, I figured it out and our build is now being built to c:/WorkingDirectory every time.

Lesson learnt: Take control and set your default directory, don't let TeamCity do it for you!
