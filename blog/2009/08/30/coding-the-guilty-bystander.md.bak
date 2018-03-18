+++
draft = false
date="2009-08-30 20:07:50"
title="Coding: The guilty bystander"
tag=['coding']
category=['Coding']
+++

While discussing the <a href="http://www.markhneedham.com/blog/2009/08/30/coding-group-the-duplication-then-remove-it/">duplication in our code based which I described in an earlier post</a> with some other colleagues earlier this week I realised that I had actually gone past this code a couple of times previously, seen that there was a problem with it but hadn't taken any steps to fix it other than to make a mental note that I would fix it when I got the chance.

At the time we needed to fix a bug around this code and noticed that the logic was scattered all around the place but decided to just add to the mess and put our fix in without refactoring the code to make it better for people coming to the code in future.

In a way then it was perhaps <a href="http://en.wikipedia.org/wiki/Poetic_justice">poetic justice</a> that when the bug was re-tested there were still problems with it.

This time we decided to fix it properly and with the improved expressiveness the code now has hopefully it will make life easier for other people who have to work with the code.

I think this was also a really clear case of the broken windows theory whereby the likelihood of someone doing something bad to the code is much higher if it's already in a suboptimal state.

After hearing me describe this <a href="http://blog.halvard.skogsrud.com/">Halvard</a> pointed out that it sounded quite like the idea of the <a href="http://www.fordhamlawandculture.org/blog/2008/11/23/we-didnt-do-anything/">guilty bystander</a> whereby <strong>if you see a problem with the code and do nothing about it then you are guilty by association even though it wasn't you who wrote it</strong>.

This sounds quite similar to a post written by Ayende where he pointed out that <a href="http://ayende.com/Blog/archive/2009/08/18/code-ownership-also-mean-code-responsibility.aspx">if you own the code then it is your responsibility to keep it in good shape</a>, you can't keep blaming the previous owners forever. 

Another colleague of mine, Silvio, pointed out that sometimes it might not be feasible for us to stop doing what we're doing to go and fix something else, especially if it's unrelated code that we just happen to come across. Indeed doing this might lead to a <a href="http://www.markhneedham.com/blog/2008/10/25/dont-shave-the-yak-ask-why-are-we-doing-this/">yak shaving</a> situation. 

In this situation he suggested that we need to let it be known that something should be done possibly by writing a 'TODO' comment in capital letters around the offending code so that the next person who comes across the code can take a look at the offending code without having to assess whether or not it's in a bad state.

To continue the analogy perhaps this would be the equivalent of calling 999/911/000 to report the situation to the police which is definitely better than just ignoring the problem although not as good as helping to solve it. 

In this case the help you're providing is a bit more indirect than calling the emergency services would be so I'm not sure if the metaphor quite fits!

There are certainly exceptions (such as when we inherit code which is a mess) but in general I always think we've gone horribly wrong when we get to the stage where we need to ask the business whether we can have a whole iteration (or more) to refactor the code into shape so that we can start moving faster again.

I believe that while in the short term it's our responsibility to make sure we deliver the features we're working on in the current iteration, we also need to make sure that we spend some time ensuring that we can continue to deliver features in future iterations as well and part of that second responsibility is taking the time to mould code into a state where we can build on top of it more easily even if it wasn't us who wrote it in the first place.
