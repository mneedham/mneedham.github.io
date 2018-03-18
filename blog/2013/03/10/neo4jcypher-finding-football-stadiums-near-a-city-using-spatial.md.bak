+++
draft = false
date="2013-03-10 22:13:41"
title="neo4j/cypher: Finding football stadiums near a city using spatial"
tag=['spatial', 'neo4j', 'cypher']
category=['neo4j']
+++

<p>One of the things that I wanted to add to my football graph was something location related so I could try out <a href="https://github.com/neo4j/spatial">neo4j spatial</a> and I thought the easiest way to do that was to model the location of football stadiums.</p>


<p>To start with I needed to add spatial as <a href="http://maxdemarzi.com/2012/11/26/extending-neo4j/">an unmanaged extension</a> to my neo4j plugins folder which involved doing the following:</p>



~~~text

$ git clone git://github.com/neo4j/spatial.git spatial
$ cd spatial
$ mvn clean package -Dmaven.test.skip=true install
$ unzip target/neo4j-spatial-0.11-SNAPSHOT-server-plugin.zip -d /path/to/neo4j-community-1.9.M04/plugins/
$ /path/to/neo4j-community-1.9.M04/bin/neo4j restart
~~~

<p>If it's installed correctly then you should see this sort of output from issuing a 'curl' against the web interface:</p>



~~~text

