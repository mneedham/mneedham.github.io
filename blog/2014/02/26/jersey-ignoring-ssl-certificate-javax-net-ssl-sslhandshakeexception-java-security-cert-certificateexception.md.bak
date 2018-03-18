+++
draft = false
date="2014-02-26 00:12:01"
title="Jersey: Ignoring SSL certificate - javax.net.ssl.SSLHandshakeException: java.security.cert.CertificateException"
tag=['java']
category=['Java']
+++

<p>Last week <a href="https://twitter.com/apcj">Alistair</a> and I were working on an internal application and we needed to make a HTTPS request directly to an AWS machine using a certificate signed to a different host.</p>


<p>We use <a href="http://mvnrepository.com/artifact/com.sun.jersey/jersey-client">jersey-client</a> so our code looked something like this:</p>



~~~java

Client client = Client.create();

client.resource("https://some-aws-host.compute-1.amazonaws.com").post();
// and so on
~~~

<p>When we ran this we predictably ran into trouble:</p>



~~~text

com.sun.jersey.api.client.ClientHandlerException: javax.net.ssl.SSLHandshakeException: java.security.cert.CertificateException: No subject alternative DNS name matching some-aws-host.compute-1.amazonaws.com found.
	at com.sun.jersey.client.urlconnection.URLConnectionClientHandler.handle(URLConnectionClientHandler.java:149)
	at com.sun.jersey.api.client.Client.handle(Client.java:648)
	at com.sun.jersey.api.client.WebResource.handle(WebResource.java:670)
	at com.sun.jersey.api.client.WebResource.post(WebResource.java:241)
	at com.neotechnology.testlab.manager.bootstrap.ManagerAdmin.takeBackup(ManagerAdmin.java:33)
	at com.neotechnology.testlab.manager.bootstrap.ManagerAdminTest.foo(ManagerAdminTest.java:11)
	at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
	at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:57)
	at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
	at org.junit.runners.model.FrameworkMethod$1.runReflectiveCall(FrameworkMethod.java:45)
	at org.junit.internal.runners.model.ReflectiveCallable.run(ReflectiveCallable.java:15)
	at org.junit.runners.model.FrameworkMethod.invokeExplosively(FrameworkMethod.java:42)
	at org.junit.internal.runners.statements.InvokeMethod.evaluate(InvokeMethod.java:20)
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
	at com.intellij.junit4.JUnit4IdeaTestRunner.startRunnerWithArgs(JUnit4IdeaTestRunner.java:74)
	at com.intellij.rt.execution.junit.JUnitStarter.prepareStreamsAndStart(JUnitStarter.java:202)
	at com.intellij.rt.execution.junit.JUnitStarter.main(JUnitStarter.java:65)
	at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
	at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:57)
	at com.intellij.rt.execution.application.AppMain.main(AppMain.java:120)
Caused by: javax.net.ssl.SSLHandshakeException: java.security.cert.CertificateException: No subject alternative DNS name matching some-aws-host.compute-1.amazonaws.com found.
	at sun.security.ssl.Alerts.getSSLException(Alerts.java:192)
	at sun.security.ssl.SSLSocketImpl.fatal(SSLSocketImpl.java:1884)
	at sun.security.ssl.Handshaker.fatalSE(Handshaker.java:276)
	at sun.security.ssl.Handshaker.fatalSE(Handshaker.java:270)
	at sun.security.ssl.ClientHandshaker.serverCertificate(ClientHandshaker.java:1341)
	at sun.security.ssl.ClientHandshaker.processMessage(ClientHandshaker.java:153)
	at sun.security.ssl.Handshaker.processLoop(Handshaker.java:868)
	at sun.security.ssl.Handshaker.process_record(Handshaker.java:804)
	at sun.security.ssl.SSLSocketImpl.readRecord(SSLSocketImpl.java:1016)
	at sun.security.ssl.SSLSocketImpl.performInitialHandshake(SSLSocketImpl.java:1312)
	at sun.security.ssl.SSLSocketImpl.startHandshake(SSLSocketImpl.java:1339)
	at sun.security.ssl.SSLSocketImpl.startHandshake(SSLSocketImpl.java:1323)
	at sun.net.www.protocol.https.HttpsClient.afterConnect(HttpsClient.java:563)
	at sun.net.www.protocol.https.AbstractDelegateHttpsURLConnection.connect(AbstractDelegateHttpsURLConnection.java:185)
	at sun.net.www.protocol.http.HttpURLConnection.getInputStream(HttpURLConnection.java:1300)
	at java.net.HttpURLConnection.getResponseCode(HttpURLConnection.java:468)
	at sun.net.www.protocol.https.HttpsURLConnectionImpl.getResponseCode(HttpsURLConnectionImpl.java:338)
	at com.sun.jersey.client.urlconnection.URLConnectionClientHandler._invoke(URLConnectionClientHandler.java:240)
	at com.sun.jersey.client.urlconnection.URLConnectionClientHandler.handle(URLConnectionClientHandler.java:147)
	... 31 more
Caused by: java.security.cert.CertificateException: No subject alternative DNS name matching some-aws-host.compute-1.amazonaws.com found.
	at sun.security.util.HostnameChecker.matchDNS(HostnameChecker.java:191)
	at sun.security.util.HostnameChecker.match(HostnameChecker.java:93)
	at sun.security.ssl.X509TrustManagerImpl.checkIdentity(X509TrustManagerImpl.java:347)
	at sun.security.ssl.X509TrustManagerImpl.checkTrusted(X509TrustManagerImpl.java:203)
	at sun.security.ssl.X509TrustManagerImpl.checkServerTrusted(X509TrustManagerImpl.java:126)
	at sun.security.ssl.ClientHandshaker.serverCertificate(ClientHandshaker.java:1323)
	... 45 more
~~~

<p>We figured that we needed to get our client to ignore the certificate and came across <a href="http://stackoverflow.com/questions/6047996/ignore-self-signed-ssl-cert-using-jersey-client">this Stack Overflow thread</a> which had some suggestions on how to do this.</p>


<p>None of the suggestions worked on their own but we ended up with a combination of a couple of the suggestions which did the trick:</p>



~~~java

public Client hostIgnoringClient() {
    try
    {
        SSLContext sslcontext = SSLContext.getInstance( "TLS" );
        sslcontext.init( null, null, null );
        DefaultClientConfig config = new DefaultClientConfig();
        Map<String, Object> properties = config.getProperties();
        HTTPSProperties httpsProperties = new HTTPSProperties(
                new HostnameVerifier()
                {
                    @Override
                    public boolean verify( String s, SSLSession sslSession )
                    {
                        return true;
                    }
                }, sslcontext
        );
        properties.put( HTTPSProperties.PROPERTY_HTTPS_PROPERTIES, httpsProperties );
        config.getClasses().add( JacksonJsonProvider.class );
        return Client.create( config );
    }
    catch ( KeyManagementException | NoSuchAlgorithmException e )
    {
        throw new RuntimeException( e );
    }
}
~~~

<p>You're welcome Future Mark.</p>

