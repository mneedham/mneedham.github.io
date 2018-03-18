+++
draft = false
date="2015-11-28 13:56:59"
title="Python: Parsing a JSON HTTP chunking stream"
tag=['python']
category=['Python']
+++

<p>
I've been playing around with meetup.com's API again and this time wanted to consume the <a href="http://www.meetup.com/meetup_api/docs/stream/2/rsvps/#http">chunked HTTP RSVP stream</a> and filter RSVPs for events I'm interested in.
</p>


<p>
I use Python for most of my hacking these days and if HTTP requests are required the <a href="http://docs.python-requests.org/en/latest/">requests library</a> is my first port of call.
</p>


<p>I started out with the following script </p>



~~~python

import requests
import json

def stream_meetup_initial():
    uri = "http://stream.meetup.com/2/rsvps"
    response = requests.get(uri, stream = True)
    for chunk in response.iter_content(chunk_size = None):
        yield chunk

for raw_rsvp in stream_meetup_initial():
    print raw_rsvp
    try:
        rsvp = json.loads(raw_rsvp)
    except ValueError as e:
        print e
        continue
~~~

<p>This mostly worked but I also noticed the following error from time to time:</p>



~~~text

No JSON object could be decoded
~~~

<p>
Although less frequent, I also saw errors suggesting I was trying to parse an incomplete JSON object. I tweaked the function to keep a local buffer and only yield that if the chunk ended in a new line character:
</p>



~~~python

def stream_meetup_newline():
    uri = "http://stream.meetup.com/2/rsvps"
    response = requests.get(uri, stream = True)
    buffer = ""
    for chunk in response.iter_content(chunk_size = 1):
        if chunk.endswith("\n"):
            buffer += chunk
            yield buffer
            buffer = ""
        else:
            buffer += chunk
~~~

<p>
This mostly works although I'm sure I've seen some occasions where two JSON objects were being yielded and then the call to 'json.loads' failed. I haven't been able to reproduce that though.
</p>


<p>
A second read through the <a href="http://docs.python-requests.org/en/latest/user/advanced/#streaming-requests">requests documentation</a> made me realise I hadn't read it very carefully the first time since we can make our lives much easier by using 'iter_lines' rather than 'iter_content':
</p>



~~~python

r = requests.get('http://stream.meetup.com/2/rsvps', stream=True)
for raw_rsvp in r.iter_lines():
    if raw_rsvp:
        rsvp = json.loads(raw_rsvp)
        print rsvp
~~~

<p>
We can then process 'rsvp', filtering out the ones we're interested in.
</p>

