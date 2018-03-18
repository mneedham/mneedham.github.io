+++
draft = false
date="2009-12-23 07:27:51"
title="Duke Nukem Forever & Reworking code"
tag=['software-development']
category=['Software Development']
+++

<a href="http://twitter.com/offbytwo">Cosmin Stejerean</a> linked to a really interesting article on wired.com which tells the story of <a href="http://www.wired.com/magazine/2009/12/fail_duke_nukem/all/1">how Duke Nukem failed over 12 years to ship their latest game</a>, eventually giving up.

Phil has written a post about the article <a href="http://fragmental.tw/2009/12/22/duke-nukem-forever-and-magic-bags-of-money"> from the angle of his experience working with these types of companies and working out how to get something into production</a> but as I read this article it seemed to have some relation to reworking code and why/how we approach this.

It can be reworking of code through either <a href="http://blogs.agilefaqs.com/2009/12/22/rewrite-vs-refactor-dilemma/">rewriting or refactoring</a>, but the general idea is that it's not directly contributing to getting something released.

One particular bit of the article stood out to me as being particularly interesting - it describes how they decided to change from the Quake II game engine to the Unreal one:
<blockquote>
One evening just after E3, while the team sat together, a programmer threw out a bombshell: Maybe they should switch to Unreal? “The room got quiet for a moment,” Broussard recalled. Switching engines again seemed insane — it would cost another massive wad of money and require them to scrap much of the work they’d done.

But Broussard decided to make the change. Only weeks after he showed off Duke Nukem Forever, he stunned the gaming industry by announcing the shift to the Unreal engine. “It was effectively a reboot of the project in many respects,”
</blockquote>

What they effectively did here is to rip out a core bit of the architecture and totally change it which would be quite a difficult decision to make if you knew you had to deliver by a certain date. 

We've made that decision on projects that I've worked on but you have need to come up with a very compelling argument to do so i.e. typically that productivity will be much improved by making the change.

Whenever we talked about refactoring code during our technical book club <a href="http://intwoplacesatonce.com/">Dave</a> always pointed out that <a href="http://weblog.raganwald.com/2008/05/narcissism-of-small-code-differences.html">refactoring for the sake of doing so</a> is pointless which to an extent explains why it makes most sense to refactor either around the code that we're currently working on or <a href="http://fabiopereira.me/blog/2009/09/01/technical-debt-retrospective/">in the areas that are causing us most pain</a>.

For me <strong>the goal of refactoring code is to make it easier to work with or easier to change</strong> but it's useful to remember that we're refactoring to help us reach another goal.

An idea which I quite like (suggested by <a href="http://www.dtsato.com/blog/">Danilo</a>) but haven't tried yet is running technical retrospectives more frequently so that we can work out which areas of the code we need to work out for our current release and then make use of <a href="http://no-new-ideas.blogspot.com/2008/11/bowling-cards.html">Stuart Caborn's bowling card idea</a> to keep track of how much effort we've spent on these problems.

It seems like any refactorings we decide to do need to be linked to a common vision which we're trying to achieve and that seems to be where Duke Nukem went wrong. The vision of what was actually required for the game to be successful was lost and as many features as possible were added in.

The Duke Nukem approach seems quite similar to going through the code and making refactorings just to make the code 'better' even though we might not see any return from doing so.

In <a href="http://www.amazon.com/gp/product/193435628X?ie=UTF8&tag=marneesblo-20&linkCode=as2&camp=1789&creative=390957&creativeASIN=193435628X">Debug It</a> Paul Butcher suggests that we need to approach bugs in software with pragmatic zero tolerance by realising that while our aim is to have no bugs we need to keep sight of our ultimate goal while doing so.

I think we can apply the same rule when reworking code. We should look to write good code which is well factored and easy to change but realise that we'll never be able to write perfect code and we shouldn't beat ourselves up about it.
