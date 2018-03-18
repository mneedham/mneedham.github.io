+++
draft = false
date="2010-11-09 18:37:10"
title="Active Record: Nested attributes"
tag=['ruby', 'active-record']
category=['Ruby']
+++

I recently learnt about quite a neat feature of Active Record called <a href="http://api.rubyonrails.org/classes/ActiveRecord/NestedAttributes/ClassMethods.html">nested attributes</a> which allows you to save attributes on associated records of a parent model. 

It's been quite useful for us as we have a few pages in our application where the user is able to update models like this.

We would typically end up with parameters coming into the controller like this:


~~~ruby

class FoosController < ApplicationController
   def update
      # params = { :id => "1", :foo => { :baz => "new_baz", :bar_attributes => { :value => "something" } } }
      Foo.update_instance(params[:id], params[:foo])
      ...
   end
end
~~~

Our original implementation of 'update_instance' looked like this:


~~~ruby

class Foo < ActiveRecord::Base
   has_one :bar

   class << self
      def update_instance(id, attributes_to_update)
         instance = Foo.find(id)
         instance.attributes = attributes_to_update
         instance
      end
   end
end
~~~

Unfortunately when we execute that code the 'bar' association gets completely removed because we didn't specify the id of 'bar' when we were updating the attributes.

We need to change the code slightly to make sure it doesn't do that:


~~~ruby

class Foo < ActiveRecord::Base
   has_one :bar

   class << self
      def update_instance(id, attributes_to_update)
         instance = Foo.find(id)
         attributes_to_update[:bar_attributes][:id] = instance.bar.id
         instance.attributes = attributes_to_update
         instance
      end
   end
end
~~~

It now works as we'd expect.

There's other cool stuff that you can do with nested attributes described on the documentation page if you have 'has_many' associations but for now we're just using the simpler 'has_one'.

