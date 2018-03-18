+++
draft = false
date="2011-09-07 20:47:14"
title="Learning Regular Expressions: Non capturing match"
tag=['software-development']
category=['Software Development']
+++

I've been working my way slowly through the O'Reilly '<a href="http://www.amazon.co.uk/Mastering-Regular-Expressions-Jeffrey-Friedl/dp/0596528124/ref=sr_1_2?ie=UTF8&qid=1315428243&sr=8-2">Mastering Regular Expressions</a>' book and recently read about the non capturing match operator which came in useful for some Git log parsing I've been doing.

On the project I'm working on we all commit as the same user and then put our names at the beginning of the commit message. 

We wanted to try and find out the statistics of who'd been pairing with each other and therefore needed to extract the pairs from commits.

Unfortunately everyone writes their names in a slightly different way so the regular expression which I used to parse each commit needed to try and handle that.

For example these are some of the ways that commit messages start:


~~~text

Uday/Charles #67 did some stuff
mark,suzuki more stuff
pat, tom: very important stuff
Uday:Marc #87 stuff
~~~

The separator between the names is different in each case but in the majority of cases can be satisfied by the following regular expression:


~~~text

([\/,][ ]?|:)
~~~

It's either:

<ul>
<li>A forward slash or comma followed by an optional space</li>
<li>A colon</li>
</ul>

Since I want to express the fact that the separator can be one thing or the other I need to group those two things together in parentheses.

Unfortunately that means that the separator will be included in the array of captures that we have when parsing the commit.

I only wanted to have the names of the two people included in that array.

The non capturing match operator '(?:' allows us to match against the expected separator without actually capturing it:


~~~text

(?:[\/,][ ]?|:)
~~~

That regular expression is part of a much larger/probably over complicated one which also helps to capture the names of the people pairing:


~~~text

var pairRegex = /^\[?([\w-]+)[ ]?[^\/, ]*(?:[\/,][ ]?|:)([\w-]+)\]?[^\/]*[\s:]/
~~~

Using the regex with the non capturing match gives us:


~~~text

"charles/mark: adios to play, hello scalatra".match(pairRegex)
["charles/mark: adios to play, hello ", "charles", "mark"]
~~~

Whereas if we used a normal capture we'd also capture the '/':


~~~text

"charles/mark: adios to play, hello scalatra".match(pairRegex)
["charles/mark: adios to play, hello ", "charles", "/", "mark"]
~~~
