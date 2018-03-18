+++
draft = false
date="2010-06-17 00:43:41"
title="Incremental Refactoring: Create factory method"
tag=['coding', 'incremental-refactoring']
category=['Incremental Refactoring']
+++

<a href="http://twitter.com/dermotkilroy">Dermot</a> and I spent a bit of time today refactoring some code where the logic had ended up in the wrong place.

The code originally looked a bit like this:


~~~csharp

public class LookupService
{
	public LookUp Find(UserData userData)
	{
		var param1 = GetParam1From(userData);
		var param2 = GetParam2From(userData);
		var param3 = GetParam3From(userData);

		var lookupKey = new LookUpKey(param1, param2, param3);
		return lookupRepository.Find(lookupKey);
	}
}
~~~


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
}
~~~

We wanted to push the logic used to create the params in 'LookUpKey' into the 'LookUpKey' since it seemed that was a more natural place for that behaviour to live.

Unfortunately there were also a few other places that were use LookUpKey's constructor so we couldn't just go and change that to take in a 'UserData' otherwise we'd break other places in the code base.

My initial thought was that we could <a href="http://www.markhneedham.com/blog/2010/04/25/small-step-refactoring-overload-constructor/">overload the constructor</a> and temporarily have two constructors until we got rid of the original.

Dermot pointed out a better approach which was to add a static factory method to 'LookUpKey' and initially push the logic into that method.


~~~csharp

public class LookUpKey
{
	...

	public static LookUpKey CreateFrom(UserData userData)
	{
		var param1 = GetParam1From(userData);
		var param2 = GetParam2From(userData);
		var param3 = GetParam3From(userData);

		return new LookUpKey(param1, param2, param3);
	}
}
~~~

The service is now much simplified:


~~~csharp

public class LookupService
{
	public LookUp Find(UserData userData)
	{
		var lookupKey = LookUpKey.CreateFrom(userData);
		return lookupRepository.Find(lookupKey);
	}
}
~~~

We can also move tests that were originally indirectly testing the key creation by checking what was passed to the repository to be directly against the 'LookUpKey'.

Eventually we want to make LookUpKey's constructor private but for now we've been able to make our change without breaking the code base elsewhere.
