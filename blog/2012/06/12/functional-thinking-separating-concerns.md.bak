+++
draft = false
date="2012-06-12 23:50:45"
title="Functional Thinking: Separating concerns"
tag=['functional-programming']
category=['Software Development']
+++

Over the weekend I was trying to port some of the neo4j import code for the ThoughtWorks graph I've been working on to make use of the <a href="http://docs.neo4j.org/chunked/snapshot/rest-api-batch-ops.html">REST Batch API</a> and I came across an interesting example of imperative vs functional thinking.

I'm using the <a href="https://github.com/maxdemarzi/neography">neography</a> gem to populate the graph and to start with I was just creating a person node and then creating an index entry for it:


~~~ruby

people_to_load = Set.new
people_to_load << { :name => "Mark Needham", :id => 1 }
people_to_load << { :name => "Jenn Smith", :id => 2 }
people_to_load << { :name => "Chris Ford", :id => 3 } 

command_index = 0
people_commands = people_to_load.inject([]) do |acc, person| 
  acc << [:create_node, {:id => person[:id], :name => person[:name]}]
  acc << [:add_node_to_index, "people", "name", person[:name], "{#{command_index}}"]
  command_index += 2
  acc
end

Neography::Rest.new.batch * people_commands
~~~

<cite>people_commands</cite> ends up containing the following arrays in the above example:


~~~text

 [
  [:create_node, {:id=>"1", :name=>"Mark Needham"}], 
  [:add_node_to_index, "people", "name", "Mark Needham", "{0}"], 
  [:create_node, {:id=>"2", :name=>"Jenn Smith"}], 
  [:add_node_to_index, "people", "name", "Jenn Smith", "{2}"], 
  [:create_node, {:id=>"3", :name=>"Chris Ford"}, 
  [:add_node_to_index, "people", "name", "Chris Ford", "{4}"]
 ]
~~~

We can refer to previously executed batch commands by referencing their 'job id' which in this case is their 0 indexed position in the list of commands. e.g. the second command which indexes me refers to the node created in 'job id' '0' i.e the first command in this batch

In the neo4j REST API we'd be able to define an arbitrary id for a command and then reference that later on but it's not implemented that way in neography.

I thought having the 'command_index += 2' was a bit rubbish because it's nothing to do with the problem I'm trying to solve so I <a href="https://twitter.com/markhneedham/status/211793005668077568">posted to twitter to see if there was a more functional way to do this</a>.

My colleague <a href="https://twitter.com/#!/ctford">Chris Ford</a> came up with a neat approach which involved using 'each_with_index' to work out the index positions rather than having a counter. His final version looked like this:


~~~ruby

insert_commands = people_to_load.map do |person|
  [:create_node, {:id => person[:id], :name => person[:name]}]
end

index_commands = people_to_load.each_with_index.map do |person, index|
  [:add_node_to_index, "people", "name", person[:name], "{#{index}}"]
end

people_commands = insert_commands + index_commands
~~~

The neat thing about this solution is that Chris has <strong>separated the two concerns</strong> - creating the node and indexing it. 

When I was thinking about this problem imperatively they seemed to belong together but there's actually no reason for that to be the case and we can write simpler code by separating them.

We do iterate through the set twice but since it's not really that big it doesn't make too much difference. to the performance.
