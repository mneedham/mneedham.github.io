+++
draft = false
date="2013-08-22 22:11:35"
title="Products & Infinite configurability"
tag=['software-development']
category=['Software Development']
+++

<p>One of the common feature requests on the <a href="http://www.thoughtworks.com/">ThoughtWorks</a> projects that I worked on was that the application we were working on should be almost infinitely configurable to cover potential future use cases.</p>


<p>My experience of attempting to do this was that you ended up with an extremely complicated code base and those future use cases often didn't come to fruition.</p>


<p>It therefore made more sense to <strong>solve the problem at hand</strong> and then make the code more configurable if/when the need arose.</p>


<p>Now that I'm working on a product and associated tools I'm trying to understand whether those rules of application development apply.</p>


<p>One thing which I think makes sense is the idea of <a href="http://en.wikipedia.org/wiki/Convention_over_configuration">convention over configuration</a>, an approach that I became familiar with after working with Ruby/Rails in 2010/2011.</p>


<blockquote>
The phrase essentially means <strong>a developer only needs to specify unconventional aspects of the application</strong>.
</blockquote>

<p>Even if we do this I wonder if it goes far enough. The more things we make configurable the more complexity we add and the more opportunity for people to create themselves problems through misconfiguration.</p>


<p>Perhaps we should only make a few things configurable and have our application work out appropriate values for everything else. </p>


<p>There are a reasonable number of people using a product who don't have much interest in learning how to configure it. They <strong>just want to use it to solve a problem they have</strong> without having to think too much.</p>


<p>Although I haven't used it I'm told that <a href="http://www.azulsystems.com/products/zing/whatisit">Azul's Zing JVM</a> takes the minimal configuration approach by only requiring you to specify one parameter - the heap size - and it handles everything else for you.</p>


<p>Of course I'm still new to this so perhaps it still does make sense to default most things but allow power users full control in case their use case differs from the average one that the defaults were created for.</p>


<p>I'd be interested in hearing the opinions of people more experienced in this arena of which there are undoubtably many.</p>

