+++
draft = false
date="2012-08-25 10:00:07"
title="Ruby: Finding where gems are"
tag=['ruby']
category=['Ruby']
+++

In my infrequent travels into Ruby land I always seem to forget where the gems that I've installed actually live on the file system but my colleague <a href="http://twitter.com/nickstenning">Nick</a> recently showed me a neat way of figuring it out.

If I'm in the folder that contains all my ThoughtWorks graph code I'd just need to run the following command:


~~~text

$ gem which rubygems
/Users/mneedham/.rbenv/versions/jruby-1.6.7/lib/ruby/site_ruby/1.8/rubygems.rb
~~~

I then loaded up irb and wrote a simple cypher query executed using neography:


~~~ruby

> require 'rubygems'
=> true

> require 'neography'
=> true

> neo = Neography::Rest.new(:port => 7476)
=> #<Neography::Rest:0x40d3ab8b @protocol="http://", @server="localhost", @cypher_path="/cypher", @log_file="neography.log", @authentication={}, @directory="", @log_enabled=false, @gremlin_path="/ext/GremlinPlugin/graphdb/execute_script", @parser={:parser=>CrackParser}, @max_threads=20, @port=7476>

> neo.execute_query("START n = node(1) RETURN n")
=> {"data"=>[[{"outgoing_relationships"=>"http://localhost:7476/db/data/node/1/relationships/out", "data"=>{"thoughtquitter"=>true, "name"=>"Marjorie Pries", "type"=>"person"}, "traverse"=>"http://localhost:7476/db/data/node/1/traverse/{returnType}", "all_typed_relationships"=>"http://localhost:7476/db/data/node/1/relationships/all/{-list|&|types}", "property"=>"http://localhost:7476/db/data/node/1/properties/{key}", "self"=>"http://localhost:7476/db/data/node/1", "properties"=>"http://localhost:7476/db/data/node/1/properties", "outgoing_typed_relationships"=>"http://localhost:7476/db/data/node/1/relationships/out/{-list|&|types}", "incoming_relationships"=>"http://localhost:7476/db/data/node/1/relationships/in", "extensions"=>{}, "create_relationship"=>"http://localhost:7476/db/data/node/1/relationships", "paged_traverse"=>"http://localhost:7476/db/data/node/1/paged/traverse/{returnType}{?pageSize,leaseTime}", "all_relationships"=>"http://localhost:7476/db/data/node/1/relationships/all", "incoming_typed_relationships"=>"http://localhost:7476/db/data/node/1/relationships/in/{-list|&|types}"}]], "columns"=>["n"]}
~~~

If I want to debug the <cite>execute_query</cite> function of neography then I'd need to make a change to <cite>/Users/mneedham/.rbenv/versions/jruby-1.6.7/lib/ruby/gems/1.8/gems/neography-0.0.26/lib/neography/rest.rb</cite> which is just a case of going up a few levels from where <cite>rubygems.rb</cite> lives and then finding the appropriate gem.

If I change that function to print a stupid message...


~~~ruby

       def execute_query(query, params = {})
          puts "just testing you come up"
           options = { :body => {:query => query, :params => params}.to_json, :headers => {'Content-Type' => 'application/json'} }
           result = post(@cypher_path, options)
       end
~~~

...when we run it through irb again we should see it:


~~~text

> neo.execute_query("START n = node(1) RETURN n")
just testing you come up
=> {"data"=>[[{"outgoing_relationships"=>"http://localhost:7476/db/data/node/1/relationships/out", "data"=>{"thoughtquitter"=>true, "name"=>"Marjorie Pries", "type"=>"person"}, "traverse"=>"http://localhost:7476/db/data/node/1/traverse/{returnType}", "all_typed_relationships"=>"http://localhost:7476/db/data/node/1/relationships/all/{-list|&|types}", "property"=>"http://localhost:7476/db/data/node/1/properties/{key}", "self"=>"http://localhost:7476/db/data/node/1", "properties"=>"http://localhost:7476/db/data/node/1/properties", "outgoing_typed_relationships"=>"http://localhost:7476/db/data/node/1/relationships/out/{-list|&|types}", "incoming_relationships"=>"http://localhost:7476/db/data/node/1/relationships/in", "extensions"=>{}, "create_relationship"=>"http://localhost:7476/db/data/node/1/relationships", "paged_traverse"=>"http://localhost:7476/db/data/node/1/paged/traverse/{returnType}{?pageSize,leaseTime}", "all_relationships"=>"http://localhost:7476/db/data/node/1/relationships/all", "incoming_typed_relationships"=>"http://localhost:7476/db/data/node/1/relationships/in/{-list|&|types}"}]], "columns"=>["n"]}
~~~

And now hopefully I won't forget where to find the gems!
