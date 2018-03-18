+++
draft = false
date="2010-08-16 04:22:40"
title="Can we always release to production incrementally?"
tag=['devops-2']
category=['DevOps']
+++

<a href="http://continuousdelivery.com/2010/08/continuous-delivery-vs-continuous-deployment/">Jez recently linked</a> to <a href="http://timothyfitz.wordpress.com/2009/02/08/continuous-deployment/">a post written by Timothy Fitz about a year ago where he talks about the way his team use continuous delivery</a> which means that every change made to the code base goes into production immediately as long as it passes their test suite.

I've become fairly convinced recently that it should always be possible to deploy to production frequently but we recently came across a situation where it seemed like doing that wouldn't make much sense.

The project involved replacing an existing website but rebranding it at the same time. One of the key goals of the project was to create a consistent brand across the whole site.

Therefore it seemed that if we chose to incrementally deploy to production then we'd need to spend some time updating the old website so that the look and feel was the same across both versions of the site.

The overall time to finish the project would therefore be higher and the value that we'd get from actually get from putting something into production early probably wouldn't justify the extra effort that it'd take to do so.

In this situation the most effective strategy seems to be to still deploy as frequently as possible to a production like environment internally but only deploy to live when the whole thing is done.

If we're replacing the backend of an old system and the end user won't see anything different then an incremental deployment approach is certainly worthwhile but when brand consistency is the most important thing I'm not sure that it still makes sense.

As always I'd be keen to hear if anyone's done anything similar and if there are any ways around this.
