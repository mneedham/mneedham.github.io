+++
draft = false
date="2015-08-11 06:59:50"
title="Java: Jersey - java.lang.NoSuchMethodError: com.sun.jersey.core.reflection.ReflectionHelper. getContextClassLoaderPA()Ljava/security/PrivilegedAction;"
tag=['software-development', 'java']
category=['Java']
+++

<p>
I've been trying to put some tests around an <a href="https://github.com/mneedham/dummy-unmanaged-extension">Neo4j unmanaged extension</a> I've been working on and ran into the following stack trace when launching the server using the <a href="http://neo4j.com/docs/stable/server-unmanaged-extensions-testing.html">Neo4j test harness</a>:
</p>



~~~java

public class ExampleResourceTest {
    @Rule
    public Neo4jRule neo4j = new Neo4jRule()
            .withFixture("CREATE (:Person {name: 'Mark'})")
            .withFixture("CREATE (:Person {name: 'Nicole'})")
            .withExtension( "/unmanaged", ExampleResource.class );

    @Test
    public void shouldReturnAllTheNodes() {
        // Given
        URI serverURI = neo4j.httpURI();
        // When
        HTTP.Response response = HTTP.GET(serverURI.resolve("/unmanaged/example/people").toString());

        // Then
        assertEquals(200, response.status());
        List content = response.content();

        assertEquals(2, content.size());
    }
}
~~~


~~~text

