+++
draft = false
date="2012-02-11 10:55:58"
title="Oracle Spatial: java.sql.SQLRecoverableException: No more data to read from socket"
tag=['oracle']
category=['Software Development']
+++

We're using Oracle Spatial on my current project so that we can locate points within geographical regions and decided earlier in the week to rename the table where we store the <a href="http://docs.oracle.com/cd/B19306_01/appdev.102/b14255/sdo_objrelschema.htm#i1004087">SDO_GEOMETRY</a> objects for each region.

We did that by using a normal table alter statement but then started seeing the following error when we tried to insert test data in that column which takes an SDO_GEOMETRY object:


~~~text

org.hibernate.exception.JDBCConnectionException: could not execute native bulk manipulation query
       at org.hibernate.exception.SQLStateConverter.convert(SQLStateConverter.java:99)
       at org.hibernate.exception.JDBCExceptionHelper.convert(JDBCExceptionHelper.java:66)
       at org.hibernate.engine.query.NativeSQLQueryPlan.performExecuteUpdate(NativeSQLQueryPlan.java:219)
       at org.hibernate.impl.SessionImpl.executeNativeUpdate(SessionImpl.java:1310)
       at org.hibernate.impl.SQLQueryImpl.executeUpdate(SQLQueryImpl.java:396)
       at $Proxy53.insertTariffZone(Unknown Source)    
       at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
       at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:57)
       at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
       at org.junit.runners.model.FrameworkMethod$1.runReflectiveCall(FrameworkMethod.java:45)
       at org.junit.internal.runners.model.ReflectiveCallable.run(ReflectiveCallable.java:15)
       at org.junit.runners.model.FrameworkMethod.invokeExplosively(FrameworkMethod.java:42)
       at org.junit.internal.runners.statements.InvokeMethod.evaluate(InvokeMethod.java:20)
       at org.junit.internal.runners.statements.RunBefores.evaluate(RunBefores.java:28)
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
       at com.intellij.junit4.JUnit4IdeaTestRunner.startRunnerWithArgs(JUnit4IdeaTestRunner.java:71)
       at com.intellij.rt.execution.junit.JUnitStarter.prepareStreamsAndStart(JUnitStarter.java:202)
       at com.intellij.rt.execution.junit.JUnitStarter.main(JUnitStarter.java:63)
       at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
       at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:57)
       at com.intellij.rt.execution.application.AppMain.main(AppMain.java:120)
Caused by: java.sql.SQLRecoverableException: No more data to read from socket
       at oracle.jdbc.driver.T4CMAREngine.unmarshalUB1(T4CMAREngine.java:1157)
       at oracle.jdbc.driver.T4CTTIfun.receive(T4CTTIfun.java:290)
       at oracle.jdbc.driver.T4CTTIfun.doRPC(T4CTTIfun.java:192)
       at oracle.jdbc.driver.T4C8Oall.doOALL(T4C8Oall.java:531)
       at oracle.jdbc.driver.T4CPreparedStatement.doOall8(T4CPreparedStatement.java:207)
       at oracle.jdbc.driver.T4CPreparedStatement.executeForRows(T4CPreparedStatement.java:1044)
       at oracle.jdbc.driver.OracleStatement.doExecuteWithTimeout(OracleStatement.java:1329)
       at oracle.jdbc.driver.OraclePreparedStatement.executeInternal(OraclePreparedStatement.java:3584)
       at oracle.jdbc.driver.OraclePreparedStatement.executeUpdate(OraclePreparedStatement.java:3665)
       at oracle.jdbc.driver.OraclePreparedStatementWrapper.executeUpdate(OraclePreparedStatementWrapper.java:1352)
       at com.mchange.v2.c3p0.impl.NewProxyPreparedStatement.executeUpdate(NewProxyPreparedStatement.java:105)
       at org.hibernate.engine.query.NativeSQLQueryPlan.performExecuteUpdate(NativeSQLQueryPlan.java:210)
       ... 39 more
~~~ 

We couldn't see anything particularly wrong in what we'd done and none of the error messages we got were being particularly helpful.

Eventually we asked the DBA on our team to help out and he showed us how to look up the Oracle system logs which in our case were located at:


~~~text

/u01/app/oracle/diag/rdbms/orcl/orcl/trace
~~~

We ran the query again and noticed new files were being written to that location, one of which had the following error message:


~~~text

Exception [type: SIGSEGV, Address not mapped to object] [ADDR:0x40] [PC:0x2FDAE7D, mdidxid()+2563] [flags: 0x0, count: 1]
DDE: Problem Key 'ORA 7445 [mdidxid()+2563]' was flood controlled (0x2) (incident: 3851)
ORA-07445: exception encountered: core dump [mdidxid()+2563] [SIGSEGV] [ADDR:0x40] [PC:0x2FDAE7D] [Address not mapped to object] []
ORA-13203: failed to read USER_SDO_GEOM_METADATA view
ssexhd: crashing the process...
Shadow_Core_Dump = PARTIAL
~~~

We'd forgotten to rename the table in the USER_SDO_GEOM_METADATA view, exactly as the message says!

Running the following statement sorted us out:


~~~text

UPDATE user_sdo_geom_metadata SET table_name = 'NEW_NAME' where table_name = 'OLD_NAME';
~~~
