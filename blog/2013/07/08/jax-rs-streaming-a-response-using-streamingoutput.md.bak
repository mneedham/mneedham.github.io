+++
draft = false
date="2013-07-08 23:19:32"
title="JAX RS: Streaming a Response using StreamingOutput"
tag=['software-development']
category=['Software Development']
+++

<p>A couple of weeks ago <a href="https://twitter.com/jimwebber">Jim</a> and I were building out a <a href="http://docs.neo4j.org/chunked/milestone/server-unmanaged-extensions.html">neo4j unmanaged extension</a> from which we wanted to return the results of a traversal which had a lot of paths.</p>


<p>Our code initially looked a bit like this:</p>



~~~java

package com.markandjim

@Path("/subgraph")
public class ExtractSubGraphResource {
    private final GraphDatabaseService database;

    public ExtractSubGraphResource(@Context GraphDatabaseService database) {
        this.database = database;
    }

    @GET
    @Produces(MediaType.TEXT_PLAIN)
    @Path("/{nodeId}/{depth}")
    public Response hello(@PathParam("nodeId") long nodeId, @PathParam("depth") int depth) {
        Node node = database.getNodeById(nodeId);

        final Traverser paths =  Traversal.description()
                .depthFirst()
                .relationships(DynamicRelationshipType.withName("whatever"))
                .evaluator( Evaluators.toDepth(depth) )
                .traverse(node);

        StringBuilder allThePaths = new StringBuilder();

        for (org.neo4j.graphdb.Path path : paths) {
            allThePaths.append(path.toString() + "\n");
        }

        return Response.ok(allThePaths.toString()).build();
    }
}
~~~

<p>We then compiled that into a JAR, placed it in 'plugins' and added the following line to 'conf/neo4j-server.properties':</p>



~~~text

org.neo4j.server.thirdparty_jaxrs_classes=com.markandjim=/unmanaged
~~~

<p>After we'd restarted the neo4j server we were able to call this end point using cURL like so:</p>



~~~text

$ curl -v  http://localhost:7474/unmanaged/subgraph/1000/10
~~~

<p>This approach works quite well but Jim pointed out that it was quite inefficient to load all those paths up into memory, something which <a href="http://blog.neo4j.org/2012/04/streaming-rest-api-interview-with.html">Michael has written about previously with respect to the the streaming REST API.</a></p>


<p>We thought it would be quite cool if we could stream it as we got to each path. Traverser wraps an iterator so we are lazily evaluating the result set in any case.</p>


<p>After a bit of searching we came <a href="http://stackoverflow.com/questions/12012724/jersey-example-of-using-streamingoutput-as-response-entity">StreamingOutput</a> which is exactly what we need. We adapted our code to use that instead:</p>



~~~java

package com.markandjim

@Path("/subgraph")
public class ExtractSubGraphResource {
    private final GraphDatabaseService database;

    public ExtractSubGraphResource(@Context GraphDatabaseService database) {
        this.database = database;
    }

    @GET
    @Produces(MediaType.TEXT_PLAIN)
    @Path("/{nodeId}/{depth}")
    public Response hello(@PathParam("nodeId") long nodeId, @PathParam("depth") int depth) {
        Node node = database.getNodeById(nodeId);

        final Traverser paths =  Traversal.description()
                .depthFirst()
                .relationships(DynamicRelationshipType.withName("whatever"))
                .evaluator( Evaluators.toDepth(depth) )
                .traverse(node);

        StreamingOutput stream = new StreamingOutput() {
            @Override
            public void write(OutputStream os) throws IOException, WebApplicationException {
                Writer writer = new BufferedWriter(new OutputStreamWriter(os));

                for (org.neo4j.graphdb.Path path : paths) {
                    writer.write(path.toString() + "\n");
                }
                writer.flush();
            }
        };

        return Response.ok(stream).build();
    }
~~~

<p>As far as I can tell the only discernible difference between the two approaches is that you get an almost immediate response from the streamed approached whereas the first approach has to put everything in the StringBuilder first.</p>


<p>Both approaches make use of <a href="http://en.wikipedia.org/wiki/Chunked_transfer_encoding">chunked transfer encoding</a> which according to tcpdump seems to have a maximum packet size of 16332 bytes:</p>



~~~bash

00:10:27.361521 IP localhost.7474 > localhost.55473: Flags [.], seq 6098196:6114528, ack 179, win 9175, options [nop,nop,TS val 784819663 ecr 784819662], length 16332

00:10:27.362278 IP localhost.7474 > localhost.55473: Flags [.], seq 6147374:6163706, ack 179, win 9175, options [nop,nop,TS val 784819663 ecr 784819663], length 16332
~~~
