+++
draft = false
date="2008-09-24 23:59:54"
title="My dislike of Java's static import"
tag=['java', 'static', 'import']
category=['Java']
+++

While playing around with <a href="http://jbehave.org/documentation/two-minute-tutorial/">JBehave</a> I was reminded of my dislike of the <a href="http://java.sun.com/j2se/1.5.0/docs/guide/language/static-import.html">import static</a> feature which was <a href="http://java.sun.com/j2se/1.5.0/docs/guide/language/static-import.html">introduced in Java 1.5</a>.

Using import static allows us to access static members defined in another class without referencing the class name. For example suppose we want to use the following method in our code:


~~~java

Math.max(1,2);
~~~

Normally we would need to include the class name (Math) that the static function (max) belongs to. By using the import static we can reference max like so:


~~~java

import static java.lang.Math.max;
...
max(1,2);
~~~

The benefit of this approach is that it makes the code read more fluently but the disadvantage is that you can't immediately tell where a method lives. I want to be able to tell what is going on in the code from looking at it and anything which prevents this is a hindrance.

The <a href="http://java.sun.com/j2se/1.5.0/docs/guide/language/static-import.html">official documentation</a> even suggests using this functionality sparingly:

<blockquote>
So when should you use static import? Very sparingly! Only use it when you'd otherwise be tempted to declare local copies of constants, or to abuse inheritance (the Constant Interface Antipattern). In other words, use it when you require frequent access to static members from one or two classes.
</blockquote>

On my last project we ended up saying that import static was allowed in test code because there were relatively few places the static methods could be imported from, but when it came to production code the fully qualified path was required.

