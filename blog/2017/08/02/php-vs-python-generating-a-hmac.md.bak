+++
draft = false
date="2017-08-02 06:09:10"
title="PHP vs Python: Generating a HMAC"
tag=['python', 'php']
category=['Python']
description="In this post I show how to generate a Base 64 encoded HMAC using Python and compare it to the same code in PHP."
+++

<p>

I've been writing a bit of code to integrate with a ClassMarker webhook, and you're required to check that an incoming request actually came from ClassMarker by <a href="https://www.classmarker.com/online-testing/api/webhooks/#verify">checking the value of a base64 hash using HMAC SHA256</a>.
</p>


<p>

The example in the documentation is written in PHP which I haven't done for about 10 years so I had to figure out how to do the same thing in Python.
</p>


<p>
This is the PHP version:
</p>



~~~bash

$ php -a
php > echo base64_encode(hash_hmac("sha256", "my data", "my_secret", true));
vyniKpNSlxu4AfTgSJImt+j+pRx7v6m+YBobfKsoGhE=
~~~

<p>
The Python equivalent is a <a href="https://stackoverflow.com/a/1306575">bit more code</a> but it's not too bad.
</p>


<h3>
Import all the libraries
</h3>


~~~python

import hmac
import hashlib
import base64
~~~

<h3>
Generate that hash
</h3>



~~~bash

data = "my data".encode("utf-8")
digest = hmac.new(b"my_secret", data, digestmod=hashlib.sha256).digest()

print(base64.b64encode(digest).decode())
'vyniKpNSlxu4AfTgSJImt+j+pRx7v6m+YBobfKsoGhE='
~~~

<p>
We're getting the same value as the PHP version so it's good times all round. 
</p>

