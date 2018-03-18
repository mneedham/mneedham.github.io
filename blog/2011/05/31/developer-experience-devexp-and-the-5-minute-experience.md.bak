+++
draft = false
date="2011-05-31 21:29:18"
title="Developer Experience (#devexp) and the 5 minute experience"
tag=['software-development', 'devexp']
category=['Software Development']
+++

My former colleague Ade Oshineye recently linked me to <a href="http://blog.oshineye.com/2011/05/what-is-devexp.html">a post he's written about Developer Experience (#devexp)</a> which is described as:

<blockquote>
[...] an aspirational movement that seeks to apply the techniques of User Experience (UX) professionals to the tools and services that we offer to developers."
</blockquote>

I think it's quite an interesting idea and I particularly like two of the ideas suggested:

<blockquote>
<strong>2. Focus on the '5 minute Out Of Box experience'</strong>

The idea here is that if you provide a library, developers should be able to go from downloading to "Hello World" in 5 minutes.
</blockquote>

<blockquote>
<strong>4. Try to "design away" common problems rather than documenting workarounds</strong>

For instance if your users struggle with getting OAuth working then create abstractions that handle it for them rather than documenting the 6 most common problems or writing up the 'simple 12 step process' for getting it working. 
</blockquote>

I've written before about the value of the '<a href="http://www.markhneedham.com/blog/2008/10/19/build-checkout-and-go/">checkout and go</a>' approach for helping new developers get their machine setup and I think the aim should be that a developer just has to execute one line on the terminal and it should take care of everything.

This applies to more than just the initial setup of the environment. We should be looking to automate tasks which have a lot of manual steps and are therefore prone to error.

On a project I worked on last year it was taking people several hours to get their local Solr instances setup with production like data because the data needed to be retrieved from 4/5 different locations and then run through different extraction scripts.

Scripting all this helped to save a lot of time and it was actually quite fun to see it all getting setup automatically in front of your eyes.

One of the common things I see is people writing steps on a wiki for how to set something and giving links for where various artifacts can be downloaded from.

It's much more useful to script that type of thing!

curl and wget give us a quick and dirty way of downloading artifacts and of course we can use <a href="http://wiki.opscode.com/display/chef/FAQ">Chef</a> or <a href="http://www.puppetlabs.com/">Puppet</a> if things get more complicated.

Despite all this automation there's always seemed to be one manual step whereby the developer would have to go and download the setup script from a wiki or be sent it as an email attachment.

I came across a couple of neat ways of getting around this on two open source projects.

<a href="https://rvm.beginrescueend.com/">RVM</a> makes use of <a href="http://tldp.org/LDP/abs/html/process-sub.html">process substitution</a> to send a shell script to 'bash':


~~~text

bash < <(curl -s https://rvm.beginrescueend.com/install/rvm)
~~~

While <a href="https://github.com/carlhuda/janus">Janus</a> achieves a similar affect by piping to 'sh':


~~~text

curl https://github.com/carlhuda/janus/raw/master/bootstrap.sh -o - | sh
~~~

We're looking to do something like this on my current project so that setting up a new machine is as simple as running one line from the terminal.
