+++
draft = false
date="2010-10-18 04:24:22"
title="Ruby: Using alias with 'indexers'"
tag=['ruby']
category=['Ruby']
+++

I've been browsing through some of the Rails routing code while following <a href="http://weblog.jamisbuck.org/2006/10/2/under-the-hood-rails-routing-dsl">Jamis' Buck's blog post</a> and I came across something I hadn't seen before while inside the 'NamedRouteCollection' class.

The bit of code which initially confused me is in RouteSet.add_named_route:
 

~~~ruby

module ActionController
  module Routing
    class RouteSet
      def initialize
        ...
        self.named_routes = NamedRouteCollection.new
      end

      def add_named_route(name, path, options = {})
        # TODO - is options EVER used?
        name = options[:name_prefix] + name.to_s if options[:name_prefix]
        named_routes[name.to_sym] = add_route(path, options)
      end	
    end
  end
end
~~~

Reading the code on line 12 I was convinced that this code was being used to set a value into an array or hash so I was confused as to how the url/path helper methods which get added for named routes were being created since there didn't seem to be any code which was calling the method in 'NamedRouteCollection' which would create them.

I eventually stumbled into the initializer code above which made me realise that 'named_routes' wasn't actually a hash or array but an instance of 'NamedRouteCollection'.

The methods '[]=' and '[]' are aliases which call the 'add' and 'get' methods on 'NamedRouteCollection'


~~~ruby

module ActionController
  module Routing
    class RouteSet
      class NamedRouteCollection
        def add(name, route)
          routes[name.to_sym] = route
          define_named_route_methods(name, route) # creates the helper methods
        end

        def get(name)
          routes[name.to_sym]
        end

        alias []=   add
        alias []    get
      end
    end
  end
end
~~~

For me it seems like perhaps the creation of the helper methods could be the responsibility of another object although I can see why it's been put in NamedRouteCollection since those helper methods are only created if you have a named route.

Either way it was pretty confusing for me initially that you could create this type of side effect from a method call that looked like it was just adding a key, value pair to an array.
