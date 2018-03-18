+++
draft = false
date="2010-09-08 18:54:50"
title="Ruby: Checking an array contains an item"
tag=['ruby']
category=['Ruby']
+++

A couple of times in the past few days I've wanted to check if a particular item exists in an array and presumably influenced by working for too long with the .NET/Java APIs I keep expecting there to be a 'contains' method that I can call on the array!

More as an attempt to help myself remember than anything else, the method we want is actually called 'include?'.

Therefore...


~~~ruby

[1,2,3].include?(2)
=> true
~~~


~~~ruby

[1,2,3,4].include?(5)
=> false
~~~

One other quite neat thing is that we can use that in tests when we want to check that an array contains one item that we're expecting. 

This is much better than having to specify a specific index which is what we often seem to end up doing in Java/C#.

We therefore end up with (RSpec) tests similar to this:

~~~ruby

response.flash[:error].include?("Some error message").should be_true
~~~
