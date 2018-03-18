+++
draft = false
date="2014-07-20 15:13:00"
title="Neo4j 2.1.2: Finding where I am in a linked list"
tag=['neo4j']
category=['neo4j']
+++

<p>I was recently asked how to calculate the position of a node in a linked list and realised that as the list increases in size this is one of the occasions when we should write an <a href="http://docs.neo4j.org/chunked/stable/server-unmanaged-extensions.html">unmanaged extension</a> rather than using cypher.</p>


<p>I wrote a quick bit of code to create a linked list with 10,000 elements in it:</p>



~~~java

public class Chains 
{
    public static void main(String[] args)
    {
        String simpleChains = "/tmp/longchains";
        populate( simpleChains, 10000 );
    }

    private static void populate( String path, int chainSize )
    {
        GraphDatabaseService db = new GraphDatabaseFactory().newEmbeddedDatabase( path );
        try(Transaction tx = db.beginTx()) {
            Node currentNode = null;
            for ( int i = 0; i < chainSize; i++ )
            {
                Node node = db.createNode();

                if(currentNode != null) {
                    currentNode.createRelationshipTo( node, NEXT );
                }
                currentNode = node;
            }
            tx.success();
        }


        db.shutdown();
    }
}
~~~

<p>To find our distance from the end of the linked list we could write the following cypher query:</p>



~~~cypher

match n  where id(n) = {nodeId}  with n 
match path = (n)-[:NEXT*]->() 
RETURN id(n) AS nodeId, length(path) AS length 
ORDER BY length DESC 
LIMIT 1;
~~~

<p>For simplicity we're finding a node by it's internal node id and then finding the 'NEXT' relationships going out from this node recursively. We then filter the results so that we only get the longest path back which will be our distance to the end of the list.</p>


<p>I noticed that this query would sometimes take 10s of seconds so I wrote a version using the <a href="http://docs.neo4j.org/chunked/stable/tutorial-traversal-java-api.html">Java Traversal API</a> to see whether I could get it any quicker.</p>


<p>This is the Java version:</p>



~~~java

try(Transaction tx = db.beginTx()) {
    Node startNode = db.getNodeById( nodeId );
    TraversalDescription traversal = db.traversalDescription();
    Traverser traverse = traversal
            .depthFirst()
            .relationships( NEXT, Direction.OUTGOING )
            .sort( new Comparator<Path>()
            {
                @Override
                public int compare( Path o1, Path o2 )
                {
                    return Integer.valueOf( o2.length() ).compareTo( o1 .length() );
                }
            } )
            .traverse( startNode );

    Collection<Path> paths = IteratorUtil.asCollection( traverse );

    int maxLength = traverse.iterator().next().length();
    System.out.print( maxLength );

    tx.failure();
}
~~~

<p>This is a bit more verbose than the cypher version but computes the same result. We've sorted the paths by length using a comparator to ensure we get the longest path back first.</p>


<p>I created a little program to warm up the caches and kick off a few iterations where I queried from different nodes and returned the length and time taken. These were the results:</p>



~~~text

--------
(Traversal API) Node:    1, Length: 9998, Time (ms):  15
       (Cypher) Node:    1, Length: 9998, Time (ms): 26225
(Traversal API) Node:  456, Length: 9543, Time (ms):  10
       (Cypher) Node:  456, Length: 9543, Time (ms): 24881
(Traversal API) Node:  761, Length: 9238, Time (ms):   9
       (Cypher) Node:  761, Length: 9238, Time (ms): 9941
--------
(Traversal API) Node:    1, Length: 9998, Time (ms):   9
       (Cypher) Node:    1, Length: 9998, Time (ms): 12537
(Traversal API) Node:  456, Length: 9543, Time (ms):   8
       (Cypher) Node:  456, Length: 9543, Time (ms): 15690
(Traversal API) Node:  761, Length: 9238, Time (ms):   7
       (Cypher) Node:  761, Length: 9238, Time (ms): 9202
--------
(Traversal API) Node:    1, Length: 9998, Time (ms):   8
       (Cypher) Node:    1, Length: 9998, Time (ms): 11905
(Traversal API) Node:  456, Length: 9543, Time (ms):   7
       (Cypher) Node:  456, Length: 9543, Time (ms): 22296
(Traversal API) Node:  761, Length: 9238, Time (ms):   8
       (Cypher) Node:  761, Length: 9238, Time (ms): 8739
--------
~~~

<p>Interestingly when I reduced the size of the linked list to 1000 the difference wasn't so pronounced:</p>



~~~text

--------
(Traversal API) Node:    1, Length: 998, Time (ms):   5
       (Cypher) Node:    1, Length: 998, Time (ms): 174
(Traversal API) Node:  456, Length: 543, Time (ms):   2
       (Cypher) Node:  456, Length: 543, Time (ms):  71
(Traversal API) Node:  761, Length: 238, Time (ms):   1
       (Cypher) Node:  761, Length: 238, Time (ms):  13
--------
(Traversal API) Node:    1, Length: 998, Time (ms):   2
       (Cypher) Node:    1, Length: 998, Time (ms): 111
(Traversal API) Node:  456, Length: 543, Time (ms):   1
       (Cypher) Node:  456, Length: 543, Time (ms):  40
(Traversal API) Node:  761, Length: 238, Time (ms):   1
       (Cypher) Node:  761, Length: 238, Time (ms):  12
--------
(Traversal API) Node:    1, Length: 998, Time (ms):   3
       (Cypher) Node:    1, Length: 998, Time (ms): 129
(Traversal API) Node:  456, Length: 543, Time (ms):   2
       (Cypher) Node:  456, Length: 543, Time (ms):  48
(Traversal API) Node:  761, Length: 238, Time (ms):   0
       (Cypher) Node:  761, Length: 238, Time (ms):  12
--------
~~~

<p>which is good news as most linked lists that we'll create will be in the 10s - 100s range rather than 10,000 which was what I was faced with.</p>


<p>I'm sure cypher will reach parity for this type of query in future which will be great as I like writing cypher much more than I do Java. For now though it's good to know we have a backup option to call on when necessary.</p>


<p>The code is <a href="https://gist.github.com/mneedham/33d42fa1edca604946ec">available as a gist</a> if you want to play around with it further.</p>

