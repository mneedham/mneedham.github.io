+++
draft = false
date="2010-09-30 07:00:57"
title="Ruby: ActiveRecord 2.3.5 object equality"
tag=['ruby', 'activerecord']
category=['Ruby']
+++

We learnt something interesting about the equality of ActiveRecord objects today while comparing two user objects - one which was being provided to our application by Warden and the other that we'd retrieved by a 'User.find' call.

Both objects referred to the same user in the database but were different instances in memory.

We needed to check that we were referring to the same user for one piece of functionality and were therefore able to make use of the '==' method defined on ActiveRecord::Base which is <a href="http://api.rubyonrails.org/classes/ActiveRecord/Base.html">defined in the documentation like so</a>:

<blockquote>
Public Instance methods
==(comparison_object)
Returns true if the comparison_object is the same object, or is of the same type and has the same id.
</blockquote>

This worked fine but when trying to write a test around this code we found it quite difficult.

We wanted to simulate the fact that we had two objects in our application that referred to the same database entry but not the same object.

Our initial approach was something like this:


~~~ruby

describe "ActiveRecord::Base Equality" do
	it "should let us have two objects which both point to the same user in the database" do
		# Create a user in the database with Factory Girl
		Factory(:user_with_x_role, :id => 15 )

		u = User.find 15
		u2 = User.find 15

		# the rest of our test where we'd insert u and u2 into the application
	end
end
~~~

Unfortunately when we ran the test we found that if we mutated 'u' in the production code then the value of 'u2' was also being mutated so they were somehow both referring to the same instance.

Our second attempt was to create a clone of the object so that they wouldn't be referring to the same instance:


~~~ruby

describe "ActiveRecord::Base Equality" do
	it "should let us have two objects which both point to the same user in the database" do
		# Create a user in the database with Factory Girl
		Factory(:user_with_x_role, :id => 15 )

		u = User.find 15

		u2 = u.clone
		u2.id = u.id

		# the rest of our test where we'd insert u and u2 into the application
	end
end
~~~

'clone' creates a copy of the object but removes the id. Since we want both our objects to have the same id so that they'll be recognised as being equal we set the id on the next line.

Unfortunately we now found that the two objects weren't being considered equal even though they were both of the same type and had the same id as per the documentation.


After a bit of binging with Google I came across an interesting post by <a href="https://rails.lighthouseapp.com/projects/8994/tickets/3120-activerecordbase-is-non-commutative-when-comparing-a-loaded-versus-initialized-object">fritz describing the code of '=='</a>:


~~~ruby

      # Returns true if the +comparison_object+ is the same object, or is of the same type and has the same id.
      def ==(comparison_object)
        comparison_object.equal?(self) ||
          (comparison_object.instance_of?(self.class) &&
            comparison_object.id == id &&
            !comparison_object.new_record?)
      end
~~~

In fact the '==' code also takes into account whether or not the object passed to '==' is new or not and since in our code we had 'u == u2' it would return false.

If we had 'u2 == u' then it would have passed!

Our current solution to the problem is to compare the ids of the objects in our code rather than the objects themselves but fritz also describes a way to monkey patch the '==' method to make it a bit more useful.
