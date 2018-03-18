+++
draft = false
date="2010-08-31 01:22:14"
title="Rails: Populating a dropdown list using 'form_for'"
tag=['ruby', 'rails']
category=['Ruby']
+++

Last week we were trying to make use of <a href="http://api.rubyonrails.org/classes/ActionView/Helpers/FormHelper.html">Rails' 'form_for' helper</a> to populate a dropdown list with the values of a collection that we'd set to an instance variable in our controller.

My colleague pointed out that we'd need to use '<a href="http://api.rubyonrails.org/classes/ActionView/Helpers/FormOptionsHelper.html#method-i-collection_select">collection_select</a>' in order to do this.

We want to put the values in the 'foos' collection onto the page. 'foos' is a hash which defines some display values and their corresponding values like so:


~~~ruby

class FooController < ActionController::Base
	def index
		# @mainFoo defined with some value irrelevant to this example
		@foos = { "value1" => 1, "value2" => 2 }
	end
end
~~~

The code we need to do this looks like this:


~~~text

<%form_for @mainFoo, :html => { :name=> "ourForm", :id=> "ourForm" },:url => {:controller => "foo", :action => :bar} do | mainFoo |%>

<%= foo.collection_select :foo_id, {"Please select"=>""}.merge!(@foos), :last, :first, { :selected => "Please select" }, {:name => "foo", :id => "foo"} %>
~~~

The method signature that we're passing those parameters to reads like this:


~~~ruby

def collection_select(method, collection, value_method, text_method, options = {}, html_options = {})
~~~

In this case we want the selected value to always be 'Please select' so we need to specify that in the 'options' hash. If 'selected' wasn't specified in the hash then the code would try to make the selected value @mainFoo.foo_id which in this case has no value anyway.

The other thing which I thought was quite neat is the way that you need to provided the 'value_method' and 'text_method' as parameters so that the dropdown list can be constructed with the appropriate labels and values.

In this case we have the display values as the keys in the hash and the values as the values in the hash so we can retrieve those entries from the collection by using the ':last' and ':first' methods.

We end up in the following method:


~~~ruby

      def options_from_collection_for_select(collection, value_method, text_method, selected = nil)
        options = collection.map do |element|
          [element.send(text_method), element.send(value_method)]
        end
~~~

This creates an array of arrays which is used later on.

In our case the values passing through this method would read like this:


~~~ruby

        collection = { "value1" => 1, "value2" => 2 }
		
        options = collection.map do |element|
          [element.send(text_method), element.send(value_method)]
        end
~~~


~~~text

 => [["value1", 1], ["value2", 2]] 
~~~

I was initially a bit confused about how we were able to call the 'collection_select' method on 'mainFoo' but <a href="http://github.com/rails/rails/blob/master/actionpack/lib/action_view/helpers/form_helper.rb">a quick browse of the ActionPack code</a> showed that 'mainFoo' actually represents a wrapper around that object rather than the object itself. 
