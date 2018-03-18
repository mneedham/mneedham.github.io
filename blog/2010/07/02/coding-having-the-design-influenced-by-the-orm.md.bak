+++
draft = false
date="2010-07-02 16:56:41"
title="Coding: Having the design influenced by the ORM"
tag=['coding']
category=['Coding']
+++

I wrote a few weeks ago about <a href="http://www.markhneedham.com/blog/2010/06/17/incremental-refactoring-create-factory-method/">incremental refactoring using a static factory method</a> where we ended up with the following code:


~~~csharp

public class LookUpKey
{
	private readonly string param1;
	private readonly string param2;
	private readonly string param3;
 
	public LookUpKey(string param1, string param2, string param3)
	{
		this.param1 = param1;
		this.param2 = param2;
		this.param3 = param3;
	}
 
	public static LookUpKey CreateFrom(UserData userData)
	{
		var param1 = GetParam1From(userData);
		var param2 = GetParam2From(userData);
		var param3 = GetParam3From(userData);
 
		return new LookUpKey(param1, param2, param3);
	}

	public string Param1Key
	{
		{ get { return param1; } }
	}

	...
}
~~~

The next step after this refactoring that we wanted to drive was to push the logic out of the static factory method so that it could just be done when those properties were evaluated. 

We wanted to drive the code into something similar to this:


~~~csharp

public class LookUpKey
{
	private readonly UserData userData;
 
	public LookUpKey(UserData)
	{
		this.userData = userData;
	}
 
	public static LookUpKey CreateFrom(UserData userData)
	{
		return new LookUpKey(userData);
	}

	public string Param1Key
	{
		{ get { return GetParam1From(userData); } }
	}

	...
}
~~~

Unfortunately we also hydrate the 'LookUpKey' from the database when we're loading 'LookUps' into memory so that we can query them in memory.


~~~csharp

public class LookupRepository
{
	public Lookup Find(LookupKey lookupKey)
	{
	     var query = currentSession.Linq<LookupRecord>();

		// this result would be cached and then queried but for the sake of the example I don't show that

	     var lookupRecord = query.Where(l => l.LookupKey.Equals(lookupKey)).FirstOrDefault();

		if(lookup == null) throw Exception(...);
		
		return lookupRecord.Lookup;
	}
}
~~~

We are therefore mapping directly to those fields to hydrate the object. The Fluent NHibernate mapping code looks like this:


~~~csharp

public class LookupRecordMapping : ClassMap<LookupRecord>
{
    public LookupRecordMapping()
    {
        ...
		
        Component(lookupRecord => lookupRecord.LookupKey, lookupKey =>
        {
            lookupKey.Map(x => x.Param1).Access.CamelCaseField();
            lookupKey.Map(x => x.Param2).Access.CamelCaseField();
            lookupKey.Map(x => x.Param3).Access.CamelCaseField();
        });
    }
}
~~~

The database table for that is as follows:


~~~text

Param1 | Param2 | Param3 | LookupValue1 | LookupValue2
~~~

Looking at the code like this makes it more obvious that 'Param1', 'Param2' and 'Param3' together represent a concept and that 'UserData' probably doesn't belong inside that object in the first place.

<a href="http://www.markhneedham.com/blog/2010/06/17/incremental-refactoring-create-factory-method/#comment-39604">Rafael Peixoto de Azevedo wondered in the comments on the original post</a> whether 'Param1', 'Param2' and 'Param3' represent a relevant concept for 'UserData' but interestingly in this case the business guys didn't have a name for this concept so we decided that it was some sort of lookup.

I found it interesting that looking at this code from a different part of the system made it clearer that the refactoring I wanted to make didn't actually make sense.