07:51:32.985 [main] WARN  o.e.j.u.component.AbstractLifeCycle - FAILED o.e.j.s.ServletContextHandler@29eda4f8{/unmanaged,null,STARTING}: java.lang.NoSuchMethodError: com.sun.jersey.core.reflection.ReflectionHelper.getContextClassLoaderPA()Ljava/security/PrivilegedAction;
java.lang.NoSuchMethodError: com.sun.jersey.core.reflection.ReflectionHelper.getContextClassLoaderPA()Ljava/security/PrivilegedAction;
	at com.sun.jersey.spi.scanning.AnnotationScannerListener.<init>(AnnotationScannerListener.java:94) ~[jersey-server-1.19.jar:1.19]
	at com.sun.jersey.spi.scanning.PathProviderScannerListener.<init>(PathProviderScannerListener.java:59) ~[jersey-server-1.19.jar:1.19]
	at com.sun.jersey.api.core.ScanningResourceConfig.init(ScanningResourceConfig.java:79) ~[jersey-server-1.19.jar:1.19]
	at com.sun.jersey.api.core.PackagesResourceConfig.init(PackagesResourceConfig.java:104) ~[jersey-server-1.19.jar:1.19]
	at com.sun.jersey.api.core.PackagesResourceConfig.<init>(PackagesResourceConfig.java:78) ~[jersey-server-1.19.jar:1.19]
	at com.sun.jersey.api.core.PackagesResourceConfig.<init>(PackagesResourceConfig.java:89) ~[jersey-server-1.19.jar:1.19]
	at com.sun.jersey.spi.container.servlet.WebComponent.createResourceConfig(WebComponent.java:696) ~[jersey-servlet-1.17.1.jar:1.17.1]
	at com.sun.jersey.spi.container.servlet.WebComponent.createResourceConfig(WebComponent.java:674) ~[jersey-servlet-1.17.1.jar:1.17.1]
	at com.sun.jersey.spi.container.servlet.WebComponent.init(WebComponent.java:203) ~[jersey-servlet-1.17.1.jar:1.17.1]
	at com.sun.jersey.spi.container.servlet.ServletContainer.init(ServletContainer.java:374) ~[jersey-servlet-1.17.1.jar:1.17.1]
	at com.sun.jersey.spi.container.servlet.ServletContainer.init(ServletContainer.java:557) ~[jersey-servlet-1.17.1.jar:1.17.1]
	at javax.servlet.GenericServlet.init(GenericServlet.java:244) ~[javax.servlet-api-3.1.0.jar:3.1.0]
	at org.eclipse.jetty.servlet.ServletHolder.initServlet(ServletHolder.java:612) ~[jetty-servlet-9.2.4.v20141103.jar:9.2.4.v20141103]
	at org.eclipse.jetty.servlet.ServletHolder.initialize(ServletHolder.java:395) ~[jetty-servlet-9.2.4.v20141103.jar:9.2.4.v20141103]
	at org.eclipse.jetty.servlet.ServletHandler.initialize(ServletHandler.java:871) ~[jetty-servlet-9.2.4.v20141103.jar:9.2.4.v20141103]
	at org.eclipse.jetty.servlet.ServletContextHandler.startContext(ServletContextHandler.java:298) ~[jetty-servlet-9.2.4.v20141103.jar:9.2.4.v20141103]
	at org.eclipse.jetty.server.handler.ContextHandler.doStart(ContextHandler.java:741) ~[jetty-server-9.2.4.v20141103.jar:9.2.4.v20141103]
	at org.eclipse.jetty.util.component.AbstractLifeCycle.start(AbstractLifeCycle.java:68) [jetty-util-9.2.4.v20141103.jar:9.2.4.v20141103]
	at org.eclipse.jetty.util.component.ContainerLifeCycle.start(ContainerLifeCycle.java:132) [jetty-util-9.2.4.v20141103.jar:9.2.4.v20141103]
	at org.eclipse.jetty.util.component.ContainerLifeCycle.doStart(ContainerLifeCycle.java:114) [jetty-util-9.2.4.v20141103.jar:9.2.4.v20141103]
	at org.eclipse.jetty.server.handler.AbstractHandler.doStart(AbstractHandler.java:61) [jetty-server-9.2.4.v20141103.jar:9.2.4.v20141103]
	at org.eclipse.jetty.util.component.AbstractLifeCycle.start(AbstractLifeCycle.java:68) [jetty-util-9.2.4.v20141103.jar:9.2.4.v20141103]
	at org.eclipse.jetty.util.component.ContainerLifeCycle.start(ContainerLifeCycle.java:132) [jetty-util-9.2.4.v20141103.jar:9.2.4.v20141103]
	at org.eclipse.jetty.server.Server.start(Server.java:387) [jetty-server-9.2.4.v20141103.jar:9.2.4.v20141103]
	at org.eclipse.jetty.util.component.ContainerLifeCycle.doStart(ContainerLifeCycle.java:114) [jetty-util-9.2.4.v20141103.jar:9.2.4.v20141103]
	at org.eclipse.jetty.server.handler.AbstractHandler.doStart(AbstractHandler.java:61) [jetty-server-9.2.4.v20141103.jar:9.2.4.v20141103]
	at org.eclipse.jetty.server.Server.doStart(Server.java:354) [jetty-server-9.2.4.v20141103.jar:9.2.4.v20141103]
	at org.eclipse.jetty.util.component.AbstractLifeCycle.start(AbstractLifeCycle.java:68) [jetty-util-9.2.4.v20141103.jar:9.2.4.v20141103]
	at org.neo4j.server.web.Jetty9WebServer.startJetty(Jetty9WebServer.java:381) [neo4j-server-2.2.3.jar:2.2.3]
	at org.neo4j.server.web.Jetty9WebServer.start(Jetty9WebServer.java:184) [neo4j-server-2.2.3.jar:2.2.3]
	at org.neo4j.server.AbstractNeoServer.startWebServer(AbstractNeoServer.java:474) [neo4j-server-2.2.3.jar:2.2.3]
	at org.neo4j.server.AbstractNeoServer.start(AbstractNeoServer.java:230) [neo4j-server-2.2.3.jar:2.2.3]
	at org.neo4j.harness.internal.InProcessServerControls.start(InProcessServerControls.java:59) [neo4j-harness-2.2.3.jar:2.2.3]
	at org.neo4j.harness.internal.InProcessServerBuilder.newServer(InProcessServerBuilder.java:72) [neo4j-harness-2.2.3.jar:2.2.3]
	at org.neo4j.harness.junit.Neo4jRule$1.evaluate(Neo4jRule.java:64) [neo4j-harness-2.2.3.jar:2.2.3]
	at org.junit.rules.RunRules.evaluate(RunRules.java:20) [junit-4.11.jar:na]
	at org.junit.runners.ParentRunner.runLeaf(ParentRunner.java:271) [junit-4.11.jar:na]
	at org.junit.runners.BlockJUnit4ClassRunner.runChild(BlockJUnit4ClassRunner.java:70) [junit-4.11.jar:na]
	at org.junit.runners.BlockJUnit4ClassRunner.runChild(BlockJUnit4ClassRunner.java:50) [junit-4.11.jar:na]
	at org.junit.runners.ParentRunner$3.run(ParentRunner.java:238) [junit-4.11.jar:na]
	at org.junit.runners.ParentRunner$1.schedule(ParentRunner.java:63) [junit-4.11.jar:na]
	at org.junit.runners.ParentRunner.runChildren(ParentRunner.java:236) [junit-4.11.jar:na]
	at org.junit.runners.ParentRunner.access$000(ParentRunner.java:53) [junit-4.11.jar:na]
	at org.junit.runners.ParentRunner$2.evaluate(ParentRunner.java:229) [junit-4.11.jar:na]
	at org.junit.runners.ParentRunner.run(ParentRunner.java:309) [junit-4.11.jar:na]
	at org.junit.runner.JUnitCore.run(JUnitCore.java:160) [junit-4.11.jar:na]
	at com.intellij.junit4.JUnit4IdeaTestRunner.startRunnerWithArgs(JUnit4IdeaTestRunner.java:78) [junit-rt.jar:na]
	at com.intellij.rt.execution.junit.JUnitStarter.prepareStreamsAndStart(JUnitStarter.java:212) [junit-rt.jar:na]
	at com.intellij.rt.execution.junit.JUnitStarter.main(JUnitStarter.java:68) [junit-rt.jar:na]
	at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method) ~[na:1.8.0_51]
	at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62) ~[na:1.8.0_51]
	at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43) ~[na:1.8.0_51]
	at java.lang.reflect.Method.invoke(Method.java:497) ~[na:1.8.0_51]
	at com.intellij.rt.execution.application.AppMain.main(AppMain.java:140) [idea_rt.jar:na]
