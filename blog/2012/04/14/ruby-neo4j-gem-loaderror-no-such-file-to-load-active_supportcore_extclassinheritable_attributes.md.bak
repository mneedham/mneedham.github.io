+++
draft = false
date="2012-04-14 10:21:40"
title="Ruby: neo4j gem - LoadError: no such file to load -- active_support/core_ext/class/inheritable_attributes"
tag=['ruby']
category=['Ruby', 'neo4j']
+++

I've been playing around with neo4j again over the past couple of days using the <a href="https://github.com/andreasronge/neo4j">neo4j.rb</a> gem to build up a graph.

I installed the gem but then ended up with the following error when I tried to 'require neo4j' in 'irb':


~~~Text

LoadError: no such file to load -- active_support/core_ext/class/inheritable_attributes
  require at org/jruby/RubyKernel.java:1033
  require at /Users/mneedham/.rbenv/versions/jruby-1.6.7/lib/ruby/site_ruby/1.8/rubygems/custom_require.rb:36
   (root) at /Users/mneedham/.rbenv/versions/jruby-1.6.7/lib/ruby/gems/1.8/gems/neo4j-1.3.1-java/lib/neo4j.rb:9
  require at org/jruby/RubyKernel.java:1033
  require at /Users/mneedham/.rbenv/versions/jruby-1.6.7/lib/ruby/gems/1.8/gems/neo4j-1.3.1-java/lib/neo4j.rb:59
   (root) at src/main/ruby/neo_test.rb:2
~~~

It seems a few others <a href="https://github.com/andreasronge/neo4j/issues/150">have come across this problem as well</a> and the problem seems to be that ActiveSupport 3.2 isn't yet supported by the gem so we need to use an earlier version of that.

There were a few suggestions in the comments but it was the following that worked for me:


~~~text

sudo gem uninstall railties 
sudo gem install railties --version 3.1
~~~
