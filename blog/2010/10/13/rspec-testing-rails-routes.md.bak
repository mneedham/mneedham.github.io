+++
draft = false
date="2010-10-13 18:25:32"
title="RSpec: Testing Rails routes"
tag=['rails', 'rspec']
category=['Ruby']
+++

Something which I keep forgetting is how to write controller tests where I want to check whether an action correctly redirected to another action.

With most of the routes in our application we've created a 'resourceful route' where each action maps to a CRUD operation in the database.

We can do that with this type of code in routes.rb:


~~~ruby

ActionController::Routing::Routes.draw do |map|
	map.resources :foos
end
~~~

<a href="http://guides.rubyonrails.org/routing.html#paths-and-urls">Several helper methods based on named rotes get created and included in our controllers</a> when we do this and we have access to those inside our specs.

We can see the named routes by executing the following command from the terminal:


~~~text

mneedham@markneedham.local ~/SandBox/rails_test$ rake routes CONTROLLER=foos
(in /Users/mneedham/SandBox)
    foos GET    /foos(.:format)          {:action=>"index", :controller=>"foos"}
         POST   /foos(.:format)          {:action=>"create", :controller=>"foos"}
 new_foo GET    /foos/new(.:format)      {:action=>"new", :controller=>"foos"}
edit_foo GET    /foos/:id/edit(.:format) {:action=>"edit", :controller=>"foos"}
     foo GET    /foos/:id(.:format)      {:action=>"show", :controller=>"foos"}
         PUT    /foos/:id(.:format)      {:action=>"update", :controller=>"foos"}
         DELETE /foos/:id(.:format)      {:action=>"destroy", :controller=>"foos"}
~~~

The following helper methods would be created for this resource as per the documentation in resources.rb:

<blockquote>
    #   Named Route   Helpers
    #   ============  =====================================================
    #   foos          foos_url, hash_for_foos_url,
    #                 foos_path, hash_for_foos_path
    #
    #   foo           foo_url(id), hash_for_foo_url(id),
    #                 foo_path(id), hash_for_foo_path(id)
    #
    #   new_foo       new_foo_url, hash_for_new_foo_url,
    #                 new_foo_path, hash_for_new_foo_path
    #
    #   edit_foo      edit_foo_url(id), hash_for_edit_foo_url(id),
    #                 edit_foo_path(id), hash_for_edit_foo_path(id)
</blockquote>

Keeping this in mind means that if we do something like this inside our 'create' action:


~~~ruby

class FoosController < ApplicationController
   def create
      ...
      redirect_to :action => :index
   end
end
~~~

We'd be able to test that redirection with a spec along the following lines:


~~~ruby

describe "POST create" do
   it "should redirect back to the index page" do
      post :create, :foo => { :bar => "value" }

      response.should redirect_to foos_path
   end
end
~~~

We can also use any of those other helper methods inside our tests which seems obvious looking at it now but wasn't for me until a colleague pointed it out.

It is pretty cool to be able to write specs like this and they seem much more readable than the equivalents you'd be able to test around ASP.NET MVC code in C#.
