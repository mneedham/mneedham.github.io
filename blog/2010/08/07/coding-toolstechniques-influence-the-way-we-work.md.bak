+++
draft = false
date="2010-08-07 13:14:05"
title="Coding: Tools/Techniques influence the way we work"
tag=['coding']
category=['Coding']
+++

Dave Astels mentions in his <a href="http://blog.daveastels.com/files/BDD_Intro.pdf">BDD paper</a> that the way we use language influences the way that we write code, quoting the <a href="http://en.wikipedia.org/wiki/Sapir-Whorf_hypothesis">Sapir-Whorf hypothesis</a>

<blockquote>
“there is a systematic relationship between the grammatical categories of the language a
person speaks and how that person both understands the world and behaves in it.”
</blockquote>

In a similar way, something which I didn't fully appreciate until the last project I worked on is how much the tools and techniques that you use can influence the way that you work.

<h3>Distributed Source Control</h3>
<a href="http://christianralph.blogspot.com">Christian</a> persuaded the client to allow us to use Mercurial for the project and it was interesting to see how we almost instinctively moved to a style of development which involved checking in much more frequently than we would have had we used Subversion.

There were still times when we'd end up working on something locally for too long but it seemed to become much more visible when this was happening and the endless ribbing that a pair got when they hadn't checked in for a while ensured that it didn't last for long.

I'm sure there are ways that we could have used Mercurial even more effectively than we did and my current thinking is that by default we'd want to use a distributed source control tool over any other.

<h3>Incremental refactoring</h3>

<a href="http://www.markhneedham.com/blog/category/coding/incremental-refactoring/">Incremental refactoring</a> is a concept that <a href="http://intwoplacesatonce.com/">Dave Cameron</a> introduced me to about a year ago and it's been talked about recently by <a href="http://www.infoq.com/presentations/responsive-design">Kent Beck</a> and <a href="http://www.markhneedham.com/blog/2010/07/05/the-limited-red-society-joshua-kerievsky/">Joshua Kerievsky</a>.

The underlying idea is that we know we want to drive our code in a certain direction but we want to do so in a way that doesn't leave our code base in a broken state while we're working towards that.

The techniques these two describe help to remove the fear and paralysis that we can often feel when we want to change a significant part of the code but know that we don't have the time to do that all at once.

<h3>Not copying and pasting tests</h3>

I've previously mentioned a post Ian Cartwright wrote a while ago where he suggested that we should <a href="http://iancartwright.com/blog/2009/04/test-code-is-just-code.html">treat test code the same way that we treat production code</a>, along the way pointing out that this meant copy/pasting tests was not the way to go.

I gave the non copy/paste approach a try last year and an interesting thing that I noticed is that when you have to type out the same types of things repeatedly you become much more aware of the duplication that you're creating and since it's costing time doing so you quickly look for ways to improve the situation.

Once we've got our tests cut down to the stage where removing any more duplication would also remove the intent of the test it doesn't seem too bad to copy the outline of tests and then change the details.

We probably can move slightly faster by using copy/paste at this stage rather than writing everything out but the amount of time saved as a total of all development effort is minimal.

I think avoiding copy/paste puts us in a much more resourceful mindset and allows us to see improvements that we otherwise wouldn't see and this it the real benefit of this technique.

Alan Skorkin has <a href="http://www.skorks.com/2010/04/a-fizzbuzz-faux-pas/">a cool post from a few months ago where he talks about the benefit of thinking about the code we're writing rather than just going into auto pilot</a> which covers similar ground.

<h3>Living prototypes</h3>
This is an idea that we used on my last project <a href="http://christianralph.blogspot.com/2010/06/living-prototypes.html#comments">whereby we had a prototype of the website being developed alongside the real version</a>.

This approach was necessary for this particular client but I really like the idea of having the real UI being developed alongside the code as it meant that whenever we showcased what we'd done to the client it was actually exactly what the final product would look like.

On previous projects we've often driven out the back end code and then styled it later which leads to a lot of questions about the UI when showcasing which may not actually be relevant when it's properly skinned. 

It also helped avoid the redundancy of showcasing something twice - once early on with just the functionality and then later on after the styling has been applied.


