+++
draft = false
date="2012-04-20 07:10:57"
title="neo4J: Searching for nodes by name"
tag=['neo4j', 'cypher']
category=['Software Development', 'neo4j']
+++

As I mentioned in a post a few days ago I've been graphing connections between ThoughtWorks people using neo4j and wanted to build auto complete functionality so I can search for the names of people in the graph.

The solution I came up was to create a Lucene index with an entry for each node and a common property on each document in the index so that I'd be able to get all the index entries easily.

I created the index like this, using the <a href="https://github.com/maxdemarzi/neography/blob/master/lib/neography/rest.rb">neography gem</a>:


~~~ruby

Neography::Rest.new.add_node_to_index("people", "type", "person", node)
~~~

I can then get all the names like this:


~~~ruby

all_people = Neography::Rest.new.get_index("people", "type", "person").map { |n| n["data"]["name"] }
~~~

It seemed like there must be a better way to do this and <a href="http://twitter.com/#!/mesirii">Michael Hunger</a> was kind enough to show me a couple of cleaner solutions.

One way is to query the initial index rather than creating a new one:


~~~ruby

all_people = Neography::Rest.new.find_node_index("people", "name:*").map { |n| n["data"]["name"] }
~~~

The 'find_node_index' method allows us to pass in a Lucene query which gets <a href="http://docs.neo4j.org/chunked/stable/rest-api-indexes.html#rest-api-find-node-by-query">executed via neo4j's REST API</a>. In this case we're using a wild card query on the 'name' property so it will return all documents.

This way of getting all the names seemed to be much more intensive than my other approach and when I ran it a few times in a row I was getting OutOfMemory errors. My graph only has a few thousand nodes in it so I'm not sure why that is yet.

I think it should be possible to query the Lucene index directly with the partial name but I was struggling to get spaces in the search term to encode correctly and was getting back no results.

Another approach is to use a cypher query to get a collection of all the nodes:


~~~ruby

all_people = Neography::Rest.new.execute_query("start n=node(*) return n")["data"].map { |n| n[0]["data"]["name"] }
~~~

I imagine this approach wouldn't scale with graph size but for my graph it works just fine.
