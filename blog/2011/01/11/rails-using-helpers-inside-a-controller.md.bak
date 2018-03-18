+++
draft = false
date="2011-01-11 17:09:49"
title="Rails: Using helpers inside a controller"
tag=['rails']
category=['Ruby']
+++

For about an hour or so this afternoon we were following the somewhat evil practice of using a method defined in a helper inside a controller.

The method was defined in the ApplicationHelper module:


~~~ruby

module ApplicationHelper
	def foo
		# do something
	end
end
~~~

So we initially assumed that we'd just be able to reference that method inside any of our controllers since they all derive from ApplicationController.

That wasn't the case so our next attempt was to try and add it as a helper:


~~~ruby

class FooController < ApplicationController
	helper :application
end
~~~

Which makes it accessible from the view but not from the controller...

Eventually we called <a href="">Ashwin</a> to help us out and he came across <a href="http://snippets.dzone.com/posts/show/1799">this thread on dzone</a>.

About half way down the page ovhaag points out that we can use '@template' to get access to helper methods:

<blockquote>
In any controller, there is a "@template"-instance and you can call helper methods on this.

I found this trick in <a href="http://media.railscasts.com/videos/132_helpers_outside_views.mov">http://media.railscasts.com/videos/132_helpers_outside_views.mov</a>
...
Ryan is not sure if this use is intended but it is very short and today it works.
</blockquote>

We can use that instance variable like so:


~~~ruby

class FooController < ApplicationController
	def our_method
		# We can call foo like this
		@template.foo
	end
end
~~~

We eventually found out another way to do what we wanted but it seems like a neat little trick
