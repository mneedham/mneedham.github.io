+++
draft = false
date="2008-10-22 22:00:33"
title="Tomcat - No caching of RESTlet resources for Firefox"
tag=['no-cache', 'tomcat', 'no-store']
category=['Java']
+++

One problem that we've been trying to solve today is how to make a <a href="http://www.restlet.org/">RESTlet</a> resource non cacheable.

The reason for this is that when a user logs out of the system and then hits the back button they shouldn't be able to see that page, but instead should see the login form.

After several hours of trawling Google and trying out various different suggestions we <a href="http://www.experts-exchange.com/Software/Server_Software/Web_Servers/Apache/Q_20880931.html?qid=20880931">came across the idea</a> of setting 'cache-control' with the value 'no-store' in the response headers.

The code to make this happen is as follows (use inside a class which extends <a href="http://www.restlet.org/documentation/1.0/api/org/restlet/resource/Resource.html">Resource</a>):


~~~java

HttpResponse response = (HttpResponse) getResponse();
Series<Parameter> headers = response.getHttpCall().getResponseHeaders();
headers.add("cache-control", "no-store");
~~~

The important part in this example is the last line. As long as it's added to the Http Response Headers that response should no longer be cached.

A bit of research revealed that Internet Explorer may change the 'no-store' value to 'no-cache' so I'm not sure if this will work for that browser.
