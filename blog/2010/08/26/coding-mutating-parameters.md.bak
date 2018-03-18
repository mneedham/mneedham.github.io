+++
draft = false
date="2010-08-26 07:47:23"
title="Coding: Mutating parameters"
tag=['coding']
category=['Coding']
+++

One of the earliest rules of thumb that I was taught by my colleagues is the idea that we should try and avoid mutating/changing values passed into a function as a parameter.

The underlying reason as I understand it is that if you're just skimming through the code you wouldn't necessarily expect the values of incoming parameters to be different depending where in the function they're used.

I think the most dangerous example of this is when we completely change the value of a parameter, like so:


~~~java

public class SomeClass
{
	public BigDecimal doSomeCalculationsOn(BigDecimal value) {   
		value = value.divide(new BigDecimal("3.2"));
		// some other calculation  on value...
		// and we keep on re-assigning value until we return the value
		return value;  
	}
}
~~~

In this case the function is really small so maybe it doesn't make that much difference readability wise but I still think it would be better if we didn't reassign the result of the calculation to 'value' but instead used a new variable name.

It wouldn't require a very big change to do that:


~~~java

public class SomeClass
{
	public BigDecimal doSomeCalculationsOn(BigDecimal value) {   
		BigDecimal newValue = value.divide(new BigDecimal("3.2"));
		// some other calculation  on newValue...
		// and we keep on re-assigning newValue until we return the newValue
		return newValue;  
	}
}
~~~

Unless the function in question is the <a href="http://en.wikipedia.org/wiki/Identity_function">identity function</a> I find it very weird when I read code which seems to return the same value that's been passed into the function.

The other way that function parameters get changed is when we mutate the values directly. The <a href="http://www.markhneedham.com/blog/2010/01/23/coding-the-collecting-parameter-pattern/">collecting parameter pattern</a> is a good example of this.

That seems to be a more common pattern and since the function names normally reveal intent better it's normally less confusing. 

It does become <a href="http://www.markhneedham.com/blog/2009/09/16/coding-watch-out-for-mutable-code/">more problematic if we're mutating an object in loads of places based on conditional statements because we can lose track of how many times it's been changed</a>.

Interestingly some of the code for <a href="http://github.com/rails/rails/blob/master/actionpack">ActionPack</a> makes use of both of these approaches in the same function!

<a href="http://github.com/rails/rails/blob/master/actionpack/lib/action_view/helpers/form_options_helper.rb">form_options_helper.rb</a>


~~~ruby

      def to_collection_select_tag(collection, value_method, text_method, options, html_options)
        html_options = html_options.stringify_keys
        add_default_name_and_id(html_options)
        ...
        content_tag(
          "select", add_options(options_from_collection_for_select(collection, value_method, text_method, :selected => selected_value, :disabled => disabled_value), options, value), html_options
        )
      end
~~~

<a href="http://github.com/rails/rails/blob/master/actionpack/lib/action_view/helpers/form_helper.rb">form_helper.rb</a>

~~~ruby

        def add_default_name_and_id(options)
          if options.has_key?("index")
            options["name"] ||= tag_name_with_index(options["index"])
          # and so on
          end
        end
~~~

I'm not sure how exactly I'd change that function so that it didn't mutate 'html_options' but I'm thinking perhaps something like this:


~~~ruby

	def create_html_options_with_default_name_and_id(html_options)
          options = html_options.stringify_keys
          if options.has_key?("index")
            options["name"] ||= tag_name_with_index(options["index"])
          # and so on
	end
~~~

And we could then change the other method to call it like so:


~~~ruby

      def to_collection_select_tag(collection, value_method, text_method, options, html_options)
	   html_options_with_defaults = create_html_options_with_default_name_and_id(html_options)
        ...
        content_tag(
          "select", add_options(options_from_collection_for_select(collection, value_method, text_method, :selected => selected_value, :disabled => disabled_value), options, value), html_options_with_defaults
        )
      end
~~~

I guess you could argue that the new function is doing more than one thing but I don't think it's too bad.

Looking back on these code examples after writing about them I'm not as confident that mutating parameters is as confusing as I originally thought...!
