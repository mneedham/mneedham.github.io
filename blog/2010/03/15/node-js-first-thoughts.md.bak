+++
draft = false
date="2010-03-15 00:09:47"
title="node.js: First thoughts"
tag=['javascript']
category=['Javascript']
+++

I recently came across <a href="http://nodejs.org/">node.js</a> via <a href="http://www.pgrs.net/2010/2/28/node-js-redis-and-resque">a blog post by Paul Gross</a> and I've been playing around with it a bit over the weekend trying to hook up some code to call through to the Twitter API and then return the tweets on my friend timeline.

node.js gives us event driven I/O using JavaScript running server side on top of <a href="http://code.google.com/p/v8/">Google's V8 JavaScript engine</a>.

Simon Willison has <a href="http://www.slideshare.net/simon/evented-io-based-web-servers-explained-using-bunnies - Simon Willison's talk">part of a presentation on slideshare</a> where he describes the difference between the typical thread per request approach and the event based approach to dealing with web requests using the metaphor of bunnies. He also has <a href="http://simonwillison.net/2009/Nov/23/node/">a blog post where he describes this is more detail</a>.

Another resource I found useful is <a href="http://jsconfeu.blip.tv/file/2899135/">a video from jsconf.eu</a> where the creator of node.js, Ryan Dahl, explains the philosophy behind event driven I/O and gives several examples using node.js.

These are some of my thoughts so far:

<ul>
<li>I'm not used to have <a href="http://en.wikipedia.org/wiki/Event-driven_programming">so many callbacks spread all around the code</a> and I'm still getting used to the idea that they aren't executed until the event actually happens! 

I often find myself looking at a piece of code and not understanding how it can possibly work because I'm assuming that the function passed in is executed immediately when in fact it isn't.
</li>
<li>If you make a web request the response comes back in chunks so the callback we setup to capture the response will be called multiple times with different parts of the response message.

For example I have this code to call Twitter and return all my friends' status updates:


~~~javascript

var sys = require("sys"),
    http = require('http')

exports.getTweets = function(callBack) {
    var twitter = http.createClient(80, "www.twitter.com");
    var request = twitter.request("GET", "/statuses/friends_timeline.json",
                                  {"host": "www.twitter.com",
                                   "Authorization" : "Basic " + "xxx"});

    request.addListener('response', function (response) {
        var tweets = "";

        response.addListener("data", function (chunk) {
            tweets += chunk;
        });

        response.addListener("end", function() {
            callBack.call(this, tweets);
        });
    });

    request.close();
};
~~~

I originally thought that the listener for 'data' would only be called once but it gets called 8 times sometimes so that I've created the 'tweets' variable which allows us to wait until we have the full response before firing the callback when the 'end' event is fired.

I'm not sure whether I'm missing the point a bit by doing this and I think I possibly need to get more used to designing functions which can deal with streams rather than expecting to have all of the data.</li>
<li>It seems like node.js would be perfect for a version of <a href="http://code.google.com/p/http-impersonator/">my colleagues Julio Maia and Fabio Lessa's  http-impersonator</a> which is a Java application used to record and replay requests/responses made across http-based protocols.

I haven't quite worked out the best way to test the above code - ideally I want to stub out the HTTP request so that the test doesn't have to go across the wire. Micheil Smith pointed me towards <a href="http://fakeweb.rubyforge.org/">fakeweb</a> which allows the faking of HTTP requests/responses in Ruby so I'll probably have a go at creating something similar. </li>
</ul>

So far node.js seems really cool and writing code using it is really fun. I'm still not sure exactly where it will fit in some of the architectures that I've worked on but the model it encourages feels really natural to work with.
