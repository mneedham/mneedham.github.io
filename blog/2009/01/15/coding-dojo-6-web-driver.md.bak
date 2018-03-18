+++
draft = false
date="2009-01-15 00:37:24"
title="Coding Dojo #6: Web Driver"
tag=['coding-dojo']
category=['Coding Dojo']
+++

We ran a sort of coding dojo/more playing around with <a href="http://code.google.com/p/webdriver/">web driver</a> learning session this evening, coding some tests in Java driving <a href="http://blogs.thoughtworks.com/">Planet TW</a> from the code.

<h3>The Format</h3>
We had the same setup as for our normal coding dojos but only one person was driving at a time and the others were watching from around them offering tips on different approaches.  I think only a couple of us drove during the session.

<h3>What We Learnt</h3>

<ul>
<li>
This was an interesting way to start learning about a tool that I hadn't previously used. Two of my colleagues had used it before and they were able to provide knowledge of best practices, such as the <a href="http://code.google.com/p/webdriver/wiki/PageObjects">Page Object</a> pattern. I finally got the value in this pattern today after seeing the way that we can use the <a href="http://code.google.com/p/webdriver/wiki/PageFactory">PageFactory</a> to help cut out a lot of the boiler plate code usually needed to get the elements on each page into a class.
</li>
<li>Web Driver seems to be <strong>simpler to setup than Selenium</strong> from my experiences tonight. We don't have to worry about the reverse proxy like we do when using Selenium which makes things much easier. The tests, especially when using the Html Unit driver, ran fairly rapidly.</li>
<li>We worked with the Safari driver for most of the time but had to put in a lot of sleeps because the calls to pages didn't seem to wait for that page to load before going onto the next step. A quick browse of the mailing list suggests that this is an area that will be worked on soon. The Html Unit Driver worked really well though.</li>
<li>I learnt about the idea of <a href="https://lift.dev.java.net/">LiFT style APIs</a> - we can write web driver tests in this style by using the correct context wrapper. Effectively an acceptance testing DSL:

<blockquote>
LiFT allows writing automated tests in a style that makes them very readable, even for non-programmers. Using the LiFT API, we can write tests that read almost like natural language, allowing business requirements to be expressed very clearly. This aids communication amongst developers and customers, helping give all stakeholders confidence that the right things are being tested. 
</blockquote>
 </li>
<li><a href="http://lizdouglass.wordpress.com/">Liz</a> mentioned an earlier discussion she had been having around the creation of strings using literals ("string") or by using the constructor (new String("string)). The latter is not encouraged as those strings are not put into the string pool and therefore cannot be reused. There is more discussion of the two approaches to creating strings on the <a href="http://www.coderanch.com/t/381271/Java-General-intermediate/Difference-between-String-s-Marcus">Code Ranch forums</a> and on <a href="http://weblogs.java.net/blog/enicholas/archive/2006/06/all_about_inter.html">Ethan Nicholas' blog</a>.</li>
</ul>

<h3>Next Time</h3>

<ul>
<li>Next week we are going to explore the <a href="http://code.google.com/p/retlang/wiki/">Retlang</a> concurrency library. I think the plan is to take a concurrency problem and try to solve it with the library. </li>
<li>I'm still not sure how well the Dojo format works for learning or exploring things that are new to most of the group. This week's one certainly wasn't as intense as last week's although I still learnt about things that I previously didn't know about.</li>
</ul>
