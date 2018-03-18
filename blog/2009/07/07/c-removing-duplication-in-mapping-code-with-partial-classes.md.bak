+++
draft = false
date="2009-07-07 18:11:36"
title="C#: Removing duplication in mapping code with partial classes"
tag=['c', 'net']
category=['.NET']
+++

One of the problems that we've come across while writing the mapping code for our <a href="http://www.markhneedham.com/blog/2009/07/07/domain-driven-design-anti-corruption-layer/">anti corruption layer</a> is that there is quite a lot of duplication of mapping similar types due to the fact that each service has different auto generated classes representing the same data structure.

We are making SOAP web service calls and generating classes to represent the requests and responses to those end points using <a href="http://msdn.microsoft.com/en-us/library/aa347733.aspx">SvcUtil</a>. We then translate from those auto generated classes to our domain model using various mapper classes.

One example of duplication which really stood out is the creation of a 'ShortAddress' which is a data structure consisting of a postcode, suburb and state.

In order to map address we have a lot of code similar to this:


~~~csharp

private ShortAddress MapAddress(XsdGeneratedAddress xsdGeneratedAddress)
{
	return new ShortAddress(xsdGeneratedAddress.Postcode, xsdGeneratedAddress.Suburb, xsdGeneratedAddress.State);
}
~~~


~~~csharp

private ShortAddress MapAddress(AnotherXsdGeneratedAddress xsdGeneratedAddress)
{
	return new ShortAddress(xsdGeneratedAddress.Postcode, xsdGeneratedAddress.Suburb, xsdGeneratedAddress.State);
}
~~~

Where the XsdGeneratedAddress might be something like this:


~~~csharp

public class XsdGeneratedAddress
{
	string Postcode { get; }
	string Suburb { get; }
	string State { get; }
	// random other code
}
~~~

It's really quite boring code to write and it's pretty much exactly the same apart from the class name. 

I realise here that if we were using a dynamic language we wouldn't have a problem since we could just write the code as if the object being passed into the method had those properties on it.

Sadly we are in C# which doesn't yet have that capability!

Luckily for us the SvcUtil generated classes are partial classes so (as <a href="http://twitter.com/davcamer">Dave</a> pointed out) we can create another partial class which inherits from an interface that we define. We can then refer to types which implement this interface in our mapping code, helping to reduce the duplication.

In this case we create a 'ShortAddressDTO' with properties that match those on the auto generated class:


~~~csharp

public interface ShortAddressDTO 
{
	string Postcode { get; }
	string Suburb { get; }
	string State { get; }
}
~~~

We then need to make the generated classes inherit from this:


~~~csharp

public partial class XsdGeneratedAddress : ShortAddressDTO {}
~~~

Which means in our mapping code we can now do the following:


~~~csharp

private ShortAddress MapAddress(ShortAddressDTO shortAddressDTO)
{
	return xsdGeneratedAddress.ConvertToShortAddress();
}
~~~

Which uses this extension method:


~~~csharp

public static class ServiceDTOExtensions 
{
	public static ShortAddress ConvertToShortAddress(ShortAddressDTO shortAddressDTO)
	{
		return new ShortAddress(shortAddressDTO.Postcode, shortAddressDTO.Suburb, shortAddressDTO.State);
	}
}
~~~

Which seems much cleaner than what we had to do before.
