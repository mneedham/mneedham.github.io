+++
draft = false
date="2008-12-09 21:13:21"
title="Javascript: Creating quick feedback loops"
tag=['javascript', 'feedback-loops', 'jquery']
category=['Software Development', 'jQuery']
+++

I've been working quite a lot with Javascript and in particular <a href="http://jquery.com/">jQuery</a> recently and since I haven't done much in this area before all the tips and tricks are new to me.

One thing which is always useful no matter the programming language is to use it in a way that you can get rapid feedback on what you are doing.

Fortunately there are quite a few tools that allow us to do this with Javascript:

<h3>Firebug</h3>
The <a href="http://getfirebug.com/">Firefox plugin</a> is perhaps the quickest way of getting feedback on anything Javascript and indeed CSS related.

The ability to see which HTTP calls have been made on a page is invaluable for checking whether AJAX functionality is working correctly and DOM manipulation can be executed and tested on the fly.

Including jQuery in a page effectively makes Firebug the jQuery Interactive Console, allowing us to try out the different functions and see their effects immediately.

<h3>Unit Testing Frameworks</h3>
There are several javascript unit testing frameworks around at the moment which run in the browser and provide the ability to write assertions on our code.

I have been using <a href="http://docs.jquery.com/QUnit">QUnit</a> and <a href="http://github.com/nkallen/screw-unit/tree/master">screw-unit</a> and while they work reasonably well for simple tests, neither seems to be at the level of JUnit or NUnit for example. I'm sure this will come as they mature.

Other frameworks I've heard about but not tried: <a href="http://code.google.com/p/rhinounit/">RhinoUnit</a>, <a href="http://www.valleyhighlands.com/testingframeworks/">JSNUnit</a>, <a href="http://www.jsunit.net/">JSUnit</a>, no doubt there are others I haven't heard about yet.

<h3>Selenium IDE</h3>

The <a href="http://seleniumhq.org/projects/ide/">sometimes forgotten Firefox plugin</a> is very useful for quickly creating repeatable scenarios to see the impact that code changes have had.

The beauty of this approach is that it takes out the manual steps in the process, so we can just make our changes and then re-run the test. The runner lights up green or red, taking out the need to manually verify the correctness of our assertions.<br />

<h3>Alert</h3>
The <a href="http://www.mediacollege.com/internet/javascript/basic/alert.html">'alert'</a> function is perhaps most useful when we want to quickly verify the path being taken through a piece of code without having to step through it using the Firebug debugger.

It's probably more useful for proving our assumptions than actual debugging and it's certainly quick and easy to set up.
