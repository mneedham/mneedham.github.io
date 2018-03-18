+++
draft = false
date="2011-11-28 00:15:00"
title="Scala: Our Retrospective of the benefits/drawbacks"
tag=['scala']
category=['Scala']
+++

As the closing part of a <a href="http://www.markhneedham.com/blog/2011/11/24/xp-day-scala-an-experience-report-liz-douglass-and-me/">Scala Experience Report</a> <a href="http://twitter.com/#!/lizdouglass">Liz</a> and I gave at XP Day we detailed a retrospective that we'd carried out on the project after 3 months where the team outlined the positives/negatives of working with Scala.

The team members who were there right at the beginning of the project 3 months earlier had come up with what they thought the proposed benefits/drawbacks would be so it was quite interesting to look at our thoughts at both times.

Some of this is available in our slides from the talk but <a href="http://twitter.com/natpryce">Nat Pryce</a> suggested it'd be interesting to post it up in more detail.

We weren't aware that we'd be doing this exercise until the session where we did it and noone looked at the original answers so hopefully some of the potential biases have been removed!

<h4>JUNE</h4>

<ul>
<li>
+++ Increased developer productivity
<ul>
<li>Higher-level language constructs (functional programming, actors, pattern matching, mixins, etc.)</li>
<li>Less code -> less time spent reading code / less defects</li>
<li>Syntax is better suited for writing DSLs (e.g. SBT, Scalatra, ScalaTest, etc.)</li>
</ul>
</li>
<li>+++ Bigger potential to attract talented developers (not using the same old 'boring' stack)</li>
<li>++  Gentle learning curve for Java devs</li>
<li>+   Built-in support at language-level for handling XML</li>
<li>+   Comes with SBT, a powerful build tool</li>
<li>+   Seamlessly integrates with Java and it's ecosystem</li>
<li>+   Runs on the JVM (i.e. no operational concerns)</li>
</ul>

<ul>
<li>--- Bigger potential to screw things up (think: "with great power comes...")</li>
<li>--  Tool support is less mature and polished (e.g. IDEs, profilers, metrics, etc.)</li>
<li>-   Community is younger and smaller</li>
<li>-   Scala compiler seems to be slower than Java counterparts</li>
</ul>


<h4>SEPTEMBER</h4>

Liked:
<ul>
<li>+8 Easy to learn</li>
<li>+8 Functional Language (Immutable, closures, etc)</li>
<li>+6 Concise code</li>
<li>+5 SBT power</li>
<li>+4 Case classes</li>
<li>+4 XML support</li>
<li>+4 Java integration</li>
<li>+3 List processing</li>
<li>+3 DSL support</li>
<li>+2 Helpful community (IRC, StackOverflow)</li>
<li>+2 Performance</li>
</ul>

Disliked:
<ul>
<li>-8 IDE support (refactoring, plugin quality)</li>
<li>-5 Slow compiler</li>
<li>-3 Code can become complex to read</li>
<li>-2 Lack of XPath support in XML</li>
<li>-2 SBT complexity</li>
<li>-2 Immature frameworks</li>
</ul>

Quite a few of the expected benefits from June were observed in June, such as having to write less code, functional programming constructs, XML support and the ability to write DSLs.

The community was one benefit which wasn't expected - we've found that every time we get stuck on something we can go on Stack Overflow and find the answer and if that doesn't work then someone on IRC will be able to help us almost immediately.

<h4>Complexity</h4>

Our experience with Scala's complexity <a href="http://blog.joda.org/2011/11/scala-feels-like-ejb-2-and-other.html">partly matches with that of Stephen Coulbourne</a> who suggests the following:

<blockquote>
Scala appears to have attracted developers who are very comfortable with type theory, hard-core functional programming and the mathematical end of programming.

...

There is also a sense that many in the Scala community struggle to understand how other developers cannot grasp Scala/Type/FP concepts which seem simple to them. This sometimes leads Scala aficionados to castigate those that don't understand as lazy or poor quality developers.
</blockquote>

We've tried to be reasonably sensible with the language and only used bits of it that the whole team are likely to understand rather than learning some obscure way of solving a problem and checking that in.

On the other hand reading the code of Scala libraries such as <a href="https://github.com/scalaz/scalaz">scalaz</a> or <a href="https://github.com/harrah/xsbt">SBT</a> is something that I, at least, find extremely difficult.

Changing the SBT build files can be quite a scary experience while you try and remember what all the different symbols mean and how they integrate together.

<h4>Learning curve</h4>

The learning curve for Java developers has been a bit of a mixed experience. 

When we started working on the project we were effectively writing Java in Scala and we've slowly learnt/introduced more Scala features into our code as time has passed.

I think everyone who has come on that journey has found the transition reasonably okay but we've had other team members who joined later on and went straight into code that they weren't familiar with and for them it's been more difficult.

<h4>Again, again!</h4>

It will be interesting to see the team's thoughts if we do the exercise again 3 more months on.

I would imagine there would be more 'dislikes' around code complexity now that the code has grown even more in size.

It probably also mean the lack of IDE support becomes more annoying as people want to refactor code and can't get the seamless experience that you get when editing Java code.
