+++
draft = false
date="2009-05-13 07:49:44"
title="Mercurial: Pulling from behind a proxy"
tag=['mercurial', 'version-control']
category=['Version Control']
+++

I've been playing around with Mercurial and the mercurial hosting website <a href="http://bitbucket.org/">bitbucket</a> a bit this year and recently wanted to pull from a repository from behind a proxy server.

With a bit of help from the <a href="http://www.nabble.com/proxy-td21973435.html">mercurial mailing list</a> and the <a href="http://www.selenic.com/mercurial/hgrc.5.html">documentation</a> this is how I was able to pull the repository for the Hambread project I've been doing a bit of work on:



~~~text

hg --config http_proxy.host=ipOfYourProxyServer:portOfYourProxyServer --config http_proxy.user=user --config http_proxy.passwd=password pull http://bitbucket.org/markhneedham/hambread~~~

After that command a 'hg update' updates your local repository with all the changes that have just been pulled.

What I found strange was that you needed to define the '-- config' part of the command three times as far as I can tell in order to pass each of the different properties related to the proxy. 

I tried just defining it once and just setting the properties individually but that just produced errors.
