+++
draft = false
date="2008-08-11 22:10:19"
title="Pair Programming: Pairing with a QA"
tag=['pairing', 'agile', 'qa']
category=['Pair Programming']
+++

I've talked about pair programming in some of my <a href="2008/02/10/pair-programming-introduction/">previous</a> <a href="2008/02/14/pair-programming-the-non-driving-pair/">posts</a> as I find the dynamic it creates quite intriguing.

One idea which was suggested around the time I wrote those posts by my project manager at the time was developers pairing with the QA or BA on certain tasks. I didn't get to experience it on that particular project but over the last week I've been doing quick a bit of build work and for some of that I was pairing with our QA.

Now doing build work might not seem an obvious pairing activity because it is often seen as tedious, and it can be quite boring for the navigator as it is harder for them to add obvious value. We decided on this occasion that because we had different expectations of the build that it would be worthwhile for both of us to work on it for the duration of a pairing session. It turned out to be a good decision.

The build pipeline that we were working on consisted of two stages when we started.

There was the main build which compiled all the code, ran all the tests, created all the artifacts, created a zip file for each artifact and then added an entry into the database for the artifact.

Then we had the functional test build which waited for this main build to finish before running its tests against the artifacts we created in the main build.

As a concept it worked reasonably well but it was becoming obvious to both of us that a lot of the functionality that I had put into the main build didn't actually need to be in there.

We spent some time discussing how to fix this problem with me focused heavily on how we could reduce the time spent on this stages. We weren't really getting anywhere until my pair made the breakthrough suggestion that we move all the actions related to artifacts into a common build which the main build could feed into and the functional tests build could depend on. The functional tests build would still be able to get everything that it needed and we were able to reduce the time of the main build by around 50%.

A vindication for pair programming indeed, proving that there is great value in having someone in the role of navigator taking a look at the bigger picture and seeing the obvious things that the driver may miss.

Clearly there are fewer opportunities to partake in Developer/Non Developer pairing because the roles have different focuses. I think in this example it also helped that our QA previously worked as a Developer and was therefore already skilled in several of the aspects of pairing. Adding this ability to his focus on the testing aspect of the build allowed us to come up with a better solution than if we had put a Developer/Developer pair on the task.

It would be interesting to see if our effectiveness would have been less had I paired with a QA who had never paired before. However, I will certainly be looking for other opportunities on this project where the other developers and I can pair with the QA on other tasks.

I am also particularly interested in the idea of pairing with a BA. I have never paired with a BA before but identified a possibility of this on a previous project where business specifications were being written using <a href="http://www.concordion.org/">Concordion</a>. In this situation I felt it would be useful to have a Developer pair with the BA to write the assertions as this required deeper knowledge of HTML than a BA would be expected to have. We didn't get the chance to try it out on that project but I certainly hope to find the opportunity to pair with other non developers in the future.

It would be interesting to know if anyone has similar experiences with pairing.
