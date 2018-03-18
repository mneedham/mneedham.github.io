+++
draft = false
date="2015-03-29 00:31:37"
title="InetAddressImpl#lookupAllHostAddr slow/hangs"
tag=['software-development']
category=['Software Development']
+++

<p>
Since I upgraded to Yosemite I've noticed that attempts to resolve localhost on my home network have been taking ages (sometimes over a minute) so I thought I'd try and work out why.
</p>


<p>
This is what my initial <cite>/etc/hosts</cite> file looked like based on the assumption that my machine's hostname was <cite>teetotal</cite>:
</p>



~~~bash

$ cat /etc/hosts
##
# Host Database
#
# localhost is used to configure the loopback interface
# when the system is booting.  Do not change this entry.
##
127.0.0.1	localhost
255.255.255.255	broadcasthost
::1             localhost
#fe80::1%lo0	localhost
127.0.0.1	wuqour.local
127.0.0.1       teetotal
~~~

<p>
I setup a little test which replicated the problem:
</p>



~~~java

import java.net.InetAddress;
import java.net.UnknownHostException;

public class LocalhostResolution
{
    public static void main( String[] args ) throws UnknownHostException
    {
        long start = System.currentTimeMillis();
        InetAddress localHost = InetAddress.getLocalHost();
        System.out.println(localHost);
        System.out.println(System.currentTimeMillis() - start);
    }
}
~~~

<p>which has the following output:</p>



~~~text

Exception in thread "main" java.net.UnknownHostException: teetotal-2: teetotal-2: nodename nor servname provided, or not known
	at java.net.InetAddress.getLocalHost(InetAddress.java:1473)
	at LocalhostResolution.main(LocalhostResolution.java:9)
	at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
	at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:57)
	at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
	at java.lang.reflect.Method.invoke(Method.java:606)
	at com.intellij.rt.execution.application.AppMain.main(AppMain.java:134)
Caused by: java.net.UnknownHostException: teetotal-2: nodename nor servname provided, or not known
	at java.net.Inet6AddressImpl.lookupAllHostAddr(Native Method)
	at java.net.InetAddress$1.lookupAllHostAddr(InetAddress.java:901)
	at java.net.InetAddress.getAddressesFromNameService(InetAddress.java:1293)
	at java.net.InetAddress.getLocalHost(InetAddress.java:1469)
	... 6 more
~~~

<p>
Somehow my hostname has changed to <cite>teetotal-2</cite> so I added the following entry to <cite>/etc/hosts</cite>:
</p>



~~~text

127.0.0.1	teetotal-2
~~~

<p>Now if we run the program we see this output instead:</p>



~~~text

teetotal-2/127.0.0.1
5011
~~~

<p>It's still taking 5 seconds to resolve which is much longer than I'd expect. After break pointing through the code it seems like it's trying to do an IPv6 resolution rather than IPv4 so I added an <cite>/etc/hosts</cite> entry for that too:


~~~text

::1             teetotal-2
~~~

<p>Now resolution is much quicker:</p>



~~~text

teetotal-2/127.0.0.1
6
~~~

<p>Happy days!</p>

