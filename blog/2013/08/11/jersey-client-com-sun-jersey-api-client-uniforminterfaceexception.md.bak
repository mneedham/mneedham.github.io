+++
draft = false
date="2013-08-11 08:07:01"
title="Jersey Client: com.sun.jersey.api.client.UniformInterfaceException"
tag=['java']
category=['Java']
+++

<p>As I mentioned in <a href="http://www.markhneedham.com/blog/2013/07/28/jersey-client-testing-external-calls/">a post a couple of weeks ago</a> we've been doing some which involved calling the neo4j server's <a href="http://docs.neo4j.org/chunked/stable/ha-rest-info.html#_the_endpoints">HA URI</a> to determine whether a machine was slave or master.</p>


<p>We started off with the following code using <a href="https://jersey.java.net/documentation/latest/user-guide.html#client">jersey-client</a>:</p>



~~~java

public class HaSpike {
    public static void main(String[] args) {
        String response = client()
                .resource("http://localhost:7474/db/manage/server/ha/slave")
                .accept(MediaType.TEXT_PLAIN)
                .get(String.class);

        System.out.println("response = " + response);
    }

    private static Client client() {
        DefaultClientConfig defaultClientConfig = new DefaultClientConfig();
        defaultClientConfig.getClasses().add(JacksonJsonProvider.class);
        return Client.create(defaultClientConfig);
    }
}
~~~

<p>which works fine when the server is actually a slave:</p>



~~~text

response = true
~~~

<p>but blows up in style if the server is the master:</p>



~~~text

Exception in thread "main" com.sun.jersey.api.client.UniformInterfaceException: GET http://localhost:7474/db/manage/server/ha/slave returned a response status of 404 Not Found
	at com.sun.jersey.api.client.WebResource.handle(WebResource.java:686)
	at com.sun.jersey.api.client.WebResource.access$200(WebResource.java:74)
	at com.sun.jersey.api.client.WebResource$Builder.get(WebResource.java:507)
	at HaSpike.main(HaSpike.java:10)
	at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
	at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:57)
	at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
	at java.lang.reflect.Method.invoke(Method.java:601)
	at com.intellij.rt.execution.application.AppMain.main(AppMain.java:120)
~~~

<p>We return a 404 status code from that URI if you're not a slave because it simplifies things for upstream load balancers but I thought Jersey would just return the body of the response rather than throwing an exception.</p>


<p>A quick browse of the Jersey code showed a way around this:</p>



~~~Java

    private <T> T handle(Class<T> c, ClientRequest ro) throws UniformInterfaceException, ClientHandlerException {
        setProperties(ro);
        ClientResponse r = getHeadHandler().handle(ro);
        
        if (c == ClientResponse.class) return c.cast(r);
        
        if (r.getStatus() < 300) return r.getEntity(c);
        
        throw new UniformInterfaceException(r,
                ro.getPropertyAsFeature(ClientConfig.PROPERTY_BUFFER_RESPONSE_ENTITY_ON_EXCEPTION, true));
    }
~~~

<p><cite>WebResource#handle</cite> gets called by <cite>WebResource#get</cite> and if we pass <cite>ClientResponse.class</cite> to it instead of <cite>String.class</cite> we can get around this because the code returns without checking the status of the response.</p>


<p>Our code needs to read like this:</p>



~~~java

public class HaSpike {
    public static void main(String[] args) {
        ClientResponse response = client()
                .resource("http://localhost:7474/db/manage/server/ha/slave")
                .accept(MediaType.TEXT_PLAIN)
                .get(ClientResponse.class);

        System.out.println("response = " + response.getEntity(String.class));
    }

    ...
}
~~~

<p>And if we run it, this time we get the expected result:</p>



~~~text

response = false
~~~
