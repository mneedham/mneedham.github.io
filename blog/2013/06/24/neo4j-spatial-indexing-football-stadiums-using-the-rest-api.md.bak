+++
draft = false
date="2013-06-24 07:17:15"
title="neo4j Spatial: Indexing football stadiums using the REST API"
tag=['neo4j']
category=['neo4j']
+++

<p>Late last week my colleague <a href="https://twitter.com/peterneubauer">Peter</a> wrote up some documentation about <a href="http://neo4j.github.io/spatial/#spatial-server-plugin">creating spatial indexes in neo4j via HTTP</a>, something I hadn't realised was possible until then.</p>


<p>I previously wrote about <a href="http://www.markhneedham.com/blog/2013/03/10/neo4jcypher-finding-football-stadiums-near-a-city-using-spatial/">indexing football stadiums using neo4j spatial</a> but the annoying thing about the approach I described was that I was using neo4j in <a href="http://docs.neo4j.org/chunked/stable/tutorials-java-embedded.html">embedded mode</a> which restricts you to using a JVM language.</p>


<p>The rest of my code is in Ruby so I thought I'd translate that code.</p>


<p>To recap, I'm parsing a CSV file of football stadiums that I downloaded from <a href="http://www.doogal.co.uk/FootballStadiums.php">Chris Bell's blog</a> which looks like this:</p>



~~~text

Name,Team,Capacity,Latitude,Longitude
"Adams Park","Wycombe Wanderers",10284,51.6306,-0.800299
"Almondvale Stadium","Livingston",10122,55.8864,-3.52207
"Amex Stadium","Brighton and Hove Albion",22374,50.8609,-0.08014
~~~

<p>The code to process the file and index the stadiums in neo4j is <a href="https://github.com/mneedham/neo4j-football-stadiums/blob/master/create_stadiums.rb">as follows</a> (and is essentially a translation of the <cite><a href="https://github.com/neo4j/spatial/blob/413317048eee7c2d3b25950d361634fc20c238d2/src/test/java/org/neo4j/gis/spatial/SpatialPluginFunctionalTest.java#L238">find_geometries_within_distance_using_cypher</a></cite> test):</p>



~~~ruby

require 'csv'
require 'httparty'
require 'json'

HTTParty.post("http://localhost:7474/db/data/ext/SpatialPlugin/graphdb/addSimplePointLayer", 
  :body => { :layer => 'geom', :lat => 'lat', :lon => 'lon' }.to_json,
  :headers => { 'Content-Type' => 'application/json' } )

HTTParty.post("http://localhost:7474/db/data/index/node", 		
  :body => { :name => 'geom', :config => { :provider => 'spatial', :geometry_type => 'point', :lat => 'lat', :lon => 'lon'  } }.to_json,
  :headers => { 'Content-Type' => 'application/json' } )

contents = CSV.read(File.join(File.dirname(__FILE__), 'data', 'stadiums.csv'))
contents.shift
contents.each do |row|
  name, team, capacity, lat, long = row

  node_id = HTTParty.post("http://localhost:7474/db/data/node", 		
    :body => { :lat => lat.to_f, :lon => long.to_f, :name => name, :team => team, :capacity => capacity }.to_json,
    :headers => { 'Content-Type' => 'application/json' } )['self'].split("/")[-1]

  HTTParty.post("http://localhost:7474/db/data/index/node/geom", 		
    :body => { :key => 'dummy', :value => 'dummy', :uri => "http://localhost:7474/db/data/node/#{node_id}"}.to_json,
    :headers => { 'Content-Type' => 'application/json' } )
end
~~~

<p>One change from the previous version is that I'm not indexing the stadiums using point based geometry rather than wkt.</p>


<p>If we want to find the number of stadiums within 10 km of Centre Point in London we'd write the following query:</p>



~~~cypher

START node = node:geom('withinDistance:[51.521348,-0.128113, 10.0]') 
RETURN node.name, node.team;
~~~


~~~text

==> +--------------------------------------------+
==> | node.name          | node.team             |
==> +--------------------------------------------+
==> | "Emirates Stadium" | "Arsenal"             |
==> | "Stamford Bridge"  | "Chelsea"             |
==> | "The Den"          | "Millwall"            |
==> | "Loftus Road"      | "Queens Park Rangers" |
==> | "Craven Cottage"   | "Fulham"              |
==> | "Brisbane Road"    | "Leyton Orient"       |
==> +--------------------------------------------+
==> 6 rows
~~~

<p>I have <a href="https://github.com/mneedham/neo4j-football-stadiums">put the code on github</a> in case you're interested in playing around with it.</p>

