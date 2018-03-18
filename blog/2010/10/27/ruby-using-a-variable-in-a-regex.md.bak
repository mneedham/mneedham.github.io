+++
draft = false
date="2010-10-27 13:55:27"
title="Ruby: Using a variable in a  regex"
tag=['ruby']
category=['Ruby']
+++

We're using Web Mock on my current project to stub out some of the external web requests in some of our integration tests and I managed to get myself very confused while trying to use a variable inside a regular expression that I was trying to pass to the 'stub_request' method.

The code was roughly like this:


~~~ruby

some_url = "http://service.com/method"

stub_request(:any, /some_url/).
        to_return(:body => File.new('/path/to/some.xml'),
                                      :headers => {'Content-Length' => 666, 'Content-Type' => 'text/xml'},
                  :status => 200,
                  :headers => {'Content-Type' => 'text/xml'}) 
~~~

The request was being stubbed when I hard coded the url inside the regular expression but not being stubbed when I used the variable like in the example above.

I somehow missed the blindingly obvious in hindsight solution of treating variables inside a regular expression as if they were being used in a string.

If we wrap the variable inside '#{}' then our problem is solved:


~~~ruby

some_url = "http://service.com/method"

stub_request(:any, /#{some_url}/).
        to_return(:body => File.new('/path/to/some.xml'),
                                      :headers => {'Content-Length' => 666, 'Content-Type' => 'text/xml'},
                  :status => 200,
                  :headers => {'Content-Type' => 'text/xml'}) 
~~~

I still can't quite believe I didn't spot it straight away.

