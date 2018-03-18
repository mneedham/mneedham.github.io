+++
draft = false
date="2009-11-14 11:20:13"
title="Mercurial: hg bisect"
tag=['mercurial', 'hg', 'bisec']
category=['Version Control']
+++

We've been using <a href="http://mercurial.selenic.com/wiki/">Mercurial</a> locally on the project I've been working on and <a href="http://fragmental.tw/">Phil</a> showed me a cool feature called '<a href="http://mercurial.selenic.com/wiki/BisectExtension">bisect</a>' a couple of weeks ago which can be helpful for working out which revision we managed to break our code in.

It's been ported across from <a href="http://git-scm.com/">Git</a> and is included in Mercurial from version 1.0.0 rather than just being an extension.

From the bisect extension page:
<blockquote>
Its behaviour is fairly simple: it takes a first revision known to be correct (i.e. without the bug) and a last revision known to be bad (i.e. with the bug). The bisect extension ouputs a revision halfway between the good and the bad ones and lets you test it. If this revision is a good one, you mark it as good with hg bisect good, otherwise you mark it as bad with hg bisect bad. In both cases, bisect outputs a new revision to test, halfway between the good and the bad ones. You repeat until only one revision is left: the culprit.
</blockquote>

The usage has changed a bit now that it's included as part of the initial download.

I was working on something yesterday and checking in fairly regularly before realising that I'd broken something.

I was fairly sure that the break had happened in the tip (revision 98) but I could only remember it definitely working in revision 96.

I defined the good and bad revisions like this:


~~~text

 

~~~text


In this case revision 97 was now checked out and I checked that the code was working with that revision before marking it:
 

~~~text

 
It's now able to work out that the problem is in fact in revision 98:


~~~text

The first bad revision is:
changeset:   98:86260809c309
tag:         tip
user:        mneedham
date:        Fri Nov 13 16:31:02 2009 +1100
summary:     seem to have screwed up the graphs. Not sure how
~~~

I managed to mess up setting up the good and bad revisions a few times - I somehow had the impression that I needed to manually update to the original good and bad revisions which isn't the case.

The reset command was my friend before I worked out what I was doing wrong:


~~~text

hg bisect -r
~~~

It seems like a neat little feature. I'm sure there are lots of other cool things like this in Mercurial so if you know any let me know!

* Update *
As Rob points out in the comments the command is 'bisect' rather than 'bisec' as I had it originally. Both commands work for the moment though!
