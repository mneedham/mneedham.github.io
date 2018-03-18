+++
draft = false
date="2014-01-27 11:32:03"
title="Neo4j: org.eclipse.jetty.io.EofException - Caused by: java.io.IOException: Broken pipe"
tag=['neo4j']
category=['neo4j']
+++

<p>From scouring the Neo4j google group and Stack Overflow I've noticed that <a href="https://www.google.co.uk/search?q=neo4j+eofexception&oq=neo4j+eofexception&aqs=chrome..69i57.2370j0j4&sourceid=chrome&espv=210&es_sm=91&ie=UTF-8">a few people</a> have been hitting the following exception when executing queries against Neo4j server:</p>



~~~text

SEVERE: The response of the WebApplicationException cannot be utilized as the response is already committed. Re-throwing to the HTTP container
javax.ws.rs.WebApplicationException: javax.ws.rs.WebApplicationException: org.eclipse.jetty.io.EofException
	at org.neo4j.server.rest.repr.OutputFormat$1.write(OutputFormat.java:174)
	at com.sun.jersey.core.impl.provider.entity.StreamingOutputProvider.writeTo(StreamingOutputProvider.java:71)
	at com.sun.jersey.core.impl.provider.entity.StreamingOutputProvider.writeTo(StreamingOutputProvider.java:57)
	at com.sun.jersey.spi.container.ContainerResponse.write(ContainerResponse.java:306)
	at com.sun.jersey.server.impl.application.WebApplicationImpl._handleRequest(WebApplicationImpl.java:1437)
	at com.sun.jersey.server.impl.application.WebApplicationImpl.handleRequest(WebApplicationImpl.java:1349)
	at com.sun.jersey.server.impl.application.WebApplicationImpl.handleRequest(WebApplicationImpl.java:1339)
	at com.sun.jersey.spi.container.servlet.WebComponent.service(WebComponent.java:416)
	at com.sun.jersey.spi.container.servlet.ServletContainer.service(ServletContainer.java:537)
	at com.sun.jersey.spi.container.servlet.ServletContainer.service(ServletContainer.java:699)
	at javax.servlet.http.HttpServlet.service(HttpServlet.java:848)
	at org.eclipse.jetty.servlet.ServletHolder.handle(ServletHolder.java:698)
	at org.eclipse.jetty.servlet.ServletHandler$CachedChain.doFilter(ServletHandler.java:1506)
	at org.neo4j.server.rest.security.SecurityFilter.doFilter(SecurityFilter.java:112)
	at org.eclipse.jetty.servlet.ServletHandler$CachedChain.doFilter(ServletHandler.java:1477)
	at org.eclipse.jetty.servlet.ServletHandler.doHandle(ServletHandler.java:503)
	at org.eclipse.jetty.server.session.SessionHandler.doHandle(SessionHandler.java:211)
	at org.eclipse.jetty.server.handler.ContextHandler.doHandle(ContextHandler.java:1096)
	at org.eclipse.jetty.servlet.ServletHandler.doScope(ServletHandler.java:432)
	at org.eclipse.jetty.server.session.SessionHandler.doScope(SessionHandler.java:175)
	at org.eclipse.jetty.server.handler.ContextHandler.doScope(ContextHandler.java:1030)
	at org.eclipse.jetty.server.handler.ScopedHandler.handle(ScopedHandler.java:136)
	at org.eclipse.jetty.server.handler.HandlerList.handle(HandlerList.java:52)
	at org.eclipse.jetty.server.handler.HandlerWrapper.handle(HandlerWrapper.java:97)
	at org.eclipse.jetty.server.Server.handle(Server.java:445)
	at org.eclipse.jetty.server.HttpChannel.handle(HttpChannel.java:268)
	at org.eclipse.jetty.server.HttpConnection.onFillable(HttpConnection.java:229)
	at org.eclipse.jetty.io.AbstractConnection$ReadCallback.run(AbstractConnection.java:358)
	at org.eclipse.jetty.util.thread.QueuedThreadPool.runJob(QueuedThreadPool.java:601)
	at org.eclipse.jetty.util.thread.QueuedThreadPool$3.run(QueuedThreadPool.java:532)
	at java.lang.Thread.run(Thread.java:744)
Caused by: javax.ws.rs.WebApplicationException: org.eclipse.jetty.io.EofException
	at org.neo4j.server.rest.repr.formats.StreamingJsonFormat$StreamingListWriter.writeValue(StreamingJsonFormat.java:316)
	at org.neo4j.server.rest.repr.ListWriter.writeValue(ListWriter.java:75)
	at org.neo4j.server.rest.repr.ValueRepresentation.addTo(ValueRepresentation.java:49)
	at org.neo4j.server.rest.repr.ListRepresentation.serialize(ListRepresentation.java:65)
	at org.neo4j.server.rest.repr.Serializer.serialize(Serializer.java:75)
	at org.neo4j.server.rest.repr.MappingSerializer.putList(MappingSerializer.java:61)
	at org.neo4j.server.rest.repr.ListRepresentation.putTo(ListRepresentation.java:85)
	at org.neo4j.server.rest.repr.ObjectRepresentation$PropertyGetter.putTo(ObjectRepresentation.java:133)
	at org.neo4j.server.rest.repr.ObjectRepresentation.serialize(ObjectRepresentation.java:144)
	at org.neo4j.server.rest.repr.MappingRepresentation.serialize(MappingRepresentation.java:41)
	at org.neo4j.server.rest.repr.OutputFormat$1.write(OutputFormat.java:160)
	... 30 more