07:51:32.991 [main] WARN  o.e.j.u.component.AbstractLifeCycle - FAILED org.eclipse.jetty.server.handler.HandlerList@2b22a1cc[o.e.j.s.h.MovedContextHandler@5e671e20{/,null,AVAILABLE}, o.e.j.s.ServletContextHandler@29eda4f8{/unmanaged,null,STARTING}, o.e.j.s.ServletContextHandler@62573c86{/db/manage,null,null}, o.e.j.s.ServletContextHandler@2418ba04{/db/data,null,null}, o.e.j.w.WebAppContext@14229fa7{/browser,jar:file:/Users/markneedham/.m2/repository/org/neo4j/app/neo4j-browser/2.2.3/neo4j-browser-2.2.3.jar!/browser,null}, o.e.j.s.ServletContextHandler@2ab0702e{/,null,null}]: java.lang.NoSuchMethodError: com.sun.jersey.core.reflection.ReflectionHelper.getContextClassLoaderPA()Ljava/security/PrivilegedAction;
java.lang.NoSuchMethodError: com.sun.jersey.core.reflection.ReflectionHelper.getContextClassLoaderPA()Ljava/security/PrivilegedAction;
	at com.sun.jersey.spi.scanning.AnnotationScannerListener.<init>(AnnotationScannerListener.java:94) ~[jersey-server-1.19.jar:1.19]
	at com.sun.jersey.spi.scanning.PathProviderScannerListener.<init>(PathProviderScannerListener.java:59) ~[jersey-server-1.19.jar:1.19]
	at com.sun.jersey.api.core.ScanningResourceConfig.init(ScanningResourceConfig.java:79) ~[jersey-server-1.19.jar:1.19]
	at com.sun.jersey.api.core.PackagesResourceConfig.init(PackagesResourceConfig.java:104) ~[jersey-server-1.19.jar:1.19]
	at com.sun.jersey.api.core.PackagesResourceConfig.<init>(PackagesResourceConfig.java:78) ~[jersey-server-1.19.jar:1.19]
	at com.sun.jersey.api.core.PackagesResourceConfig.<init>(PackagesResourceConfig.java:89) ~[jersey-server-1.19.jar:1.19]
	at com.sun.jersey.spi.container.servlet.WebComponent.createResourceConfig(WebComponent.java:696) ~[jersey-servlet-1.17.1.jar:1.17.1]
	at com.sun.jersey.spi.container.servlet.WebComponent.createResourceConfig(WebComponent.java:674) ~[jersey-servlet-1.17.1.jar:1.17.1]
	at com.sun.jersey.spi.container.servlet.WebComponent.init(WebComponent.java:203) ~[jersey-servlet-1.17.1.jar:1.17.1]
	at com.sun.jersey.spi.container.servlet.ServletContainer.init(ServletContainer.java:374) ~[jersey-servlet-1.17.1.jar:1.17.1]
	at com.sun.jersey.spi.container.servlet.ServletContainer.init(ServletContainer.java:557) ~[jersey-servlet-1.17.1.jar:1.17.1]
	at javax.servlet.GenericServlet.init(GenericServlet.java:244) ~[javax.servlet-api-3.1.0.jar:3.1.0]
	at org.eclipse.jetty.servlet.ServletHolder.initServlet(ServletHolder.java:612) ~[jetty-servlet-9.2.4.v20141103.jar:9.2.4.v20141103]
	at org.eclipse.jetty.servlet.ServletHolder.initialize(ServletHolder.java:395) ~[jetty-servlet-9.2.4.v20141103.jar:9.2.4.v20141103]
	at org.eclipse.jetty.servlet.ServletHandler.initialize(ServletHandler.java:871) ~[jetty-servlet-9.2.4.v20141103.jar:9.2.4.v20141103]
	at org.eclipse.jetty.servlet.ServletContextHandler.startContext(ServletContextHandler.java:298) ~[jetty-servlet-9.2.4.v20141103.jar:9.2.4.v20141103]
	at org.eclipse.jetty.server.handler.ContextHandler.doStart(ContextHandler.java:741) ~[jetty-server-9.2.4.v20141103.jar:9.2.4.v20141103]
	at org.eclipse.jetty.util.component.AbstractLifeCycle.start(AbstractLifeCycle.java:68) [jetty-util-9.2.4.v20141103.jar:9.2.4.v20141103]
	at org.eclipse.jetty.util.component.ContainerLifeCycle.start(ContainerLifeCycle.java:132) [jetty-util-9.2.4.v20141103.jar:9.2.4.v20141103]
	at org.eclipse.jetty.util.component.ContainerLifeCycle.doStart(ContainerLifeCycle.java:114) [jetty-util-9.2.4.v20141103.jar:9.2.4.v20141103]
	at org.eclipse.jetty.server.handler.AbstractHandler.doStart(AbstractHandler.java:61) [jetty-server-9.2.4.v20141103.jar:9.2.4.v20141103]
	at org.eclipse.jetty.util.component.AbstractLifeCycle.start(AbstractLifeCycle.java:68) [jetty-util-9.2.4.v20141103.jar:9.2.4.v20141103]
	at org.eclipse.jetty.util.component.ContainerLifeCycle.start(ContainerLifeCycle.java:132) [jetty-util-9.2.4.v20141103.jar:9.2.4.v20141103]
	at org.eclipse.jetty.server.Server.start(Server.java:387) [jetty-server-9.2.4.v20141103.jar:9.2.4.v20141103]
	at org.eclipse.jetty.util.component.ContainerLifeCycle.doStart(ContainerLifeCycle.java:114) [jetty-util-9.2.4.v20141103.jar:9.2.4.v20141103]
	at org.eclipse.jetty.server.handler.AbstractHandler.doStart(AbstractHandler.java:61) [jetty-server-9.2.4.v20141103.jar:9.2.4.v20141103]
	at org.eclipse.jetty.server.Server.doStart(Server.java:354) [jetty-server-9.2.4.v20141103.jar:9.2.4.v20141103]
	at org.eclipse.jetty.util.component.AbstractLifeCycle.start(AbstractLifeCycle.java:68) [jetty-util-9.2.4.v20141103.jar:9.2.4.v20141103]
	at org.neo4j.server.web.Jetty9WebServer.startJetty(Jetty9WebServer.java:381) [neo4j-server-2.2.3.jar:2.2.3]
	at org.neo4j.server.web.Jetty9WebServer.start(Jetty9WebServer.java:184) [neo4j-server-2.2.3.jar:2.2.3]
	at org.neo4j.server.AbstractNeoServer.startWebServer(AbstractNeoServer.java:474) [neo4j-server-2.2.3.jar:2.2.3]
	at org.neo4j.server.AbstractNeoServer.start(AbstractNeoServer.java:230) [neo4j-server-2.2.3.jar:2.2.3]
	at org.neo4j.harness.internal.InProcessServerControls.start(InProcessServerControls.java:59) [neo4j-harness-2.2.3.jar:2.2.3]
	at org.neo4j.harness.internal.InProcessServerBuilder.newServer(InProcessServerBuilder.java:72) [neo4j-harness-2.2.3.jar:2.2.3]
	at org.neo4j.harness.junit.Neo4jRule$1.evaluate(Neo4jRule.java:64) [neo4j-harness-2.2.3.jar:2.2.3]
	at org.junit.rules.RunRules.evaluate(RunRules.java:20) [junit-4.11.jar:na]
	at org.junit.runners.ParentRunner.runLeaf(ParentRunner.java:271) [junit-4.11.jar:na]
	at org.junit.runners.BlockJUnit4ClassRunner.runChild(BlockJUnit4ClassRunner.java:70) [junit-4.11.jar:na]
	at org.junit.runners.BlockJUnit4ClassRunner.runChild(BlockJUnit4ClassRunner.java:50) [junit-4.11.jar:na]
	at org.junit.runners.ParentRunner$3.run(ParentRunner.java:238) [junit-4.11.jar:na]
	at org.junit.runners.ParentRunner$1.schedule(ParentRunner.java:63) [junit-4.11.jar:na]
	at org.junit.runners.ParentRunner.runChildren(ParentRunner.java:236) [junit-4.11.jar:na]
	at org.junit.runners.ParentRunner.access$000(ParentRunner.java:53) [junit-4.11.jar:na]
	at org.junit.runners.ParentRunner$2.evaluate(ParentRunner.java:229) [junit-4.11.jar:na]
	at org.junit.runners.ParentRunner.run(ParentRunner.java:309) [junit-4.11.jar:na]
	at org.junit.runner.JUnitCore.run(JUnitCore.java:160) [junit-4.11.jar:na]
	at com.intellij.junit4.JUnit4IdeaTestRunner.startRunnerWithArgs(JUnit4IdeaTestRunner.java:78) [junit-rt.jar:na]
	at com.intellij.rt.execution.junit.JUnitStarter.prepareStreamsAndStart(JUnitStarter.java:212) [junit-rt.jar:na]
	at com.intellij.rt.execution.junit.JUnitStarter.main(JUnitStarter.java:68) [junit-rt.jar:na]
	at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method) ~[na:1.8.0_51]
	at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62) ~[na:1.8.0_51]
	at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43) ~[na:1.8.0_51]
	at java.lang.reflect.Method.invoke(Method.java:497) ~[na:1.8.0_51]
	at com.intellij.rt.execution.application.AppMain.main(AppMain.java:140) [idea_rt.jar:na]
