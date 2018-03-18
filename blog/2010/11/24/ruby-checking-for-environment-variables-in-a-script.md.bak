+++
draft = false
date="2010-11-24 18:34:45"
title="Ruby: Checking for environment variables in a script"
tag=['ruby']
category=['Ruby']
+++

I've been working on a Ruby script to allow us to automate part of our <a href="http://lucene.apache.org/solr/">Solr</a> data setup and part of the task was to check that some environment variables were set and throw an exception if not.

I got a bit stuck initially trying to work out how to return a message showing only the missing environment variables but it turned out to be pretty simple when I came back to it a couple of hours later.

So for my future reference than anything else, this is what I ended up with:


~~~ruby

  variables = %w{VARIABLE_1 VARIABLE_2}
  missing = variables.find_all { |v| ENV[v] == nil }
  unless missing.empty?
    raise "The following variables are missing and are needed to run this script: #{missing.join(', ')}."
  end
~~~

I recently came across '%w' which creates a string array out of the values that we specify.

In this case we therefore end up with...


~~~ruby

> %w{VARIABLE_1 VARIABLE_2}
["VARIABLE_1", "VARIABLE_2"]
~~~

...which I think is pretty neat!

The other neat method is 'join' on line 4 which concatenates all the elements of an array while putting the provided separator in between each element.

In this case if we had neither of the variables specified we'd end up with the following:


~~~ruby

> ["VARIABLE_1", "VARIABLE_2"].join(', ')
"VARIABLE_1, VARIABLE2"
~~~


