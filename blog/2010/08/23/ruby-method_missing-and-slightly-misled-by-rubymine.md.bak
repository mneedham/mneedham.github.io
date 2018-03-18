+++
draft = false
date="2010-08-23 21:07:46"
title="Ruby: 'method_missing' and slightly misled by RubyMine"
tag=['ruby']
category=['Ruby']
+++

Another library that we're using on my project is <a href="http://am.rubyonrails.org/">ActionMailer</a> and before reading through the documentation I was confused for quite a while with respect to how it actually worked.

We have something similar to the following piece of code...


~~~ruby

Emailer.deliver_some_email
~~~

...which when you click its definition in RubyMine takes you to this class definition:


~~~ruby

class Emailer < ActionMailer::Base
	def some_email
		recipients "some@email.com"
		from "some_other_email@whatever.com"
		# and so on
	end
end
~~~

I initially thought that method was called 'deliver_some_mail' but having realised that it wasn't I was led to the 'magic' that is 'method_missing' on 'ActionMailer::Base' which is defined as follows:


~~~ruby

module ActionMailer
...
	class Base
		def method_missing(method_symbol, *parameters) #:nodoc:
        		if match = matches_dynamic_method?(method_symbol)
          		case match[1]
            			when 'create'  then new(match[2], *parameters).mail
            			when 'deliver' then new(match[2], *parameters).deliver!
            			when 'new'     then nil
            			else super
          		end
        		else
				super
        		end
		end
	end
end
~~~

The 'matches_dynamic_method?' function allows us to extract 'some_email' from the 'method_symbol'. That value is then passed into the object's initializer method and is eventually called executing all the code inside that method.


~~~ruby

        def matches_dynamic_method?(method_name) #:nodoc:
          method_name = method_name.to_s
          /^(create|deliver)_([_a-z]\w*)/.match(method_name) || /^(new)$/.match(method_name)
        end
~~~

Reading through the documentation, the author gives the following reasons for having separate 'create' and 'deliver' methods:


~~~text

ApplicationMailer.create_signed_up("david@loudthinking.com")  # => tmail object for testing
ApplicationMailer.deliver_signed_up("david@loudthinking.com") # sends the email
ApplicationMailer.new.signed_up("david@loudthinking.com")     # won't work!
~~~

In C# or Java I think we'd probably use another object to build up the message and then pass that to the 'Emailer' to deliver it so it's quite interesting that both these responsibilities are in the same class.

It also takes care of rendering templates and from what I can tell the trade off for having this much complexity in one class is that it makes it quite easy for the library's clients - we just have to extend 'ActionMailer::Base' and we have access to everything that we need.
