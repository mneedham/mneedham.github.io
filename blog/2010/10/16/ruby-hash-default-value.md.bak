+++
draft = false
date="2010-10-16 14:02:37"
title="Ruby: Hash default value"
tag=['ruby']
category=['Ruby']
+++

I've been pairing a fair bit with <a href="http://twitter.com/#!/ashwinraghav">Ashwin</a> this week and one thing he showed me which I hadn't previously seen is the ability to <a href="http://ruby-doc.org/core/classes/Hash.html#M002853">set a default value for a hash</a> which gets returned if we search for a key that doesn't exist.

This is an idea that I originally came across while playing around with Clojure but with Clojure the default value was defined in the calling code rather than in the hash definition.

For example:


~~~lisp

(def scores {:mark 10 :dave 20})

(get scores :tony :0)
~~~

For a similar piece of code in Ruby we could write the following:

~~~ruby

scores = { :mark => 10, :dave => 20 }
scores.default = 0
~~~

Now if we search for a key that doesn't exist in the hash then we'll get the value 0:


~~~ruby

scores[:some_other_guy]
0
~~~

We're using this in a couple of places in our code base already but it'll be particularly useful for an upcoming piece of functionality where we want to vary the look and feel of some pages depending on certain criteria.

For the majority of users the look and feel will remain the same but for some of them it will vary slightly. Controlling that behaviour by using a hash with some default settings therefore seems like a reasonably good fit.
