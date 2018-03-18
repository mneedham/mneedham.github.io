+++
draft = false
date="2013-08-22 21:26:10"
title="Model to answer your questions rather than modelling reality"
tag=['modeling']
category=['Software Development', 'neo4j']
+++

<p>On the recommendation of <a href="https://twitter.com/iansrobinson">Ian Robinson</a> I've been reading the 2nd edition of William's Kent's '<a href="http://www.waterstones.com/waterstonesweb/products/william+kent/data+and+reality/5270709/">Data and Reality</a>' and the author makes an interesting observation at the end of the first chapter which resonated with me:</p>


<blockquote>
Once more: we are not modelling reality, but the way information about reality is processed, by people.
</blockquote>

<p>It reminds me of similar advice in Eric Evans' <a href="http://www.amazon.co.uk/Domain-driven-Design-Tackling-Complexity-Software/dp/0321125215">Domain Driven Design</a> and it's advice which I believe is helpful when designing a model in a graph database.</p>


<p>Last year I wrote a post explaining how I'd be using an approach of <a href="http://www.markhneedham.com/blog/2012/05/05/neo4j-what-question-do-you-want-to-answer/">defining questions that I wanted to ask</a> before modelling my data and in <a href="http://www.neo4j.org/">neo4j</a> land we can do this by writing <a href="http://docs.neo4j.org/chunked/snapshot/cypher-query-lang.html">cypher</a> queries up front.</p>


<p>We can then play around with increasing the size of our data set in different ways to check that our queries are still performant and tweak our model if necessary.</p>


<p>For example one simple optimisation would be to run an offline query to <a href="http://www.markhneedham.com/blog/2012/07/21/neo4j-embracing-the-sub-graph/">make implicit relationships explicit</a>.</p>


<p>Although graphs are very <a href="http://neo4j.rubyforge.org/guides/why_graph_db.html">whiteboard friendly</a> and it can be tempting to design our whole model before writing any queries this often causes problems later on.</p>


<p>When we eventually get to asking questions of our data we may find that we've modelled some things unnecessarily or have designed the model in a way that leads to inefficient queries.</p>


<p>I've found an effective approach is to <strong>keep the feedback loop tight</strong> by minimising the amount of time between drawing parts of our model on a whiteboard and writing queries against it.</p>


<p>If you're interested in learning more, Ian has <a href="http://flex.winfxpro.info/download/?noderef=workspace://SpacesStore/c1d32b3e-67f1-4f0d-b5b9-b055ebdf9444">a slide deck from a talk he did at JAX 2013</a> which covers this idea and others when building out graph database applications.</p>

