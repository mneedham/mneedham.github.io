+++
draft = false
date="2013-08-17 20:25:28"
title="Jersey Client: java.net.ProtocolException: Server redirected too many times/Setting cookies on request"
tag=['java', 'jersey']
category=['Java']
+++

<p>A couple of weeks ago I was trying to write a test around some OAuth code that we have on an internal application and I was using <a href="https://jersey.java.net/documentation/latest/user-guide.html#client">Jersey Client</a> to send the various requests.</p>


<p>I initially started with the following code:</p>



~~~java

Client = Client.create();
ClientResponse response = client.resource( "http://localhost:59680" ).get( ClientResponse.class );
~~~

<p>but when I ran the test I was getting the following exception:</p>



~~~text

com.sun.jersey.api.client.ClientHandlerException: java.net.ProtocolException: Server redirected too many  times (20)
	at com.sun.jersey.client.urlconnection.URLConnectionClientHandler.handle(URLConnectionClientHandler.java:151)
	at com.sun.jersey.api.client.Client.handle(Client.java:648)
	at com.sun.jersey.api.client.WebResource.handle(WebResource.java:680)
	at com.sun.jersey.api.client.WebResource.get(WebResource.java:191)
	at com.neotechnology.testlab.manager.webapp.AuthenticationIntegrationTest.shouldRedirectToGitHubForAuthentication(AuthenticationIntegrationTest.java:81)
	at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
	at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:39)
	at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:25)
	at org.junit.runners.model.FrameworkMethod$1.runReflectiveCall(FrameworkMethod.java:45)
	at org.junit.internal.runners.model.ReflectiveCallable.run(ReflectiveCallable.java:15)
	at org.junit.runners.model.FrameworkMethod.invokeExplosively(FrameworkMethod.java:42)
	at org.junit.internal.runners.statements.InvokeMethod.evaluate(InvokeMethod.java:20)
	at com.neotechnology.kirkaldy.testing.Resources$1.evaluate(Resources.java:84)
	at com.neotechnology.kirkaldy.testing.FailureOutput$2.evaluate(FailureOutput.java:37)
	at org.junit.rules.RunRules.evaluate(RunRules.java:18)
	at org.junit.runners.ParentRunner.runLeaf(ParentRunner.java:263)
	at org.junit.runners.BlockJUnit4ClassRunner.runChild(BlockJUnit4ClassRunner.java:68)
	at org.junit.runners.BlockJUnit4ClassRunner.runChild(BlockJUnit4ClassRunner.java:47)
	at org.junit.runners.ParentRunner$3.run(ParentRunner.java:231)
	at org.junit.runners.ParentRunner$1.schedule(ParentRunner.java:60)
	at org.junit.runners.ParentRunner.runChildren(ParentRunner.java:229)
	at org.junit.runners.ParentRunner.access$000(ParentRunner.java:50)
	at org.junit.runners.ParentRunner$2.evaluate(ParentRunner.java:222)
	at org.junit.runners.ParentRunner.run(ParentRunner.java:300)
	at org.junit.runner.JUnitCore.run(JUnitCore.java:157)
	at com.intellij.rt.execution.junit.JUnitStarter.main(JUnitStarter.java:63)
Caused by: java.net.ProtocolException: Server redirected too many  times (20)
	at sun.net.www.protocol.http.HttpURLConnection.getInputStream(HttpURLConnection.java:1446)
	at java.net.HttpURLConnection.getResponseCode(HttpURLConnection.java:379)
	at com.sun.jersey.client.urlconnection.URLConnectionClientHandler._invoke(URLConnectionClientHandler.java:249)
	at com.sun.jersey.client.urlconnection.URLConnectionClientHandler.handle(URLConnectionClientHandler.java:149)
	... 28 more
~~~

<p>If we check the traffic going across port 59680 we can see what's going wrong:</p>



~~~text

