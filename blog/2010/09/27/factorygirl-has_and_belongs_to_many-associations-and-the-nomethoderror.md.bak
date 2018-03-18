+++
draft = false
date="2010-09-27 14:18:48"
title="FactoryGirl: 'has_and_belongs_to_many' associations and the 'NoMethodError'"
tag=['ruby', 'factorygirl']
category=['Ruby']
+++

We ran into a somewhat frustrating problem while using <a href="http://github.com/thoughtbot/factory_girl">Factory Girl</a> to create an object which had a 'has_and_belongs_to_many' association with another object.

The relevant code in the two classes was like this..


~~~ruby

class Bar < ActiveRecord::Base
	has_and_belongs_to_many :foos, :class_name => "Foo", :join-table => "bar_foos"
end
~~~ 


~~~ruby

class Foo < ActiveRecord::Base
	has_many :bars
end
~~~

...and we originally defined our 'Bar' factory like so:


~~~ruby

Factory.define :bar do |f|
  f.association(:foos, :factory => :foo)
end
~~~


~~~ruby

Factory.define :foo do |f|
   ...
end
~~~

On calling the following in our test


~~~ruby

Factory(:bar)
~~~

we ended up with this stack trace: 


~~~text

NoMethodError in 'SomeController GET for some action'
undefined method `each' for #<Bar:0x102faabd8>
/Users/mneedham/.rvm/gems/jruby-1.5.1/gems/activerecord-2.3.5/lib/active_record/attribute_methods.rb:260:in `method_missing'
/Users/mneedham/.rvm/gems/jruby-1.5.1/gems/activerecord-2.3.5/lib/active_record/associations/association_collection.rb:320:in `replace'
/Users/mneedham/.rvm/gems/jruby-1.5.1/gems/activerecord-2.3.5/lib/active_record/associations.rb:1325:in `foos='
/Users/mneedham/.rvm/gems/jruby-1.5.1/gems/factory_girl-1.3.2/lib/factory_girl/proxy/build.rb:13:in `send'
/Users/mneedham/.rvm/gems/jruby-1.5.1/gems/factory_girl-1.3.2/lib/factory_girl/proxy/build.rb:13:in `set'
/Users/mneedham/.rvm/gems/jruby-1.5.1/gems/factory_girl-1.3.2/lib/factory_girl/proxy/build.rb:17:in `associate'
/Users/mneedham/.rvm/gems/jruby-1.5.1/gems/factory_girl-1.3.2/lib/factory_girl/attribute/association.rb:15:in `add_to'
/Users/mneedham/.rvm/gems/jruby-1.5.1/gems/factory_girl-1.3.2/lib/factory_girl/factory.rb:324:in `run'
/Users/mneedham/.rvm/gems/jruby-1.5.1/gems/factory_girl-1.3.2/lib/factory_girl/factory.rb:322:in `each'
/Users/mneedham/.rvm/gems/jruby-1.5.1/gems/factory_girl-1.3.2/lib/factory_girl/factory.rb:322:in `run'
/Users/mneedham/.rvm/gems/jruby-1.5.1/gems/factory_girl-1.3.2/lib/factory_girl/factory.rb:250:in `build'
/Users/mneedham/SandBox/ruby/some_controller_spec.rb:7:
~~~

The problem is that the Active Record code assumes that it will be passed an array when the 'foo=' method is called on the proxy 'Bar' object it creates. Unfortunately we're passing a single 'Foo'.

Instead we need to use the more verbose syntax and wrap the call to association in an array:


~~~ruby

Factory.define :bar do |f|
  f.foos { |a| [a.association(:bar)] }
end
~~~

<a href="http://ditoinfo.wordpress.com/2008/11/19/factory-girl-and-has_many-has_many-through-associations/">Dante Regis has written about this before</a> but I found it sufficiently sufficiently frustrating that I thought I'd document it as well.
