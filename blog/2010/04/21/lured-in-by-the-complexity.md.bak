+++
draft = false
date="2010-04-21 07:21:55"
title="Lured in by the complexity"
tag=['software-development']
category=['Software Development']
+++

We recently ran into an interesting problem when running the website we're building on our 'user replica machine' where you can access the application via a web browser running on Citrix.

The problem we were having was that the result of a post redirect get request that we were making via the <a href="http://jquery.malsup.com/form/">jQuery Form plugin</a> was failing to update the fragment of the page correctly. It looked like it was replacing it with the original HTML.

We're running on Internet Explorer 6 on that machine but it was working fine on that browser on a couple of our development machines.

We decided to temporarily change the code to not do a post request get and instead just to return the new page straight from the POST. Everything updated correctly using that approach.

Having come up with all sorts of grand theories on how the problem was somehow related to the fact that we were running through Citrix we somewhat came to/were somewhat guided on the internal mailing list by <a href="http://iansrobinson.com/">Ian Robinson</a> that the page was probably just getting cached, either by <a href="http://msdn.microsoft.com/en-us/library/aa383928%28VS.85%29.aspx">WinINet</a> or the corporate proxy, because we hadn't put a <a href="http://tools.ietf.org/html/rfc2616#section-14.9.2">'no-store' directive</a> in the headers of the response.

<blockquote>
   no-store

      The purpose of the no-store directive is to prevent the
      inadvertent release or retention of sensitive information (for
      example, on backup tapes). The no-store directive applies to the
      entire message, and MAY be sent either in a response or in a
      request. If sent in a request, a cache MUST NOT store any part of
      either this request or any response to it. If sent in a response,
      a cache MUST NOT store any part of either this response or the
      request that elicited it. This directive applies to both non-
      shared and shared caches. "MUST NOT store" in this context means
      that the cache MUST NOT intentionally store the information in
      non-volatile storage, and MUST make a best-effort attempt to
      remove the information from volatile storage as promptly as
      possible after forwarding it.

      Even when this directive is associated with a response, users
      might explicitly store such a response outside of the caching
      system (e.g., with a "Save As" dialog). History buffers MAY store
      such responses as part of their normal operation.
</blockquote>

<a href="http://stackoverflow.com/questions/1160105/asp-net-mvc-disable-browser-cache">JKG posted some code</a> defining an attribute that we can place on actions that we don't want to be cached in an ASP.NET MVC application:


~~~csharp

public class NoCache : ActionFilterAttribute, IActionFilter
{  
    public override void OnResultExecuting(ResultExecutingContext filterContext)
    {
        filterContext.HttpContext.Response.Cache.SetExpires(DateTime.UtcNow.AddDays(-1));
        filterContext.HttpContext.Response.Cache.SetValidUntilExpires(false);
        filterContext.HttpContext.Response.Cache.SetRevalidation(HttpCacheRevalidation.AllCaches);
        filterContext.HttpContext.Response.Cache.SetCacheability(HttpCacheability.NoCache);
        filterContext.HttpContext.Response.Cache.SetNoStore();

        base.OnResultExecuting(filterContext);
    }

    public override void OnResultExecuted(ResultExecutedContext filterContext)
    {
        base.OnResultExecuted(filterContext);
    }
}
~~~

We put that code in and the page started refreshing correctly. 

<a href="http://chrisleishman.com/">Chris Leishman</a> pointed out that another approach would be to make use of '<a href="http://en.wikipedia.org/wiki/HTTP_ETag">ETags</a>' on the response header so that the page would only be retrieved from the server if it had actually changed.

Either way we found it amusing that we automatically assumed something complicated was going wrong when actually it was anything but!