$ sudo ngrep -d lo0 port 59680
interface: lo0 (127.0.0.0/255.0.0.0)
filter: (ip) and ( port 59680 )
#####
T 127.0.0.1:59704 -> 127.0.0.1:59680 [AP]
  GET / HTTP/1.1..User-Agent: Java/1.6.0_45..Host: localhost:59680..Accept: text/html, image/gif, image/jpeg, *; q=.2, */*; q=.2..Connection: keep-alive....
##
T 127.0.0.1:59680 -> 127.0.0.1:59704 [AP]
  HTTP/1.1 302 Found..Set-Cookie: JSESSIONID=mdyw3a4fmqc1b6p53birm4dd;Path=/..Expires: Thu, 01 Jan 1970 00:00:00 GMT..Location: http://localhost:59679/authorize?client_id=basic-client&state=the-state&scope=user%2Crepo..Content-Length
  : 0..Server: Jetty(8.1.8.v20121106)....
###########
T 127.0.0.1:59707 -> 127.0.0.1:59680 [AP]
  GET /auth/callback?code=timey-wimey&state=the-state HTTP/1.1..User-Agent: Java/1.6.0_45..Host: localhost:59680..Accept: text/html, image/gif, image/jpeg, *; q=.2, */*; q=.2..Connection: keep-alive....
##
T 127.0.0.1:59680 -> 127.0.0.1:59707 [AP]
  HTTP/1.1 302 Found..Cache-Control: no-cache..Set-Cookie: JSESSIONID=8gggez0ns9ftiex4314mbgz9;Path=/..Expires: Thu, 01 Jan 1970 00:00:00 GMT..Location: http://localhost:59680/..Content-Length: 0..Server: Jetty(8.1.8.v20121106)....
