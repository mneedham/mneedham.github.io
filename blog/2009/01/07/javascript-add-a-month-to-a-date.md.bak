+++
draft = false
date="2009-01-07 23:00:58"
title="Javascript: Add a month to a date"
tag=['javascript', 'datejs']
category=['Javascript']
+++

We've been doing a bit of date manipulation in Javascript on my current project and one of the things that we wanted to do is add 1 month to a given date.

We can kind of achieve this using the standard date libraries but it doesn't work for edge cases. 

For example, say we want to add one month to January 31st 2009. We would expect one month from this date to be February 28th 2009:


~~~javascript

var jan312009 = new Date(2009, 1-1, 31);
var oneMonthFromJan312009 = new Date(new Date(jan312009).setMonth(jan312009.getMonth()+1));
~~~

The output of these two variables is:


~~~javascript

Sat Jan 31 2009 00:00:00 GMT+1100 (EST)
Tue Mar 03 2009 00:00:00 GMT+1100 (EST)
~~~

Not quite what we want!

Luckily there is a library called <a href="http://www.datejs.com/">datejs</a> which has taken care of this problem for us. It provides a really nice <a href="http://www.martinfowler.com/bliki/DomainSpecificLanguage.html">DSL</a> which makes it very easy for us to do what we want.

We can add a month to a date very easily now:


~~~javascript

var jan312009 = new Date(2009, 1-1, 31);
var oneMonthFromJan312009 = new Date(jan312009).add(1).month();
~~~


~~~javascript

Sat Jan 31 2009 00:00:00 GMT+1100 (EST)
Sat Feb 28 2009 00:00:00 GMT+1100 (EST)
~~~

There are loads of other useful date manipulation functions which you can read more about on the <a href="http://code.google.com/p/datejs/wiki/APIDocumentation">API</a>, just don't forget that date in Javascript is mutable so any manipulation done to dates contained in vars will change the original value.
