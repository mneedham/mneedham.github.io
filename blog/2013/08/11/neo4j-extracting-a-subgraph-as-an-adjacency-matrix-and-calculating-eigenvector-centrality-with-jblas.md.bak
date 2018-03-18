+++
draft = false
date="2013-08-11 07:23:31"
title="neo4j: Extracting a subgraph as an adjacency matrix and calculating eigenvector centrality with JBLAS"
tag=['java', 'neo4j', 'eigenvector-centrality', 'jblas']
category=['neo4j']
+++

<p>Earlier in the week I wrote a blog post showing <a href="http://www.markhneedham.com/blog/2013/08/05/javajblas-calculating-eigenvector-centrality-of-an-adjacency-matrix/">how to calculate the eigenvector centrality of an adjacency matrix</a> using <a href="http://mikiobraun.github.io/jblas/">JBLAS</a> and the next step was to work out the eigenvector centrality of a neo4j sub graph.</p>


There were 3 steps involved in doing this:

<ol>
<li>Export the neo4j sub graph as an adjacency matrix</li>
<li>Run JBLAS over it to get eigenvector centrality scores for each node</li>
<li>Write those scores back into neo4j</li>
</ol>

<p>I decided to make use of the <a href="https://github.com/mneedham/revere/blob/neo4j/data/PaulRevereAppD.csv">Paul Revere data set</a> from <a href="http://kieranhealy.org/blog/archives/2013/06/09/using-metadata-to-find-paul-revere/">Kieran Healy's blog post</a> which consists of people and groups that they had membership of.</p>


<p>The <a href="https://github.com/mneedham/revere/blob/neo4j/scripts/import.rb">script</a> to import the data is on <a href="https://github.com/mneedham/revere/tree/neo4j">my fork of the revere repository</a>.</p>


<p>Having imported the data the next step was to write a cypher query which would give me the people in an <a href="http://en.wikipedia.org/wiki/Adjacency_matrix">adjacency matrix</a> with the number in each column/row intersection showing how many common groups that pair of people had.<p>

<p>I thought it'd be easier to build this query incrementally so I started out writing a query which would return one row of the adjacency matrix:</p>



~~~cypher

MATCH p1:Person, p2:Person
WHERE p1.name = "Paul Revere"
WITH p1, p2
MATCH p = p1-[?:MEMBER_OF]->()<-[?:MEMBER_OF]-p2

WITH p1.name AS p1, p2.name AS p2, COUNT(p) AS links
ORDER BY p2
RETURN p1, COLLECT(links) AS row
~~~

<p>Here we start with Paul Revere and then find the relationships between him and every other person by way of a common group membership.<p>

<p>We use an optional relationship since we need to include a value in each column/row of our adjacency matrix we need to return a 0 value for anyone he doesn't intersect with.</p>


<p>If we run that query we get back the following:</p>



~~~text

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| p1            | row                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| "Paul Revere" | [2,1,1,1,1,1,1,1,1,1,1,1,1,1,2,3,1,1,1,1,1,1,3,3,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,3,2,1,1,2,1,2,1,1,1,1,1,0,1,1,1,1,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,2,1,1,1,1,1,1,2,1,3,1,3,2,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,0,1,0,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,4,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,1,1,1,1,1,2,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,3,1,1,2,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,1,2,1,1,1,1,1,1,1,1,3,1,1,1,1,3,1,1,1,1,0,1,2,1,1,1,1,1,1,1] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
~~~

<p>As it turns outs we've only got to remove the WHERE clause and order everybody and we've get the adjacency matrix for everyone:</p>



~~~cypher

MATCH p1:Person, p2:Person
WITH p1, p2
MATCH p = p1-[?:MEMBER_OF]->()<-[?:MEMBER_OF]-p2

WITH p1.name AS p1, p2.name AS p2, COUNT(p) AS links
ORDER BY p2
RETURN p1, COLLECT(links) AS row
ORDER BY p1
~~~


~~~text

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| p1                      | row                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| "Abiel Ruddock"         | [0,1,1,1,0,1,0,1,0,0,1,1,1,0,1,2,0,1,0,1,1,1,2,2,1,0,0,1,1,0,1,1,1,1,1,0,0,0,0,1,1,0,0,2,2,0,0,1,1,2,1,1,1,0,1,0,1,1,0,0,2,1,0,0,0,0,1,0,0,1,1,0,0,0,0,0,0,0,1,1,0,1,1,1,1,1,1,1,1,1,0,2,1,2,1,0,0,0,0,1,1,0,1,0,0,1,0,2,0,0,1,0,0,0,1,0,0,2,0,1,0,1,1,1,0,0,1,1,0,0,0,0,0,0,2,0,0,0,0,0,0,0,1,0,1,1,0,1,1,1,2,0,0,1,1,0,0,2,0,1,2,1,1,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,1,2,1,0,1,1,1,1,1,0,0,1,1,0,0,0,0,1,0,1,1,0,0,1,0,0,2,1,0,0,1,1,1,1,0,1,0,0,0,1,0,1,0,1,1,0,0,1,0,1,0,1,0,0,1,0,2,1,1,0,0,2,0,1,0,0,0,0,1,0,1,0,1,0,1,0] |
| "Abraham Hunt"          | [1,0,1,1,0,1,0,0,0,0,0,1,0,0,0,1,0,1,0,1,1,0,1,1,0,0,0,1,1,0,1,0,0,1,0,0,0,0,0,1,0,0,0,1,1,0,0,0,1,1,1,1,1,0,0,0,1,0,0,0,1,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,0,0,1,1,0,1,0,1,1,1,1,0,0,0,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,1,0,1,0,0,1,1,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,1,0,0,0,1,0,1,0,0,0,1,0,0,1,0,1,1,0,1,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,1,0,1,0,1,0,1,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,1,0,0,0,1,1,1,1,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,1,0,0,0,0,0,0,0,0,1,0,1,0,1,0] |
...
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
254 rows
9897 ms
~~~

