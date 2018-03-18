+++
draft = false
date="2010-12-07 05:01:44"
title="Ruby: One method, two parameter types"
tag=['ruby']
category=['Ruby']
+++

One interesting thing that I've noticed while coding in Ruby is that due to the dynamicness of the language it's possible to pass values of different types into a given method as parameters.

For example, I've recently come across a few examples of methods designed like this:


~~~ruby

def calculate_foo_prices(foos)
   ...
   [foos].flatten.each do |foo|
      # do something
   end
end
~~~

This allows us to use the method like this:


~~~ruby

# foos would come in as an array from the UI
foos = [Foo.new, Foo.new, Foo.new]
calculate_foo_prices(foos)
~~~

Or like this:


~~~ruby

calculate_foo_prices(Foo.new)
~~~

It becomes quite confusing to understand why what is supposedly already a collection is being put inside an array on line 3 of the first example when you first read it.

An alternative would be to pull out a different method for calculating the price of the single Foo:


~~~ruby

def calculate_foo_price(foo)
   calculate_foo_prices([foo])
end
~~~

And then simplify the original method:


~~~ruby

def calculate_foo_prices(foos)
   ...
   foos.each do |foo|
      # do something
   end
end
~~~

While writing this I was thinking that another way could be to change the original method to look like this by using the splat operator:


~~~ruby

def calculate_foo_prices(*foos)
   ...
   foos.each do |foo|
      # do something
   end
end
~~~

Which means that we can use the same method for both situations:


~~~ruby

calculate_foo_prices(Foo.new)
~~~				


~~~ruby

# foos would come in as an array from the UI
foos = [Foo.new, Foo.new, Foo.new]
calculate_foo_prices(*foos)
~~~

I'm guessing the latter is more idiomatic Ruby or perhaps there's another way I'm not aware of yet?

