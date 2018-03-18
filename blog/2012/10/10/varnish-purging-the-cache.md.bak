+++
draft = false
date="2012-10-10 23:28:40"
title="Varnish: Purging the cache"
tag=['software-development', 'varnish']
category=['Software Development']
+++

We're using <a href="https://www.varnish-cache.org/">varnish</a> to cache all the requests that come through our web servers and especially in our pre-production environments we deploy quite frequently and want to see the changes that we've made.

This means that we need to purge the pages we're accessing from varnish so that it will actually pass the request through to the application server and serve up the latest version of the page.

For some reason my google-fu when trying to remember/work out how to do this has always been weak but my colleague <a href="http://www.linkedin.com/pub/shodhan-sheth/2/277/287">Shodhan</a> helped me understand how to do this today so I thought I better record it so I don't forget!

The way we've configured varnish to allow us to purge entries is similar to that described on the <a href="https://www.varnish-cache.org/docs/trunk/users-guide/purging.html">purging and banning page</a>.

We have the following code in our <cite>/etc/varnish/default.vcl</cite>:


~~~text

acl purge_acl {
  "localhost";
}

# purge individual URLs from the cache
if(req.request == "PURGE") {
  if(!client.ip ~ purge_acl) {
    error 405 "Not allowed";
  } else {
    purge("req.url == " req.url);

    error 200 "Purged";
  }
}
~~~

We only allow purging to be done if you're on the machine i.e. your IP needs to be localhost and if you pass a request method of 'PURGE' that will remove that specific URL from varnish.

Any requests made will go first through nginx before being passed onto varnish.

If we start off with a URL which is already cached:


~~~text

$ curl --insecure -I -H "Host: www.realhostgoeshere.com" https://localhost
HTTP/1.1 200 OK
Server: nginx
Date: Wed, 10 Oct 2012 23:21:36 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 12929
Connection: keep-alive
Vary: Accept-Encoding
Vary: Accept-Encoding
Vary: Accept-Encoding
Status: 200 OK
Cache-Control: max-age=1800, public
X-UA-Compatible: IE=Edge,chrome=1
ETag: "9b2569322b89a71aca8c67f5f2b3a873"
X-Request-Id: 9c783ff4386fa9a7937f31d22854dcc8
X-Varnish: 1045982044 1045982042
Via: 1.1 varnish
age: 0
X-Cache: HIT
Strict-Transport-Security: max-age=2419200
~~~

We can see that we got a varnish cache hit based on the 'X-Cache' header returned on the second last line. 

To purge the cache for the root URL we'd do this:


~~~text

$ curl --insecure -I -H "Host: www.realhostgoeshere.com" https://localhost -X PURGE
HTTP/1.1 200 Purged
Server: nginx
Date: Wed, 10 Oct 2012 23:22:46 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 449
Connection: keep-alive
Vary: Accept-Encoding
Retry-After: 0
X-Varnish: 1045982047
Age: 0
Via: 1.1 varnish
X-Cache: MISS
Strict-Transport-Security: max-age=2419200
~~~

The 200 response code tells us that we were successful with our purging although from my brief experiments it seems like you would get that response code even if you purged a URL that didn't exist!

If we hit that URL again:


~~~text

curl --insecure -I -H "Host: www.realhostgoeshere.com" https://localhost
HTTP/1.1 200 OK
Server: nginx
Date: Wed, 10 Oct 2012 23:23:17 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 12929
Connection: keep-alive
Vary: Accept-Encoding
Vary: Accept-Encoding
Vary: Accept-Encoding
Status: 200 OK
Cache-Control: max-age=1800, public
X-UA-Compatible: IE=Edge,chrome=1
ETag: "9b2569322b89a71aca8c67f5f2b3a873"
X-Request-Id: bfcf1568382ce42ee0f9d4245b23f5cd
X-Varnish: 1045982048
Via: 1.1 varnish
age: 0
X-Cache: MISS
Strict-Transport-Security: max-age=2419200
~~~

We can see that it's been purge and varnish therefore had to go and request the page from the application server. If we hit it one more time we can see that it's now cached again!


~~~text

curl --insecure -I -H "Host: www.realhostgoeshere.com" https://localhost
HTTP/1.1 200 OK
Server: nginx
Date: Wed, 10 Oct 2012 23:26:43 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 12929
Connection: keep-alive
Vary: Accept-Encoding
Vary: Accept-Encoding
Vary: Accept-Encoding
Status: 200 OK
Cache-Control: max-age=1800, public
X-UA-Compatible: IE=Edge,chrome=1
ETag: "9b2569322b89a71aca8c67f5f2b3a873"
X-Request-Id: bfcf1568382ce42ee0f9d4245b23f5cd
X-Varnish: 1045982050 1045982048
Via: 1.1 varnish
age: 0
X-Cache: HIT
Strict-Transport-Security: max-age=2419200
~~~
