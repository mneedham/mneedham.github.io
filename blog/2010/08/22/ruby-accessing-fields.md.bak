+++
draft = false
date="2010-08-22 18:26:17"
title="Ruby: Accessing fields"
tag=['ruby']
category=['Ruby']
+++

I've spent a little time browsing through some of the libraries used by my project and one thing which I noticed in <a href="http://as.rubyonrails.org/">ActiveSupport</a> is that fields don't seem to be accessed directly but rather are accessed through a method which effectively encapsulates them inside the object.

For example the following function is defined in 'inheritable_attributes.rb'


~~~ruby

  def write_inheritable_attribute(key, value)
    if inheritable_attributes.equal?(EMPTY_INHERITABLE_ATTRIBUTES)
      @inheritable_attributes = {}
    end
    inheritable_attributes[key] = value
  end
~~~


~~~ruby

  def inheritable_attributes
    @inheritable_attributes ||= EMPTY_INHERITABLE_ATTRIBUTES
  end
~~~


~~~ruby

EMPTY_INHERITABLE_ATTRIBUTES = {}.freeze unless const_defined?(:EMPTY_INHERITABLE_ATTRIBUTES)
~~~

If we were using C# we'd have instantiated '@inheritable_attributes' at the field definition with 'EMPTY_INHERITABLE_ATTRIBUTES' like so...


~~~csharp

public class SomeClass {
	private Dictionary<string, object> inheritableAttributes = new Dictionary<string, object>();
}
~~~

...but we can't do that in Ruby because we don't need to explicitly define all our fields, we just start using them.

I'm assuming this is quite a common pattern in Ruby and in a way it's quite neat because it restricts the number of direct field  references which will make it easier to change the underlying implementation.  <a href="http://www.markhneedham.com/blog/2010/07/05/the-limited-red-society-joshua-kerievsky/">Kerievsky's narrowed change refactoring</a> suddenly becomes less necessary!

For that reason I wonder whether it would be a useful pattern in C#/Java or if it would be overkill.
