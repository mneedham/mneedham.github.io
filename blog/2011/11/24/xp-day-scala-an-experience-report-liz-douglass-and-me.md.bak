+++
draft = false
date="2011-11-24 23:52:18"
title="XP Day: Scala: An Experience Report (Liz Douglass and me)"
tag=['scala', 'xpday']
category=['XP Day']
+++

At XP Day my colleague <a href="http://twitter.com/lizdouglass">Liz Douglass</a> and I presented the following experience report on our last 6 months working together on our project.

<div style="width:425px" id="__ss_10314357"> <strong style="display:block;margin:12px 0 4px"><a href="http://www.slideshare.net/markhneedham/scala-an-experience-report" title="Scala: An experience report" target="_blank">Scala: An experience report</a></strong> <iframe src="http://www.slideshare.net/slideshow/embed_code/10314357" width="425" height="355" frameborder="0" marginwidth="0" marginheight="0" scrolling="no"></iframe> <div style="padding:5px 0 12px"> View more <a href="http://www.slideshare.net/" target="_blank">presentations</a> from <a href="http://www.slideshare.net/markhneedham" target="_blank">markhneedham</a> </div> </div>

We wanted to focus on answering the following questions with our talk:

<ul>
<li>Should the project have been done in Java?</li>
<li>Does it really speed up development as was hoped?</li>
<li>What features of the language and patterns of usage have been successes?</li>
<li>Is it easier to maintain and extend than an equivalent Java code base?</li>
</ul>

We covered the testing approach we've taken, our transition from using <a href="http://scalate.fusesource.org/documentation/mustache.html">Mustache</a> as our templating language to using <a href="http://scalate.fusesource.org/documentation/jade.html">Jade</a> and the different features of the language and how we've been using/abusing them.

The approach we used while presenting was to <strong>cover each topic in chronological order</strong> such that we showed how the code had evolved from June until November and the things we'd learned over that time.

It was actually an interesting exercise to go through while we were preparing the talk and I think it works reasonably well as it makes it possible to take people on the same journey that you've been on.

These were a few of the points that we focused on in the talk:

<ul>
<li>In our code base at the moment we have <strong>449 unit tests, 280 integration tests and 353 functional tests</strong> which is a much different ratio than I've seen on other code bases that I've worked on.

Normally we'd have way more unit tests and very few functional tests but a lot of the early functionality was transformations from XML to HTML and it was really easy to make a functional test pass so all the tests ended up there. 

Unfortunately the build time has grown in line with the approach as you might expect!</li>
<li>We originally started off using Mustache as our templating language but eventually switched to Jade because we were <strong>unable to call functions from Mustache templates</strong>. This meant that we ended up pushing view logic into our models.

The disadvantage of switching to Jade is that it becomes possible to put whatever logic you want into the Jade files so we have to remain more disciplined so we don't create an untestable nightmare.</li>
<li>On our team <strong>the most controversial language feature that we used was an implicit value</strong> which we created to pass the user's language through the code base so we could display things in English or German.

Half the team liked it and the other half found it very confusing so we've been trying to refactor to a solution where we don't have it anymore.

Our general approach to writing code in Scala has been to write it as Java-like as possible so that we don't shoot ourselves in the foot before we know what we're doing and it's arguable that this is one time when we tried to be too clever.</li>
<li>In the closing part of our talk we went through a <strong>code retrospective</strong> which we did with our whole team a couple of months ago.

In that retrospective we wrote down the things we liked about working with Scala and the things that we didn't and then compared them with a similar list which had been created during the project inception.

Those are covered on the last few slides of the deck but it was interesting to note that most of the expected gains were being achieved and some of the doubts hadn't necessarily materialised.</li>
</ul>

Our conclusion was that we probably would use Scala if we were to redo the project again, mainly because the data we're working with is all XML and the support for that is much better in Scala then in Java.

There is much less code than there would be in an equivalent Java code base but I think the maintenance of it probably requires a bit of time working with Scala, it wouldn't necessarily be something a Java developer would pick up immediately.

We're still learning how to use traits and options but they've worked out reasonably well for us. We haven't moved onto any of the complicated stuff such as what's in <a href="http://code.google.com/p/scalaz/">scalaz</a> and I'm not sure we really need to for a line of business application.

In terms of writing less code using Scala has sped up development but I'm not sure whether the whole finds Scala code as easy to read as they would the equivalent Java so it's debatable whether we've succeeded on that front.
