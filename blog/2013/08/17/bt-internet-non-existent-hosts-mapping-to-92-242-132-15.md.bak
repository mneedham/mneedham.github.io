+++
draft = false
date="2013-08-17 21:13:27"
title="BT Internet: Non existent hosts mapping to 92.242.132.15"
tag=['software-development']
category=['Software Development']
+++

We have a test in our code which checks for unresolvable hosts and it started failing for me because instead of throwing an UnknownHostException from the following call:


~~~java

InetAddress.getByName( "host.that.is.invalid" )
~~~

<p>I was getting back a valid although unreachable host. When I called ping it was easier to see what was going on:</p>



~~~bash

$ ping host.that.is.invalid
PING host.that.is.invalid (92.242.132.15): 56 data bytes
Request timeout for icmp_seq 0
Request timeout for icmp_seq 1
Request timeout for icmp_seq 2
~~~

<p>As you can see, that hostname is resolving to '92.242.132.15' which I thought was a bit weird but dig confirmed that this was happening:</p>



~~~bash

$ dig host.that.is.invalid

; <<>> DiG 9.8.3-P1 <<>> host.that.is.invalid
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 30043
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 0

;; QUESTION SECTION:
;host.that.is.invalid.		IN	A

;; ANSWER SECTION:
host.that.is.invalid.	300	IN	A	92.242.132.15
~~~

<p>It turns out that <a href="http://community.bt.com/t5/BB-Speed-Connection-Issues/DNS-oddity/td-p/49653">BT have plugged into DNS searches</a> and if one fails it redirects you to one of their pages instead - something I hadn't noticed before.</p>


<p>The site they direct you to is www.webaddresshelp.bt.com which contains a list of sponsored results for the search term 'host.that.is.invalid' in this case.</p>



~~~bash

$ ping www.webaddresshelp.bt.com
PING www.webaddresshelp.bt.com (92.242.134.15): 56 data bytes
~~~

<p>Luckily this can be disabled by going to <a href="">BT Web Address Help</a> and then choosing to <a href="http://preferences.webaddresshelp.bt.com/selfcare/preferences.cgi">disable BT Web Address Help</a>.</p>


<p>If we then wait a little bit for our DNS cache to clear the ping works as expected:</p>



~~~bash

$ ping host.that.is.invalid
ping: cannot resolve host.that.is.invalid: Unknown host
~~~