07:51:33.013 [main] INFO  o.e.jetty.server.ServerConnector - Started ServerConnector@19962194{HTTP/1.1}{localhost:7475}
07:51:33.014 [main] WARN  o.e.j.u.component.AbstractLifeCycle - FAILED org.eclipse.jetty.server.Server@481e91b6: java.lang.NoSuchMethodError: com.sun.jersey.core.reflection.ReflectionHelper.getContextClassLoaderPA()Ljava/security/PrivilegedAction;
java.lang.NoSuchMethodError: com.sun.jersey.core.reflection.ReflectionHelper.getContextClassLoaderPA()Ljava/security/PrivilegedAction;
	at com.sun.jersey.spi.scanning.AnnotationScannerListener.<init>(AnnotationScannerListener.java:94) ~[jersey-server-1.19.jar:1.19]
	at com.sun.jersey.spi.scanning.PathProviderScannerListener.<init>(PathProviderScannerListener.java:59) ~[jersey-server-1.19.jar:1.19]
	at com.sun.jersey.api.core.ScanningResourceConfig.init(ScanningResourceConfig.java:79) ~[jersey-server-1.19.jar:1.19]
	at com.sun.jersey.api.core.PackagesResourceConfig.init(PackagesResourceConfig.java:104) ~[jersey-server-1.19.jar:1.19]
	at com.sun.jersey.api.core.PackagesResourceConfig.<init>(PackagesResourceConfig.java:78) ~[jersey-server-1.19.jar:1.19]
	at com.sun.jersey.api.core.PackagesResourceConfig.<init>(PackagesResourceConfig.java:89) ~[jersey-server-1.19.jar:1.19]
	at com.sun.jersey.spi.container.servlet.WebComponent.createResourceConfig(WebComponent.java:696) ~[jersey-servlet-1.17.1.jar:1.17.1]
	at com.sun.jersey.spi.container.servlet.WebComponent.createResourceConfig(WebComponent.java:674) ~[jersey-servlet-1.17.1.jar:1.17.1]
	at com.sun.jersey.spi.container.servlet.WebComponent.init(WebComponent.java:203) ~[jersey-servlet-1.17.1.jar:1.17.1]
	at com.sun.jersey.spi.container.servlet.ServletContainer.init(ServletContainer.java:374) ~[jersey-servlet-1.17.1.jar:1.17.1]
	at com.sun.jersey.spi.container.servlet.ServletContainer.init(ServletContainer.java:557) ~[jersey-servlet-1.17.1.jar:1.17.1]
	at javax.servlet.GenericServlet.init(GenericServlet.java:244) ~[javax.servlet-api-3.1.0.jar:3.1.0]
	at org.eclipse.jetty.servlet.ServletHolder.initServlet(ServletHolder.java:612) ~[jetty-servlet-9.2.4.v20141103.jar:9.2.4.v20141103]
	at org.eclipse.jetty.servlet.ServletHolder.initialize(ServletHolder.java:395) ~[jetty-servlet-9.2.4.v20141103.jar:9.2.4.v20141103]
	at org.eclipse.jetty.servlet.ServletHandler.initialize(ServletHandler.java:871) ~[jetty-servlet-9.2.4.v20141103.jar:9.2.4.v20141103]
	at org.eclipse.jetty.servlet.ServletContextHandler.startContext(ServletContextHandler.java:298) ~[jetty-servlet-9.2.4.v20141103.jar:9.2.4.v20141103]
	at org.eclipse.jetty.server.handler.ContextHandler.doStart(ContextHandler.java:741) ~[jetty-server-9.2.4.v20141103.jar:9.2.4.v20141103]
	at org.eclipse.jetty.util.component.AbstractLifeCycle.start(AbstractLifeCycle.java:68) ~[jetty-util-9.2.4.v20141103.jar:9.2.4.v20141103]
	at org.eclipse.jetty.util.component.ContainerLifeCycle.start(ContainerLifeCycle.java:132) ~[jetty-util-9.2.4.v20141103.jar:9.2.4.v20141103]
	at org.eclipse.jetty.util.component.ContainerLifeCycle.doStart(ContainerLifeCycle.java:114) ~[jetty-util-9.2.4.v20141103.jar:9.2.4.v20141103]
	at org.eclipse.jetty.server.handler.AbstractHandler.doStart(AbstractHandler.java:61) ~[jetty-server-9.2.4.v20141103.jar:9.2.4.v20141103]
	at org.eclipse.jetty.util.component.AbstractLifeCycle.start(AbstractLifeCycle.java:68) ~[jetty-util-9.2.4.v20141103.jar:9.2.4.v20141103]
	at org.eclipse.jetty.util.component.ContainerLifeCycle.start(ContainerLifeCycle.java:132) ~[jetty-util-9.2.4.v20141103.jar:9.2.4.v20141103]
	at org.eclipse.jetty.server.Server.start(Server.java:387) ~[jetty-server-9.2.4.v20141103.jar:9.2.4.v20141103]
	at org.eclipse.jetty.util.component.ContainerLifeCycle.doStart(ContainerLifeCycle.java:114) ~[jetty-util-9.2.4.v20141103.jar:9.2.4.v20141103]
	at org.eclipse.jetty.server.handler.AbstractHandler.doStart(AbstractHandler.java:61) ~[jetty-server-9.2.4.v20141103.jar:9.2.4.v20141103]
	at org.eclipse.jetty.server.Server.doStart(Server.java:354) ~[jetty-server-9.2.4.v20141103.jar:9.2.4.v20141103]
	at org.eclipse.jetty.util.component.AbstractLifeCycle.start(AbstractLifeCycle.java:68) ~[jetty-util-9.2.4.v20141103.jar:9.2.4.v20141103]
	at org.neo4j.server.web.Jetty9WebServer.startJetty(Jetty9WebServer.java:381) [neo4j-server-2.2.3.jar:2.2.3]
	at org.neo4j.server.web.Jetty9WebServer.start(Jetty9WebServer.java:184) [neo4j-server-2.2.3.jar:2.2.3]
	at org.neo4j.server.AbstractNeoServer.startWebServer(AbstractNeoServer.java:474) [neo4j-server-2.2.3.jar:2.2.3]
	at org.neo4j.server.AbstractNeoServer.start(AbstractNeoServer.java:230) [neo4j-server-2.2.3.jar:2.2.3]
	at org.neo4j.harness.internal.InProcessServerControls.start(InProcessServerControls.java:59) [neo4j-harness-2.2.3.jar:2.2.3]
	at org.neo4j.harness.internal.InProcessServerBuilder.newServer(InProcessServerBuilder.java:72) [neo4j-harness-2.2.3.jar:2.2.3]
	at org.neo4j.harness.junit.Neo4jRule$1.evaluate(Neo4jRule.java:64) [neo4j-harness-2.2.3.jar:2.2.3]
	at org.junit.rules.RunRules.evaluate(RunRules.java:20) [junit-4.11.jar:na]
	at org.junit.runners.ParentRunner.runLeaf(ParentRunner.java:271) [junit-4.11.jar:na]
	at org.junit.runners.BlockJUnit4ClassRunner.runChild(BlockJUnit4ClassRunner.java:70) [junit-4.11.jar:na]
	at org.junit.runners.BlockJUnit4ClassRunner.runChild(BlockJUnit4ClassRunner.java:50) [junit-4.11.jar:na]
	at org.junit.runners.ParentRunner$3.run(ParentRunner.java:238) [junit-4.11.jar:na]
	at org.junit.runners.ParentRunner$1.schedule(ParentRunner.java:63) [junit-4.11.jar:na]
	at org.junit.runners.ParentRunner.runChildren(ParentRunner.java:236) [junit-4.11.jar:na]
	at org.junit.runners.ParentRunner.access$000(ParentRunner.java:53) [junit-4.11.jar:na]
	at org.junit.runners.ParentRunner$2.evaluate(ParentRunner.java:229) [junit-4.11.jar:na]
	at org.junit.runners.ParentRunner.run(ParentRunner.java:309) [junit-4.11.jar:na]
	at org.junit.runner.JUnitCore.run(JUnitCore.java:160) [junit-4.11.jar:na]
	at com.intellij.junit4.JUnit4IdeaTestRunner.startRunnerWithArgs(JUnit4IdeaTestRunner.java:78) [junit-rt.jar:na]
	at com.intellij.rt.execution.junit.JUnitStarter.prepareStreamsAndStart(JUnitStarter.java:212) [junit-rt.jar:na]
	at com.intellij.rt.execution.junit.JUnitStarter.main(JUnitStarter.java:68) [junit-rt.jar:na]
	at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method) ~[na:1.8.0_51]
	at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62) ~[na:1.8.0_51]
	at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43) ~[na:1.8.0_51]
	at java.lang.reflect.Method.invoke(Method.java:497) ~[na:1.8.0_51]
	at com.intellij.rt.execution.application.AppMain.main(AppMain.java:140) [idea_rt.jar:na]

