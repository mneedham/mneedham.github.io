+++
draft = false
date="2009-01-17 21:01:38"
title="YAGNI: Some thoughts"
tag=['coding']
category=['Coding']
+++

If you hang around a team practicing <a href="http://www.extremeprogramming.org/">XP</a> for long enough, one of the phrases you are bound to hear is <a href="http://c2.com/xp/YouArentGonnaNeedIt.html">YAGNI</a> (You Ain't Gonna Need It).

Although it can sometimes be used to ignore things we don't want to focus on <a href="http://iancartwright.com/blog/2009/01/five-kinds-of-technical-debt.html">as Ian points out</a>, in general the aim is to stop people from working on code that isn't currently required.

So assuming our team isn't being lazy and trying to avoid decisions that they don't want to think about, why do we hear the YAGNI call and more importantly, perhaps, what happens when we don't heed that call.

<h3>Jack of all trades, master of none</h3>
One of the problems of writing APIs that are designed based on potential future use (by multiple clients) is that the <strong>API ends up not being what any of the clients want</strong> - it does its job but not in a way that makes life easy for any of the clients.

From my experience the easiest way to design usable APIs is to drive the design by using examples. We only write code if we have an example/test to drive that out. 

At a higher level this means that we should drive the design of our code by working out how the client is going to use it rather than trying to anticipate how it might be used. This is sometimes known as <a href="http://www.code-magazine.com/article.aspx?quickid=0805061&page=2">client driven development as opposed to assumption driven development</a>. 

Joe Walnes' <a href="http://xstream.codehaus.org/">XStream</a> library is often referenced as an easy to use library because he only added features that he needed (as a client of the library) rather than trying to imagine what features people might want.

<h3>Change becomes difficult</h3>
If we have driven our code based on assumptions of how we think it might be used in the future then it becomes more difficult to change it because we need to ensure that the changes we make won't cause problems for these potential future clients.

Code driven this way rather than by examples tends to be <strong>much more complicated</strong> because we don't know which cases we need to handle and which we don't - we end up trying to handle them all.

Making changes to code after it has been written is quite common but we have now made this more difficult for ourselves. Changes end up taking longer and we can't be sure that the change will work for anyone beyond our current clients anyway.  

<h3>Takes longer</h3>
When we only develop an API for clients that currently exist we are writing much less code than when we try to code for the generic case and therefore we can accomplish our task much more quickly. The inverse being that when we don't <strong>we spend a lot of time</strong> trying to write a solution that veers more and more towards being a framework.

This doesn't mean that we should completely tie our API to that client - instead we should ensure that our solution is flexible and easy to change in the future. 
