+++
draft = false
date="2009-03-30 22:52:52"
title="DDD: Recognising relationships between bounded contexts"
tag=['ddd', 'domain-driven-design']
category=['Domain Driven Design']
+++

One of the <a href="http://www.markhneedham.com/blog/category/qcon/">big takeaways for me</a> from the <a href="http://qconlondon.com/london-2009/tracks/show_track.jsp?trackOID=228">Domain Driven Design track</a> at the recent <a href="http://qconlondon.com/">QCon London</a> conference was that the organisational patterns in the second half of the book are probably more important than the actual patterns themselves.

There are various patterns used to describe the relationships between different <a href="http://www.markhneedham.com/blog/2009/03/07/ddd-bounded-contexts/">bounded contexts</a>:

<ul>
<li><strong>Shared Kernel</strong> - This is where two teams share some subset of the domain model. This shouldn't be changed without the other team being consulted.</li>
<li><strong>Customer/Supplier Development Teams</strong> - This is where the downstream team acts as a customer to the upstream team. The teams define automated acceptance tests which validate the interface the upstream team provide. The upstream team can then make changes to their code without fear of breaking something downstream. I think this is where <a href="http://iansrobinson.com/category/consumer-driven-contracts/">Ian Robinson's Consumer Driven Contracts</a> come into play.</li>
<li><strong>Conformist</strong> - This is where the downstream team conforms to the model of the upstream team despite that model not meeting their needs. The reason for doing this is so that we will no longer need a complicated anti corruption layer between the two models. This is not the same as customer/supplier because the teams are not using a cooperative approach - the upstream are deriving the interfaces independently of what downstream teams actually need.</li>
<li><strong>Partner</strong> - This was suggested by Eric Evans during his <a href="http://www.markhneedham.com/blog/2009/03/13/qcon-london-2009-what-ive-learned-about-ddd-since-the-book-eric-evans/">QCon presentation</a>, and the idea is that two teams have a mutual dependency on each other for delivery.  They therefore need to work together on their modeling efforts.</li>
</ul>

I think it's useful for us to know which situation we are in because then we can make decisions on what we want to do while being aware of the various trade offs we will need to make.

An example of this is when we recognise that we have a <a href="http://www.markhneedham.com/blog/2008/12/28/internalexternal-domain-models/">strong dependency on the domain model of another team</a> where I think the approach that we take depends on the relationship the two teams have.

If we have a cooperative relationship between the teams then an approach where we pretty much rely on at least some part of the supplier's model  is less of an issue than if we don't have this kind of relationship. After all we have an influence on the way the model is being developed and maybe even worked on it with the other team.

On the other hand if we realise that we don't have a cooperative relationship, which may happen due to a variety of reasons...

<blockquote>
When two teams with an upstream/downstream relationship are not effectively being directed from the same source, a cooperative pattern such as CUSTOMER/SUPPLIER TEAMS is not going to work. 
...
This can be the case in a large company in which the two teams are far apart in the management hierarchy or where the shared supervisor is indifferent to the relationship of the two teams. It also arises between teams in different companies when the customer's business is not individually important to the supplier. Perhaps the supplier has many small customers, or perhaps the supplier is changing market direction and no longer values the old customers. The supplier may just be poorly run. It may have gone out of business. Whatever the reason, the reality is that the downstream is on its own.

(from the <a href="http://domaindrivendesign.org/">book</a>)
</blockquote>

...we need to be more careful about which approach we take.

We are now potentially in conformist territory although I don't think that is necessarily the route that we want to take.

If we choose to conform to the supplier's model then we need to be aware that any changes made to that model will require us to make changes all over our code and since these changes are likely to all over the place it's going to be quite expensive to make those changes. On the other hand we don't have to spend time writing translation code.

The alternative approach is to create an <a href="http://moffdub.wordpress.com/2008/09/21/anatomy-of-an-anti-corruption-layer-part-1/">anti corruption layer</a> where we interact with the other team's service and isolate all that code into one area, possibly behind a <a href="http://www.markhneedham.com/blog/2009/03/10/ddd-repository-not-only-for-databases/">repository</a>. The benefit here is that we can isolate all changes in the supplier's model in one place which from experience saves a lot of time, the disadvantage of course being that we have to write a lot of translation code which can get a bit tricky at times. The supplier's model still influences our approach but it isn't our approach.

I'm not sure what pattern this would be defined as - it doesn't seem to fit directly into any of the above as far as I can see but I think it's probably quite common in most organisations.

There are always multiple approaches to take to solve a problem but I think it's useful to know what situation we have before choosing our approach.