Caused by: org.eclipse.jetty.io.EofException
	at org.eclipse.jetty.io.ChannelEndPoint.flush(ChannelEndPoint.java:186)
	at org.eclipse.jetty.io.WriteFlusher.write(WriteFlusher.java:335)
	at org.eclipse.jetty.io.AbstractEndPoint.write(AbstractEndPoint.java:125)
	at org.eclipse.jetty.server.HttpConnection$ContentCallback.process(HttpConnection.java:784)
	at org.eclipse.jetty.util.IteratingCallback.iterate(IteratingCallback.java:79)
	at org.eclipse.jetty.server.HttpConnection.send(HttpConnection.java:356)
	at org.eclipse.jetty.server.HttpChannel.sendResponse(HttpChannel.java:631)
	at org.eclipse.jetty.server.HttpChannel.write(HttpChannel.java:661)
	at org.eclipse.jetty.server.HttpOutput.write(HttpOutput.java:198)
	at com.sun.jersey.spi.container.servlet.WebComponent$Writer.write(WebComponent.java:307)
	at com.sun.jersey.spi.container.ContainerResponse$CommittingOutputStream.write(ContainerResponse.java:134)
	at org.codehaus.jackson.impl.Utf8Generator._flushBuffer(Utf8Generator.java:1754)
	at org.codehaus.jackson.impl.Utf8Generator.writeNumber(Utf8Generator.java:886)
	at org.codehaus.jackson.map.ser.StdSerializers$LongSerializer.serialize(StdSerializers.java:170)
	at org.codehaus.jackson.map.ser.StdSerializers$LongSerializer.serialize(StdSerializers.java:158)
	at org.codehaus.jackson.map.ser.StdSerializerProvider._serializeValue(StdSerializerProvider.java:610)
	at org.codehaus.jackson.map.ser.StdSerializerProvider.serializeValue(StdSerializerProvider.java:256)
	at org.codehaus.jackson.map.ObjectMapper.writeValue(ObjectMapper.java:1613)
	at org.codehaus.jackson.impl.JsonGeneratorBase.writeObject(JsonGeneratorBase.java:314)
	at org.neo4j.server.rest.repr.formats.StreamingJsonFormat$StreamingListWriter.writeValue(StreamingJsonFormat.java:312)
	... 40 more
Caused by: java.io.IOException: Broken pipe
	at sun.nio.ch.FileDispatcherImpl.writev0(Native Method)
	at sun.nio.ch.SocketDispatcher.writev(SocketDispatcher.java:51)
	at sun.nio.ch.IOUtil.write(IOUtil.java:148)
	at sun.nio.ch.SocketChannelImpl.write(SocketChannelImpl.java:524)
	at org.eclipse.jetty.io.ChannelEndPoint.flush(ChannelEndPoint.java:167)
	... 59 more
~~~

<p>I'd not come across it myself but the error message suggests that the client has closed the connection while the server is still trying to write out a response.</p>


<p>This suggests that you need to write a query which runs for a long time. I created the following data set to try and force this to happen:</p>



~~~java

public class DenseNodes
{
    private static final DynamicRelationshipType FOO = DynamicRelationshipType.withName( "FOO" );
    private static final Label BAR = DynamicLabel.label( "Bar" );

    public static void main( String[] args ) throws IOException
    {
        String path = "/tmp/dense";

        FileUtils.deleteRecursively( new File( path ) );

        GraphDatabaseService db = new GraphDatabaseFactory().newEmbeddedDatabase( path );

        for ( int i = 0; i < 10; i++ )
        {
            try ( Transaction tx = db.beginTx() )
            {
                Node node = db.createNode( BAR );

                for ( int j = 0; j < 100_000; j++ )
                {
                    node.createRelationshipTo( db.createNode(), FOO );
                }

                tx.success();
            }
        }
    }
}
~~~

<p>This script creates 10 nodes with 100,000 relationships and as a by-product we have 1,000,000 nodes with 1 relationship.</p>


<p>We can execute the following query using a Jersey client to take us over the timeout and force the EOFException:</p>



~~~java

public class DenseMe
{
    public static void main( String[] args ) throws IOException
    {
        String query = "MATCH (a:Bar)-[:`FOO`]->(b) RETURN a,b";

        long start = System.currentTimeMillis();
        executeViaHTTP( query );
        long end = System.currentTimeMillis();

        System.out.println(end - start);
    }

