+++
draft = false
date="2010-09-07 03:52:32"
title="Ruby: Hash ordering"
tag=['ruby']
category=['Ruby']
+++

The application that I'm working on at the moment is deployed into production on JRuby but we also use the C Ruby 1.8.7 interpreter when developing locally since this allows us much quicker feedback.

As a result we sometimes come across interesting differences in the way that the two runtimes work.

One that we noticed yesterday is that if you create a hash, the order of the keys in the hash will be preserved when interpreted on JRuby but not with the C Ruby interpreter.

For example if we create the following hash in Ruby 1.8.7 it will be resorted into alphabetical order:


~~~text

ruby-1.8.7 > a_hash = { :a => 1, :d => 2, :c => 3 }
 => {:a=>1, :c=>3, :d=>2} 
~~~

Whereas in JRuby it will maintain its order:


~~~text

jruby-1.5.1 > a_hash = { :a => 1, :d => 2, :c => 3 }
 => {:a=>1, :d=>2, :c=>3} 
~~~

We found <a href="http://www.ruby-forum.com/topic/153146">a post on the Ruby mailing list from a couple of years ago</a> which pointed out that from Ruby 1.9 the order is in fact maintained.

However, Gregory Seidman also pointed out that...

<blockquote>
Hashes are inherently unordered. Hashes provide amortized O(1) insertion and retrieval of elements by key, and that's it. If you need an ordered set of pairs, use an array of arrays. Yes, this is a pet peeve of mine.
</blockquote>

Since that is indeed what we want we've created an array of arrays in our code instead. The code to retrieve values from the array of arrays is a bit more verbose but at least the order is now guaranteed!