org.neo4j.server.ServerStartupException: Starting Neo4j Server failed: com.sun.jersey.core.reflection.ReflectionHelper.getContextClassLoaderPA()Ljava/security/PrivilegedAction;
	at org.neo4j.server.AbstractNeoServer.start(AbstractNeoServer.java:258)
	at org.neo4j.harness.internal.InProcessServerControls.start(InProcessServerControls.java:59)
	at org.neo4j.harness.internal.InProcessServerBuilder.newServer(InProcessServerBuilder.java:72)
	at org.neo4j.harness.junit.Neo4jRule$1.evaluate(Neo4jRule.java:64)
	at org.junit.rules.RunRules.evaluate(RunRules.java:20)
	at org.junit.runners.ParentRunner.runLeaf(ParentRunner.java:271)
	at org.junit.runners.BlockJUnit4ClassRunner.runChild(BlockJUnit4ClassRunner.java:70)
	at org.junit.runners.BlockJUnit4ClassRunner.runChild(BlockJUnit4ClassRunner.java:50)
	at org.junit.runners.ParentRunner$3.run(ParentRunner.java:238)
	at org.junit.runners.ParentRunner$1.schedule(ParentRunner.java:63)
	at org.junit.runners.ParentRunner.runChildren(ParentRunner.java:236)
	at org.junit.runners.ParentRunner.access$000(ParentRunner.java:53)
	at org.junit.runners.ParentRunner$2.evaluate(ParentRunner.java:229)
	at org.junit.runners.ParentRunner.run(ParentRunner.java:309)
	at org.junit.runner.JUnitCore.run(JUnitCore.java:160)
	at com.intellij.junit4.JUnit4IdeaTestRunner.startRunnerWithArgs(JUnit4IdeaTestRunner.java:78)
	at com.intellij.rt.execution.junit.JUnitStarter.prepareStreamsAndStart(JUnitStarter.java:212)
	at com.intellij.rt.execution.junit.JUnitStarter.main(JUnitStarter.java:68)
	at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
	at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
	at com.intellij.rt.execution.application.AppMain.main(AppMain.java:140)
