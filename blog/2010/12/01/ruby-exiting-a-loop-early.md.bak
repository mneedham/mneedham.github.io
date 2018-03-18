+++
draft = false
date="2010-12-01 17:56:51"
title="Ruby: Exiting a 'loop' early"
tag=['ruby']
category=['Ruby']
+++

We recently had a problem to solve which at its core required us to iterate through a collection, look up a value for each key and then exit as soon as we'd found a value.

The original solution looped through the collection and then explicitly returned once a value had been found:


~~~ruby

def iterative_version
  v = nil
  [1,2,3,4,5].each do |i|
    v = long_running_method i
    return v unless v.nil?
  end
  v
end
~~~


~~~ruby

def long_running_method(value)
  puts "inside the long running method with #{value}"
  return nil if value > 3
  value
end
~~~

Which we run like so:


~~~ruby

p "iterative value is #{iterative_version.to_s}"
~~~

This prints the following when we run it:


~~~text

inside the long running method with 1
"iterative value is 1"
~~~

I figured there must be a more functional way to solve the problem and I eventually came up with this:


~~~ruby

def functional_version
  [1,2,3,4,5].map {|i| long_running_method i }.find { |i| !i.nil? }
end
~~~

Which prints the following when we run it:


~~~ruby

inside the long running method with 1
inside the long running method with 2
inside the long running method with 3
inside the long running method with 4
inside the long running method with 5
"functional value is 1"
~~~

The problem is that collections in Ruby are eager evaluated so we evaluate every single item in the collection before we get the first non nil value.

Luckily the <a href="http://flori.github.com/lazylist/">lazylist</a> gem comes to our rescue and allows us to solve the problem in a functional way:


~~~ruby

require 'lazylist'
def lazy_version
  lazy_list([1,2,3,4,5]).find { |i| !i.nil? }
end

def lazy_list(values)
  list(long_running_method(values.first)) { lazy_list(values - [values.first]) } 
end
~~~

Running that gives us this:

~~~text

inside the long running method with 1
"lazy value is 1"
~~~

I've never come across a problem where I needed to use a lazy list but finally I have and I think the version which uses it is pretty neat.
