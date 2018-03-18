+++
draft = false
date="2014-08-17 12:21:15"
title="Ruby: Receive JSON in request body"
tag=['ruby']
category=['Ruby']
+++

<p>I've been building a little <a href="http://www.sinatrarb.com/intro.html">Sinatra</a> app to play around with the Google Drive API and one thing I struggled with was processing JSON posted in the request body.</p>


<p>I came across a few posts which suggested that the request body would be available as <cite>params['data']</cite> or <cite>request['data']</cite> but after trying several ways of sending a POST request that doesn't seem to be the case.</p>


<p>I eventually came across <a href="http://stackoverflow.com/questions/17049569/how-to-parse-json-request-body-in-sinatra-just-once-and-expose-it-to-all-routes">this StackOverflow post</a> which shows how to do it:</p>



~~~ruby

require 'sinatra'
require 'json'

post '/somewhere/' do
  request.body.rewind
  request_payload = JSON.parse request.body.read

  p request_payload

  "win"
end
~~~

<p>I can then POST to that endpoint and see the JSON printed back on the console:</p>


<cite>dummy.json</cite>

~~~json

{"i": "am json"}

~~~


~~~bash

$ curl -H "Content-Type: application/json" -XPOST http://localhost:9393/somewhere/ -d @dummy.json
~~~


~~~text

{"i"=>"am json"}
~~~

<p>Of course if I'd just <a href="http://www.sinatrarb.com/intro.html">RTFM</a> I could have found this out much more quickly!</p>

