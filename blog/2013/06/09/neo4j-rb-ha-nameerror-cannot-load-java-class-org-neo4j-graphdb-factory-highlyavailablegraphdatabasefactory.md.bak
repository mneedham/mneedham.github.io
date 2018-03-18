+++
draft = false
date="2013-06-09 16:57:35"
title="neo4j.rb HA: NameError: cannot load Java class org.neo4j.graphdb.factory.HighlyAvailableGraphDatabaseFactory"
tag=['neo4j']
category=['neo4j']
+++

<p><a href="https://github.com/andreasronge/neo4j">neo4.rb</a> is a JRuby gem that allows you to create an <a href="http://docs.neo4j.org/chunked/stable/tutorials-java-embedded.html">embedded neo4j database</a> and last week I was working out how to setup a neo4j 1.8.2 HA cluster using the gem.</p>


<p>There is an example showing how to <a href="https://github.com/andreasronge/neo4j/tree/master/example/ha-cluster">create a HA cluster using neo4j.rb</a> so I thought I could adapt that to do what I wanted.</p>


<p>I had the following Gemfile:</p>



~~~ruby

source 'http://rubygems.org'

gem 'neo4j', '2.2.4'

gem 'neo4j-community', '1.8.2'
gem 'neo4j-advanced', '1.8.2' 
gem 'neo4j-enterprise', '1.8.2'
~~~

<p>And the following code copied from <a href="https://github.com/andreasronge/neo4j/blob/master/example/ha-cluster/myapp.rb">the example</a> to start up the cluster:</p>



~~~ruby

require "rubygems"
require "bundler"
require 'fileutils'
require 'neo4j'

def start(machine_id)
  # override this default config with this machine configuration
  Neo4j.config['enable_ha'] = true
  Neo4j.config['ha.server_id'] = machine_id
  Neo4j.config['ha.server'] = "localhost:600#{machine_id}"
  Neo4j.config['ha.pull_interval'] = '500ms'
  Neo4j.config['ha.discovery.enabled'] = false
  other_machines = [1,2,3].map{|id| "localhost:500#{id}"}.join(',')
  puts "ha.initial_hosts: #{other_machines}"
  Neo4j.config['ha.initial_hosts'] = other_machines
  Neo4j.config['ha.cluster_server'] = "localhost:500#{machine_id}"

  Neo4j.config[:storage_path] = "db/neo#{machine_id}"
  Neo4j.start
end
~~~

<p>As per the example's instructions I started up an irb session and tried to start up an instance:</p>



~~~ruby

$ bundle exec install
$ bundle exec irb
irb(main):001:0> require 'myapp'
=> true
irb(main):002:0> start 1
ha.initial_hosts: localhost:5001,localhost:5002,localhost:5003
I, [2013-06-09T17:23:09.110000 #33848]  INFO -- : starting Neo4j in HA mode, machine id: 1 at localhost:6001 db /Users/markhneedham/projects/neo4j-rb-ha/db/neo1
NameError: cannot load Java class org.neo4j.graphdb.factory.HighlyAvailableGraphDatabaseFactory
	from org/jruby/javasupport/JavaClass.java:1225:in `for_name'
	from org/jruby/javasupport/JavaUtilities.java:34:in `get_proxy_class'
	from file:/Users/markhneedham/.rbenv/versions/jruby-1.7.1/lib/jruby.jar!/jruby/java/java_package_module_template.rb:4:in `const_missing'
	from /Users/markhneedham/.rbenv/versions/jruby-1.7.1/lib/ruby/gems/shared/gems/neo4j-core-2.2.4-java/lib/neo4j-core/database.rb:188:in `start_ha_graph_db'
	from /Users/markhneedham/.rbenv/versions/jruby-1.7.1/lib/ruby/gems/shared/gems/neo4j-core-2.2.4-java/lib/neo4j-core/database.rb:62:in `start'
	from org/jruby/ext/thread/Mutex.java:149:in `synchronize'
	from /Users/markhneedham/.rbenv/versions/jruby-1.7.1/lib/ruby/gems/shared/gems/neo4j-core-2.2.4-java/lib/neo4j-core/database.rb:53:in `start'
	from /Users/markhneedham/.rbenv/versions/jruby-1.7.1/lib/ruby/gems/shared/gems/neo4j-core-2.2.4-java/lib/neo4j/neo4j.rb:41:in `start'
	from /Users/markhneedham/projects/neo4j-rb-ha/myapp.rb:21:in `start'
	from (irb):2:in `evaluate'
	from org/jruby/RubyKernel.java:1066:in `eval'
	from org/jruby/RubyKernel.java:1392:in `loop'
	from org/jruby/RubyKernel.java:1174:in `catch'
	from org/jruby/RubyKernel.java:1174:in `catch'
	from /Users/markhneedham/.rbenv/versions/jruby-1.7.1/bin/irb:13:in `(root)'
~~~

<p>A quick scan of the neo4j code indicated that the class <cite>HighlyAvailableGraphDatabaseFactory</cite> didn't actually exist in any of the neo4j 1.8.2 jars and <a href="https://twitter.com/maxdemarzi">Max</a> then pointed out the <a href="https://github.com/andreasronge/neo4j/blob/master/CHANGELOG">neo4j.rb change log</a> which indicated that the clustering example was based around a neo4j 1.9 cluster.</p>


<p>If we want to create a neo4j 1.8 cluster then we need to tweak the settings a bit.</p>


<p>The instructions are available from <a href="https://github.com/andreasronge/neo4j/commit/022d93909739245703d2321761de0f2218f6184c">an earlier revision of the neo4j.rb</a> repository but I've cloned the repository and created a <a href="https://github.com/mneedham/neo4j-1/tree/1.8HA/example/ha-cluster">1.8HA tag</a> for future reference.</p>


<p>Essentially we'd need to revert back to the '2.2.1' version of the neo4j.rb gem and then run a script to startup some Zookeeper instances before following a similar process as described at the beginning of this post.</p>

