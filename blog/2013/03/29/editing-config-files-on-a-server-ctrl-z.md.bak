+++
draft = false
date="2013-03-29 10:51:37"
title="Editing config files on a server & Ctrl-Z"
tag=['software-development']
category=['Software Development']
+++

<p>A couple of weeks ago <a href="https://twitter.com/timrgoodwin">Tim</a> and I were spinning up a new service on a machine which wasn't quite working so we were manually making changes to the <cite>/etc/nginx/nginx.conf</cite> file and restarting nginx to try and sort it out.</p>


<p>This process is generally not that interesting - you open the file in vi, make some changes, close it, then restart nginx and see if it works. If not then you open the file again and repeat.</p>


<p>Except Tim had a slight variation on this workflow which is an improvement that I don't want to forget!</p>


<p>Once we'd finished making the changes to the file in vi Tim hit '<a href="http://en.wikipedia.org/wiki/Control-Z">Ctrl + Z</a>' which suspended the vi process and put us back at the shell prompt.</p>


<p>We could then restart nginx or do whatever else we needed to do and then type '<a href="http://en.wikipedia.org/wiki/Fg_(Unix)">fg</a>' to go back into vi again.</p>


<p>Not only is this workflow quicker, it also keeps the history of the changes that we've made to the file so if one of our changes really screws things up we can easily undo it. Previously we'd have to remember what changes we'd made and do that manually.</p>


<p>In summary this workflow is a pretty simple idea but nevertheless one I had never thought about or seen anyone else do and I'll be using it in future.</p>

