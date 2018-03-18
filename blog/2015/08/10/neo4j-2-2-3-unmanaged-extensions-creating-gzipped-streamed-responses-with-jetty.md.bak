+++
draft = false
date="2015-08-10 23:57:01"
title="Neo4j 2.2.3: Unmanaged extensions - Creating gzipped streamed responses with Jetty"
tag=['neo4j']
category=['neo4j']
+++

<p>
Back in 2013 I wrote a <a href="http://www.markhneedham.com/blog/2013/07/08/jax-rs-streaming-a-response-using-streamingoutput/">couple of</a> <a href="http://www.markhneedham.com/blog/2013/07/08/neo4j-unmanaged-extension-creating-gzipped-streamed-responses-with-jetty/">blog posts</a> showing examples of an unmanaged extension which had a streamed and gzipped response but two years on I realised they were a bit out of date and deserved a refresh.
</p>


<p>
When writing unmanaged extensions in Neo4j a good rule of thumb is to try and reduce the amount of objects you keep hanging around. In this context this means that we should stream our response to the client as quickly as possible rather than building it up in memory and sending it in one go.
</p>


<p>
The <a href="http://neo4j.com/docs/2.2.3/server-unmanaged-extensions.html#server-unmanaged-extensions-streaming">documentation has a good example showing how to stream a list of colleagues</a> but in this blog post we'll look at how to do something simpler - we'll create a couple of nodes representing people and then write an unmanaged extension to return them.
</p>


<p>
We'll first create an unmanaged extension which runs a cypher query, iterates through the rows returned and sends them to the client:
</p>



~~~java

@Path("/example")
public class ExampleResource {
    private final GraphDatabaseService db;
    private static final ObjectMapper OBJECT_MAPPER = new ObjectMapper();

    public ExampleResource(@Context GraphDatabaseService db) {
        this.db = db;
    }

    @GET
    @Produces(MediaType.APPLICATION_JSON)
    @Path("/people")
    public Response allNodes() throws IOException {
        StreamingOutput stream = streamQueryResponse("MATCH (n:Person) RETURN n.name AS name");
        return Response.ok().entity(stream).type(MediaType.APPLICATION_JSON).build();
    }

    private StreamingOutput streamQueryResponse(final String query) {
        return new StreamingOutput() {
                @Override
                public void write(OutputStream os) throws IOException, WebApplicationException {
                    JsonGenerator jg = OBJECT_MAPPER.getJsonFactory().createJsonGenerator(os, JsonEncoding.UTF8);
                    jg.writeStartArray();

                    writeQueryResultTo(query, jg);

                    jg.writeEndArray();
                    jg.flush();
                    jg.close();
                }
            };
    }

    private void writeQueryResultTo(String query, JsonGenerator jg) throws IOException {
        try (Result result = db.execute(query)) {
            while (result.hasNext()) {
                Map<String, Object> row = result.next();

                jg.writeStartObject();
                for (Map.Entry<String, Object> entry : row.entrySet()) {
                    jg.writeFieldName(entry.getKey());
                    jg.writeString(entry.getValue().toString());
                }
                jg.writeEndObject();
            }
        }
    }
}
~~~

<p>There's nothing too complicated going on here although notice that we make much more fine grained calls to the JSON Library rather than created a JSON object in memory and calling <cite>ObjectMapper#writeValueAsString</cite> on it.</p>


<p>To get this to work we'd build a JAR containing this class, put that into the plugins folder and then add the following property to <cite>conf/neo4j-server.properties</cite> (or the Neo4j desktop equivalent) before restarting the server:</p>



~~~text

org.neo4j.server.thirdparty_jaxrs_classes=org.neo4j.unmanaged=/unmanaged
~~~

<p>
We can then test it out like this:
</p>



~~~bash

$ curl http://localhost:7474/unmanaged/example/people
[{"name":"Mark"},{"name":"Nicole"}]
~~~

<p>
I've put in a couple of test people nodes - full instructions are available on the <a href="https://github.com/mneedham/dummy-unmanaged-extension">github README page</a>.
</p>


<p>
Next we want to make it possible to send that response in the gzip format. To do that we need to add a GzipFilter to the Neo4j lifecycle. This class has moved to a different namespace in Jetty 9 which Neo4j 2.2.3 depends on, but the following class does the job:
</p>



~~~java

import org.eclipse.jetty.servlets.GzipFilter;

public class GZipInitialiser implements SPIPluginLifecycle {
    private WebServer webServer;

    @Override
    public Collection<Injectable<?>> start(NeoServer neoServer) {
        webServer = getWebServer(neoServer);
        GzipFilter filter = new GzipFilter();

        webServer.addFilter(filter, "/*");
        return Collections.emptyList();
    }

    private WebServer getWebServer(final NeoServer neoServer) {
        if (neoServer instanceof AbstractNeoServer) {
            return ((AbstractNeoServer) neoServer).getWebServer();
        }
        throw new IllegalArgumentException("expected AbstractNeoServer");
    }

    @Override
    public Collection<Injectable<?>> start(GraphDatabaseService graphDatabaseService, Configuration configuration) {
        throw new IllegalAccessError();
    }

    @Override
    public void stop() {

    }
}
~~~

<p>
I needed to include the <cite>jersey-servlets</cite> JAR in my unmanaged extension JAR in order for this to work correctly. Once we redeploy the JAR and restart Neo4j we can try making the same request as above but with a gzip header:
</p>



~~~bash

$ curl -v -H "Accept-Encoding:gzip,deflate" http://localhost:7474/unmanaged/example/people
��V�K�MU�R�M,�V�Ձ��2��sR�jcf(�#
~~~

<p>We can unpack that on the fly by piping it through gunzip to check we get a sensible result:</p>



~~~bash

$ curl -v -H "Accept-Encoding:gzip,deflate" http://localhost:7474/unmanaged/example/people | gunzip
[{"name":"Mark"},{"name":"Nicole"}]
~~~

<p>
And there we have it - a gzipped streamed response. <a href="https://github.com/mneedham/dummy-unmanaged-extension">All the code is on github</a> so give it a try and give me a shout if it doesn't work. The fastest way to get me is probably on our new shiny <a href="http://neo4j-users-slack-invite.herokuapp.com/">neo4j-users Slack group</a>.
</p>

