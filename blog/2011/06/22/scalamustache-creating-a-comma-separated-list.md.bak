+++
draft = false
date="2011-06-22 21:24:06"
title="Scala/Mustache: Creating a comma separated list"
tag=['scala', 'mustache']
category=['Scala']
+++

We're using the <a href="http://scalate.fusesource.org/documentation/mustache.html">Mustache</a> templating engine on my project at the moment and one thing that we wanted to do was build a comma separated list.

Mustache is designed so that you pretty much can't do any logic in the template which made it really difficult to do what we wanted.

It's easy enough to get a comma after each item in a list with something like the following code:


~~~text

{{#people}}<a href="/link/to/{{toString}}">{{toString}}</a>{{/people}}
~~~

where <cite>people</cite> is passed to the template as a collection of strings.

To get rid of the trailing comma we ended up building a collection of <cite>Pairs</cite> containing the person's name and a boolean value indicating whether or not to show the comma.

We need to show the comma before every element except for the first one so we can pass the following collection to the template:


~~~scala

val values = names.zipWithIndex.map { case(item, index) => if(index == 0) (item, false) else (item, true) }
~~~

<cite>zipWithIndex</cite> returns a collection of pairs containing the original strings and their position in the collection.

We can then map to a different result for just the first element and then use those pairs in the template like so:


~~~text

{{#people}} {{#_2}}, {{/_2}}<a href="/link/to/{{_1}}">{{_1}}</a>{{/people}}
~~~

It's truly horrendous so if anyone knows a better way then please let me know!
