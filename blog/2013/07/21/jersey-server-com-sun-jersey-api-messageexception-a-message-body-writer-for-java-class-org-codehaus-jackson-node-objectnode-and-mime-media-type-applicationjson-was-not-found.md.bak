+++
draft = false
date="2013-07-21 10:37:45"
title="Jersey Server: com.sun.jersey.api.MessageException: A message body writer for Java class org.codehaus.jackson.node.ObjectNode and MIME media type application/json was not found"
tag=['jersey']
category=['Java']
+++

<p>I've been <a href="http://www.markhneedham.com/blog/2012/11/28/jersey-com-sun-jersey-api-client-clienthandlerexception-a-message-body-reader-for-java-class-and-mime-media-type-applicationjson-was-not-found/">reacquainted</a> with my good friend <a href="https://jersey.java.net/">Jersey</a> over the last couple of days and in getting up and running was reminded that things which seemed easy at the time aren't as easy when starting from scratch.</p>


<p>I eventually settled on using <a href="https://github.com/sunnygleason">Sunny Gleason</a>'s <a href="https://github.com/sunnygleason/j4-minimal">j4-minimal</a> repository which wires up Jersey with Jackson, Guice and Jetty which seemed like a good place to start.</p>


<p>I prefer building up JSON objects explicitly rather than setting up automatic mapping so the first thing I did was change the <cite><a href="https://github.com/sunnygleason/j4-minimal/blob/master/src/main/java/com/g414/j4/minimal/JacksonResource.java">JacksonResource</a></cite> to have an end point that returned a manually built up JSON object:</p>



~~~java

@Path("/jackson")
public class JacksonResource {
    @GET
    @Produces( { MediaType.APPLICATION_JSON })
    @Path("/awesome/{who}")
    public Response sayOtherGreeting(@PathParam("who") String name) {
        ObjectNode result = JsonNodeFactory.instance.objectNode();
        result.put("name", name);
        return Response.ok().entity(result).build();
    }
}
~~~

<p>When I tried to hit that in the browser I ended up with the following exception:</p>



~~~text

SEVERE: The registered message body writers compatible with the MIME media type are:
application/json ->
  com.sun.jersey.json.impl.provider.entity.JSONJAXBElementProvider$App
  com.sun.jersey.json.impl.provider.entity.JSONArrayProvider$App
  com.sun.jersey.json.impl.provider.entity.JSONObjectProvider$App
  com.sun.jersey.json.impl.provider.entity.JSONRootElementProvider$App
  com.sun.jersey.json.impl.provider.entity.JSONListElementProvider$App
