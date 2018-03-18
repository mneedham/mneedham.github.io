+++
draft = false
date="2010-10-24 17:30:26"
title="Ruby: Mocking or stubbing methods on the system under test"
tag=['ruby']
category=['Ruby']
+++

An approach to testing which I haven't seen before and am therefore assuming is more specific to Ruby is the idea of stubbing or mocking out functions on the system under test.

I've come across a couple of situations where this seems to be done:

<ol>
<li>When stubbing out calls to methods which are being mixed into the class via a module</li>
<li>When stubbing out calls to private methods within the class</li>
</ol>

I think the first approach is fine because typically we'll have a direct test against that module's methods elsewhere and it doesn't make much sense to test the same thing again.

I initially liked the second approach as well because it simplifies the spec we're writing.

For example if we have this code:


~~~ruby

class FoosController : ApplicationController
   def index
      populate_something
   end

   private

   def populate_something
      @something = Something.find(...)    
   end
end
~~~

Then by stubbing out 'populate_something' we can write a spec like this:


~~~ruby

describe FoosController do
   it "should populate something" do
      controller.stub(:populate_something) # and so on

      get :index
   end
end
~~~

Rather than:


~~~ruby

describe FoosController do
   it "should populate something" do
      Something.stub(:find) # and so on

      get :index
   end
end
~~~

This is a fairly contrived example of course and the temptation to stub out a method on the system under test increases as the amount of dependencies and the complexity of them increases.

The problem we create for ourselves is that if we want to change the internal structure of our class, perhaps by inlining those private methods, then we'll end up with specs failing even if the external behaviour remains exactly the same.

My current thinking is that if we get in a situation where we want to stub out something on the system under test then it'd probably be better to listen to that pain and try and work out a cleaner way of solving the problem.
