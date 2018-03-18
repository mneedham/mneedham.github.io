+++
draft = false
date="2012-08-05 09:45:08"
title="neo4j: Creating a custom index with neo4j.rb"
tag=['neo4j']
category=['neo4j']
+++

As I <a href="http://www.markhneedham.com/blog/2012/07/30/london-bus-stops-api-mapping-northingeasting-values-to-latlong/">mentioned in my last post</a> I've been playing around with the <a href="http://www.tfl.gov.uk/businessandpartners/syndication/16493.aspx#17463">TFL Bus stop location and routes API</a> and one thing I wanted to do was load all the bus stops into a neo4j database using the <a href="https://github.com/andreasronge/neo4j">neo4j.rb</a> gem.

I initially populated the database via <a href="https://github.com/maxdemarzi/neography/">neography</a> but it was taking around 20 minutes each run and I figured it'd probably be much quicker to populate it directly rather than using the REST API.

Creating nodes is reasonably simple, and the code to add bus stops looks like this:


~~~ruby

require 'neo4j'

Neo4j::Transaction.run do
  stops_to_add = [ {:name => "Walworth Road", :code => 10001 }]

  stops_to_add.each do |stop|
    node = Neo4j::Node.new(:name => stop[:name], :code => stop[:code], :type => "stop")
    puts "Code: #{stop[:code]}, Stop: #{stop[:name]}"
  end
end
~~~

I wanted to be able to search for bus stops using cypher so I needed to create an index for each stop to allow me to do that easily. 

I initially tried creating a <cite>Stop</cite> class and defining the index in there <a href="http://neo4j.rubyforge.org/guides/lucene.html">as suggested in the documentation</a> but from what I could tell it created an index named after the string representation of the <cite>Stop</cite> object which made it difficult to use in <a href="http://docs.neo4j.org/chunked/stable/cypher-query-lang.html">cypher</a>.

Eventually I came across <a href="https://github.com/andreasronge/neo4j/wiki/Neo4j%3A%3ACore-Lucene">another page</a> which explained that I needed to create a 'custom index' if I wanted to be able to reference it by name.

I ended up with the following:


~~~ruby

class StopsIndex
  extend Neo4j::Core::Index::ClassMethods
  include Neo4j::Core::Index

  self.node_indexer do
    index_names :exact => 'stops'
    trigger_on :type => "stop"
  end

  index :code
end
~~~

As far as I understand this index gets triggered when you're inside a transaction adding a node of type 'stop' which is what I'm doing here.

With the index defined this way it's now possible to look up stops using cypher:


~~~text

START stop = node:stops(code = "10001")
RETURN stop
~~~

And when later on in the code I wanted to add a 'route' between stops I could look up the stops like so:


~~~ruby

Neo4j::Transaction.run do
  stop1 = StopsIndex.find("code: \"10001\"").first
  stop2 = StopsIndex.find("code: \"10002\"").first				
  Neo4j::Relationship.new(:route, stop1, stop2, { :bus_number => 1 })
end
~~~

The <a href="https://github.com/mneedham/london-buses/blob/master/data/load.rb">full code for this is on github</a>.
