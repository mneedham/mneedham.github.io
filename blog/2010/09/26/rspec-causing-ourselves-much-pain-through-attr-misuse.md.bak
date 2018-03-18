+++
draft = false
date="2010-09-26 18:57:53"
title="RSpec: Causing ourselves much pain through 'attr' misuse"
tag=['ruby', 'rspec']
category=['Ruby']
+++

While testing some code that we were mixing into one of our controllers we made what I thought was an interesting mistake.

The module we wanted to test had some code a bit like this...


~~~ruby

module OurModule
  def some_method
    @User = User.find(params[:id])

    # in the test code this is always true
    if @user == user
      ...
    end
  end
end
~~~

..and we had the spec setup like so:


~~~ruby

describe 'OurController' do
  class TestController
    include OurModule
    attr_accessor :user
  end
	
  before(:each) do
    @controller = TestController.new
    @controller.user = Factory(:user)
  end	

  it "should do something" do
    # whole load of setup not related to our mistake
    @controller.some_method
  end
end
~~~

We created the 'attr_accessor' so that we would be able to choose a value for 'user' to simulate the fact that Warden mixes in a 'user' method into our ApplicationController at runtime.

The problem we ran into was that both 'user' and '@user' inside 'some_method' were always returning the same value even though we set 'user' to be something else in our spec before each spec is run.

We eventually <a href="http://www.markhneedham.com/blog/2008/11/04/pair-programming-benefits-of-the-pair-switch-mid-story/">rotated pairs</a> and immediately realised that the reason that was happening was because 'user' was in fact referring to the value we'd just set for '@user' since in the test 'user' is created by an 'attr_accessor' call.

As it turns out Warden also mixes in a 'current_user' method so we changed the code to make use of that instead of 'user' since that was the team's agreed standard and the call to 'user' hadn't yet been replaced.

It does show an interesting side effect of setting instance variables in modules and also suggested that we had setup the test wrong to being with.

A better approach would have been to simulate what the actual code would do more closely and define a 'user' method which returned a canned user in a way that only relied on code in the test and wouldn't change based on what the system under test did.
