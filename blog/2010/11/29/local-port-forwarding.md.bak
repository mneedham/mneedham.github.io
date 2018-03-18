+++
draft = false
date="2010-11-29 19:42:13"
title="Local port forwarding"
tag=['software-development']
category=['Software Development']
+++

A colleague and I ran into an interesting problem today which we wanted to use local port forwarding to solve.

In our environment.rb file we have a Solr instance url defined like so:


~~~ruby

SOLR_CONFIG = {
  :service_url => "http://some.internal.address:9983/solr/sco_slave_1"        
}
~~~

It's defined like that because our colleagues in Chicago have setup a Solr instance on a test environment and all the developers hit the same box.

In Pune everyone has Solr configured on their own box so we really wanted to configure that url to be 'localhost' on port '8983'.

Several other colleagues have just changed their environment.rb file and then remember not to check that in.

I always forget about that type of thing though so I wanted to find a work around.

We started by putting the following in /etc/hosts:


~~~text

127.0.0.1		some.internal.address
~~~

Having done that we needed to forward anything coming in on port 9983 to 8983 to complete the forwarding.

I think there's a proper way of doing this using iptables but we didn't want to shave the yak and hence used <a href="http://search.cpan.org/~acg/tcpforward-0.01/tcpforward">this tcpforward perl script</a>:


~~~text

./tcpforward -k -l some.internal.address:9983 -c 127.0.0.1:8983
~~~

If anyone knows a better way or the proper way to do this I'd be interesting in hearing about that but for now this does the job!
