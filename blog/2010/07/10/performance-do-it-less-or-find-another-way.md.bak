+++
draft = false
date="2010-07-10 22:49:52"
title="Performance: Do it less or find another way"
tag=['performance']
category=['Software Development']
+++

One thing that we tried to avoid on the project that I've been working on is making use of <a href="http://msdn.microsoft.com/en-us/library/bb397951.aspx">C# expressions trees</a> in production code.

We found that the areas of the code where we compiled these expressions trees frequently showed up as being the least performant areas of the code base when run through a performance profiler. 

In a discussion about the ways to improve the performance of an application <a href="http://twitter.com/christianralph">Christian</a> pointed out that once we've identified the area for improvement there are two ways to do this:

<ul>
<li>Do it less</li>
<li>Find another way to do it</li>
</ul>

We were able to find another way to achieve what we wanted without using them and we favoured this approach because it was much easier to do,

An alternative would have been to cache the compilation of the expression so that it wouldn't happen every single time a request passed through that code path.

A lot of the time it seems like it's actually possible to just do something less frequently rather than changing our approach...

For example:

<ul>
<li>Caching a HTTP response so that not every request has to go all the way to the server.</li>
<li>Grouping together database inserts into a bulk query rather than executing each one individually.</li>
</ul>

... and most of the time this would probably be a simpler way to solve our problem.

I quite like this heuristic for looking at performance problems but I haven't done a lot of work in this area so I'd be interested in hearing other approaches as well.
