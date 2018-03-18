+++
draft = false
date="2011-04-07 19:18:04"
title="Unix: Getting the sound from 'say' as a wav file"
tag=['software-development']
category=['Software Development']
+++

I spent a bit of time yesterday afternoon working out how to get the output from the Unix command 'say' to be played whenever our build breaks.

We're using <a href="http://ccnet.sourceforge.net/CCNET/CCTray.html">cctray</a> on a Windows box for that purpose which means that we need to have the file in the 'wav' format.

Unfortunately 'say' doesn't seem to be able to output a file in that format:


~~~text

> say "WARNING! Drainage has occurred, please fix it. Drainage has occurred, please fix it." --output-file drain.wav

Opening output file failed: fmt?
~~~

So I first converted it into a 'wmv':


~~~text

> say "WARNING! Drainage has occurred, please fix it. Drainage has occurred, please fix it." --output-file drain.wmv
~~~

And then converted it into a 'wav' via <a href="http://media.io/">media.io</a>.

Sadly media.io doesn't seem to have an API so I can't fully automate it. 

If anyone knows a service that does have an API let me know!
