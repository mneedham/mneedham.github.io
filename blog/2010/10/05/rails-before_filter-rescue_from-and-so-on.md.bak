+++
draft = false
date="2010-10-05 08:53:48"
title="Rails: before_filter, rescue_from and so on"
tag=['ruby', 'rails']
category=['Ruby']
+++

One thing I've noticed while browsing our Rails code base is that the first entry point inside a controller is much less frequently the method corresponding to the action than it would be with a C# ASP.NET MVC application.

The concept of filters exists in ASP.NET MVC but on the projects I've worked on they've been used significantly less than before filters would be in a Rails application.

As a result I'm getting much more in the habit of checking for the before filters in the ApplicationController when an action isn't working as expected to try and figure out what's going on.

One which caught us out the other day is the 'rescue_from' method which gets mixed in from Rescuable.

Every single time we tried to login we were just getting redirected back to the login page again with no exception being reported anywhere.

Eventually we realised that the InvalidAuthenticityToken exception was being thrown because we somehow had a different token stored in our browser's cookie than was in the form.

Since our LoginController extends the ApplicationController, the following logic was being used to handle the exception:


~~~ruby

class ApplicationController < ActionController::Base
   rescue_from ActionController::InvalidAuthenticityToken, :with => :redirect_to_referer

  def redirect_to_referer_or_path
    redirect_to request.referer
  end
~~~

We initially didn't spot it because it was hidden away between a whole load of other before filters and includes of modules.

The convention as far as I can tell is to try and keep as little code as possible inside the action method and handle common logic - such as looking up a user based on an id or handling exceptions - in filters.

It helps to keep the code inside actions pretty clean and remove duplication but I just need to remember to check both the action and the top of the class for any filters when investigating problems. 
