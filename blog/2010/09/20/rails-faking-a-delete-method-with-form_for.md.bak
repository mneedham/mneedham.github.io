+++
draft = false
date="2010-09-20 18:52:15"
title="Rails: Faking a delete method with 'form_for'"
tag=['ruby', 'rails']
category=['Ruby']
+++

We recently had a requirement to delete an item based on user input and wanting to adhere to the 'RESTful' approach that Rails encourages we therefore needed to fake a HTTP Delete method request.

The <a href="http://guides.rubyonrails.org/form_helpers.html#how-do-forms-with-put-or-delete-methods-work">documentation talks a little about this</a>:


<blockquote>
The Rails framework encourages RESTful design of your applications, which means you’ll be making a lot of “PUT” and “DELETE” requests (besides “GET” and “POST”). However, most browsers don’t support methods other than “GET” and “POST” when it comes to submitting forms.

Rails works around this issue by emulating other methods over POST with a hidden input named "_method", which is set to reflect the desired method:
</blockquote>

The example provided is for the 'form_tag' helper method where you just need to pass a hash containing an entry with a key ':method' and value 'delete'.

We tried to do the same with 'form_for' but unfortunately found that that the hidden '_method' field was still being set to 'POST'.

It turns out that 'form_for' expects the ':method' to be provided as part of the right hand most argument as part of a hash with the key ':html'.

We therefore need to write something like this if we want to simulate a delete request:


~~~ruby

 <% form_for(item, :html => {:method => 'delete'}) do  %>
 ...
 <% end %>
~~~

The hidden field is eventually created inside <a href="http://github.com/rails/rails/blob/master/actionpack/lib/action_view/helpers/form_tag_helper.rb">form_tag_helper.rb</a>:


~~~ruby

def extra_tags_for_form(html_options)
          ...
          method_tag = case method
            when /^get$/i # must be case-insensitive, but can't use downcase as might be nil
              html_options["method"] = "get"
              ''
            when /^post$/i, "", nil
              html_options["method"] = "post"
              token_tag
            else
              html_options["method"] = "post"
              tag(:input, :type => "hidden", :name => "_method", :value => method) + token_tag
          end

         ...
end
~~~

I'm not finding the method signatures of many Ruby libraries particularly intuitive at the moment. 

It seems like a lot of times the favoured approach is to pass in a hash into methods and then work off implicit knowledge that Ruby/Rails programmers have about the way that hashes are typically used.

While this makes methods very flexible it seems more difficult to understand how to use them as a consumer than if they took in specifically typed values as parameters.

It'll be interesting to see if/how my opinion changes with respect to this.

