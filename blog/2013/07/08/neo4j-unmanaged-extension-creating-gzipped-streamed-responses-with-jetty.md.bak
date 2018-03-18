+++
draft = false
date="2013-07-08 23:48:23"
title="neo4j Unmanaged Extension: Creating gzipped streamed responses with Jetty"
tag=['neo4j']
category=['neo4j']
+++

<p>I recently wrote a blog post describing how we <a href="http://www.markhneedham.com/blog/2013/07/08/jax-rs-streaming-a-response-using-streamingoutput/">created a streamed response</a> and the next thing we wanted to do was gzip the response to shrink it's size a bit.</p>


<p>A bit of searching led to <a href="http://stackoverflow.com/questions/7546783/uncompress-gzip-http-response-using-jersey-client-api-java">GZIPContentEncodingFilter popping up a lot of times</a> but this is actually needed for a client processing a gripped response rather than helping us to gzip a response from the server.</p>


<p>I noticed that there was <a href="https://groups.google.com/forum/#!topic/neo4j/D_2HcLufDTw">a question about this on the mailing list from about a year ago</a> although <a href="https://twitter.com/mesirii">Michael</a> pointed out that the repository has now moved and <a href="https://github.com/neo4j-contrib/authentication-extension/blob/1.9/src/main/java/org/neo4j/server/extension/auth/AuthenticationExtensionInitializer.java#L84">the example is available here</a> instead.</p>


<p>I adapted the example a bit and ended up with the following lifecycle plugin:</p>



~~~java

package com.markandjim;

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

<p>I then added the following line to 'resources/META-INF/services/org.neo4j.server.plugins.PluginLifecycle:</p>



~~~text

com.markandjim.GZipInitialiser
~~~

<p>After compiling that and deploying the JAR to the 'plugins' I tried calling the end point using cURL:</p>



~~~text

$ curl -H "Accept-Encoding:gzip,deflate" -v  http://localhost:7474/unmanaged/subgraph/1000/1
* About to connect() to localhost port 7474 (#0)
*   Trying ::1...
* Connection refused
*   Trying 127.0.0.1...
* connected
* Connected to localhost (127.0.0.1) port 7474 (#0)
> GET /unmanaged/subgraph/1000/1 HTTP/1.1
> User-Agent: curl/7.24.0 (x86_64-apple-darwin12.0) libcurl/7.24.0 OpenSSL/0.9.8r zlib/1.2.5
> Host: localhost:7474
> Accept: */*
> Accept-Encoding:gzip,deflate
>
< HTTP/1.1 200 OK
< Content-Type: text/plain
< Access-Control-Allow-Origin: *
< Content-Encoding: gzip
< Transfer-Encoding: chunked
< Server: Jetty(6.1.25)

---

gibberish!
~~~

<p>The GZIPContentEncodingFilter that I mentioned earlier comes in handy if we want to call the end point from a Jersey client:</p>



~~~java

public class Neo4jJerseyClient {
    public static void main(String[] args) {
        Client client = Client.create();
        client.addFilter(new GZIPContentEncodingFilter(false));

        WebResource webResource = client.resource("http://localhost:7474/unmanaged/subgraph/1000/1");

        ClientResponse response  = webResource.header("accept-encoding", "gzip,deflate").get(ClientResponse.class);

        System.out.println("response = " + response.getEntity(String.class));
    }
}
~~~

<p>We could also call it using HTTParty from the land of Ruby:</p>



~~~ruby

response = HTTParty.get("http://localhost:7474/unmanaged/subgraph/1000/1", 
  :headers => { 'Accept-Encoding' => 'gzip,deflate' } )

p response
~~~
