+++
draft = false
date="2009-04-04 11:41:23"
title="Functional C#: The hole in the middle pattern"
tag=['c', 'net']
category=['.NET']
+++

While reading <a href="http://manning.com/petricek/">Real World Functional Programming</a> I came across an interesting pattern that I have noticed in some code bases recently which I liked but didn't know had been given a name!

The <a href="http://enfranchisedmind.com/blog/posts/the-hole-in-the-middle-pattern/">hole in the middle pattern</a>, coined by Brian Hurt, shows a cool way of using higher order functions in order to reuse code in cases where the code typically looks something like this:


~~~csharp

public void SomeServiceCall() 
{
	var serviceClient = CreateServiceClient();

	try 
	{
		serviceClient.MakeMethodCall();
	}
	catch(SomeServiceException someServiceException) 
	{
		// Handle exception
	}
	finally 
	{
		serviceClient.Close();
	}
}
~~~

The first and the third lines (initialisation and finalisation) are always the same but the service.MakeMethodCall() varies depending on which service we are using. The more services we have the more boring it gets writing out the same code over and over again.

In C# 3.0 we could reuse code in this situation by passing in a lambda expression which calls that method, allowing us to vary the important part of the method call while keeping the scaffolding the same.


~~~csharp

public void SomeServiceCall(Action<TServiceClient> callService) 
{
	var serviceClient = CreateServiceClient();

	try 
	{
		callService(serviceClient);
	}
	catch(SomeServiceException someServiceException) 
	{
		// Handle exception
	}
	finally 
	{
		serviceClient.Close();
	}
}
~~~


~~~csharp

SomeServiceCall(service => service.SomeMethodCall()) 
~~~

One of the things I've noticed with the ability to pass in functions to methods is that sometimes we end up making the code really difficult to read by doing so but when we're dealing with services this seems to be one of the best and most obvious uses of Actions/Funcs in C# 3.0 and it leads to a more reusable and easy to understand API. 