Caused by: java.lang.NoSuchMethodError: com.sun.jersey.core.reflection.ReflectionHelper.getContextClassLoaderPA()Ljava/security/PrivilegedAction;
	at com.sun.jersey.spi.scanning.AnnotationScannerListener.<init>(AnnotationScannerListener.java:94)
	at com.sun.jersey.spi.scanning.PathProviderScannerListener.<init>(PathProviderScannerListener.java:59)
	at com.sun.jersey.api.core.ScanningResourceConfig.init(ScanningResourceConfig.java:79)
	at com.sun.jersey.api.core.PackagesResourceConfig.init(PackagesResourceConfig.java:104)
	at com.sun.jersey.api.core.PackagesResourceConfig.<init>(PackagesResourceConfig.java:78)
	at com.sun.jersey.api.core.PackagesResourceConfig.<init>(PackagesResourceConfig.java:89)
	at com.sun.jersey.spi.container.servlet.WebComponent.createResourceConfig(WebComponent.java:696)
	at com.sun.jersey.spi.container.servlet.WebComponent.createResourceConfig(WebComponent.java:674)
	at com.sun.jersey.spi.container.servlet.WebComponent.init(WebComponent.java:203)
	at com.sun.jersey.spi.container.servlet.ServletContainer.init(ServletContainer.java:374)
	at com.sun.jersey.spi.container.servlet.ServletContainer.init(ServletContainer.java:557)
	at javax.servlet.GenericServlet.init(GenericServlet.java:244)
	at org.eclipse.jetty.servlet.ServletHolder.initServlet(ServletHolder.java:612)
	at org.eclipse.jetty.servlet.ServletHolder.initialize(ServletHolder.java:395)
	at org.eclipse.jetty.servlet.ServletHandler.initialize(ServletHandler.java:871)
	at org.eclipse.jetty.servlet.ServletContextHandler.startContext(ServletContextHandler.java:298)
	at org.eclipse.jetty.server.handler.ContextHandler.doStart(ContextHandler.java:741)
	at org.eclipse.jetty.util.component.AbstractLifeCycle.start(AbstractLifeCycle.java:68)
	at org.eclipse.jetty.util.component.ContainerLifeCycle.start(ContainerLifeCycle.java:132)
	at org.eclipse.jetty.util.component.ContainerLifeCycle.doStart(ContainerLifeCycle.java:114)
	at org.eclipse.jetty.server.handler.AbstractHandler.doStart(AbstractHandler.java:61)
	at org.eclipse.jetty.util.component.AbstractLifeCycle.start(AbstractLifeCycle.java:68)
	at org.eclipse.jetty.util.component.ContainerLifeCycle.start(ContainerLifeCycle.java:132)
	at org.eclipse.jetty.server.Server.start(Server.java:387)
	at org.eclipse.jetty.util.component.ContainerLifeCycle.doStart(ContainerLifeCycle.java:114)
	at org.eclipse.jetty.server.handler.AbstractHandler.doStart(AbstractHandler.java:61)
	at org.eclipse.jetty.server.Server.doStart(Server.java:354)
	at org.eclipse.jetty.util.component.AbstractLifeCycle.start(AbstractLifeCycle.java:68)
	at org.neo4j.server.web.Jetty9WebServer.startJetty(Jetty9WebServer.java:381)
	at org.neo4j.server.web.Jetty9WebServer.start(Jetty9WebServer.java:184)
	at org.neo4j.server.AbstractNeoServer.startWebServer(AbstractNeoServer.java:474)
	at org.neo4j.server.AbstractNeoServer.start(AbstractNeoServer.java:230)
	... 22 more
