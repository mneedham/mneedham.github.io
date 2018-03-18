+++
draft = false
date="2009-01-07 23:17:05"
title="Javascript Dates - Be aware of mutability"
tag=['javascript', 'dates']
category=['Javascript']
+++

It seems that <a href="http://www.markhneedham.com/blog/2008/09/18/using-javautildate-safely/">much like in Java</a>, dates in Javascript are mutable, meaning that it is possible to change a date after it has been created.

We had this painfully shown to us when using the <a href="http://datejs.com/">datejs</a> library to <a href="http://www.markhneedham.com/blog/2009/01/07/javascript-add-a-month-to-a-date/">manipulate some dates</a>.

The erroneous code was similar to this:


~~~javascript

var jan312009 = new Date(2008, 1-1, 31);
var oneMonthFromJan312009 = new Date(jan312009.add(1).month());
~~~

See the subtle error? Outputting these two values gives the following:


~~~text

Fri Feb 29 2008 00:00:00 GMT+1100 (EST)
Fri Feb 29 2008 00:00:00 GMT+1100 (EST)
~~~

The error is around how we have created the 'oneMonthFromJan312009':

<blockquote>
var oneMonthFromJan312009 = new Date(<strong>jan312009.add(1).month()</strong>);
</blockquote>

We created a new Date but we are also changing the value in 'jan312009' as well.

It was the case of having the bracket in the wrong place. It should actually be after the 'jan312009' rather than at the end of the statement.

This is the code we wanted:


~~~javascript

var jan312009 = new Date(2008, 1-1, 31);
var oneMonthFromJan312009 = new Date(jan312009).add(1).month());
~~~

Which leads to more expected results:


~~~text

Sat Jan 31 2009 00:00:00 GMT+1100 (EST)
Sat Feb 28 2009 00:00:00 GMT+1100 (EST)
~~~

