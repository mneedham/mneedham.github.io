+++
draft = false
date="2008-10-21 07:19:56"
title="If you use an 'if' you deserve to suffer"
tag=['coding', 'if-statement']
category=['Coding']
+++

One of the things I dislike the most when coding is writing if statements. and while I don't believe that if should be completely abolished from our toolkit, I think the <a href="http://www.cuberick.com/2007/11/down-with-if.html">anti if campaign</a> started about a year ago is going along the right lines.

While there is certainly value in using an if statement as a <a href="http://c2.com/cgi/wiki?GuardClause">guard block</a> it usually feels that we have missed an abstraction if we are using it elsewhere.

Given my dislike of the construct, when I have to use it I like to being very explicit about the scope in which it is applicable. I think this approach stems from being caught out back in my university days and trying to debug something along the lines of:


~~~java

if(thisHappens())
	doThis();
	doThat();
~~~

The code was much messier than that but I spent ages trying to work out why the correct behaviour wasn't happening. Eventually I realised that 'doThat()' was being called every time regardless of the value returned by 'thisHappens()'.

Ever since then I have written if statements like so:


~~~java

if(thisHappens()) {
	doThis();
	doThat();
}
~~~

It doesn't look as nice but with one glance at the code I can see exactly what is happening. I definitely prefer to have this advantage although I do appreciate that if there is only one statement following the if statement then <a href="http://c2.com/xp/YouArentGonnaNeedIt.html">YAGNI</a> might be applicable.

I prefer to take the more conservative approach - once bitten, twice shy.

So what is the title of this post all about?

Often when pair programming there is some discussion over which approach is better and in one such session last week a colleague of mine, who happened to favour the more verbose approach, came up with a phrase along those lines when I asked why they favoured that approach. If you're going to use an if statement then you're just going to have to put up with the eye sore those extra curly braces create in your code!

Being in favour of this approach already I really like the idea and while maybe not quite as scientific as describing the technical reasons for doing so, it is perhaps more effective.
