+++
draft = false
date="2010-09-23 14:33:29"
title="Ruby: Control flow using 'and'"
tag=['ruby']
category=['Ruby']
+++

Something I've noticed while reading Ruby code is that quite frequently the flow of a program is controlled by the 'chaining' of different operations through use of the 'and' keyword.

I've noticed that <a href="http://www.markhneedham.com/blog/2010/03/28/reading-code-underscore-js/">this pattern is used in Javascript code as well</a> and it's particularly prevalent when we want to get a status for those operations after they've all been executed.

For example we might have the following code...


~~~ruby

status = user.is_allowed_to_edit_foo? and user.update_foo(params[:foo]) and user.save
~~~

..where the user's foo would only get updated and the record saved if they were actually allowed to edit their foo.

At the moment it seems quite strange to me because when I see operations chained together like that I assume that they're all 'query' type operations but in Ruby it seems like 'command' type operations are used too.

To an extent the <a href="http://martinfowler.com/bliki/CommandQuerySeparation.html">command query separation principle</a> is being broken but it seems quite common to return a boolean value to indicate whether or not a state changing operation was successful.

I'd be more familiar with that type of code being written like this but I don't think it reads as well:


~~~ruby

status = false
if user.is_allowed_to_edit_foo?
	if user.update_foo(params[:foo])
		status = user.save
	end
end
~~~

While trying to think of a way of writing that code which I think would be more intention revealing I ended up with the following:


~~~ruby

class User
  def is_allowed_to_edit_foo?(foo, &block)
    yield and return true if can_edit_foo?
    false
  end

  def update_foo(&block)
    #do some awesome stuff
    successful_update = true
    yield and return true if successful_update
    false
  end 
  
  def can_edit_foo?
    true
  end  
end
~~~


~~~ruby

user = User.new
status = user.is_allowed_to_edit_foo?(params[:foo]) do
  user.update_foo do
     user.save
  end
end
~~~

I'm guessing the original code I posted is more idiomatic Ruby but I still think it's interesting to see the different styles that you can write code in.
