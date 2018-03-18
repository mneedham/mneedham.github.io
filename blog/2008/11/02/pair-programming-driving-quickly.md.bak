+++
draft = false
date="2008-11-02 22:13:33"
title="Pair Programming: Driving quickly"
tag=['pairing', 'pair-programming']
category=['Pair Programming']
+++

In order to experience the full benefits of pair programming it is important to try and reduce the chance of the navigator getting bored and losing focus.

One of the main ways that we can do this is by ensuring that we have a quick turnaround between the driver and navigator, and this can be done by ensuring that when we are driving we are doing so as quickly as possible.

There are three areas that come to mind where we can gain speed improvements when driving in a pair programming session:

<h3>IDE shortcuts</h3>
Learning the IntelliJ shortcuts was one of the first things that I was encouraged to do on the first Java project that I worked on at ThoughtWorks.

I found the most effective way for me was if my pair pointed out potential shortcuts whenever I was using the mouse to try and do something. On my current project we have installed an IntelliJ plugin called <a href="http://plugins.intellij.net/plugin/?id=1003">Key Promoter</a> which pops up a message telling you the shortcuts every time you use one of the menu options. I learnt about this plugin from Neal Ford's book, <a href="http://www.markhneedham.com/blog/2008/09/05/the-productive-programmer-book-review/">The Productive Programmer</a>.

Additionally there are PDFs available, which list every single shortcut available for the various different platforms, on the <a href="http://www.jetbrains.com/idea/documentation/documentation.html">IntelliJ documentation page</a>.

The same applies whether we are using TextMate, Visual Studio + Resharper or any other IDE. Knowing the shortcuts allows you to execute tasks more quickly and (for me at least) also has the benefit of making you feel more confident about what you are doing.


<h3>IDE templates/Plug ins</h3>

Setting up templates for frequent operations is another useful way to save time.

In particular I find it especially wasteful to write out the code to define a JUnit test every time so I always create a <a href="http://intelligentsoftwareengineering.blogspot.com/2006/09/intellij-live-templates.html">template</a> which does this for me. 

IntelliJ also provides a set of built in templates for creating simple code snippets - accessible by using the Command + J keyboard shortcut on the Mac or Ctrl + J on Windows.

In addition we can install plugins which help us to be more productive. <a href="http://plugins.intellij.net/plugin/?id=96">TestDox</a> is one such plug in for IntelliJ which allows you to create the test class for any class with one keyboard shortcut. We can then switch between the test and the code using the same shortcut.

For Ruby, <a href="http://code.leadmediapartners.com/2008/3/28/rubyamp">RubyAmp</a> is a TextMate plugin which I have come across which adds class, method and whole project searching for Ruby code.

<h3>The Shell</h3>

Using the shell or command line effectively is another way that we can can speed improvements.

I wrote about <a href="http://www.markhneedham.com/blog/2008/10/15/browsing-around-the-unix-shell-more-easily/">some of the ways I have learnt for doing this</a> and several people provided other suggestions in the comments on the post, but the key pattern here seems to be to <strong>reduce the amount of typing</strong> and <strong>avoid repetition</strong>. It's all about <a href="http://jchyip.blogspot.com/2008/10/copy-and-paste-once-never-copy-and.html">reducing duplication of effort</a> when it comes to using the shell effectively.

Often when using the shell we want to reuse some of the commands that we have entered previously.

I was aware of two ways of doing this until last week - using the up and down arrows to go through the history and searching through the history using Ctrl + R.

A third way I learnt last week was to type the following command into the shell:


~~~text

history
~~~

This returns the list of items that we have previously searched for:


~~~test

 533  man grep
 534  grep -r "JarTask" *.*
 535  grep -r "JarTask" .
 536  cd java/
~~~

A <a href="http://lizdouglass.wordpress.com/">colleague</a> showed me that we can repeat these commands by typing '![NumberOfCommand]'. To repeat the 'man grep' command we would type the following:


~~~text

!533
~~~

Spotting patterns of repetition is also useful. For example, to redeploy our application for manual CSS testing we had several steps which involved stopping Tomcat, redeploying our WAR, updating the database and then restarting the database. 

This involved 4 separate commands until one of my colleagues put it all together into a simple 'restart' script. Quite a simple idea but it reduces human effort.

<h3>Overall</h3>

These are some of the ways that I have noticed where we can make pair programming go more smoothly and keep both people on the pair engaged. 

The common theme is that we should <strong>make our tools do the work</strong> and save our time for thinking.
