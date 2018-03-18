+++
draft = false
date="2011-01-19 17:46:39"
title="Coding: Spike Driven Development"
tag=['coding']
category=['Coding']
+++

While reading <a href="http://dannorth.net/2011/01/15/on-craftsmanship/">Dan North's second post about software craftsmanship</a> I was able to resonate quite a lot with a point he made in the 'On value' section:

<blockquote>
I’m not going to mandate test-driving anything (which is a huge about-face from what I was saying a year ago), unless it will help. Copy-and-paste is fine too. (Before you go all shouty at me again, hold off until I blog about the benefits of copy-and-paste, as it appears in a couple of patterns I’m calling <em>Spike and Stabilize</em> and <em>Ginger Cake</em>. You might be surprised.)
</blockquote> 

I've been finding that quite frequently with some of the problems I've worked on recently that we haven't known exactly how to solve it when we started and ended up hacking/spiking the code quite a bit at that stage until we figured out what we needed to do.

Dan replied with <a href="http://twitter.com/tastapod/status/26401996319760385">the following on twitter</a> when I mentioned this to him:

<blockquote>
@markhneedham kind of deliberately discovering the best way forward by actively reducing your ignorance? hmm, might catch on...
</blockquote>

He wrote about this a few months ago in a post titled '<a href="http://dannorth.net/2010/08/30/introducing-deliberate-discovery/">Introducing Deliberate Discovery</a>'.

I nearly always feel pretty bad when I take this approach because I'm not TDDing code which easily be written using that style.

The reason I don't is that it slows me down when I'm in discovery mode.

I could TDD what I <strong>think</strong> the code needs to look like and end up with nice looking code which doesn't actually solve the problem but that seems to miss the point.

Another approach could be to drive from a higher level by using cucumber or a similar tool but that always ends up being quite fiddly from my experience and again it slows down the discovery that I want to make.

We had a recent example of this while trying to work out how to display the next part of a page we were working on.

Our initial approach was to make an AJAX call to the server and get back a JSON representation of our resource which we could render on the page.

While implementing this approach we realised that there were already a some post backs being made to the server from various other parts of the page which resulted in the page being refreshed.

We initially thought that this would mean that we could use the data being passed to the view on those post backs to do what we wanted.

We kept a copy of our original code and then started trying to implement what we thought would be a simpler solution.

Unfortunately after  playing around with that approach for a few hours we realised that it wasn't going to work because loading the data that way led to another part of the page getting completely screwed up.

We therefore ended up back at the first approach again.

One side effect of taking that second approach was that eventually the logic got too complicated for us to verify that what we had written was correct just by eye balling it.

We therefore slowed down a bit and TDD'd the code so that we could document our understanding of what was supposed to happen.

<a href="http://cleancoder.posterous.com/software-craftsmanship-things-wars-commandmen">Uncle Bob wrote a reply</a> to Dan a couple of days ago in which he ends with the following:

<blockquote>
So when you see someone wearing a green wrist-band that says "Clean Code" or "Test First" or "Test Obsessed"
...

<em>It's a promise made to one's self:  "I will do a good job.  I will not rush.  I will write tests.  I will go fast by going well.  I will not write crap. And I will practice, practice practice so that I can be a professional."</em>
</blockquote>

The code I'm writing during the time when I'm discovering what I need to do certainly isn't clean or test first but it is part of an attempt to allow me to figure out what to do in order to go faster.

I'm more used to taking the approach I've described when explicitly working on 'spikes' or '<a href="http://rethrick.tumblr.com/post/1677240946/experimenting-with-agile-at-google">experiments</a>' but in a way what we've done is perhaps closer to <a href="http://www.markhneedham.com/blog/2009/09/19/set-based-concurrent-engineering-a-simple-example/">concurrent set based engineering</a>.

I think the skill I still quite haven't got right is realising when I've taken the spiking/hacking too far and would benefit from going and TDDing a bit of code but I'm sure I'll figure it out with practice.
