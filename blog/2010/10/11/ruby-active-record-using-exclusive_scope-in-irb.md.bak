+++
draft = false
date="2010-10-11 19:03:39"
title="Ruby: Active Record - Using 'exclusive_scope' in IRB"
tag=['ruby']
category=['Ruby']
+++

<a href="http://twitter.com/#!/ashwinraghav">Ashwin</a> and I have been working recently on a bit of code to make it possible to 'soft delete' some objects in our system. 

We're doing this by creating an additional column in that table called 'deleted_at_date' which we populate if a record is 'deleted'.

As we wanted the rest of the application to ignore 'deleted' records we added a <a href="http://ryandaigle.com/articles/2008/11/18/what-s-new-in-edge-rails-default-scoping">default scope</a> to it:


~~~ruby

class Foo < ActiveRecord::Base
   default_scope :conditions => "deleted_at_date is null"   
end
~~~

This works fine but we wanted to be able to see the status of all the records in IRB and with the default scope 'Foo.all' no longer returns 'soft deleted' records.

Luckily Active Record provides a protected method called '<a href="http://stackoverflow.com/questions/1648971/rails-why-is-withexclusivescope-protected-any-good-practice-on-how-to-use-it">with_exclusive_scope</a>' which we can use to get around this:


~~~ruby

Foo.send(:with_exclusive_scope) { Foo.find(:all) }
~~~

Since it's a protected method we can only access it in IRB by using 'send' which is a bit hacky, something David Heinemeier Hansson would refer to as <a href="http://www.loudthinking.com/arc/2006_10.html">syntactic vinegar</a>.

Interestingly our first attempt to use 'with_exclusive_scope' involved writing the above code like this...


~~~ruby

Foo.send(:with_exclusive_scope) { find(:all) }
~~~

..which results in the following error because when the closure was created 'self' referred to the main object rather than to 'Foo':


~~~text

NoMethodError: undefined method `find' for #<Object:0xb77cd94c>
    from (irb):62
    from /var/lib/gems/1.8/gems/activerecord-2.3.5/lib/active_record/base.rb:2143:in `with_scope'
    from /var/lib/gems/1.8/gems/activerecord-2.3.5/lib/active_record/base.rb:2151:in `with_exclusive_scope'
    from (irb):62:in `send'
    from (irb):62
    from :0
~~~

Since the main object has no method called 'find' we get an exception thrown.
