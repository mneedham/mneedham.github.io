+++
draft = false
date="2013-03-31 21:44:19"
title="Embracing the logs"
tag=['logs']
category=['Software Development']
+++

<p>Despite the fact that I've been working full time in software for almost 8 years now every now and then I still need a reminder of how useful reading logs can be in helping solve problems.</p>


<p>I had a couple of such instances recently which I thought I'd document.</p>


<p>The first was a couple of weeks ago when <a href="https://twitter.com/timrgoodwin">Tim</a> and I were pairing on <a href="http://www.markhneedham.com/blog/2013/03/24/incrementally-rolling-out-machines-with-a-new-puppet-role/">moving some applications from Passenger to Unicorn</a> and were testing whether or not we'd  done so successfully.</p>


<p>We were doing this by creating an <cite>/etc/hosts</cite> entry from our top level domain to an nginx proxy node which was to forward on the request to the application server.</p>



~~~text

Request -> nginx on proxy node -> nginx on app server node -> unicorn on app server node
~~~

<p>This didn't work and we got a 404 response code so I logged onto the server hosting the application server and started writing our a cURL command to simulate what the proxy should be doing to see if the problem was there.</p>


<p>After watching me do this a couple of times Tim suggested that we might be more successful if we opened a bunch of tabs on the shell tailing the various log files that the request should pass through.</p>


<p>We set up tail commands against the following files:</p>


<ul>
<li>nginx access log on proxy node</li>
<li>nginx error log on proxy node</li>
<li>nginx access log on the app server node</li>
<li>unicorn log on the app server node</li>
</ul>

<p>Immediately it became clear that we actually had a problem on the proxy node because we'd configured one of the nginx directives incorrectly.</p>


<p>Once we'd fixed this the request flowed through smoothly.</p>


<p>We extended this tailing of files idea when testing multiple nodes through a load balancer except this time we <a href="http://www.markhneedham.com/blog/2013/01/15/fabric-tailing-log-files-on-multiple-machines/">made use of Fabric</a> to make things a bit easier.</p>


<p>The second was earlier this week when <a href="https://twitter.com/barisbalic">Baris</a> and I were trying to configure puppet so that we could install different Ruby versions on different machines.</p>


<p>We were having trouble figuring out why the wrong version was getting installed so eventually we chatted to <a href="https://twitter.com/supersheep">Andy</a> who amongst other things had a look at the apt history log @ <cite>/var/log/apt/history.log</cite> and was able to figure out how this was happening.</p>


<p>Lesson of the last two weeks: <strong>embrace the logs</strong>!</p>

