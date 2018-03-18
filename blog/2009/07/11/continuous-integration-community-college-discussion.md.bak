+++
draft = false
date="2009-07-11 14:13:48"
title="Continuous Integration: Community College Discussion"
tag=['software-development']
category=['Software Development']
+++

We ran a session on Continuous Integration at the most recent Community College in the ThoughtWorks Sydney office.

It was roughly based around a <a href="http://www.anthillpro.com/blogs/anthillpro-blog/2009/05/05/1241542860000.html">CI Maturity Model</a> which I recently came across although the intention was to find out what other teams were doing CI wise.

I became a bit more aware of how little I know about CI after listening to a <a href="http://www.se-radio.net/podcast/2009-04/episode-133-continuous-integration-chris-read">Software Engineering Radio interview with my colleague Chris Read</a> so I was keen to see how other teams are approaching this problem.

These were some of the most intersting parts of our discussion.

<ul>
<li><strong>Handling external dependencies</strong> - the idea here is that you don't have control over these end points and their reliability and it is very frustrating for the build to fail due to a problem with a dependency rather than a problem in your application.

Several teams were testing integration of their application against these in a separate build something which we are also doing with a set of NUnit tests which run every 10 minutes directly against our service level end point.

On my project we are also making use of an <a href="http://www.markhneedham.com/blog/2009/06/21/seams-some-thoughts/">impersonator</a> of our main integration point early in our build pipeline and then testing end to end integration at a later stage in the pipeline. We are not completely protected at the moment but we're getting there. 

The trade off here is finding the balance between making the impersonator way too complicated such that people can't understand it and we can't be sure that it actually works. It seems that if we are doing anything beyond a state machine with regards to handling requests & responses and are putting actual business logic inside the impersonator then we've probably gone too far.</li>
<li>The importance of creating a single artifact if using a build pipeline and then running every unit, integration and functional test against that same artifact was pointed out. 

On my project we are recompiling our code at each stage of the build pipeline (from the same revision of the code in Subversion) as we haven't yet found a good way of putting the artifact somewhere where each build stage can pick it up from - some colleagues are making use of Ivy & Maven repositories to do this on Java projects.

We also spoke about keeping the configuration of the application separate to the artifact so that we can easily deploy the application into different environments.
</li>
<li>We discussed the fact that <strong>keeping the build time very low by paying constant attention to it</strong> is one of the most important things to do to ensure quick feedback for the development team yet it is often allowed to slip to the point where we end up with build times exceeding an hour. 

Most of the teams had a pre commit build time of less than 10 minutes although only a couple had a build time of less than 10 minutes on their CI server.

I've never seen it done but the idea of failing the build if it exceeded an agreed time was suggested forcing the team to address the problem rather than letting it gradually get slower and slower until the quick feedback cycle it originally provided has gone.</li>
<li>The idea of <strong>running performance tests in the build</strong> was something which I found quite interesting - several colleagues pointed out that the point here is not to test the performance of the application when it's live but more to see the trend in how well our application is performing so that if it suddently dips we can address this straight away rather than waiting until later on to do this.

We also spoke about including security tests - such as trying to inject evil SQL into every field - in the build although it was also suggested that these should be there anyway as part of the functional tests that we include. I think testing for <a href="http://www.markhneedham.com/blog/2009/02/12/aspnet-mvc-preventing-xss-attacks/">XSS attacks</a> might also fall into this area.</li>
<li>Another interesting area of discussion was around <strong>whether it's acceptable for the build to break due to a change that we made</strong>. If we decide that it isn't then the only reason that it should fail is due to a problem with a depedency problems. To get to this stage it would need to be possible to run the entire build before checking in probably by having a grid of machines setup which we can assign local builds to run on. Dean Cornish has written an intersting post where he covers the idea of having <a href="http://deancornish.blogspot.com/2009/07/continuous-integration-without-ci.html">continuous integration without a CI server</a>.

On all the projects I've worked on we haven't done this so in these situations I subscribe more to <a href="http://blog.runcoderun.com/post/72393206/its-okay-to-break-the-build">Stuart Halloway's thinking that it is actually ok to break the build in some circumstances</a>. We are leaning on the CI server a bit to give us feedback but I don't think it's too bad to do this if it allows us to check in more frequently.</li>
<li>We also spoke about the importance of getting the <strong>whole team to agree to a collection of CI practices</strong> if CI is really going to work on a project. These might include behaviours such as not checking in when the build's red, looking at why the build has broken if you're checkin broke it, rolling back your changes if you can't fix the problem quickly and so on.</li>
</ul>


