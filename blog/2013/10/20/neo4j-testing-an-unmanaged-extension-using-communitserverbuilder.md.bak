+++
draft = false
date="2013-10-20 21:46:16"
title="Neo4j: Testing an unmanaged extension using CommunityServerBuilder"
tag=['neo4j']
category=['neo4j']
+++

<p>I've been playing around with <a href="http://docs.neo4j.org/chunked/milestone/server-unmanaged-extensions.html">Neo4j unmanaged extensions</a> recently and I wanted to be able to check that it worked properly without having to deploy it to a real Neo4j server.</p>


<p>I'd previously used <cite><a href="http://grepcode.com/file/repo1.maven.org/maven2/org.neo4j/neo4j-kernel/1.2-1.2/org/neo4j/kernel/ImpermanentGraphDatabase.java">ImpermanentGraphDatabase</a></cite> when using Neo4j embedded and <a href="https://twitter.com/iansrobinson">Ian</a> pointed me towards <cite>CommunityServerBuilder</cite> which allows us to do a similar thing in Neo4j server world.</p>


<p>I've created an example of a <a href="https://github.com/mneedham/dummy-unmanaged-extension/blob/master/src/main/java/org/neo4j/unmanaged/DummyResource.java">dummy unmanaged extension</a> and <a href="https://github.com/mneedham/dummy-unmanaged-extension/blob/master/src/test/java/org/neo4j/unmanaged/DummyResourceTest.java">test</a> showing this approach but it's reasonably simple.</p>


<p>Given the following unmanaged extension:</p>



~~~java

package org.neo4j.unmanaged;

@Path("/dummy")
public class DummyResource
{
    private final ExecutionEngine executionEngine;
    private static final ObjectMapper OBJECT_MAPPER = new ObjectMapper();

    public DummyResource( @Context GraphDatabaseService database )
    {
        this.executionEngine = new ExecutionEngine(database);
    }

    @GET
    @Produces(MediaType.APPLICATION_JSON)
    @Path("/all-nodes")
    public Response uploadNodesFile(  ) throws IOException
    {
        ExecutionResult result = executionEngine.execute("START n = node(*) RETURN n.name ORDER BY n.name");

        ObjectNode root = JsonNodeFactory.instance.objectNode();
        for (String column : result.columns()) {
            ResourceIterator<Object> rows = result.columnAs(column);

            ArrayNode resultRows = JsonNodeFactory.instance.arrayNode();
            while(rows.hasNext()) {
                Object row = rows.next();

                if(row != null) {
                    resultRows.add(row.toString());
                }
            }

            root.put(column, resultRows);
        }

        return Response.status( 200 )
                .entity(OBJECT_MAPPER.writeValueAsString(root))
                .type(MediaType.APPLICATION_JSON).build();
    }
}
~~~

<p>We would write the following test which exposes the 'all-nodes' resource at '/unmanaged/dummy/all-nodes':</p>



~~~java

package org.neo4j.unmanaged;

public class DummyResourceTest {
    private GraphDatabaseAPI db;
    private CommunityNeoServer server;

    @Before
    public void before() throws IOException {
        ServerSocket serverSocket = new ServerSocket(0);

        server = CommunityServerBuilder
                .server()
                .onPort(serverSocket.getLocalPort())
                .withThirdPartyJaxRsPackage("org.neo4j.unmanaged", "/unmanaged")
                .build();

        server.start();
        db = server.getDatabase().getGraph();
    }

    @After
    public void after() {
        server.stop();
    }

    @Test
    public void shouldReturnAllTheNodes() {
        Transaction tx = db.beginTx();
        db.createNode().setProperty("name", "Mark");
        db.createNode().setProperty("name", "Dave");
        tx.success();
        tx.close();

        JsonNode response = jerseyClient()
                .resource(server.baseUri().toString() + "unmanaged/dummy/all-nodes")
                .get(ClientResponse.class)
                .getEntity(JsonNode.class);

        assertEquals("Dave", response.get("n.name").get(0).asText());
        assertEquals("Mark", response.get("n.name").get(1).asText());
    }

    private Client jerseyClient() {
        DefaultClientConfig defaultClientConfig = new DefaultClientConfig();
        defaultClientConfig.getClasses().add(JacksonJsonProvider.class);
        return Client.create(defaultClientConfig);
    }
}
~~~

<p>Here we add a couple of nodes directly against the Java API and then call our unmanaged extension using a Jersey HTTP client. <cite>CommunityServerBuilder</cite> spins up an ephemeral store under the covers and we pick a random free port for Neo4j server by using <cite>ServerSocket#getLocalPort</cite>.</p>


<p>We import <cite>CommunityServerBuilder</cite> by including the following dependency:</p>



~~~xml

        <dependency>
            <groupId>org.neo4j.app</groupId>
            <artifactId>neo4j-server</artifactId>
            <version>${neo4j.version}</version>
            <type>test-jar</type>
        </dependency>
~~~

<p>And that's it!</p>