    private static void executeViaHTTP( String query ) throws IOException
    {
        ObjectNode entity = JsonNodeFactory.instance.objectNode();
        entity.put("query", query );

        ClientResponse response = client().resource( "http://localhost:7474/db/data/cypher" )
                .accept( MediaType.APPLICATION_JSON_TYPE )
                .type(MediaType.APPLICATION_JSON_TYPE)
                .post( ClientResponse.class, entity );

        InputStream stream = response.getEntityInputStream();

        BufferedReader reader = new BufferedReader( new InputStreamReader( stream ) );
        char[] buffer = new char[1024];
        int bytesRead;
        while ( (bytesRead = reader.read( buffer )) != -1 )
        {
            for ( int i = 0; i < bytesRead; i++ )
            {
                System.out.print( buffer[i] );
            }
        }
    }

    private static Client client()
    {
        DefaultClientConfig defaultClientConfig = new DefaultClientConfig();
        defaultClientConfig.getClasses().add( JacksonJsonProvider.class );
        Client client = Client.create( defaultClientConfig );
        return client;
    }
}
~~~

<p>There are two ways that we can attempt to work around this problem:</p>


<ol>
<li>Increase the timeout on the Jersey Client</li>
<li>Stream the response to the client so we don't build up such a huge response on the server</p>

</ol>

<p>We'll start with the former, which requires the following tweak to the <cite>client</cite> function:</p>



~~~java

private static Client client()
{
    DefaultClientConfig defaultClientConfig = new DefaultClientConfig();
    defaultClientConfig.getClasses().add( JacksonJsonProvider.class );
    Client client = Client.create( defaultClientConfig );
    client.setConnectTimeout(1_000_000);
    client.setReadTimeout( 1_000_000 );
    return client;
}
~~~

<p>If we run that we'll end up with the following response using a 4GB heap:</p>



~~~text

{
  "message" : "Java heap space",
  "exception" : "OutOfMemoryError",
  "fullname" : "java.lang.OutOfMemoryError",
  "stacktrace" : [ ]
}
~~~

<p>I was tailing the GC logs while running the query and the majority of time was being spent in Full GC while the query was running:</p>



~~~text

2014-01-27T10:27:26.101+0000: 239848.812: Total time for which application threads were stopped: 5.5309550 seconds
2014-01-27T10:27:26.101+0000: 239848.812: [Full GC2014-01-27T10:27:26.101+0000: 239848.812: [CMS: 3512768K->3512768K(3512768K), 5.4359920 secs] 4126207K->4126207K(4126208K), [CMS Perm : 41512K->41512K(69300K)], 5.4360820 secs] [Times: user=5.43 sys=0.00, real=5.43 secs]
2014-01-27T10:27:31.537+0000: 239854.249: [Full GC2014-01-27T10:27:31.537+0000: 239854.249: [CMS: 3512768K->3512768K(3512768K), 5.4878690 secs] 4126207K->4126207K(4126208K), [CMS Perm : 41512K->41512K(69300K)], 5.4879470 secs] [Times: user=5.49 sys=0.01, real=5.49 secs]
2014-01-27T10:27:37.025+0000: 239859.737: Total time for which application threads were stopped: 10.9243140 seconds
2014-01-27T10:27:37.025+0000: 239859.737: [Full GC2014-01-27T10:27:37.025+0000: 239859.737: [CMS: 3512768K->3512768K(3512768K), 5.4437040 secs] 4126207K->4126207K(4126208K), [CMS Perm : 41512K->41512K(69300K)], 5.4437790 secs] [Times: user=5.44 sys=0.01, real=5.44 secs]
2014-01-27T10:27:42.469+0000: 239865.181: [Full GC2014-01-27T10:27:42.469+0000: 239865.181: [CMS: 3512768K->3512768K(3512768K), 5.4283480 secs] 4126207K->4126207K(4126208K), [CMS Perm : 41512K->41512K(69300K)], 5.4284400 secs] [Times: user=5.43 sys=0.00, real=5.43 secs]
2014-01-27T10:27:47.898+0000: 239870.609: Total time for which application threads were stopped: 10.8724950 seconds
2014-01-27T10:27:47.898+0000: 239870.609: [Full GC2014-01-27T10:27:47.898+0000: 239870.609: [CMS: 3512768K->3512768K(3512768K), 5.4385630 secs] 4126208K->4126207K(4126208K), [CMS Perm : 41512K->41512K(69300K)], 5.4386540 secs] [Times: user=5.43 sys=0.01, real=5.44 secs]
2014-01-27T10:27:53.337+0000: 239876.048: Total time for which application threads were stopped: 5.4389110 seconds
~~~

<p>The second option is to <a href="http://docs.neo4j.org/chunked/stable/rest-api-streaming.html">stream back the response</a> by adding the following header to our request:</p>



~~~java

ClientResponse response = client().resource( "http://localhost:7474/db/data/cypher" )
    .accept( MediaType.APPLICATION_JSON_TYPE )
    .type(MediaType.APPLICATION_JSON_TYPE)
    .header( "X-Stream", "true" )
    .post( ClientResponse.class, entity );
~~~

<p>If we do that then we'll get back the first rows of the query immediately although although we'll have to be careful with what we do with the response or we could see an OutOfMemory exception on the client instead.</p>


<p>We might also want to think whether we actually need to return that many rows in the first place. A lot of the time a subset is more than enough.</p>

