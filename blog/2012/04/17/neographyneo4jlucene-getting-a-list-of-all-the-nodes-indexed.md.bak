+++
draft = false
date="2012-04-17 06:54:38"
title="neography/neo4j/Lucene: Getting a list of all the nodes indexed"
tag=['neo4j', 'neography', 'lucene']
category=['Software Development']
+++

I've been playing around with neo4j using the <a href="https://github.com/maxdemarzi/neography">neography</a> gem to create a graph of all the people in ThoughtWorks and the connections between them based on working with each other.

I created a UI where you could type in the names of two people and see when they've worked together or the path between the shortest path between them if they haven't.

I thought it would be cool to have auto complete functionality when typing in a name but I couldn't figure out how to partially query the index of people's names that I'd created.

I have this Lucene index:


~~~ruby

@neo = Neography::Rest.new
@neo.create_node_index("people", "fulltext", "lucene") 
~~~

Which I add to like this:


~~~ruby

node = @neo.create_node("name" => "Mark Needham")
@neo.add_node_to_index("people", "name", "Mark Needham", node)
~~~


~~~text

> @neo.get_index("people", "name", "Mark Needham")
=> [{"indexed"=>"http://localhost:7474/db/data/index/node/people/name/Mark%20Needham/979", "outgoing_relationships"=>"http://localhost:7474/db/data/node/979/relationships/out", "data"=>{"name"=>"Mark Needham"}, "traverse"=>"http://localhost:7474/db/data/node/979/traverse/{returnType}", "all_typed_relationships"=>"http://localhost:7474/db/data/node/979/relationships/all/{-list|&|types}", "property"=>"http://localhost:7474/db/data/node/979/properties/{key}", "self"=>"http://localhost:7474/db/data/node/979", "properties"=>"http://localhost:7474/db/data/node/979/properties", "outgoing_typed_relationships"=>"http://localhost:7474/db/data/node/979/relationships/out/{-list|&|types}", "incoming_relationships"=>"http://localhost:7474/db/data/node/979/relationships/in", "extensions"=>{}, "create_relationship"=>"http://localhost:7474/db/data/node/979/relationships", "paged_traverse"=>"http://localhost:7474/db/data/node/979/paged/traverse/{returnType}{?pageSize,leaseTime}", "all_relationships"=>"http://localhost:7474/db/data/node/979/relationships/all", "incoming_typed_relationships"=>"http://localhost:7474/db/data/node/979/relationships/in/{-list|&|types}"}]
~~~

I came across <a href="http://www.jguru.com/faq/view.jsp?EID=587213">an old mailing list thread</a> which suggested the following solution:

<blockquote>
One solution is to add a field with a known and constant value to each document in the index. Then searching for that field and value will give you all documents in the index. 
</blockquote>

I changed my code to do that:


~~~ruby

node = @neo.create_node("name" => "Mark Needham")
@neo.add_node_to_index("people", "name", "Mark Needham", node)
@neo.add_node_to_index("people", "type", "person", node) 
~~~

From my sinatra web app I then put the names of all the people in an <a href="http://stackoverflow.com/questions/5188211/persisting-variables-in-sinatra">application level variable</a> like so:


~~~ruby

configure do
  set :all_people, Neography::Rest.new.get_index("people", "type", "person").map { |n| n["data"]["name"] }
end
~~~

And then search through that like so:


~~~ruby

get '/people' do
    search_term = params["term"] ||= ""
    settings.all_people.select { |p| p.downcase.start_with?(search_term.downcase) }.to_json
end
~~~

It works and since there's only one query to get the Lucene index when I first start the web server it's pretty quick but surely there's a less hacky/proper way?
