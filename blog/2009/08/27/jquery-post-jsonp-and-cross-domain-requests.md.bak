+++
draft = false
date="2009-08-27 22:39:26"
title="jQuery: $.post, 'jsonp' and cross-domain requests"
tag=['jquery']
category=['jQuery']
+++

We spent a bit of time yesterday looking through the jQuery code trying to work out why a cross domain request we were making using jQuery's '$.post' function wasn't working.

In hindsight perhaps it should have been obvious that you wouldn't be able to do that but I didn't completely understand how we were able to do cross domain requests were possible at all but we had some '$.getJson' 'jsonp' function calls around our code base which were doing just that.

The <a href="http://docs.jquery.com/Ajax/jQuery.post">jQuery documentation</a> seemed to suggest it was possible to do a 'jsonp' 'POST' request but when we tried to do so we got the following error:


~~~text

Error: uncaught exception: [Exception... "Access to restricted URI denied" code: "1012" nsresult: "0x805303f4 (NS_ERROR_DOM_BAD_URI)"
~~~

The failure was occurring in this part of the code on line 3517 inside the 'ajax' function:


~~~javascript

		// Open the socket
		// Passing null username, generates a login popup on Opera (#2865)
		if( s.username )
			xhr.open(type, s.url, s.async, s.username, s.password);
		else
			xhr.open(type, s.url, s.async);
~~~

I had initially thought that passing in 'jsonp' to the function did something clever to fool the browser into sending the Xml Http Request but actually in a <a href="http://groups.google.com/group/jquery-dev/browse_thread/thread/e7eb4a23eef342fb?pli=1">thread from the jQuery mailing list</a> from a year ago where Michael Geary explains what's actually happening:

<blockquote>
Cross-domain JSONP isn't AJAX at all. It doesn't use XMLHttpRequest. It's nothing more than a dynamic script element that loads JavaScript code.

You can't do a POST with a dynamic script element. Where would you put the POST data?

I don't know what the $.ajax code is trying to do - maybe it should fail in a more informative way. It will fail one way or another regardless. 
</blockquote>

We could see where this was being done in the jQuery code:


~~~javascript

		// If we're requesting a remote document
		// and trying to load JSON or Script with a GET
		if ( s.dataType == "script" && type == "GET" && parts
			&& ( parts[1] && parts[1] != location.protocol || parts[2] != location.host )){

			var head = document.getElementsByTagName("head")[0];
			var script = document.createElement("script");
			script.src = s.url;
			if (s.scriptCharset)
				script.charset = s.scriptCharset;

			...

			head.appendChild(script);
			...
		}
~~~

On line 3477 a script tag is dynamically added into the page and on line 3478 we set 'src' to be the url for our cross domain request.

We can see on line 3473 that this only happens if we have a 'GET' request.

It turned out for us that we were actually only doing this cross domain request on one of our early test environments and that in latter test environments we have everything running on the same domain. 

On this occasion we have decided to stop using this environment since it's not reflective of what our application will run like in production but if we wanted to do a cross domain request then we would need to make use of the '$.get' method with 'jsonp' passed as an option.

I was talking about this with Dave Yeung at our coding dojo last night and he pointed me to <a href="https://developer.mozilla.org/En/HTTP_Access_Control">an article describing how Firefox 3.5 is now supporting the 'access control for cross site requests' recommendation</a> which will <a href="http://dev.w3.org/2006/waf/access-control/">allow cross domain XHR requests to happen</a> by providing some extra header tags and then reading some additional tags sent back in the response where the server on the other domain can decide which domains are allowed to make calls to it.

I'm still learning this stuff so if anything I've said isn't accurate please point that out.
