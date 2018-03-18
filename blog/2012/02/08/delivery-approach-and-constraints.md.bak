+++
draft = false
date="2012-02-08 22:34:02"
title="Delivery approach and constraints"
tag=['software-development']
category=['Software Development']
+++

In my latest post I described an approach we'd been taking when analysing how to rewrite part of an existing system so that we could <a href="http://www.markhneedham.com/blog/2012/02/06/looking-for-the-seam/">build the new version in an incremental way</a>.

Towards the end I pointed out that we weren't actually going to be using an incremental approach as we'd initially thought which was due to a couple of constraints that we have to work under.

<h4>Hardware provisioning</h4>
One of the main reasons that we favoured an incremental approach is that we'd be able to deploy to production early which would allow us to show a quicker return on investment.

Unfortunately we later on came to learn that it takes <strong>around 6-9 months to provision production hardware</strong>.

It therefore didn't make a lot of sense to take an approach where we tried to integrate into the existing system since we wouldn't be able to deploy that work.

We're working under the assumption that in 6-9 months we'll probably be able to rewrite the whole thing and can therefore avoid the need to write the code which would allow us to integrate into the existing version.

We couldn't see any value in writing bridging code between the existing and new versions of the application if it never sees production - we'd put in all the effort for no reward.

<h4>Running two systems side by side</h4>
Even if we had been able to provision hardware in time to release incrementally we came to learn that <strong>the business would be uncomfortable with having two versions of the same application in production at the same time</strong>.

The application is used to do pricing and the worry was that the different versions might produce different results for the same inputs.

It's arguably something we may have been able to overcome if we could prove that the new version worked exactly the same as the existing one by running both applications against a set of scenarios and checking that they returned the same results.

Theoretically I suppose the first problem could also be overcome but it's a battle we've chosen to leave alone for the moment.

What I found interesting in the discussions about the way we should deliver our solution was that I'd worked under the assumption that an incremental approach was always a better approach but with these constraints it isn't.
