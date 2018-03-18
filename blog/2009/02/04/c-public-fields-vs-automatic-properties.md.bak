+++
draft = false
date="2009-02-04 17:52:03"
title="C#: Public fields vs automatic properties "
tag=['c', 'net']
category=['.NET']
+++

An interesting new feature in C# 3.0 is that of <a href="http://msdn.microsoft.com/en-us/library/bb384054.aspx">automatic properties</a> on objects - this allows us to define a get/set property and the creation of the underlying field is taken care off for us.

We can therefore create a class like this:


~~~csharp

public class Foo {
	public string Bar { get; set; }
}
~~~

Now ignoring the fact that it's terrible OO to write a class like that, one thing that we've been wondering is what's the difference between doing the above and just creating a public field on Foo called Bar like so:


~~~csharp

public class Foo 
{
	public string Bar;
}
~~~

In terms of how we use the class in our code it's conceptually the same but there are a couple of subtle differences.

We can change our implementation more easily if we use the automated properties. If we decide that we want to do something else apart from just setting a field or returning it then we can do that more easily without having to recompile assemblies that depend on that class.

If we decided we only wanted the getter to be public but to have a private setter that would be an easier change using automated properties, and if we want to reflect on the class I find it's much easier to do that when we have properties rather than fields.

That's all I can think of at least. Are there any other differences?
