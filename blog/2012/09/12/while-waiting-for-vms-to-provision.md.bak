+++
draft = false
date="2012-09-12 22:53:39"
title="While waiting for VMs to provision..."
tag=['shell']
category=['Shell Scripting']
+++

<a href="https://twitter.com/philandstuff">Phil</a> and I spent part of the day provisioning new virtual machines for some applications that we need to deploy which involves running a provisioning script and then opening another terminal and repeatedly trying to ssh into the box until it succeeds.

Eventually we got bored of doing that so we figured out a nice little one liner to use instead:


~~~text

while :; do ssh 10.0.0.2; done 
~~~

The ':' is a <a href="http://urchin.earth.li/~twic/Some_Bash_Scripting_Notes.html">bash noop</a> and is <a href="http://tldp.org/LDP/abs/html/special-chars.html">defined like so</a>:

<blockquote>
<strong>null command [colon].</strong> 

This is the shell equivalent of a "NOP" (no op, a do-nothing operation). It may be considered a synonym for the shell builtin true. The ":" command is itself a Bash builtin, and its exit status is true (0).
</blockquote>

In this case it helps us to create an infinite loop which exits once an ssh session is established, meaning that the machine has its ssh daemon running and is ready to roll.

Since we're using a puppet client/server setup we also want to run something on the puppet master to make sure that the client's certificate has been signed. 

Here we can use the '<a href="http://en.wikipedia.org/wiki/Watch_(Unix)">watch</a>' command to help us out:


~~~text

watch "puppet cert list -a | grep new-client-new"
~~~

So we'll see an empty screen until the client has sent a certificate request that's been picked up by the puppet master and then we'll see it come up.

As usual if you know any cooler ways to do the same things let me know in the comments!
