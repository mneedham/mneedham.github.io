+++
draft = false
date="2008-11-09 21:55:17"
title="Debugging 3rd party libraries more effectively"
tag=['debugging']
category=['Software Development']
+++

Debugging 3rd party library code quickly and effectively is one of the skills which most obviously separates Senior and Junior developers from my experience.

From observation over the last couple of years there are some patterns in the approaches which the best debuggers take.

<h3>Get more information</h3>

Sometimes it's difficult to understand exactly how to solve a problem without getting more information.

Verbose logging mode is available on the majority of libraries and provides the information showing how everything fits together which is normally enough information to work out how to solve the problem.

<h3>Look at the source code</h3>

My natural approach, when stuck using a 3rd party library for example, is to read the documentation but I have noticed that better debuggers than myself head to the source code much earlier and try to work out  what is going on from there.

This approach certainly makes sense and when I have problems with project code my instinct is to look at the offending code straight away and try to work out what's going on. I haven't quite got this discipline when it comes to library code just yet.

The art of this approach comes in being able to read through the code and realising quickly which parts of the code are important and which can be skimmed over. 

An article I read about the <a href="http://www.sciam.com/article.cfm?id=the-expert-mind">expert mind</a> seems to confirm this, stating that an expert in any discipline doesn't analyse more options than others, only better ones.

<h3>Don't assume it works</h3>
Closely linked to the above is the assumptions we make when debugging. 

The best debuggers don't assume that the code does exactly what they expect it to, they take a more critical approach and try to work out whether or not it is actually working by changing small things and seeing what the impact is.

If it does turn out that there is a bug then we can look at the source code and work out whether there is a way around the problem or if there is only one way to solve the problem, submit a patch to fix it.

<h3>One change at a time</h3>
I think this is probably the most important yet the simplest of the approaches.

It sounds so obvious yet it's so easy to make change after change after change and eventually solve the problem but have no idea which change or combination of changes it was that fixed it.

We need to ensure that we know why we are making each change and revert it if it doesn't have the desired effect.

<h3>Read the error message</h3>

Reading the error messages that we get and not the error message that we think we saw is yet another obvious approach but one which I have certainly violated.

Sometimes we need to slow down a bit when debugging problems and read exactly what the message is telling us and work from there.

<h3>In Summary</h3>

Most of the approaches I've noticed seem very obvious but I find that it requires quite a lot of discipline to apply them. When I do approach debugging with this more logical approach problems become much easier to solve.

<h4>Some debugging books</h4>

One of the best books I have read with regards to debugging code is <a href="http://www.amazon.co.uk/Debugging-David-J-Agans/dp/0814474578/ref=sr_1_3?ie=UTF8&s=books&qid=1225801432&sr=8-3">Debugging - The 9 Indispensable Rules for Finding Even The Most Elusuive Software and Hardware Problems</a> - I actually had the 9 rules stuck to my machine for a couple of months earlier this year, and probably should do that again. 

I also noticed that the Pragmatic Programmers have a new book coming out called '<a href="http://www.pragprog.com/titles/pbdp/debug-it">Debug It</a>' - it will be interesting to see the similarities and differences between this book and the other one.
