+++
draft = false
date="2010-12-12 08:11:31"
title="Distributed Agile: Other observations"
tag=['distributed-agile-2']
category=['Distributed Agile']
+++

Some of the difficulties of working in an offshore environment were clear to me before I even came to India but I've come across a few others lately which I either didn't think about before or didn't realise how annoying they were!

<h3>Getting data from the client's network</h3>
For several of the stories that we've been working on lately we needed to make use of huge amounts of reference data residing on the client's network.

If we were working in the same building then it would be very quick to download that and use it for whatever we needed.

Working offshore we've been downloading those dumps via scp which can take around 5 hours for a 300 MB file.

I don't know a lot about networks but I'm told that it would be possible to create a direct VPN between our office and the client's which would allow the transfer of this type of data to be much quicker.

<h3>Dealing with internal IP addresses</h3>
Since we're working on a different network any IP addresses for test environments of external systems aren't directly accessible.

We have a box setup in our office connected via a VPN to the client's network which forwards requests we make to local IP addresses to the equivalent IPs on the client's network.

There have been several occasions when there have been internal IP addresses hard coded in our configuration files and we've completely forgotten that we need to create an equivalent local address.

It's not a big time waster but it's something you wouldn't have to think about if working in the client's office.

<h3>Slowness of the feedback cycle</h3>
It's obvious that if the client is in a different country to you that there will be less face to face communication but I didn't realise how frustrating that would be.

If you have an observation about a piece of functionality and the offshore BAs don't have the answer then you'll most likely have to wait 5/6 hours to speak to someone onshore about it or write your thoughts in an email.

While both of those are viable options I find my motivation to express my opinion is much lower if I can't get feedback straight away.

As a result of this communication lag I think that we spend more time building functionality which doesn't necessarily add a lot of value.
