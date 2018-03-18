+++
draft = false
date="2011-07-23 12:05:05"
title="Scala: Making it easier to abstract code"
tag=['software-development']
category=['Scala']
+++

A couple of months ago I attended <a href="http://www.markhneedham.com/blog/2011/05/11/xp-2011-michael-feathers-brutal-refactoring/">Michael Feathers' 'Brutal Refactoring' workshop</a> at XP 2011 where he opined that <strong>developers generally do the easiest thing when it comes to code bases</strong>.

More often than not this means adding to an existing method or existing class rather than finding the correct place to put the behaviour that they want to add.

Something interesting that I've noticed so far on the project I'm working on is that so far <strong>we haven't been seeing the same trend</strong>.

Our code at the moment is comprised of lots of little classes with small amounts of logic in them and I'm inclined to believe that Scala as a language has had a reasonable influence on that.

The following quote from '<a href="http://soft.vub.ac.be/~tvcutsem/whypls.html">Why programming languages?</a>' sums it up quite well:

<blockquote>
Sometimes the growing complexity of existing programming languages prompts language designers to design new languages that lie within the same programming paradigm, but with the explicit goal of minimising complexity and maximising consistency, regularity and uniformity (in short, conceptual integrity).
</blockquote>

It's incredibly easy to pull out a new class in Scala and the amount of code required to do so is minimal which seems to be contributing to the willingness to do so.

At the moment nearly all the methods in our code base are one line long and the ones which aren't do actually stand out which I think psychologically makes you want to find a way to keep to the one line method pattern.

<h4>Traits</h4>

As I've mentioned previously we've been <a href="http://www.markhneedham.com/blog/2011/07/09/scala-traits-galore/">pulling out a lot of traits</a> as well and the only problem we've had there is ensuring that we don't end up testing their behaviour multiple times in the objects which mix-in the trait.

I tend to pull traits out when it seems like there might be an opportunity to use that bit of code rather than waiting for the need to arise.

That's generally not a good idea but it seems to be a bit of a trade off between making potentially reusable code discoverable and abstracting out the wrong bit of code because we did it too early. 

<h4>Companion Objects</h4>

The fact that we have <a href="http://www.markhneedham.com/blog/2011/07/23/scala-companion-objects/">companion objects</a> in the language also seems to help us push logic into the right place rather than putting it into an existing class.

We often have companion objects which take in an XML node, extract the appropriate parts of the document and then instantiate a case class object.

<h4>In Summary</h4>

There's no reason you couldn't achieve the same things in C# or Java but I haven't seen code bases in those languages evolve in the same way.

It will be interesting to see if my observations remain the same as the code base increases in size.
