+++
draft = false
date="2010-09-12 14:25:06"
title="Ruby: FactoryGirl & declarative_authorization - Random thoughts"
tag=['ruby']
category=['Ruby']
+++

Two other gems that we're using on my current project are <a href="http://github.com/thoughtbot/factory_girl">FactoryGirl</a> and <a href="http://github.com/stffn/declarative_authorization">declarative_authorization</a>.

We use declarative_authorization for controlling access to various parts of the application and FactoryGirl allows us to build objects for use in our tests.

We wanted to be able to deactivate the authorization when creating test objects because otherwise our test wouldn't have permission to create certain objects.

Our original approach was to create a 'God' role which we could assign to the 'current_user' in our tests therefore allowing us to create whatever objects we wanted.

The problem with this approach is that it means we end up creating this role as part of the production data.

One way to get around this is to put an if statement into the seed data where the role creation happens and only allow that role to be created in test/development environments but that's a bit of a hack.

In any case declarative_authorization provides a function to get around this problem and if we pass a block to that function any code executed within the block will be free of the authorization rules setup:


~~~ruby

require 'declarative_authorization/maintenance'
include Authorization::TestHelper

without_access_control do
	Factory(:foo, :bar => "myBar")
end
~~~

This works pretty well and there is <a href="http://github.com/stffn/declarative_authorization">more documentation on the github page</a>.

Unfortunately we already had 400 or so usages of the Factory throughout the code base which weren't wrapped with 'without_access_control' and had been relying on the 'God' role.

We'd have the same problem if we created a 'create_without_access_control' method on Factory as well so came up with the idea of overriding the 'create' method of FactoryGirl to always be called inside the 'without_access_block':


~~~ruby

require 'declarative_authorization/maintenance'
include Authorization::TestHelper

class Factory
  class << self
    alias_method :original_create, :create

    def create(name, overrides = {})
      without_access_control do
        original_create(name, overrides)
      end
    end
  end
end
~~~

This helps solve the problem although I guess it could be quite misleading since the 'create' method being called would be a different one than you might expect.

On the other hand FactoryGirl is only being used to create tests objects and we never directly test our authorization functionality using FactoryGirl so it doesn't seem to be too much of a problem to change it in this way.
