+++
draft = false
date="2012-09-15 09:06:02"
title="cURL and the case of the carriage return"
tag=['shell']
category=['Shell Scripting']
+++

We were doing some work this week where we needed to make a couple of calls to an API via a shell script and in the first call we wanted to capture one of the lines of the HTTP response headers and use that as in input to the second call.

The way we were doing this was something like the following:


~~~text

#!/bin/bash

# We were actually grabbing a different header but for the sake 
# of this post we'll say it was 'Set-Cookie'
AUTH_HEADER=`curl -I http://www.google.co.uk | grep Set-Cookie`

echo $AUTH_HEADER
~~~

When we echoed <cite>$AUTH_HEADER</cite> it looked exactly as we'd expect...


~~~text

$ ./blah.txt 2>/dev/null
Set-Cookie: NID=63=gwfYa4fhbdqYyEdySrFn1AYybExgjQbQUKPdC5sZ5orRznGY-bt3gTwlc0XaPXv
TxmCIyjDzKWOGBCYlOouQ5-2l7gQGOAj90VrY3LLabRqwJ5Y3zlf-dNR6Y5U3VDKw; 
expires=Sun, 17-Mar-2013 08:28:25 GMT; path=/; domain=.google.co.uk; HttpOnly
~~~

...but when we passed that value into the next cURL command it was returning a 401 response code which suggested that we hadn't even sent the header at all.

We changed the code so that we manually assigned <cite>AUTH_HEADER</cite> with the correct value and then everything worked fine which suggested there was something weird in the value we were getting back from cURL.

We were constructing the arguments to our next cURL command like so:


~~~text

#!/bin/bash

# We were actually grabbing a different header but for the sake 
# of this post we'll say it was 'Set-Cookie'
AUTH_HEADER=`curl -I http://www.google.co.uk | grep Set-Cookie`

echo $AUTH_HEADER

ARGS="-H $AUTH_HEADER OTHER RANDOM STUFF HERE"
echo $ARGS
~~~

When we ran that we noticed that <cite>$ARGS</cite> was displaying some quite strange behaviour where the text after <cite>$AUTH_HEADER</cite> was overriding the value of <cite>$AUTH_HEADER</cite>:


~~~text

$ ./blah.txt 2>/dev/null

Set-Cookie: NID=63=rma3ah7oBhyirDUqFPODHfaTK9XOqs0CPapYVgTM6vHyCgDTcXs2P_mVDI_hnsap
33E3E6k54b50J8MLc85JadBAiMdhq5HDeH-LbLqwy_hUAOj-1w-YwZOHW7okuiEy; 
expires=Sun, 17-Mar-2013 08:37:47 GMT; path=/; domain=.google.co.uk; HttpOnly

Set-Cookie: NID=63=rma3ah7oBhyirDUqFPODHfaTK9XOqs0CPapYVgTM6vHyCgDTcXs2P_mVDI_hnsap
33E3E6k54b50J8MLc85JadBAiMdhq5HDeH-LbLqwy_hUAOj-1w-YwZOHW7okuiEy; 
expires=Sun, 17-Mar-2013 08:37:47 GMT; path=/; dom RANDOM TEXT SO RANDOMpOnly
~~~

<a href="https://twitter.com/psd">Paul</a> was wondering by at the time so we asked him if he could think of anything that could be leading to what we were seeing. He suggested there was probably a <a href="http://www.maxi-pedia.com/Line+termination+line+feed+versus+carriage+return+0d0a">carriage return</a> lurking at the end of the line.

<a href="https://twitter.com/nickstenning">Nick</a> showed us how we could prove that was the case using <cite><a href="http://linuxcommand.org/man_pages/xxd1.html">xxd</a></cite>:


~~~text

xxd <<< $AUTH_HEADER
~~~

When we ran the script again we could see the carriage return character (0d) at the end of the line:


~~~text

$ ./blah.txt 2>/dev/null
Set-Cookie: NID=63=QDECY69302tLN0CSMyug-TzzczxzGNWs70i8huV60qM7BFv18F63dNSz4trqzHXvzbKXNLb
gBcLKKCTuOSTCjS6w_6UNJVrkZ6G_lLxSSyCeHaK4iJGW8XWu86i7CsOB; 
expires=Sun, 17-Mar-2013 08:55:37 GMT; path=/; domain=.google.co.uk; HttpOnly
...
0000160: 2f3b 2064 6f6d 6169 6e3d 2e67 6f6f 676c  /; domain=.googl
0000170: 652e 636f 2e75 6b3b 2048 7474 704f 6e6c  e.co.uk; HttpOnl
0000180: 790d 0d0a                                y..
~~~

Nick then showed us how to get rid of it using <cite>tr</cite> like so:


~~~text

AUTH_HEADER=`curl -I http://www.google.co.uk | grep Set-Cookie` | tr -d '\r'`
~~~
