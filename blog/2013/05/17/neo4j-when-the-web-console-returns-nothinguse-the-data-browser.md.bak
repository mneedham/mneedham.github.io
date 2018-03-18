+++
draft = false
date="2013-05-17 00:00:16"
title="neo4j: When the web console returns nothing…use the data browser!"
tag=['neo4j']
category=['neo4j']
+++

<p>In my time playing around with <a href="http://www.neo4j.org/">neo4j</a> I've run into a problem a few times where I executed a query using the web console (usually accessible @ <a href="http://localhost:7474/webadmin/#/console/">http://localhost:7474/webadmin/#/console/</a>) and have got absolutely no response.</p>


<p>I noticed a similar thing today when <a href="https://twitter.com/rickardoberg">Rickard</a> and I were having a look at why a Lucene index query wasn't behaving as we expected.</p>


<p>I setup some data in a neo4j database using <a href="https://github.com/maxdemarzi/neography">neography</a> with the following code:</p>



~~~ruby

require 'neography'

@neo = Neography::Rest.new

@neo.create_node_index("Id_Index", "exact", "lucene")

node1 = @neo.create_node("Hour" => 1, "name" => "Max")
node2 = @neo.create_node("Hour" => 2, "name" => "Mark")
node3 = @neo.create_node("Hour" => 3, "name" => "Rickard")

@neo.add_node_to_index("Id_Index", "Hour", 1, node1)
@neo.add_node_to_index("Id_Index", "Hour", 2, node2) 
@neo.add_node_to_index("Id_Index", "Hour", 3, node3) 
~~~

<p>I then ran the following query which I was expecting to return all the nodes:</p>



~~~cypher

start hour=node:Id_Index("Hour:[00 TO 02] or Hour:[03 TO 05]") RETURN hour
~~~

<p>Instead it returned nothing and I couldn't see anything being logged either.</p>
 

<p>Rickard pointed out was because the exception is only returned to the API caller and that it would be better to run the query from the Data Browser which is typically accessible from <a href="http://localhost:7474/webadmin/#/data/search/">http://localhost:7474/webadmin/#/data/search/</a></p>


<p>If we run the query from there then we can see what's going wrong:</p>



~~~text

BadInputException

StackTrace:
org.neo4j.server.rest.repr.RepresentationExceptionHandlingIterable.exceptionOnHasNext(RepresentationExceptionHandlingIterable.java:50)
org.neo4j.helpers.collection.ExceptionHandlingIterable$1.hasNext(ExceptionHandlingIterable.java:60)
org.neo4j.helpers.collection.IteratorWrapper.hasNext(IteratorWrapper.java:42)
org.neo4j.server.rest.repr.ListRepresentation.serialize(ListRepresentation.java:58)
org.neo4j.server.rest.repr.Serializer.serialize(Serializer.java:75)
org.neo4j.server.rest.repr.MappingSerializer.putList(MappingSerializer.java:61)
org.neo4j.server.rest.repr.CypherResultRepresentation.serialize(CypherResultRepresentation.java:57)
org.neo4j.server.rest.repr.MappingRepresentation.serialize(MappingRepresentation.java:42)
org.neo4j.server.rest.repr.OutputFormat.assemble(OutputFormat.java:179)
org.neo4j.server.rest.repr.OutputFormat.formatRepresentation(OutputFormat.java:131)
org.neo4j.server.rest.repr.OutputFormat.response(OutputFormat.java:117)
org.neo4j.server.rest.repr.OutputFormat.ok(OutputFormat.java:55)
org.neo4j.server.rest.web.CypherService.cypher(CypherService.java:94)
java.lang.reflect.Method.invoke(Method.java:597)
~~~

<p>There seemed to be some strangeness going on with how Lucene handles the query when a default search field isn't provided but we noticed that it behaved as expected if we didn't use an OR since Lucene has an implicit OR between statements anyway. </p>



~~~cypher

start hour=node:Id_Index("Hour:[00 TO 02] Hour:[03 TO 05]") RETURN hour
~~~

<p>Either way, the lesson for me was if the console isn't giving a result run the query in the data browser to work out what's going wrong!</p>

