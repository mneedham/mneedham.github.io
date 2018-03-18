+++
draft = false
date="2012-03-30 06:21:00"
title="IntelliJ: Find/Replace using regular expressions with capture groups"
tag=['software-development', 'intellij']
category=['Software Development']
+++

Everyone now and then we end up having to write a bunch of mapping code and I quite like using IntelliJ's 'Replace' option to do it but always end up spending about 5 minutes trying to remember how to do capture groups so I thought I'd write it down this time.

Given the following text in our file:


~~~scala

val mark = 0
val dave = 0
val john = 0
val alex = 0
~~~

Let's say we wanted to prefix each of those names with 'cool' and had decided not to use Column mode for whatever reason.

One way of doing that is to capture the names and then replace each of them with 'cool' appended on the beginning:

A (very hacky) find regex could be this:

~~~text

\s([a-zA-Z]+)\s=
~~~

Where we capture all the letters in the variable name inside a group and then build our replacement string like so:

~~~text

 cool$1 =
~~~

I always expect the capture group replacement syntax to be '\1', '\2' and so on but it actually uses a '$' instead.

Hopefully now I shall remember!
