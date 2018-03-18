+++
draft = false
date="2012-11-28 06:03:55"
title="Jersey: com.sun.jersey.api.client.ClientHandlerException: A message body reader for Java class [...] and MIME media type application/json was not found"
tag=['java', 'jersey']
category=['Java']
+++

We've used the <a href="http://jersey.java.net/">Jersey</a> library on the last couple of Java based applications that I've worked on and one thing we've done on both of them is write services that communicate with each other using JSON.

On both occasions we didn't quite setup the Jersey client correctly and ended up with an error along these lines when making a call to an end point:


~~~java

com.sun.jersey.api.client.ClientHandlerException: A message body reader for Java class java.util.ArrayList, and Java type java.util.ArrayList<com.blah.Message>, and MIME media type application/json was not found
! at com.sun.jersey.api.client.ClientResponse.getEntity(ClientResponse.java:561)
! at com.sun.jersey.api.client.ClientResponse.getEntity(ClientResponse.java:535)
! at com.sun.jersey.api.client.WebResource.handle(WebResource.java:696)
! at com.sun.jersey.api.client.WebResource.access$300(WebResource.java:74)
! at com.sun.jersey.api.client.WebResource$Builder.get(WebResource.java:512)
...
! at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
! at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:57)
! at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
! at java.lang.reflect.Method.invoke(Method.java:601)
! at com.sun.jersey.spi.container.JavaMethodInvokerFactory$1.invoke(JavaMethodInvokerFactory.java:60)
! at com.sun.jersey.server.impl.model.method.dispatch.AbstractResourceMethodDispatchProvider$TypeOutInvoker._dispatch(AbstractResourceMethodDispatchProvider.java:185)
! at com.sun.jersey.server.impl.model.method.dispatch.ResourceJavaMethodDispatcher.dispatch(ResourceJavaMethodDispatcher.java:75)
! at com.yammer.metrics.jersey.InstrumentedResourceMethodDispatchProvider$TimedRequestDispatcher.dispatch(InstrumentedResourceMethodDispatchProvider.java:34)
! at com.sun.jersey.server.impl.uri.rules.HttpMethodRule.accept(HttpMethodRule.java:302)
! at com.sun.jersey.server.impl.uri.rules.RightHandPathRule.accept(RightHandPathRule.java:147)
! at com.sun.jersey.server.impl.uri.rules.ResourceObjectRule.accept(ResourceObjectRule.java:100)
! at com.sun.jersey.server.impl.uri.rules.RightHandPathRule.accept(RightHandPathRule.java:147)
! at com.sun.jersey.server.impl.uri.rules.RootResourceClassesRule.accept(RootResourceClassesR
~~~

To get around this problem we need to make sure we've added the 'JacksonJsonProvider' to the Jersey client config like so:


~~~java

DefaultClientConfig defaultClientConfig = new DefaultClientConfig();
defaultClientConfig.getClasses().add(JacksonJsonProvider.class);
Client client = Client.create(defaultClientConfig);
~~~

I'm pretty sure that's documented somewhere in the depths of the Jersey wiki but since we've now ended up debugging this problem twice I thought it was worth writing down!
