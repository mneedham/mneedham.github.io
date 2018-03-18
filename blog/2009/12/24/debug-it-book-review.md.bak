+++
draft = false
date="2009-12-24 05:26:46"
title="Debug It: Book Review"
tag=['books', 'debugging']
category=['Books']
+++

David Agans' '<a href="http://www.amazon.com/gp/product/0814474578?ie=UTF8&tag=marneesblo-20&linkCode=as2&camp=1789&creative=390957&creativeASIN=0814474578">Debugging</a>' is the best debugging book that I've read so I was intrigued to see that there was another book being written on the subject. 

Paul Butcher offered me a copy of the book to review so I was keen to see whether it was more like 'Debugging' or '<a href="http://www.amazon.com/gp/product/0978739213?ie=UTF8&tag=marneesblo-20&linkCode=as2&camp=1789&creative=390957&creativeASIN=0978739213">Release It</a>' <a href="http://blogs.tedneward.com/2009/11/23/Book+Review+Debug+It+Paul+Butcher+Pragmatic+Bookshelf.aspx">as Ted Neward suggests</a>.

<h3>The Book</h3>

<a href="http://www.amazon.com/gp/product/193435628X?ie=UTF8&tag=marneesblo-20&linkCode=as2&camp=1789&creative=390957&creativeASIN=193435628X">Debug It</a> by Paul Butcher

<h3>The Review</h3>

<a href="http://devlicio.us/blogs/krzysztof_kozmic/archive/2009/08/30/book-review-debug-it-find-repair-and-prevent-bugs-in-your-code.aspx">Much like Krzysztof Kozmic</a> I found that a lot of the ideas early on in the book were similar to what I've been taught by my ThoughtWorks colleagues over the last 3 1/2 years.

I do think it's really good seeing these ideas in words though because it's quite easy to forget about the best way to approach problems in the heat of the moment and the approaches suggested by Paul certainly aren't done everywhere in my experience.

These were some of my favourite parts of the book:

<ul>
<li>When chasing a bug Butcher suggests that a useful technique to use is to<strong> try and disprove your theory of why the problem has happened</strong>. Too often we come up with a theory and just adapt any data to fit our thinking. This is also known as <a href="http://en.wikipedia.org/wiki/Confirmation_bias">confirmation bias</a>. 

In his talk '<a href="http://www.markhneedham.com/blog/2009/04/25/pimp-my-architecture-dan-north/">Pimp my architecture</a>' Dan North suggests a similar approach more generally when working out how to tackle any problem. Each person has to take the other person's argument and then fight for that to be used instead. I quite like this idea - certainly something to try out.</li>
<li>When discussing the need to refactor code as we go along, the author points out that <strong>if the code we want to change doesn't have any tests around it then we need to write some</strong> to provide us with a safety net.

<blockquote>
Remember, however, that refactoring crucially depends upon the support of an extensive suite of automated tests. Without tests, you’re not refactoring. You’re hacking. 
</blockquote>

Hamlet D'Arcy <a href="http://hamletdarcy.blogspot.com/2009/06/forgotten-refactorings.html">makes a similar point but perhaps more forcibly in a really good blog post</a> and Michael Feathers' '<a href="http://www.amazon.com/gp/product/0131177052?ie=UTF8&tag=marneesblo-20&linkCode=as2&camp=1789&creative=390957&creativeASIN=0131177052">Working Effectively With Legacy Code</a>' covers the topic in much more detail.
</li>
<li>One tip which seems obvious but is still one I've tripped up on many times is to <strong>go through the list of changes that we've made before checking in</strong>! It's incredibly easy to forget about some seemingly insignificant change that we made before checking it in and perhaps breaking our application unexpectedly.

Somewhat tied in with this is the idea of checking in small changes more frequently and <a href="http://www.markhneedham.com/blog/2009/12/22/one-change-at-a-time/">only changing one thing at a time which I wrote about previously</a>.</li>
<li>I like that Butcher puts a lot of emphasis on <strong>ensuring that we actually know what's going wrong before we attempt to fix anything</strong>. 

<blockquote>Without ﬁrst understanding the true root cause of the bug, we are outside the realms of software engineering and delving instead into voodoo programming or programming by coincidence.
</blockquote>

This is particularly true when addressing performance problems where he rightly suggests that we should look to profile the code before making a premature optimisation. 

He also suggests using the <a href="http://www.markhneedham.com/blog/2009/03/20/coding-reassessing-what-the-debugger-is-for/">debugger</a> so that we can get a good idea about what the code is actually doing when it's running. While I think this is useful I feel that the need to use the debugger in this way frequently might suggest that our code is difficult to reason about which could well be something to address. </li>

<li>A couple of other cool suggestions are to<a href="http://www.markhneedham.com/blog/2009/09/07/a-reminder-that-sometimes-its-best-just-to-ask/"> call on team mates to help us out</a> if we're getting stuck trying to fix a bug and if that's not possible then to either <a href="http://www.markhneedham.com/blog/2009/11/15/a-reminder-to-talk-to-the-rubber-duck/">write out the problem or talk to the rubber duck</a>.

<blockquote>
If you don’t have someone to play the role of cardboard cutout, all is not necessarily lost. Try scribbling down a narrative of the problem on paper or perhaps composing an email to a friend. The trick is not to censor yourself — just like a writer would. 
</blockquote>

I don't think <strong>the importance of communicating with team mates can be underestimated</strong> and Butcher points out that if we notice a bad pattern in the code than it's no good just going through and changing it everywhere. We need to talk with the rest of the team to decide whether we can get an agreement on the way we'll develop code going forwards.</li>
<li>The only idea I disagreed with is that of putting <a href="http://www.markhneedham.com/blog/2009/02/14/coding-assertions-in-constructors/">assertions</a> <a href="http://www.markhneedham.com/blog/2009/10/31/coding-invariant-checking-on-dependency-injected-components/">into</a> <a href="http://www.markhneedham.com/blog/2009/10/29/coding-consistency-when-invariant-checking/">the code</a> which I feel adds clutter to our code even though it makes it fail faster than would otherwise be the case. From my experience if we write good enough unit tests and have <a href="http://watchitlater.com/blog/archives/115">good logging</a> in our code then the assertions aren't needed.</li>
</ul>

<h3>In Summary</h3>
The book is pretty quick to read at around 200 pages and packs a lot of useful tips into that space. I'd say it's a pretty useful book to keep by your desk to refer to now and then.