<p>The next step was to wire up the query results with the JBLAS code that I wrote in the previous post. I ended up with the <a href="https://github.com/mneedham/revere/blob/neo4j/src/main/java/Neo4jAdjacencyMatrixSpike.java">following</a>:</p>



~~~java

public class Neo4jAdjacencyMatrixSpike {
    public static void main(String[] args) throws SQLException {
        ClientResponse response = client()
                .resource("http://localhost:7474/db/data/cypher")
                .entity(queryAsJson(), MediaType.APPLICATION_JSON)
                .accept(MediaType.APPLICATION_JSON)
                .post(ClientResponse.class);

        JsonNode result = response.getEntity(JsonNode.class);
        ArrayNode rows = (ArrayNode) result.get("data");

        List<Double> principalEigenvector = JBLASSpike.getPrincipalEigenvector(new DoubleMatrix(asMatrix(rows)));

        List<Person> people = asPeople(rows);
        updatePeopleWithEigenvector(people, principalEigenvector);

        System.out.println(sort(people).take(10));
    }

    private static double[][] asMatrix(ArrayNode rows) {
        double[][] matrix = new double[rows.size()][254];
        int rowCount = 0;

        for (JsonNode row : rows) {
            ArrayNode matrixRow = (ArrayNode) row.get(2);

            double[] rowInMatrix = new double[254];
            matrix[rowCount] = rowInMatrix;
            int columnCount = 0;
            for (JsonNode jsonNode : matrixRow) {
                matrix[rowCount][columnCount] = jsonNode.asInt();
                columnCount++;
            }

            rowCount++;
        }
        return matrix;
    }

    // rest cut for brevity
}
~~~

<p>Here we are taking the query and then converting it into an array of arrays before passing it to our JBLAS code to calculate the principal eigenvector. We then return the top 10 people:</p>



~~~text

Person{name='William Cooper', eigenvector=0.172604992239612, nodeId=68},
Person{name='Nathaniel Barber', eigenvector=0.17260499223961198, nodeId=18},
Person{name='John Hoffins', eigenvector=0.17260499223961195, nodeId=118},
Person{name='Paul Revere', eigenvector=0.17171142003936804, nodeId=207},
Person{name='Caleb Davis', eigenvector=0.16383970722169897, nodeId=71},
Person{name='Caleb Hopkins', eigenvector=0.16383970722169897, nodeId=121},
Person{name='Henry Bass', eigenvector=0.16383970722169897, nodeId=21},
Person{name='Thomas Chase', eigenvector=0.16383970722169897, nodeId=54},
Person{name='William Greenleaf', eigenvector=0.16383970722169897, nodeId=104},
Person{name='Edward Proctor', eigenvector=0.15600043886738055, nodeId=201}
~~~

<p>I get back the same 10 people as Kieran Healy although they have different eigenvector values. As far as I understand the absolute value doesn't matter, what's more important is the relative score to other people so I think we're ok.</p>


<p>The final step was to write these eigenvector values back into neo4j which we can do with the following code:</p>



~~~java

    private static void updateNeo4jWithEigenvectors(List<Person> people) {
        for (Person person : people) {
            ObjectNode request = JsonNodeFactory.instance.objectNode();
            request.put("query", "START p = node({nodeId}) SET p.eigenvectorCentrality={value}");

            ObjectNode params = JsonNodeFactory.instance.objectNode();
            params.put("nodeId", person.nodeId);
            params.put("value", person.eigenvector);

            request.put("params", params);

            client()
                    .resource("http://localhost:7474/db/data/cypher")
                    .entity(request, MediaType.APPLICATION_JSON)
                    .accept(MediaType.APPLICATION_JSON)
                    .post(ClientResponse.class);
        }
    }
~~~

<p>Now we might use that eigenvector centrality value in other queries, such as one to show who the most central/potentially influential people are in each group:</p>



~~~cypher

MATCH g:Group<-[:MEMBER_OF]-p

WITH g.name AS group, p.name AS personName, p.eigenvectorCentrality as eigen
ORDER BY eigen DESC

WITH group, COLLECT(personName) AS people
RETURN group, HEAD(people) + [HEAD(TAIL(people))] + [HEAD(TAIL(TAIL(people)))] AS mostCentral
~~~


~~~text

+--------------------------------------------------------------------------+
| group             | mostCentral                                          |
+--------------------------------------------------------------------------+
| "StAndrewsLodge"  | ["Paul Revere","Joseph Warren","Thomas Urann"]       |
| "BostonCommittee" | ["William Cooper","Nathaniel Barber","John Hoffins"] |
| "LoyalNine"       | ["Caleb Hopkins","William Greenleaf","Caleb Davis"]  |
| "LondonEnemies"   | ["William Cooper","Nathaniel Barber","John Hoffins"] |
| "LongRoomClub"    | ["Paul Revere","John Hancock","Benjamin Clarke"]     |
| "NorthCaucus"     | ["William Cooper","Nathaniel Barber","John Hoffins"] |
| "TeaParty"        | ["William Cooper","Nathaniel Barber","John Hoffins"] |
+--------------------------------------------------------------------------+
7 rows
280 ms
~~~

<p>Our top ten feature frequently although it's interesting that only one of them is in the 'LongRoomClub' group which perhaps indicates that people in that group are less likely to be members of the other ones.</p>


<p>I'd be interested if anyone can think of other potential uses for eigenvector centrality once we've got it back in the graph.</p>


<p>All the code described in this post is <a href="https://github.com/mneedham/revere/tree/neo4j">on github</a> if you want to take it for a spin.</p>

