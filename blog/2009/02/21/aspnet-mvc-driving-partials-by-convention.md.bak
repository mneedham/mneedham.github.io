+++
draft = false
date="2009-02-21 10:39:49"
title="ASP.NET MVC: Driving partials by convention"
tag=['aspnet-mvc']
category=['.NET']
+++

I like to have conventions in the code I write - I find it makes the code i write much cleaner which still providing flexibility. 

One of the conventions that Jeremy Miller coined for working with ASP.NET MVC applications is that of using one model per controller method aka <a href="http://codebetter.com/blogs/jeremy.miller/archive/2008/10/23/our-opinions-on-the-asp-net-mvc-introducing-the-thunderdome-principle.aspx">"The Thunderdome principle"</a>. I think we can take this further by having one model per <a href="http://bradwilson.typepad.com/blog/2008/08/partial-renderi.html">partial</a> that we use inside our views.

The benefit of having a model especially for a partial is that we remove confusion about data available to populate our controls by restricting the amount of data we actually have. It also makes more sense from a conceptual point of view.

Given this approach it started to become quite annoying having to type the following code all the time.


~~~csharp

<% Html.RenderPartial("_Foo", new FooModel()); %>
~~~

We realised that a neater approach would be if we could just pass in the model and it would work out which partial needed to be rendered, assuming the convention that each model is only used on one partial.

We are using strongly typed models on our views so the code behind in each of the partials extends ViewPage<T>, making it possible to work out the partial we want to load by looking up the model.


~~~csharp

public static class HtmlHelperExtensions
{
    public static void RenderPartialFrom(this HtmlHelper htmlHelper,  object model)
    {
        var thePartial = FindMeThePartial(model);
        htmlHelper.RenderPartial(thePartial, model);
    }

    private static string FindMeThePartial<T>(T model) where T : class
    {
        var projectAssembly = Assembly.Load("Project");
        var types = projectAssembly.GetTypes();

        foreach (var type in types)
        {
            if (type.BaseType == typeof(ViewPage<T>))
            {
                return type.Name;
            }
        }
        return string.Empty;
    }
}
~~~

You can then refer to this in views like so:


~~~csharp

<% Html.RenderPartialFrom(new FooModel()); %>
~~~

Obviously it takes the first result it finds, so the convention we have is that each model should only be used on one partial which I think is a reasonable idea.
