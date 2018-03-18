+++
draft = false
date="2011-04-09 10:54:59"
title="HTML encoding/escaping with StringTemplate and Spring MVC"
tag=['software-development']
category=['Software Development']
+++

Last week my colleague T.C. and I had to work out how to HTML encode the values entered by the user when redisplaying those onto the page to prevent a cross site scripting attack on the website.

I wrote a blog post a couple of years ago <a href="http://www.markhneedham.com/blog/2009/02/12/aspnet-mvc-preventing-xss-attacks/">describing how to do this in ASP.NET MVC</a> and the general idea is that we need to have a custom renderer which HTML encodes any strings that pass through it.

In our case this means that we needed to write a custom renderer for String Template and hook that into Spring MVC.

We already had a view class <cite>StringTemplateView</cite> so we needed to add to that class and add our custom renderer.

The viewResolver was defined like so:


~~~java

    @Bean
    public ViewResolver viewResolver() {
        InternalResourceViewResolver viewResolver = new InternalResourceViewResolver();
        viewResolver.setPrefix("/WEB-INF/templates/");
        viewResolver.setViewClass(StringTemplateView.class);
        viewResolver.setSuffix(".st");
        return viewResolver;
    }
~~~

And after some guidance from <a href="http://twitter.com/jimbarritt">Jim</a> we changed <cite>StringTemplateView</cite> to look like this:


~~~java

public class StringTemplateView extends InternalResourceView {

    @Override
    protected void renderMergedOutputModel(Map<String, Object> model, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String templateRootDir = format("%s/WEB-INF/templates", getServletContext().getRealPath("/"));

        StringTemplateGroup group = new StringTemplateGroup("view", templateRootDir);
        StringTemplate template = group.getInstanceOf(getBeanName());

        AttributeRenderer htmlEncodedRenderer = new HtmlEncodedRenderer();
        template.registerRenderer(String.class,  htmlEncodedRenderer);

	...
    }
	
    private class HtmlEncodedRenderer implements AttributeRenderer {
        @Override
        public String toString(Object o) {
            return HtmlUtils.htmlEscape(o.toString());
        }

        @Override
        public String toString(Object o, String formatName) {
            return HtmlUtils.htmlEscape(o.toString());
        }
    }
}
~~~

At the moment we want to HTML encode everything that we render through StringTemplate but if that changes then we could <a href="http://www.antlr.org/wiki/display/ST/Object+rendering">make use of the formatName parameter</a> which we're currently ignoring.

In retrospect this looks pretty simple to do but my Googling skills were pretty much failing me at the time so I thought it'd be good to document.
