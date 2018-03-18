+++
draft = false
date="2016-07-11 05:21:43"
title="Neo4j 3.0 Drivers - Failed to save the server ID and the certificate received from the server"
tag=['neo4j']
category=['neo4j']
+++

<p>
I've been using the <a href="https://neo4j.com/developer/java/">Neo4j Java Driver</a> on various local databases over the past week and ran into the following certificate problem a few times:
</p>



~~~text

org.neo4j.driver.v1.exceptions.ClientException: Unable to process request: General SSLEngine problem
	at org.neo4j.driver.internal.connector.socket.SocketClient.start(SocketClient.java:88)
	at org.neo4j.driver.internal.connector.socket.SocketConnection.<init>(SocketConnection.java:63)
	at org.neo4j.driver.internal.connector.socket.SocketConnector.connect(SocketConnector.java:52)
	at org.neo4j.driver.internal.pool.InternalConnectionPool.acquire(InternalConnectionPool.java:113)
	at org.neo4j.driver.internal.InternalDriver.session(InternalDriver.java:53)
Caused by: javax.net.ssl.SSLHandshakeException: General SSLEngine problem
	at sun.security.ssl.Handshaker.checkThrown(Handshaker.java:1431)
	at sun.security.ssl.SSLEngineImpl.checkTaskThrown(SSLEngineImpl.java:535)
	at sun.security.ssl.SSLEngineImpl.writeAppRecord(SSLEngineImpl.java:1214)
	at sun.security.ssl.SSLEngineImpl.wrap(SSLEngineImpl.java:1186)
	at javax.net.ssl.SSLEngine.wrap(SSLEngine.java:469)
	at org.neo4j.driver.internal.connector.socket.TLSSocketChannel.wrap(TLSSocketChannel.java:270)
	at org.neo4j.driver.internal.connector.socket.TLSSocketChannel.runHandshake(TLSSocketChannel.java:131)
	at org.neo4j.driver.internal.connector.socket.TLSSocketChannel.<init>(TLSSocketChannel.java:95)
	at org.neo4j.driver.internal.connector.socket.TLSSocketChannel.<init>(TLSSocketChannel.java:77)
	at org.neo4j.driver.internal.connector.socket.TLSSocketChannel.<init>(TLSSocketChannel.java:70)
	at org.neo4j.driver.internal.connector.socket.SocketClient$ChannelFactory.create(SocketClient.java:251)
	at org.neo4j.driver.internal.connector.socket.SocketClient.start(SocketClient.java:75)
	... 14 more
Caused by: javax.net.ssl.SSLHandshakeException: General SSLEngine problem
	at sun.security.ssl.Alerts.getSSLException(Alerts.java:192)
	at sun.security.ssl.SSLEngineImpl.fatal(SSLEngineImpl.java:1728)
	at sun.security.ssl.Handshaker.fatalSE(Handshaker.java:304)
	at sun.security.ssl.Handshaker.fatalSE(Handshaker.java:296)
	at sun.security.ssl.ClientHandshaker.serverCertificate(ClientHandshaker.java:1497)
	at sun.security.ssl.ClientHandshaker.processMessage(ClientHandshaker.java:212)
	at sun.security.ssl.Handshaker.processLoop(Handshaker.java:979)
	at sun.security.ssl.Handshaker$1.run(Handshaker.java:919)
	at sun.security.ssl.Handshaker$1.run(Handshaker.java:916)
	at java.security.AccessController.doPrivileged(Native Method)
	at sun.security.ssl.Handshaker$DelegatedTask.run(Handshaker.java:1369)
	at org.neo4j.driver.internal.connector.socket.TLSSocketChannel.runDelegatedTasks(TLSSocketChannel.java:142)
	at org.neo4j.driver.internal.connector.socket.TLSSocketChannel.unwrap(TLSSocketChannel.java:203)
	at org.neo4j.driver.internal.connector.socket.TLSSocketChannel.runHandshake(TLSSocketChannel.java:127)
	... 19 more
Caused by: java.security.cert.CertificateException: Unable to connect to neo4j at `localhost:10003`, because the certificate the server uses has changed. This is a security feature to protect against man-in-the-middle attacks.
If you trust the certificate the server uses now, simply remove the line that starts with `localhost:10003` in the file `/Users/markneedham/.neo4j/known_hosts`.
The old certificate saved in file is:
-----BEGIN CERTIFICATE-----
7770ee598be69c8537b0e576e62442c84400008ca0d3e3565b379b7cce9a51de
0fd4396251df2e8da50eb1628d44dcbca3fae5c8fb9c0adc29396839c25eb0c8

-----END CERTIFICATE-----
The New certificate received is:
-----BEGIN CERTIFICATE-----
01a422739a39625ee95a0547fa99c7e43fbb33c70ff720e5ae4a8408421aa63b
2fe4f5d6094c5fd770ed1ad214dbdc428a6811d0955ed80d48cc67d84067df2c

-----END CERTIFICATE-----

	at org.neo4j.driver.internal.connector.socket.TrustOnFirstUseTrustManager.checkServerTrusted(TrustOnFirstUseTrustManager.java:153)
	at sun.security.ssl.AbstractTrustManagerWrapper.checkServerTrusted(SSLContextImpl.java:936)
	at sun.security.ssl.ClientHandshaker.serverCertificate(ClientHandshaker.java:1484)
	... 28 more
~~~

<p>
I got a bit lazy and just nuked the file it mentions in the error message - <cite>/Users/markneedham/.neo4j/known_hosts</cite> - which led to this error the next time I call the driver in my application:
</p>



~~~text

Failed to save the server ID and the certificate received from the server to file /Users/markneedham/.neo4j/known_hosts.
Server ID: localhost:10003
Received cert:
-----BEGIN CERTIFICATE-----
933c7ec5d6a1b876bd186dc6d05b04478ae771262f07d26a4d7d2e6b7f71054c
3e6b7c172474493b7fe93170d940b9cc3544661c7966632361649f2fda7c66be

-----END CERTIFICATE-----
~~~

<p>
I recreated the file with no content and tried again and it worked fine. Alternatively we can choose to turn off encryption when working with local databases and avoid the issue:
</p>



~~~java

Config config = Config.build().withEncryptionLevel( Config.EncryptionLevel.NONE ).toConfig();

try ( Driver driver = GraphDatabase.driver( "bolt://localhost:7687", config );
      Session session = driver.session() )
{
   // use the driver
}
~~~
