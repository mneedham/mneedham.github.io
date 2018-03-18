+++
draft = false
date="2010-06-29 06:45:11"
title="NHibernate 2nd level cache: Doing it wrong?"
tag=['nhibernate']
category=['Hibernate']
+++

I wrote a couple of weeks ago about how we'd been trying to make use of the <a href="http://www.markhneedham.com/blog/2010/06/16/fluent-nhibernate-and-the-2nd-level-cache/">NHibernate 2nd level cache</a> and we were able to cache our data by following the various posts that I listed.

Unfortunately when we ran some performance tests we found that the performance of the application was significantly worse than when we just wrote our own 'cache' - an object which had a dictionary containing the reference data items we'd previously tried to lookup and the appropriate values.

We don't need to handle cache invalidation. The client's policy is to restart production servers every night so if we want to update any of the reference data then we just need to make sure a database script is run before the servers get restarted.

<h3>Explicit transactions when reading</h3>

There is a post on the NHibernate Profiler website which describes why <a href="http://nhprof.com/Learn/Alerts/DoNotUseImplicitTransactions">we should not use implicit transactions</a> when using NHibernate. Instead we should create explicit ones:

<blockquote>
When we don't define our own transactions, it falls back into implicit transaction mode, where every statement to the database runs in its own transaction, resulting in a large performance cost (database time to build and tear down transactions), and reduced consistency.

Even if we are only reading data, we should use a transaction, because using transactions ensures that we get consistent results from the database.
</blockquote>

We ended up with something like this:


~~~csharp

public class OurRepository
{
	public ReferenceDataObject Find(ReferenceDataObjectKey key)
	{
		using(var session = SessionFactory.OpenSession())
		{
			using(var tx = session.BeginTransaction())
			{
				var query = session.Linq<ReferenceDataObject>().Where(r => r.Key == key);
				query.QueryOptions.SetCachable(true).SetCacheMode(CacheMode.Normal);
				// and so	 on
			}
		}
 
		// return the object
	}
}
~~~

As well as performance tests, we found that our integration tests became much slower than when we used our own 'cache'.

We have some tests which look up 100s of different bits of reference data and the total time taken to run those tests went from around 4 seconds up to 30 seconds.

As I understand it, putting a transaction around a query means that we create a transaction with the database on every request even if the query is cached and we're going to retrieve the results from the 2nd level cache rather than the database.

We took out the transaction which reduced the time taken to 7 seconds but it was still slower than when we used our hand rolled cache.

It seems like we must be doing something wrong or not understand something with respect to the NHibernate 2nd level cache because it seems ridiculous that the performance could be this different?