$ curl -L http://localhost:7474/db/data
{
  "extensions" : {
...
    "SpatialPlugin" : {
      "addEditableLayer" : "http://localhost:7474/db/data/ext/SpatialPlugin/graphdb/addEditableLayer",
      "addCQLDynamicLayer" : "http://localhost:7474/db/data/ext/SpatialPlugin/graphdb/addCQLDynamicLayer",
      "findGeometriesWithinDistance" : "http://localhost:7474/db/data/ext/SpatialPlugin/graphdb/findGeometriesWithinDistance",
      "updateGeometryFromWKT" : "http://localhost:7474/db/data/ext/SpatialPlugin/graphdb/updateGeometryFromWKT",
      "addGeometryWKTToLayer" : "http://localhost:7474/db/data/ext/SpatialPlugin/graphdb/addGeometryWKTToLayer",
      "getLayer" : "http://localhost:7474/db/data/ext/SpatialPlugin/graphdb/getLayer",
      "addSimplePointLayer" : "http://localhost:7474/db/data/ext/SpatialPlugin/graphdb/addSimplePointLayer",
      "findGeometriesInBBox" : "http://localhost:7474/db/data/ext/SpatialPlugin/graphdb/findGeometriesInBBox",
      "addNodeToLayer" : "http://localhost:7474/db/data/ext/SpatialPlugin/graphdb/addNodeToLayer"
    },
…
  },
...
  "neo4j_version" : "1.9.M04"
~~~

<p>The next step was to create a spatial index containing the stadiums latitudes/longitudes.</p>


<p>There's a good example in <cite><a href="https://github.com/mneedham/spatial/blob/master/src/test/java/org/neo4j/gis/spatial/IndexProviderTest.java#L251">IndexProviderTest</a></cite> which I was able to adapt to do what I wanted.</p>


<p>I got a list of stadiums along with their locations as a CSV from <a href="http://www.doogal.co.uk/FootballStadiums.php">Chris Bell's blog</a>.</p>


<p>The output looks like this:</p>



~~~text

Name,Team,Capacity,Latitude,Longitude
"Adams Park","Wycombe Wanderers",10284,51.6306,-0.800299
"Almondvale Stadium","Livingston",10122,55.8864,-3.52207
"Amex Stadium","Brighton and Hove Albion",22374,50.8609,-0.08014
"Anfield","Liverpool",45522,53.4308,-2.96096
"Ashton Gate","Bristol City",21497,51.44,-2.62021
"B2net Stadium","Chesterfield",10400,53.2535,-1.4272
~~~

<p>I ended up with the following code to create nodes for each of the stadium and add them to the spatial index:</p>



~~~java

// imports excluded

public class SampleSpatialGraph {
    public static void main(String[] args) throws IOException {
        List<String> lines = readFile("/path/to/stadiums.csv");
 
        EmbeddedGraphDatabase db = new EmbeddedGraphDatabase("/path/to/neo4j-community-1.9.M04/data/graph.db");
        Index<Node> index = createSpatialIndex(db, "stadiumsLocation");
        Transaction tx = db.beginTx();
 
        for (String stadium : lines) {
            String[] columns = stadium.split(",");
            Node stadiumNode = db.createNode();
            stadiumNode.setProperty("wkt", String.format("POINT(%s %s)", columns[4], columns[3]));
            stadiumNode.setProperty("name", columns[0]);
            index.add(stadiumNode, "dummy", "value");
        }
 
        tx.success();
        tx.finish();
    }
 
    private static Index<Node> createSpatialIndex(EmbeddedGraphDatabase db, String indexName) {
        return db.index().forNodes(indexName, SpatialIndexProvider.SIMPLE_WKT_CONFIG);
    }
 
    // readFile function excluded
}
~~~

<p>The full code is on <a href="https://gist.github.com/mneedham/5130545">this gist</a> if you're interested.</p>


<p>We can now query the stadiums using cypher to find say the stadiums within 5 kilometres of <a href="https://maps.google.co.uk/maps?q=53.488454,-2.248764&hl=en&ll=53.488454,-2.248764&spn=0.027219,0.084028&sll=53.525411,-2.087402&sspn=0.108782,0.336113&t=m&z=14">Manchester</a>:</p>



~~~cypher

START n=node:stadiumsLocation('withinDistance:[53.489271, -2.246704, 5.0]') 
RETURN n.name, n.wkt;
~~~


~~~text

==> +------------------------------------------------+
==> | n.name             | n.wkt                     |
==> +------------------------------------------------+
==> | ""Etihad Stadium"" | "POINT(-2.20024 53.483)"  |
==> | ""Old Trafford""   | "POINT(-2.29139 53.4631)" |
==> +------------------------------------------------+
==> 2 rows
==> 214 ms
~~~

<p>Or we could use a <a href="http://en.wikipedia.org/wiki/Minimum_bounding_rectangle">bounding box query</a> whereby we return all the stadiums within a virtual box based on coordinates. For example the following query returns all the stadiums which are within the M25:</p>



~~~cypher

START n=node:stadiumsLocation('bbox:[-0.519104,0.22934, 51.279958,51.69299]')
RETURN n.name, n.wkt;
~~~


~~~text

==> +----------------------------------------------------+
==> | n.name                | n.wkt                      |
==> +----------------------------------------------------+
==> | ""White Hart Lane""   | "POINT(-0.065684 51.6033)" |
==> | ""Wembley""           | "POINT(-0.279543 51.5559)" |
==> | ""Victoria Road""     | "POINT(0.159739 51.5478)"  |
==> | ""Vicarage Road""     | "POINT(-0.401569 51.6498)" |
==> | ""Underhill Stadium"" | "POINT(-0.191789 51.6464)" |
==> | ""The Valley""        | "POINT(0.036757 51.4865)"  |
==> | ""The Den""           | "POINT(-0.050743 51.4859)" |
==> | ""Stamford Bridge""   | "POINT(-0.191034 51.4816)" |
==> | ""Selhurst Park""     | "POINT(-0.085455 51.3983)" |
==> | ""Craven Cottage""    | "POINT(-0.221619 51.4749)" |
==> | ""Griffin Park""      | "POINT(-0.302621 51.4882)" |
==> | ""Loftus Road""       | "POINT(-0.232204 51.5093)" |
==> | ""Boleyn Ground""     | "POINT(0.039225 51.5321)"  |
==> | ""Emirates Stadium""  | "POINT(-0.108436 51.5549)" |
==> | ""Brisbane Road""     | "POINT(-0.012551 51.5601)" |
==> +----------------------------------------------------+
==> 15 rows
==> 23 ms
~~~

<p>Now I just need to wire the stadiums in with the rest of the graph and I'll be able to write queries based on players performance in different parts of the country.</p>

