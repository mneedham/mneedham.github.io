+++
draft = false
date="2010-09-13 17:44:04"
title="Ruby: Caught out by no type checking"
tag=['ruby']
category=['Ruby']
+++

I got caught out for a little while today when comparing a value coming into a controller from 'params' which we were then comparing with a collection of numbers.

The code was roughly like this...


~~~ruby

class SomeController

	def some_action
		some_collection = [1,2,3,4,5]
		selected_item = some_collection.find { |item| item == params[:id] }
	end
end
~~~

...and since the 'id' being passed in was '1' I was expected that we should have a selected item but we didn't.

The actual code being executed would be...


~~~ruby

[1,2,3,4,5].find { |item| item == "1" }
~~~

...which of course doesn't match any values since we're comparing a string to an integer.

The fix is relatively simple...


~~~ruby

class SomeController

	def some_action
		some_collection = [1,2,3,4,5]
		selected_item = some_collection.find { |item| item == params[:id].to_i }
	end
end
~~~

...but I found it interesting that this is the type of thing that would have been caught if we had static type checking but is something you'd aim to cover with a test with a dynamic language.

In this case we had been refactoring the code and having slightly changed the way it worked internally our interaction tests didn't quite cover this scenario properly so we had to go and update those.

So far I've certainly seen that Ruby/Rails can make you more productive and this is the first time I've seen a situation where I wished for C#'s static typing...if just for a little while.
