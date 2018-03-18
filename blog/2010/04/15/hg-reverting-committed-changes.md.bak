+++
draft = false
date="2010-04-15 22:35:53"
title="hg: Reverting committed changes"
tag=['mercurial']
category=['Version Control']
+++

Continuing with our learning with Mercurial, yesterday we wanted to revert a couple of change sets that we had previously committed and go back to an old version of the code and continue working from there.

As an example, say we wanted to go back to Revision 1 and had the following changes committed:


~~~text

Revision 3
Revision 2
Revision 1
Revision 0
~~~

My original thought was that we could merge revision 1 with the current tip:


~~~text

hg merge -r 1
~~~

Sadly that won't work because we can't merge with an ancestor:


~~~text

'abort: can't merge with ancestor'
~~~

I <a href="http://twitter.com/markhneedham/statuses/12189578740">put the question to twitter</a> and got a few different suggestions.

The first was to use 'revert' and go back to revision 1 like so:


~~~text

hg revert -r 1
~~~

This works pretty well although <a href="http://twitter.com/BestFriendChris/statuses/12190736162">my colleague Chris Turner pointed out that we could also use 'backout'</a> like so:


~~~text

hg backout -merge 3
hg backout -merge 2
~~~

The neat thing about that approach is that we get 2 changesets checked in showing the reversing of the changes that we previously checked in. We therefore have a <a href="http://twitter.com/BestFriendChris/statuses/12191376829">better history of what exactly we're reverted</a>.

With this approach we could also back out changes which weren't right near the tip of the repository as was the case in my example.

Another alternative is to clone the repository from the revision that we want to keep:


~~~text

hg clone -r 1
~~~

With this approach we would lose the history of anything beyond that revision but if that's what we want then it's another approach to achieve our goal!

It'd be interesting to hear your opinions on which approach you take and if there are any others to solve the problem I described.
