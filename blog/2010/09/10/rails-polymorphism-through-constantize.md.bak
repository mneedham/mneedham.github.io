+++
draft = false
date="2010-09-10 21:26:04"
title="Rails: Polymorphism through 'constantize'"
tag=['ruby']
category=['Ruby']
+++

One interesting feature of Rails which <a href="http://in.linkedin.com/in/shishirdas">Shishir</a> pointed out the other day is the ability to take a user provided value and make use of Active Support's 'constantize' method to effectively achieve polymorphism directly from the user's input.

As an example if we were creating different types of widgets from the same web page we might have several different forms that the user could submit.

We could have a hidden field representing the type of the widget like so:


~~~html

 <%= hidden_field_tag :widget_name, :foo  %>
~~~

And then when the form is submitted we can instantiate the appropriate widget class.


~~~ruby

class WidgetController
  def some_action
     widget_name.constantize.new(params)
  end

  def widget_name
    "#{params[:widget_name]}_widget".camelize
  end
end
~~~

Where the individual widget classes would be like this:


~~~ruby

class FooWidget

end
~~~


~~~ruby

class BarWidget

end
~~~

The closest we'd get to doing this with C#/associated frameworks would be to create a dictionary with the widget name as the key and a function representing the object instantiation as the value.

Therefore if we wanted to add a new widget we'd still have to change the WidgetController whereas with the Rails solution we'd just have to change the HTML and add a new report which would then be automatically hooked up.

I'm sure there's some other clever things you can do with Rails that I don't yet know about but this struck me as one of those things that helps explain why it's possible to develop some web applications much more quickly with Rails than with other frameworks. 
