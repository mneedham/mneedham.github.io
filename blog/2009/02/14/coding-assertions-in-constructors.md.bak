+++
draft = false
date="2009-02-14 01:32:10"
title="Coding: Assertions in constructors"
tag=['coding']
category=['Coding']
+++

While browsing through the <a href="http://www.codeplex.com/aspnet">ASP.NET MVC source</a> I noticed that they use an interesting pattern on the constructors to ensure that an exception will be thrown if an object is not instantiated correctly.


~~~csharp

public ControllerContext(HttpContextBase httpContext, RouteData routeData, ControllerBase controller)
    : base(httpContext, routeData) {
    if (controller == null) {
        throw new ArgumentNullException("controller");
    }
    Controller = controller;
}
~~~

If you pass in a null Controller you shall go no further! 

We have discussed the merits of putting assertions in constructors several times in our <a href="http://domaindrivendesign.org">Domain Driven Design</a> book club but without ever really coming to a conclusion with respect to whether or not it is a good pattern. 

Spring is an example of a framework which does internal assertions on the values being passed to its objects and will throw assertions appropriately. There is even a custom <a href="http://static.springframework.org/spring/docs/2.5.x/api/org/springframework/util/Assert.html">Assert</a> class to do so.

The benefit of this approach is that our <strong>code will fail early</strong> if there is a problem. The disadvantage is that we may end up putting <strong>Asserts all over our code</strong> to cater for every place where the input could be invalid. If we were to use the Spring Assert class we would then have a coupling to that in our production code.

The approach I am more familiar with is that we would <strong>validate any input from the UI or from systems that we don't have control over</strong>, but apart from these boundary cases we would assume that our classes are <a href="http://docs.codehaus.org/display/PICO/Good+Citizen">good citizens</a> and will call each other with valid data.

My understanding of the implicit contract of a constructor is that we should never be passing null values into them. If we are contemplating doing so then we are probably doing something wrong and either need to reconsider or create a new constructor and then default the value for the extra parameters in other constructors.

In a way I suppose this is a limitation of the Java/C# type system that you can't prevent null values being passed into a constructor or that you can even have a null value in the first place.