~~~

<p>I was a bit baffled at first but if we look closely about 5 - 10 lines down the stack trace we can see the mistake I've made:</p>



~~~text

	at com.sun.jersey.api.core.PackagesResourceConfig.(PackagesResourceConfig.java:89) ~[jersey-server-1.19.jar:1.19]
	at com.sun.jersey.spi.container.servlet.WebComponent.createResourceConfig(WebComponent.java:696) ~[jersey-servlet-1.17.1.jar:1.17.1]
	at com.sun.jersey.spi.container.servlet.WebComponent.createResourceConfig(WebComponent.java:674) ~[jersey-servlet-1.17.1.jar:1.17.1]
~~~

<p>
We have different versions of the Jersey libraries. Since we're writing the extension for Neo4j 2.2.3 we can quickly check which version it depends on:
</p>



~~~bash

$ ls -alh neo4j-community-2.2.3/system/lib/ | grep jersey
-rwxr-xr-x@  1 markneedham  staff   426K 22 Jun 04:57 jersey-core-1.19.jar
-rwxr-xr-x@  1 markneedham  staff    52K 22 Jun 05:02 jersey-multipart-1.19.jar
-rwxr-xr-x@  1 markneedham  staff   686K 22 Jun 05:02 jersey-server-1.19.jar
-rwxr-xr-x@  1 markneedham  staff   126K 22 Jun 05:02 jersey-servlet-1.19.jar
~~~

<p>
So we should't have 1.17.1 in our project and it was easy enough to find my mistake by looking in the pom file:
</p>



~~~xml

<properties>
...
    <jersey.version>1.17.1</jersey.version>
...
</properties>

<dependencies>
...

    <dependency>
        <groupId>com.sun.jersey</groupId>
        <artifactId>jersey-servlet</artifactId>
        <version>${jersey.version}</version>
    </dependency>

...
</dependencies>
~~~

<p>Also easy enough to fix!</p>



~~~xml

<properties>
...
    <jersey.version>1.19</jersey.version>
...
</properties>
~~~

<p>
You can see <a href="https://github.com/mneedham/dummy-unmanaged-extension/blob/master/src/test/java/org/neo4j/unmanaged/ExampleResourceTest.java">an example of this working on github</a>.
</p>

