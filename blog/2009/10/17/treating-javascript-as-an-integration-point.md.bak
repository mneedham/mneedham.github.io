+++
draft = false
date="2009-10-17 09:16:12"
title="Treating Javascript as an integration point"
tag=['javascript']
category=['Javascript']
+++

A couple of weeks ago <a href="http://www.markhneedham.com/blog/2009/10/05/my-software-development-journey-year-3-4/">I wrote a post about my software development journey</a> over the last year and towards the end I described the difficulties we were having in making changes to some C# code while being sure that we hadn't broken javascript functionality that also relied on that code.

We typically have code which looks like this:


~~~csharp

public class SomeController
{
	public ActionResult SomeControllerAction()
	{
		var someModel = new SomeModel { Property1 = "my Property" };

		return new JsonResult { Data = someModel };
	}
}

public class SomeModel 
{
	public string Property1 { get; set; }
}
~~~

We would make use of this type of object in javascript code like so:


~~~javascript

$.getJSON("/SomeController/SomeControllerAction",
        function(data){
			var value = data.Property1;
			// do some cool stuff with that value
		}
);
~~~

My colleague Raymond Maung recently came up with the idea of writing tests to ensure that the properties we make use of in Javascript exist on the C# objects which we return in JSON calls.

We now have a testing extension method which uses reflection to check that the expected properties are set.


~~~csharp

public static class TestingExtensions 
{
        public static void AssertHasProperty(this Type type, string propertyName)
        {
            var property = type.GetProperty(propertyName);
            Assert.IsNotNull(property, "Expected {0} to have property '{1}' but it didn't", type.Name, propertyName);
        }
}
~~~


~~~csharp

[Test]
public void ShouldEnsurePropertiesRequiredInJavascriptAreSet()
{
	var type = typeof(SomeModel);
	type.AssertHasProperty("Property1");
	// and so on
}
~~~

It still requires the developer to remember to put a test in if they add a property to the C# model but I think it's working better than having to switch between the javascript and C# files checking that you haven't broken anything. 