*/* ->
  com.sun.jersey.core.impl.provider.entity.FormProvider
  com.sun.jersey.server.impl.template.ViewableMessageBodyWriter
  com.sun.jersey.core.impl.provider.entity.StringProvider
  com.sun.jersey.core.impl.provider.entity.ByteArrayProvider
  com.sun.jersey.core.impl.provider.entity.FileProvider
  com.sun.jersey.core.impl.provider.entity.InputStreamProvider
  com.sun.jersey.core.impl.provider.entity.DataSourceProvider
  com.sun.jersey.core.impl.provider.entity.XMLJAXBElementProvider$General
  com.sun.jersey.core.impl.provider.entity.ReaderProvider
  com.sun.jersey.core.impl.provider.entity.DocumentProvider
  com.sun.jersey.core.impl.provider.entity.StreamingOutputProvider
  com.sun.jersey.core.impl.provider.entity.SourceProvider$SourceWriter
  com.sun.jersey.json.impl.provider.entity.JSONJAXBElementProvider$General
  com.sun.jersey.json.impl.provider.entity.JSONArrayProvider$General
  com.sun.jersey.json.impl.provider.entity.JSONObjectProvider$General
  com.sun.jersey.json.impl.provider.entity.JSONWithPaddingProvider
  com.sun.jersey.core.impl.provider.entity.XMLRootElementProvider$General
  com.sun.jersey.core.impl.provider.entity.XMLListElementProvider$General
  com.sun.jersey.json.impl.provider.entity.JSONRootElementProvider$General
  com.sun.jersey.json.impl.provider.entity.JSONListElementProvider$General
  com.sun.jersey.json.impl.provider.entity.JacksonProviderProxy

Jul 21, 2013 11:11:17 AM com.sun.jersey.spi.container.ContainerResponse logException
SEVERE: Mapped exception to response: 500 (Internal Server Error)
javax.ws.rs.WebApplicationException: com.sun.jersey.api.MessageException: A message body writer for Java class org.codehaus.jackson.node.ObjectNode, and Java type class org.codehaus.jackson.node.ObjectNode, and MIME media type application/json was not found
	at com.sun.jersey.spi.container.ContainerResponse.write(ContainerResponse.java:285)
	at com.sun.jersey.server.impl.application.WebApplicationImpl._handleRequest(WebApplicationImpl.java:1451)
	at com.sun.jersey.server.impl.application.WebApplicationImpl.handleRequest(WebApplicationImpl.java:1363)
	at com.sun.jersey.server.impl.application.WebApplicationImpl.handleRequest(WebApplicationImpl.java:1353)
	at com.sun.jersey.spi.container.servlet.WebComponent.service(WebComponent.java:414)
	at com.sun.jersey.spi.container.servlet.ServletContainer.service(ServletContainer.java:537)
	at com.sun.jersey.spi.container.servlet.ServletContainer.service(ServletContainer.java:708)
	at javax.servlet.http.HttpServlet.service(HttpServlet.java:848)
	at com.google.inject.servlet.ServletDefinition.doService(ServletDefinition.java:263)
	at com.google.inject.servlet.ServletDefinition.service(ServletDefinition.java:178)
	at com.google.inject.servlet.ManagedServletPipeline.service(ManagedServletPipeline.java:91)
	at com.google.inject.servlet.FilterChainInvocation.doFilter(FilterChainInvocation.java:62)
	at com.google.inject.servlet.ManagedFilterPipeline.dispatch(ManagedFilterPipeline.java:118)
	at com.google.inject.servlet.GuiceFilter.doFilter(GuiceFilter.java:113)
	at org.eclipse.jetty.servlet.ServletHandler$CachedChain.doFilter(ServletHandler.java:1338)
	at org.eclipse.jetty.servlet.ServletHandler.doHandle(ServletHandler.java:484)
	at org.eclipse.jetty.server.session.SessionHandler.doHandle(SessionHandler.java:231)
	at org.eclipse.jetty.server.handler.ContextHandler.doHandle(ContextHandler.java:1065)
	at org.eclipse.jetty.servlet.ServletHandler.doScope(ServletHandler.java:413)
	at org.eclipse.jetty.server.session.SessionHandler.doScope(SessionHandler.java:192)
	at org.eclipse.jetty.server.handler.ContextHandler.doScope(ContextHandler.java:999)
	at org.eclipse.jetty.server.handler.ScopedHandler.handle(ScopedHandler.java:117)
	at org.eclipse.jetty.server.handler.HandlerWrapper.handle(HandlerWrapper.java:111)
	at org.eclipse.jetty.server.Server.handle(Server.java:350)
	at org.eclipse.jetty.server.AbstractHttpConnection.handleRequest(AbstractHttpConnection.java:454)
	at org.eclipse.jetty.server.AbstractHttpConnection.headerComplete(AbstractHttpConnection.java:890)
	at org.eclipse.jetty.server.AbstractHttpConnection$RequestHandler.headerComplete(AbstractHttpConnection.java:944)
	at org.eclipse.jetty.http.HttpParser.parseNext(HttpParser.java:630)
	at org.eclipse.jetty.http.HttpParser.parseAvailable(HttpParser.java:230)
	at org.eclipse.jetty.server.AsyncHttpConnection.handle(AsyncHttpConnection.java:77)
	at org.eclipse.jetty.io.nio.SelectChannelEndPoint.handle(SelectChannelEndPoint.java:606)
	at org.eclipse.jetty.io.nio.SelectChannelEndPoint$1.run(SelectChannelEndPoint.java:46)
	at org.eclipse.jetty.util.thread.QueuedThreadPool.runJob(QueuedThreadPool.java:603)
	at org.eclipse.jetty.util.thread.QueuedThreadPool$3.run(QueuedThreadPool.java:538)
	at java.lang.Thread.run(Thread.java:722)
Caused by: com.sun.jersey.api.MessageException: A message body writer for Java class org.codehaus.jackson.node.ObjectNode, and Java type class org.codehaus.jackson.node.ObjectNode, and MIME media type application/json was not found
	... 35 more
~~~

<p>This is exactly the same problem that I <a href="http://www.markhneedham.com/blog/2012/11/28/jersey-com-sun-jersey-api-client-clienthandlerexception-a-message-body-reader-for-java-class-and-mime-media-type-applicationjson-was-not-found/">wrote about last year with respect to Jersey Client</a>.</p>


<p>It took me a little while but I eventually found a solution to the problem hidden about half way down <a href="http://stackoverflow.com/questions/13108161/a-message-body-writer-for-java-class-not-found">a StackOverflow post for a similar exception</a>.</p>


<p>We need to add the following property to our Jersey config:</p>



~~~java

Map<String, Object> config = new HashMap<String, Object>();
config.put("com.sun.jersey.api.json.POJOMappingFeature", true);
~~~

<p>If we <a href="https://github.com/mneedham/j4-minimal/commit/b2b4ab44da2286cdc0ff3a079ec399b1e5286438">edit the SampleConfig from the template</a> it will now look like this:</p>



~~~java

public class SampleConfig extends GuiceServletContextListener {
    @Override
    protected Injector getInjector() {
        return Guice.createInjector(new ServletModule() {
            @Override
            protected void configureServlets() {
                /* bind the REST resources */
                bind(BenchResource.class);
                bind(SampleResource.class);
                bind(JacksonResource.class);

                /* bind jackson converters for JAXB/JSON serialization */
                bind(MessageBodyReader.class).to(JacksonJsonProvider.class);
                bind(MessageBodyWriter.class).to(JacksonJsonProvider.class);
                Map<String, String> initParams = new HashMap<String, String>();
                initParams.put("com.sun.jersey.config.feature.Trace",
                        "true");
                initParams.put("com.sun.jersey.api.json.POJOMappingFeature", "true");
                serve("*").with(
                        GuiceContainer.class,
                        initParams);
            }
        });
    }

}
~~~

<p>If we hit '/jackson/awesome/mark' it now returns JSON as expected:</p>



~~~bash

$ curl http://localhost:8080/jackson/awesome/mark -w "\n"
{"name":"mark"}
~~~
