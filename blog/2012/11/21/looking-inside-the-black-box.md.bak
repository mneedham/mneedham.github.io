+++
draft = false
date="2012-11-21 19:42:15"
title="Looking inside the black box"
tag=['software-development']
category=['Software Development']
+++

I recently came across a <a href="http://angeleah.com/blog/2012/11/02/black-box-abstraction.html">really interesting post about black box abstraction</a> by Angeleah where she talks about developers desire to know how things work and the need to understand when and when not to follow that instinct.

Angeleah defines black box abstraction like so:

<blockquote>
It is a technique for controlling complexity and abstracting detail. The point of doing this is to allow you to to build bigger things. Hopefully bigger boxes. This is done all the time in methods or functions, in gems, in frameworks. 
</blockquote>

We have to be particularly careful about knowing how far to look inside the black box when working with new systems that we know nothing about. 

About a year ago my colleague <a href="http://www.linkedin.com/pub/alex-harin/13/40b/716">Alex Harin</a> and I were looking through the code of a pricing engine of one of our clients and our goal was to try and work out how we'd be able to wire in a replacement for some parts of it. 

In Michael Feathers' terminology we were looking for the <a href="http://www.markhneedham.com/blog/2009/06/21/seams-some-thoughts/">application's seams</a>.

We knew that configurations weren't being priced in real time because we'd watched a training video explaining that. We were therefore led to believe that the application had some mechanism for queuing up configurations and then pricing them.

We worked out an entry point into the application and then started drilling down to figure out how exactly this was being done. 

After a little bit of time it became clear that when Alex was driving we were starting to understand how the application was designed and when I was driving we were going down a lot of black holes.

When I asked him to explain to me what he was doing he explained that he was <a href="http://www.markhneedham.com/blog/2011/12/29/reading-code-know-what-youre-looking-for/">pattern matching the code against application design patterns that he'd seen previously</a> and was therefore quickly able to rule out bits of code that were irrelevant.

This is a skill which obviously improves with experience but it's still something to keep in mind even if you've only programmed for a few years as you are bound to have come across a range of different designs either at work or in open source software - knowledge which can be used when looking at new systems.

In Angeleah's post she suggests the following technique to work out when we're going down the rabbit hole which seems very sensible:

<blockquote>
you should ask yourself to what level you need to know that information and if knowing it at this point in time will truly help you with what you are working on. 
</blockquote>

I think it's especially difficult to know the answer to this question when you're less experienced and I'm certain that I spent much more time going down black box dead ends a few years ago than now.

If you <strong>can't remember why you're in a specific bit of code anymore</strong> then it's a good sign that you've strayed off the path and would be better off stepping a few levels up the stack to check whether the current black box expedition is worthwhile.

Having said that, when you do decide you want to go and look inside the black box I find that while it's important to keep the big picture in mind <strong>sometimes it is necessary to carefully read each line of code rather than skimming over it</strong>. 

This is something that <a href="http://twitter.com/jennifersmithco">Jen</a> and I have found particularly true when looking at the implementations of machine learning algorithms in <a href="http://mahout.apache.org/">Mahout</a>. In that case we've been switching between the code and a textual description of what the algorithm is actually supposed to do to check our understanding.

Looking back at this post I realise that while there are a couple of techniques here that can help us to reflect on what we're doing it does seem to be one of those areas of software development that is based on gut feel more than anything else.
