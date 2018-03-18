+++
draft = false
date="2008-12-28 00:19:13"
title="Internal/External Domain Models"
tag=['ddd', 'domain-model', 'soa']
category=['Domain Driven Design']
+++

One of the underlying characteristic of most of the projects I have worked on is that we have defined our own domain model.

On my current project due to the fact that most of the logic in the system is being handled through other services we decided to use <a href="http://hotmail.com/">WCF</a> messages as the domain model, meaning that our domain model is being defined externally by the team defining the message contracts.

<h3>Internal Domain Model</h3>
This is the approach I have seen on my previous projects and if our system does have some level of business logic/behaviour in then it is the approach we want to take if we are following a domain driven approach.

We can then make use of an <a href="http://moffdub.wordpress.com/2008/09/21/anatomy-of-an-anti-corruption-layer-part-1/">anti corruption</a> <a href="http://www.domaindrivendesign.org/practitioner_reports/peng_sam_2007_06.pdf">layer</a> to ensure that incoming data from other systems is converted into a format that had meaning in our domain before we made use of it.

If we don't have sufficient behaviour then the anti corruption layer will start to become a burden for the benefit it provides and we might be better off not defining our own domain model.

<h3>External Domain Model</h3>
The reason you might decide to take the approach we have chosen is if the domain in our system is the same as that defined elsewhere, in which case the mapping code would not be adding much value.

The problem with this approach is that we don't have control over the messages and when changes are made to it our code breaks all over the place. I guess one way to try and overcome this problem would be to use <a href="http://iansrobinson.com/2008/03/22/consumer-driven-contracts-a-retrospective/">consumer driven contracts</a>.

An additional problem is that it is quite difficult to change the domain when we learn new information since this would require changing the message definitions which are being done by another team. The domain model we have therefore seems less expressive than ones on other projects I've worked on and I don't think we achieve the <a href="http://domaindrivendesign.org/discussion/messageboardarchive/UbiquitousLanguage.html">ubiquitous language</a> as much although certainly the domain terms exist in the code.

<h3>Overall</h3>
Both of these approaches have their merits and each may be appropriate given the right situation.

From my experience the majority of the time we will want to build our own domain model of rich objects. I actually think coding is much more fun when you have your own domain model.

I've started to come to the conclusion, while writing this, that if your domain is defined as message contracts then maybe it's not Domain Driven Design at all, perhaps it's more about SOA with a Ubiquitous language.

It does feel to me like some of the aspects of DDD are present though, just not all of them.
