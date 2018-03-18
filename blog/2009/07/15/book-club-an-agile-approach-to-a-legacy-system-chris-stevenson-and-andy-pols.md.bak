+++
draft = false
date="2009-07-15 00:53:45"
title="Book Club: An agile approach to a legacy system (Chris Stevenson and Andy Pols)"
tag=['book-club', 'legacy-code']
category=['Book Club']
+++

Our latest book club session was a discussion on a paper written by my colleague Chris Stevenson and Andy Pols titled '<a href="http://www.skizz.biz/whitepapers/an-agile-approach-to-a-legacy-system.pdf">An Agile Approach to a Legacy System</a>' which I think was written in 2004. This paper was suggested by <a href="http://intwoplacesatonce.com/">Dave Cameron</a>.

These are some of my thoughts and our discussion of the paper:

<ul>
<li>The first thing that was quite interesting was that the authors pointed out that <strong>if you just try and rewrite a part of a legacy system you are actually just writing legacy code yourself</strong> - we weren't sure exactly what was meant by this since for me at least the definition of legacy code is 'code which we are scared to change [because it has no tests]' but presumably the new code did have tests so it wasn't legacy in this sense. Rewriting the code doesn't really add any value to the business though as they point out since all that code might not even being used in which case it is just wasted effort. The idea of not rewriting is something that <a href="http://blog.objectmentor.com/articles/2009/01/09/the-big-redesign-in-the-sky">Uncle Bob advocates</a> and <a href="http://gojko.net/2009/06/19/eric-evans-why-do-efforts-to-replace-legacy-systems-fail/">Eric Evans also mentions the dangers of trying to replace legacy systems in his latest presentations</a>.</li>
<li>I thought it was interesting that the team d<strong>idn't make use of automatic integration since they were frequently integrating on their own machines</strong> - I'm not sure how well this would work on a big team but certainly if you have a team of people fairly experienced with CI then I can imagine that it would work really well. Dean has written <a href="http://deancornish.blogspot.com/2009/07/continuous-integration-without-ci.html">a post about serverless CI</a> which covers the idea in more details.</li>
<li>I liked the idea of <strong>putting up politics as user requirements on the story wall</strong> and then prioritising them just like any other requirement. More often the approach tends to be to try and address these problems as soon as they arise and then end up not really solving them and then getting burnt later on. This approach sounds much better. </li>
<li>Another idea that I like is that <strong>the team didn't get hung up on process</strong> - the teams I've been on which worked the best weren't slaves to process and I've often heard it suggested that having a process is just a way of dealing with the fact that there is a lack of trust in the team. Jay Fields recently wrote about the idea of having <a href="http://blog.jayfields.com/2009/07/more-trust-less-cardwall.html">more trust and less card wall</a> and Ron Jeffries has a recent post where he talks about  <a href="http://xprogramming.com/blog/needles/how-should-user-stories-be-written.htm">the light weight way that we should be making use of stories</a>.</li>
<li>Another really cool idea which I don't remember seeing before is <strong>having the whole team involved in major refactorings</strong> until the whole refactoring has been completed. Quite often with refactorings like this one pair might go off and do it and then when they checkin later there are a lot of changes and the other pairs have trouble merging and now have a lot of code which they are unfamiliar with. </li>
<li>The idea of having a <strong>self selected team</strong> sounds like an interesting idea as you then only have people on the team who actually want to be on it and want to make things happen. I'm not sure how often this would actually happen but it is a nice idea.</li>
<li>The importance of <strong>testing the system against a live database</strong> before putting it into production is emphasised and this goes beyond just using production data in a test environment. The team also made use of data verification testing to ensure that the new system and the current ones were working identically.  </li>
</ul>

Although this paper is relatively short it's probably been the most interesting one that we've looked at so far. I think a lot of the ideas outlined can be used in any project and not just when dealing with legacy systems - definitely worth reading.
