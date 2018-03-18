+++
draft = false
date="2011-09-13 13:33:43"
title="Javascript: Internet Explorer 8 - trim() leads to 'Object doesn't support this property or method' error"
tag=['javascript']
category=['Javascript']
+++

We make use of the Javascript <cite><a href="https://developer.mozilla.org/en/JavaScript/Reference/Global_Objects/String/trim">trim()</a></cite> function in our application but didn't realise that it isn't implemented by Internet Explorer until version 9.

This led to the following error on IE8 when we used it:

<blockquote>
Message: Object doesn't support this property or method
Line: 18
Char: 13
Code: 0
URI: http://our.app/file.js
</blockquote>

There's a <a href="http://stackoverflow.com/questions/2308134/trim-in-javascript-not-working-in-ie">stackoverflow thread</a> suggesting some different ways of implementing your own 'trim()' method but since we're using jQuery already we decided to just use the '$.trim()' function from there.

Therefore:


~~~javascript

var cleaned = ourString.trim();
~~~

becomes:


~~~javascript

var cleaned = $.trim(ourString);
~~~

I'm sure I must have come across this before but I don't remember when!
