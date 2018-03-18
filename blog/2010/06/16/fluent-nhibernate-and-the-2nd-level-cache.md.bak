+++
draft = false
date="2010-06-16 00:07:43"
title="Fluent NHibernate and the 2nd level cache"
tag=['nhibernate', 'fluent-nhibernate']
category=['Hibernate']
+++

We've been trying to cache some objects using NHibernate's second level cache which always proves to be a trickier task than I remember it being the previous time!

We're storing some reference data in the database and then using LINQ to NHibernate to query for the specific row that we want based on some user entered criteria.

We can cache that query by calling 'SetCacheable' on the 'QueryOptions' property of our query:


~~~csharp

public class OurRepository
{
	public ReferenceDataObject Find(string criteria1, string criteria2)
	{
		var query = session.Linq<ReferenceDataObject>();
		query.QueryOptions.SetCachable(true).SetCacheMode(CacheMode.Normal);
		// and so on
	}
}
~~~

That helps to ensure that if we do the exact same query again it won't go to the database again. Instead it will just retrieve the id of the appropriate object from the 2nd level cache and then go and retrieve that.

In order to ensure that the 'ReferenceDataObject' does not get retrieved from the database each time we need to ensure that it is cached as well.

We can do that by adding the following to its mapping file:


~~~csharp

public class ReferenceDataObjectMappings : ClassMap<ReferenceDataObject>
{
	...

	Cache.ReadOnly();

	// or

	Cache.ReadWrite();

	// depending on whether we want to update the value in the cache based on it changing in the database or not

	..

}
~~~

The next step is to ensure that we have the query cache and second level cache turned on in the place where we configure our session factory:


~~~csharp

Fluently
.Configure()
.Database(MsSqlConfiguration.MsSql2000.ConnectionString("connection string")
	.Cache(c => c.UseQueryCache().ProviderClass(typeof(NHibernate.Caches.SysCache.SysCacheProvider).AssemblyQualifiedName)))
.Mappings(m => m.FluentMappings.AddFromAssemblyOf<ICurrentSessionFactory>())
.BuildSessionFactory();
~~~

The 'SysCacheProvider' is one we can use for web applications although there are all sorts of others available too.

Having got all this setup we wrote an integration test which added an item to the reference data table and then tried to retrieve it several times with the theory being that we would only see one call to the database.


~~~csharp

[Test]
public void ShouldCacheTheReferenceData()
{
	var myReferenceObject = new ReferenceDataObject(...);
	
	using(var session = SessionFactory.OpenSession())
	{
		session.Save(myReferenceDataObject);
		session.Flush();
	}
	
	// try and retrieve the object a few times here
}
~~~

Unfortunately we were seeing the database being hit every single time which confused us greatly until we came across  <a href="http://blogs.hibernatingrhinos.com/nhibernate/archive/2008/11/09/first-and-second-level-caching-in-nhibernate.aspx">the following explanation on Gabriel Schenker's blog</a>:

<blockquote>
A common error (It happened to me as well!) is to <strong>forget to commit or omit a transaction when adding or changing an entity/aggregate to the database</strong>. If we now access the entity/aggregate from another session then the 2nd level cache will not be prepared to provide us the cached instances and NHibernate makes an (unexpected round trip to the database).
</blockquote>

We need to change our test to commit the object in a transaction if we want the object to be propagated down to the 2nd level cache:


~~~csharp

[Test]
public void ShouldCacheTheReferenceData()
{
	var myReferenceObject = new ReferenceDataObject(...);
	
	using(var session = SessionFactory.OpenSession())
	{
		using(var tx = session.BeginTransaction())
		{
    			session.Save(myReferenceObject);
    			tx.Commit();        // important otherwise caching does NOT work!
		}
	}
	
	// try and retrieve the object a few times here
}
~~~




