+++
draft = false
date="2008-10-25 01:55:18"
title="Selenium - Selecting the original window"
tag=['testing', 'selenium']
category=['Testing']
+++

I've not used <a href="http://selenium.openqa.org/">Selenium</a> much in my time - all of my previous projects have been client side applications or service layers - but I've spent a bit of time getting acquainted with it this week.

While activating some acceptance tests this week I noticed quite a strange error happening if the tests ran in a certain order:


~~~text

com.thoughtworks.selenium.SeleniumException: ERROR: Current window or frame is closed! 
at com.thoughtworks.selenium.HttpCommandProcessor.doCommand(HttpCommandProcessor.java:73)
at com.thoughtworks.selenium.HttpCommandProcessor.getString(HttpCommandProcessor.java:154)
at com.thoughtworks.selenium.HttpCommandProcessor.getBoolean(HttpCommandProcessor.java:227)
at com.thoughtworks.selenium.DefaultSelenium.isElementPresent(DefaultSelenium.java:394)
~~~

I tried commenting out some of the tests and then running the other ones and everything worked fine but when I ran all of them the problem returned. 

Eventually after some eagle eyed debugging by a colleague of mine we realised that the only difference was the lack of the following line in the failing test:


~~~java

selenium.selectWindow(null);
~~~

A quick look at the <a href="http://release.openqa.org/selenium-remote-control/0.9.2/doc/java/">documentation</a> explains precisely why this works:

<blockquote>
if windowID is null, (or the string "null") then it is assumed the user is referring to the original window instantiated by the browser).
</blockquote>

What had in fact happened was that the previous test had launched a pop up window and when it closed that window the focus wouldn't return to the original window launched when Selenium first started unless we executed the above method call.

