+++
draft = false
date="2010-09-30 07:03:07"
title="RSpec: Another newbie mistake"
tag=['ruby']
category=['Ruby']
+++

We recently had a spec which was checking that we didn't receive a call to a specific method on an object...


~~~ruby

describe "Our Object" do
	it "should not update property if user is not an admin" do
		our_user = Factory("user_with_role_x)
		User.stub!(:find).and_return(our_user)

		user.stub!(:is_admin?).and_return(false)
		user.should_not_receive(:property)
	end
end
~~~

...where 'property' refers to a field in the users table. In the code 'property' would get set like this:


~~~ruby

class ObjectUnderTest

	def method_under_test
		user = User.find 4

		if user.is_admin?
			user.property = "random value"			
		end
	end
~~~

That test always passed but when we wrote the test to check that 'property' would be set if the user was an admin we found that it always failed.

The mistake is quite simple - the method that we wanted to check was received is actually called 'property=' rather than 'property'!

Changing the spec to read like this solves the problem:


~~~ruby

describe "Our Object" do
	it "should describe something" do
		our_user = Factory("user_with_role_x)
		User.stub!(:find).and_return(our_user)

		user.stub!(:is_admin?).and_return(false)
		user.should_not_receive(:property=)
	end
end
~~~

It didn't take that long to figure it out but this is certainly a mistake you wouldn't be able to make in a statically typed language.
