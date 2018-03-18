+++
draft = false
date="2010-09-17 19:53:37"
title="Ruby: Testing declarative_authorization"
tag=['ruby']
category=['Ruby']
+++

<a href="http://www.markhneedham.com/blog/2010/09/12/ruby-factorygirl-declarative_authorization-random-thoughts/">As I mentioned in a post earlier in the week</a> we're using the <a href="http://github.com/stffn/declarative_authorization">declarative_authorization</a> gem to control access to various parts of our application and as we've been migrating parts of the code base over to use that framework one thing we've noticed is that there seems to be a diminishing return in how much value we get from writing specs to cover each rule that we create. 

We found that while it is possible to write a spec to cover every single rule it sometimes seems like the spec is just duplicating what the rule already describes.

This is especially the case if the rule just describes access to a particular controller action.

For example we had something similar to the following:


~~~ruby

  role :x do
    has_permission_on :some, :to => [:action_1, :action_2, :action_3]
  end
~~~

For which we wrote specs similar to this (which make use of the <a href="http://www.tzi.org/~sbartsch/declarative_authorization/master/classes/Authorization/TestHelper.html">test helpers provided with the framework</a>):


~~~ruby

context "user with role x" do
  before(:each) do
    @some_user = Factory.build(:user_with_role_x)
    Authorization.current_user=@some_user
  end
  context "some controller" do
    [:action_1, :action_2, :action_3].each do |action|
      it "should be allow to view #{action}" do
        should_be_allowed_to action, :some
      end
    end
  end
end
~~~

It certainly seems to me that if the code we're writing uses a DSL then we lose the value of testing as a documentation feature and to an extent our tests are another slightly different DSL.

There is certainly still value in writing specs for more complicated rules where it is quite easy to write the code wrong but otherwise it seems like we're just increasing the build time (albeit slightly) without necessarily getting much value.

Another approach that we're using to test authorisation more indirectly is to ensure that we have automated tests at a higher level covering pieces of functionality which make use of the declarative authorization rules.

It doesn't make sense to cover every single rule with this type of test because they take longer to run but I think there is still some value in ensuring that everything is 'glued' together correctly.
