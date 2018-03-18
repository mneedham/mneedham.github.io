+++
draft = false
date="2014-02-05 12:21:30"
title="Jython/Neo4j: java.lang.ExceptionInInitializerError: java.lang.ExceptionInInitializerError"
tag=['jython']
category=['neo4j', 'Python']
+++

<p>I've been playing around with calling Neo4j's Java API from Python via <a href="http://www.jython.org/">Jython</a> and immediately ran into the following exception when trying to create an embedded instance:</p>



~~~bash

$ jython -Dpython.path /path/to/neo4j.jar
Jython 2.5.3 (2.5:c56500f08d34+, Aug 13 2012, 14:48:36)
[Java HotSpot(TM) 64-Bit Server VM (Oracle Corporation)] on java1.7.0_45
Type "help", "copyright", "credits" or "license" for more information.

>>> import org.neo4j.graphdb.factory
>>> org.neo4j.graphdb.factory.GraphDatabaseFactory().newEmbeddedDatabase("/tmp/foo")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
	at org.neo4j.graphdb.factory.GraphDatabaseFactory$1.newDatabase(GraphDatabaseFactory.java:83)
	at org.neo4j.graphdb.factory.GraphDatabaseBuilder.newGraphDatabase(GraphDatabaseBuilder.java:198)
	at org.neo4j.graphdb.factory.GraphDatabaseFactory.newEmbeddedDatabase(GraphDatabaseFactory.java:69)
	at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
	at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:57)
	at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
	at java.lang.reflect.Method.invoke(Method.java:606)

java.lang.ExceptionInInitializerError: java.lang.ExceptionInInitializerError
~~~

<p>I eventually ended up at <cite>GraphDatabaseSettings</cite> so I tried to import that:</p>



~~~bash

>>> import org.neo4j.graphdb.factory.GraphDatabaseSettings
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
java.lang.ExceptionInInitializerError
	at java.lang.Class.forName0(Native Method)
	at java.lang.Class.forName(Class.java:270)
	at org.python.core.Py.loadAndInitClass(Py.java:909)
	at org.python.core.Py.findClassInternal(Py.java:844)
	at org.python.core.Py.findClassEx(Py.java:895)
	at org.python.core.packagecache.SysPackageManager.findClass(SysPackageManager.java:133)
	at org.python.core.packagecache.PackageManager.findClass(PackageManager.java:28)
	at org.python.core.packagecache.SysPackageManager.findClass(SysPackageManager.java:122)
	at org.python.core.PyJavaPackage.__findattr_ex__(PyJavaPackage.java:137)
	at org.python.core.PyObject.__findattr__(PyObject.java:863)
	at org.python.core.PyObject.impAttr(PyObject.java:1001)
	at org.python.core.imp.import_next(imp.java:720)
	at org.python.core.imp.import_logic(imp.java:782)
	at org.python.core.imp.import_module_level(imp.java:842)
	at org.python.core.imp.importName(imp.java:917)
	at org.python.core.ImportFunction.__call__(__builtin__.java:1220)
	at org.python.core.PyObject.__call__(PyObject.java:357)
	at org.python.core.__builtin__.__import__(__builtin__.java:1173)
	at org.python.core.imp.importOne(imp.java:936)
	at org.python.pycode._pyx5.f$0(<stdin>:1)
	at org.python.pycode._pyx5.call_function(<stdin>)
	at org.python.core.PyTableCode.call(PyTableCode.java:165)
	at org.python.core.PyCode.call(PyCode.java:18)
	at org.python.core.Py.runCode(Py.java:1275)
	at org.python.core.Py.exec(Py.java:1319)
	at org.python.util.PythonInterpreter.exec(PythonInterpreter.java:215)
	at org.python.util.InteractiveInterpreter.runcode(InteractiveInterpreter.java:89)
	at org.python.util.InteractiveInterpreter.runsource(InteractiveInterpreter.java:70)
	at org.python.util.InteractiveInterpreter.runsource(InteractiveInterpreter.java:46)
	at org.python.util.InteractiveConsole.push(InteractiveConsole.java:110)
	at org.python.util.InteractiveConsole.interact(InteractiveConsole.java:90)
	at org.python.util.jython.run(jython.java:317)
	at org.python.util.jython.main(jython.java:129)
Caused by: java.lang.ArrayIndexOutOfBoundsException: 0
	at org.neo4j.graphdb.factory.GraphDatabaseSettings.<clinit>(GraphDatabaseSettings.java:69)
	... 33 more

java.lang.ExceptionInInitializerError: java.lang.ExceptionInInitializerError
~~~

<p>This bit of code is used to work out the default cache type. It does by first reading the available cache types from a file on the class path and then picking the first one on the list.</p>


<p>I could see that the file it was trying to read was in the JAR and I thought passing the JAR to 'python.path' would put it on the classpath. Alistair suggested checking that assumption by checking what was actually on the classpath:</p>



~~~bash

>>> import java.lang
>>> java.lang.System.getProperty("java.class.path")
u'/usr/local/Cellar/jython/2.5.3/libexec/jython.jar:'
~~~

<p>As you can see our JAR is missing from the list which explains the problem with reading the file. If we launch the jython REPL with our JAR passed explicitly to the Java classpath then it works:</p>



~~~bash

$ jython -J-cp /path/to/neo4j.jar
Jython 2.5.3 (2.5:c56500f08d34+, Aug 13 2012, 14:48:36)
[Java HotSpot(TM) 64-Bit Server VM (Oracle Corporation)] on java1.7.0_45
Type "help", "copyright", "credits" or "license" for more information.

>>> import java.lang
>>> java.lang.System.getProperty("java.class.path")
u'/usr/local/Cellar/jython/2.5.3/libexec/jython.jar:/path/to/neo4j.jar:'
~~~

<p>We can now create an embedded database with no problems:</p>



~~~bash

>>> import org.neo4j.graphdb.factory
>>> org.neo4j.graphdb.factory.GraphDatabaseFactory().newEmbeddedDatabase("/tmp/foo")
EmbeddedGraphDatabase [/tmp/foo]
~~~
