+++
draft = false
date="2010-06-15 23:15:30"
title="Fluent NHibernate: Seeing the mapping files generated"
tag=['nhibernate']
category=['Hibernate']
+++

We've been fiddling around with <a href="http://fluentnhibernate.org/">Fluent NHibernate</a> a bit over the last couple of days and one of the things that we wanted to do was output the NHibernate mapping files being generated so we could see if they were as expected.

I couldn't figure out how to do it but thanks to the help of <a href="http://twitter.com/jagregory/status/16210304123">James Gregory</a>, <a href="http://twitter.com/trullock/status/16214631489">Andrew Bullock</a> and <a href="http://twitter.com/MatthewErbs/status/16213970597">Matthew Erbs</a> on twitter this is the code that you need in order to do that:


~~~csharp

Fluently
.Configure()
.Database(MsSqlConfiguration.MsSql2000.ConnectionString("connection string"))
.Mappings(m => m.FluentMappings.ExportTo("c:\\directory-to-output-files-to"))
.BuildSessionFactory();
~~~

The 4th line is the important one here and we can choose which directory the mappings files get outputted to and then check that everything is getting setup as we'd expect.
