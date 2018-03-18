+++
draft = false
date="2010-10-18 15:52:28"
title="Coding: Context independent code"
tag=['coding']
category=['Coding']
+++

I've been flicking through <a href="http://www.growing-object-oriented-software.com/">Growing Object Oriented Software Guided By Tests</a> again and in Chapter 6 on Object Oriented Style I came across the part of the chapter which talks about writing context independent code which reminded me of some code I've worked on recently.

The authors suggest the following:

<blockquote>
A system is easier to change if its objects are context-independent; that is, if each object has no built-in knowledge about the system in which it executes
</blockquote>

I was writing a bit of code in our ApplicationHelper which would only be used in a certain context within one of the views.

The view code was roughly like this: 


~~~ruby

<% unless current_user.blank? %>
   <% if show_something_for(current_user) %>
      <!-- some html -->
   <% else %>
	 <!-- some other html -->
   <% end %>
<% end %>
~~~

with the 'show_something_for' method defined like so:


~~~ruby

module ApplicationHelper
   def show_something_for(user)
      user.has_foo? and user.has_bar?
   end
end
~~~

Inside the 'show_something_for' method we're working off the assumption that user will not be nil based on that fact that it's being used inside a context where we've already checked that we do in fact have a user.

It's not identical to the situation the authors are describing but there is an implicit assumption in this method which would mean that we couldn't necessarily just go and use it anywhere else in the code base and assume that it'd work.

Having said that, the code is slightly simpler than if we had to assume that 'user' might be nil.

The situation in which we don't have 'current_user' happens when no user has logged in so the method warden mixes into our ApplicationController returns nil. 

I think it would be possible to make use of the <a href="http://en.wikipedia.org/wiki/Null_Object_pattern">null object pattern</a> and store a guest user in the session but there are a fair few places in the code base that rely on the current implementation at the moment.
