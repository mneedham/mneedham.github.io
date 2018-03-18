+++
draft = false
date="2010-09-21 20:24:47"
title="Ruby: Returning hashes using merge! and merge"
tag=['ruby']
category=['Ruby']
+++

We came across an interesting problem today with some code which was unexpectedly returning nil.

The code that we had looked like this...

~~~ruby

class SomeClass
	def our_method	
		a_hash = { :a => 2 }
		a_hash.merge!({:b => 3}) unless some_condition.nil?
	end
end
~~~

...and we didn't notice the 'unless' statement on the end which meant that if 'some_condition' was nil then the return value of the method would be nil.

One way around it is to ensure that we explicitly return a_hash at the end of the method...


~~~ruby

class SomeClass
	def our_method	
		a_hash = { :a => 2 }
		a_hash.merge!({:b => 3}) unless some_condition.nil?
		a_hash
	end
end
~~~

...but I think that looks a bit ugly. 

Luckily Rails provides a method called 'returning' which I first learnt about from <a href="http://github.com/raganwald/homoiconic/blob/master/2008-10-29/kestrel.markdown#readme">Reg Braithwaite's blog post about the kestrel combinator</a>.

That method is defined like so:


~~~ruby

  def returning(value)
    yield(value)
    value
  end
~~~

And we can use it in our code like this:


~~~ruby

class SomeClass
	def our_method	
		a_hash = { :a => 2 }
		returning a_hash do |h|
			h..merge!({:b => 3}) unless some_condition.nil?
		end
	end
end
~~~

Another way to return the merged hash without mutating the original would be to use the 'merge' method rather than 'merge!':


~~~ruby

class SomeClass
	def our_method	
		a_hash = { :a => 2 }
		a.hash.merge(!some_condition.nil? ? {:b => 3} : {})
	end
end
~~~

We could use that approach with 'merge!' as well but I'm not sure that it reads as nicely as the version which uses the 'unless' way.

Another approach that I started messing around with could be this...


~~~ruby

class SomeClass
  def our_method
    a_hash = { :a => 2 }
    merge_unless(a_hash, {:b => 3}, proc { some_condition.nil? })
  end
end

def merge_unless(hash, other_hash, condition)
  if condition.call()
    hash
  else
    hash.merge(other_hash)
  end 
end
~~~

...although that's probably a bit over the top seeing the collection of other ways we already have.