###########
T 127.0.0.1:59713 -> 127.0.0.1:59680 [AP]
  GET / HTTP/1.1..User-Agent: Java/1.6.0_45..Host: localhost:59680..Accept: text/html, image/gif, image/jpeg, *; q=.2, */*; q=.2..Connection: keep-alive....
##
~~~

<p>The response we receive includes a direction to the client to store a cookie but we can see on the next request that the cookie hasn't been included.</p>


<p>I came across <a href="http://stackoverflow.com/questions/6713893/jersey-client-adding-cookies-to-request">this post which had a few suggestions on how to get around the problem</a> but the only approach that worked for me was to use jersey-apache-client for which I added the following dependency:</p>



~~~xml

<dependency>
  <groupId>com.sun.jersey.contribs</groupId>
  <artifactId>jersey-apache-client</artifactId>
  <version>1.13</version>
  <type>jar</type>
</dependency>
~~~

<p>I then change my client code to read like this:</p>



~~~java

ApacheHttpClientConfig config = new DefaultApacheHttpClientConfig();
config.getProperties().put(ApacheHttpClientConfig.PROPERTY_HANDLE_COOKIES, true);
ApacheHttpClient client = ApacheHttpClient.create( config );
client.setFollowRedirects(true);
client.getClientHandler().getHttpClient().getParams().setBooleanParameter( HttpClientParams.ALLOW_CIRCULAR_REDIRECTS, true );
ClientResponse response = client.resource( "http://localhost:59680" ).get( ClientResponse.class );
~~~

<p>If we run that and watch the output using ngrep we can see that it now handles cookies correctly:</p>



~~~text

$ sudo ngrep -d lo0 port 59680
Password:
interface: lo0 (127.0.0.0/255.0.0.0)
filter: (ip) and ( port 59680 )
	#####
T 127.0.0.1:60372 -> 127.0.0.1:59680 [AP]
  GET / HTTP/1.1..User-Agent: Jakarta Commons-HttpClient/3.1..Host: localhost:59680....
##
T 127.0.0.1:59680 -> 127.0.0.1:60372 [AP]
  HTTP/1.1 302 Found..Set-Cookie: JSESSIONID=vn8zzf9ep3x4mtw66ydm0n6a;Path=/..Expires: Thu, 01 Jan 1970 00:00:00 GMT..Location: http://localhost:60322/authorize?client_id=basic-client&state=the-state&scope=user%2Crepo..Content-Length
  : 0..Server: Jetty(8.1.8.v20121106)....
##
T 127.0.0.1:60372 -> 127.0.0.1:59680 [AP]
  GET /auth/callback?code=timey-wimey&state=the-state HTTP/1.1..User-Agent: Jakarta Commons-HttpClient/3.1..Host: localhost:59680..Cookie: $Version=0; JSESSIONID=vn8zzf9ep3x4mtw66ydm0n6a; $Path=/....
##
T 127.0.0.1:59680 -> 127.0.0.1:60372 [AP]
  HTTP/1.1 302 Found..Cache-Control: no-cache..Location: http://localhost:59680/..Content-Length: 0..Server: Jetty(8.1.8.v20121106)....
##
T 127.0.0.1:60372 -> 127.0.0.1:59680 [AP]
  GET / HTTP/1.1..User-Agent: Jakarta Commons-HttpClient/3.1..Host: localhost:59680..Cookie: $Version=0; JSESSIONID=vn8zzf9ep3x4mtw66ydm0n6a; $Path=/....
##
T 127.0.0.1:59680 -> 127.0.0.1:60372 [AP]
  HTTP/1.1 200 OK..Vary: Accept-Encoding..Accept-Ranges: bytes..Content-Type: text/html..Content-Length: 2439..Last-Modified: Tue, 23 Jul 2013 10:48:15 GMT..Server: Jetty(8.1.8.v20121106)....<!DOCTYPE html>.<html>.<head>.  <title>Tes
  t Lab</title>.  <meta name="viewport" content="width=device-width initial-scale=1.0 maximum-scale=1.0 user-scalable=0"/>.  <link rel="stylesheet" type="text/css" href="css/bootstrap.css">.  <link rel="stylesheet" type="text/css" hr
  ef="css/bootstrap-responsive.css">.  <link rel="stylesheet" type="text/css" href="css/test-lab.css">.  <link rel="icon" type="image/png" href="images/testlab-16.png">.  <script src="js/require.js"></script>.  <script src="js/d3.v3.
  js" charset="UTF-8"></script>.  <script src="js/jquery-1.8.3.min.js"></script>.  <script src="js/bootstrap.js"></script>.  <script src="js/test-lab.js"></script>.  <script type="text/javascript" src="js/google-analytics.js"></scrip
  t>.</head>.<body>..<a href="navbar.html" class="inline-replacement"></a>..<div class="container">..  <h1 class="title">Neo Technology Test Lab</h1>..  <div class="dev-mode">Viewing dev-mode</div>..  <h2>Benchmark Series Results</h2
  >..  <table id="benchmarkseries_list" class="table">.    <thead></thead>.    <tbody></tbody>.  </table>..  <a href="new-benchmark-series.html" class="btn load-modal"><i class="icon-plus"></i> Create Benchmark Series...</a>..  <h2>T
  ests</h2>..  <table id="test_list" class="table">.    <thead></thead>.    <tbody></tbody>.  </table>..  <a href="run-test.html" class="btn load-modal"><i class="icon-plus"></i> Run Test...</a>.  <a href="run-benchmark.html" class="
  btn load-modal"><i class="icon-plus"></i> Run Benchmark...</a>..  <h2>Clusters</h2>..  <table id="cluster_list" class="table"></table>..  <a href="new-database-cluster.html" class="btn load-modal"><i class="icon-plus"></i> New Data
  base Cluster...</a>.  <a href="new-load-generation-cluster.html" class="btn load-modal"><i class="icon-plus"></i> New Load Generation Cluster...</a>..  <h2>Datasets</h2>..  <table id="dataset_list" class="table">.    <thead></thead
  >.    <tbody></tbody>.  </table>..  <a href="new-dataset.html" class="btn load-modal"><i class="icon-plus"></i> Create New Dataset...</a>..  <a href="confirm.html" class="inline-replacement"></a>..</div>..<script type="text/javascr
  ipt">.  (function ().  {.    window.setInterval( function ().    {.      d3.json( "/public/authenticated", function ( status ).      {.        if ( !status.authenticated ).        {.          window.location.reload();.        }.
     } );.    }, 5000 );.    kirkaldy.initializeUI();.  })();.</script>..</body>.</html>.
~~~
