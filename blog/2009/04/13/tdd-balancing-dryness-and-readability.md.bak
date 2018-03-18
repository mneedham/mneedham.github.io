+++
draft = false
date="2009-04-13 00:47:00"
title="TDD: Balancing DRYness and Readability"
tag=['tdd', 'testing']
category=['Testing']
+++

I wrote previously about <a href="http://www.markhneedham.com/blog/2009/01/30/tdd-test-dryness/">creating DRY tests</a> and after some conversations with my colleagues recently about the balance between reducing duplication but maintaining readability I think I've found the compromise between the two that works best for me.

The underlying idea is that in any unit test I want to be aiming for a distinct 3 sections in the test - Given/When/Then, Arrange/Act/Assert or whatever your favourite description for those is.

<h3>Why?</h3>

I find that tests written like this are the <strong>easiest for me to understand</strong> - there would typically be a blank line between each distinct section so that scanning through the test it is easy to understand what is going on and I can zoom in more easily on the bit which concerns me at the time.

When there's expectations on mocks involved in the test then we might end up with the meat of the 'Then' step being defined before the 'When' section but for other tests it should be possible to keep to the structure.

A lot of the testing I've been working on recently has been around mapping data between objects - there's not that much logic going on but it's still important to have some sort of <a href="http://www.markhneedham.com/blog/2009/04/02/tdd-testing-mapping-code/">verification that we have mapped everything that we need to</a>.

We often end up with a couple of tests which might look something like this:


~~~csharp

public void ShouldEnsureThatFemaleCustomerIsMappedCorrectly()
{
	var customer = new Customer() 
					{
						Gender = Gender.Female
						Address = new Address(...)
					}
					
	var customerMessage = new CustomerMapper().MapFrom(customer)
	
	Assert.AreEqual(CustomerMessage.Gender.Female, customerMessage.Gender);
	Assert.AreEqual(new Address(..), customerMessage.Address);
	// and so on...
}

public void ShouldEnsureThatMaleCustomerIsMappedCorrectly()
{
	var customer = new Customer() 
				{
					Gender = Gender.Male
					Address = new Address(...)
				}
				
	var customerMessage = new CustomerMapper().MapFrom(customer)

	Assert.AreEqual(CustomerMessage.Gender.Male, customerMessage.Gender);
	Assert.AreEqual(new Address(..), customerMessage.Address);
	// and so on...
}
~~~

(For the sake of this example 'CustomerMessage' is being auto generated from an xsd)

We've got a bit of duplication here - it's not that bad but if there are changes to the CustomerMessage class, for example, we have more than one place to change.

It is actually possible to refactor this so that we encapsulate nearly everything in the test, but I've never found a clean way to do this so that you can still understand the intent of the test.


~~~csharp

public void ShouldEnsureThatFemaleCustomerIsMappedCorrectly()
{
	AssertCustomerDetailsAreMappedCorrectly(customer, Gender.Female, CustomerMessage.Gender.Female);
}

public void ShouldEnsureThatMaleCustomerIsMappedCorrectly()
{				
	AssertCustomerDetailsAreMappedCorrectly(customer, Gender.Male, CustomerMessage.Gender.Male);
}

private void AssertCustomerDetailsAreMappedCorrectly(Customer customer, Gender gender, CustomerMessage.Gender gender)
{			
	var customer = new Customer() 
					{				
						Gender = gender,
						Address = new Address(...)
					}

	var customerMessage = new CustomerMapper().MapFrom(customer)

	Assert.AreEqual(CustomerMessage.Gender.Male, customerMessage.Gender);
	// and so on...	
}
~~~
(Of course we would be mapping more than just gender normally but gender helps illustrate the pattern that I've noticed)

We've achieved our goal of reducing duplication but it's not immediately obvious what we're testing because that's encapsulated too. I find with this approach that it's more difficult to <a href="http://www.markhneedham.com/blog/2009/01/28/tdd-design-tests-for-failure/">work out what went wrong when the test stops working</a>, so I prefer to refactor to somewhere in between the two extremes.


~~~csharp

public void ShouldEnsureThatFemaleCustomerIsMappedCorrectly()
{
	var customer = CreateCustomer(Gender.Female, new Address(...));
	
	var customerMessage = MapCustomerToCustomerMessage(customer);
	
	AssertFemaleCustomerDetailsAreMappedCorrectly(customer, customerMessage);
}

public void ShouldEnsureThatMaleCustomerIsMappedCorrectly()
{
	var customer = CreateCustomer(Gender.Male, new Address(...));
	
	var customerMessage = MapCustomerToCustomerMessage(customer);
	
	AssertMaleCustomerDetailsAreMappedCorrectly(customer, customerMessage);
}

private CustomerMessage MapCustomerToCustomerMessage(Customer customer)
{
	return new CustomerMapper().MapFrom(customer);
}

private Customer CreateCustomer(Gender gender, Address address)
{
	return new Customer() 
				{
					Gender = gender,
					Address = address
				};
}

private void AssertMaleCustomerDetailsAreMappedCorrectly(Customer customer, CustomerMessage customerMessage)
{			
	Assert.AreEqual(CustomerMessage.Gender.Male, customerMessage.Gender);
	// and so on...	
}

private void AssertFemaleCustomerDetailsAreMappedCorrectly(Customer customer, CustomerMessage customerMessage)
{			
	Assert.AreEqual(CustomerMessage.Gender.Female, customerMessage.Gender);
	// and so on...	
}
~~~

Although this results in more code than the 1st approach I like it because there's a clear three part description of what is going on which will make it easier for me to work out which bit is going wrong. I've also split the assertions for Male and Female because I think it makes the test easier to read.

I'm not actually sure whether we need to put the 2nd step into its own method or not - it's an idea I've been experimenting with lately.

I'm open to different ideas on this - until recently I was quite against the idea of encapsulating all the assertion statements in one method but a few conversations with <a href="http://fabiopereira.me/blog/">Fabio</a> have led me to trying it out and I think it does help reduce some duplication without hurting our ability to debug a test when it fails.
