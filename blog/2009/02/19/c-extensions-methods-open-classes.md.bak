+++
draft = false
date="2009-02-19 06:22:07"
title="C#: Extension methods != Open classes"
tag=['c', 'net', 'extension-methods', 'open-classes']
category=['.NET']
+++

When I first heard about <a href="http://weblogs.asp.net/gunnarpeipman/archive/2007/11/18/c-extension-methods.aspx">extension methods</a> in C# it sounded like a pretty cool idea but I wasn't sure how they differed to the idea of open classes that I had seen when doing a bit of Ruby.

After a bit of a struggle recently to try and override some extension methods on HtmlHelper in ASP.NET MVC it's clear to me that we don't quite have the same power that open classes would provide.

To start with we can't access private variables of a class in an extension method - as far as I understand an extension method is just syntactic sugar to make our code look pretty at compile time.

We therefore only have access to public fields, methods and properties from extension methods. Anything protected is also out of our reach.

I'm no expert of Ruby's open classes but from what I have <a href="http://memeagora.blogspot.com/2007/05/are-open-classes-evil.html">read</a> and remember you can override private methods, use private variables and even remove methods if you want to. We could also add methods to a specific instance of a class which we can't do using extension methods.

We therefore tend to be limited to using C#'s extension methods for applying operations directly to an object - applying different types of formatting to strings is one common use.

Before extension methods existed this type of code would typically have gone on a StringUtils class so this is a definite improvement.

We can 'add' more functional methods to a class as long as it only uses data accessible from the class' API but we haven't tended to do this so much on the projects I've worked on.

The ability to override methods added to a class away from its original definition is something that we don't have using extension methods.

As I mentioned we has some problems with this recently when trying to work out how to override some calls to HtmlHelper methods.

In this case it would have been nice to be able to open up the HtmlHelper class and change these methods. Unfortunately since they were defined as extension methods, extending HtmlHelper didn't give access to them so we ended up coming up with a solution which feels <a href="http://www.markhneedham.com/blog/2009/02/12/aspnet-mvc-preventing-xss-attacks/">a bit too hacky for my liking</a>.

As <a href="http://www.25hoursaday.com/weblog/2008/01/23/C30VsRubyThoughtsOnExtensionMethodsAndOpenClasses.aspx">Dare Obasanjo points out towards the end of his post</a> we also don't have the ability to create extension properties. Seeing as properties are compiled to get/set methods under the hood I wouldn't have thought it would be that difficult to add this in the next release.

Overall though extension methods are a nice addition but they still don't quite give us the full power that open classes would provide.

