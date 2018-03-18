+++
draft = false
date="2012-08-06 21:50:07"
title="VCloud Guest Customization Script : [: postcustomization: unexpected operator"
tag=['shell-scripting-2']
category=['Shell Scripting']
+++

We have been doing some work to automatically provision machines using the VCloud API via fog and one of the things we wanted to do was <a href="http://blogs.vmware.com/vsphere/2012/06/using-a-guest-customization-script-to-tell-when-vappvm-is-ready-in-vcloud-director.html">run a custom script the first time that a node powers on</a>.

The following <a href="http://kb.vmware.com/selfservice/microsites/search.do?language=en_US&cmd=displayKC&externalId=1026614">explains how customization scripts work</a>:
<blockquote>
In vCloud Director, when setting a customization script in a virtual machine, the script:
<ul>
<li>Is called only on initial customization and force recustomization.</li>
<li>Is called with the precustomization command line parameter before out-of-box customization begins.</li>
<li>Is called with the postcustomization command line parameter after out-of-box customization finishes.</li>
<li>Needs to be a batch file for Windows virtual machines and a shell script for Unix virtual machines.</li>
</ul>
</blockquote>

We wanted the script to run only when passed the 'postcustomization' flag because our script relied on some networking configuration which hadn't yet been done in the 'precustomization' state.

We wrote something like the following script:


~~~text

#!/bin/bash
if [ x$1 == x"postcustomization" ]; then
  echo post customization
fi
~~~

Unfortunately when we provisioned the node it hadn't run any of the code within the if block and we saw the following message in <cite>/var/log/vmware-inc/customization.log</cite>:


~~~text

5: [: xpostcustomization: unexpected operator
~~~

<a href="https://twitter.com/nickstenning">Nick</a> pointed out that the <a href="http://pubs.opengroup.org/onlinepubs/9699919799/utilities/test.html#top">test</a> utility which we're using to do the comparison on the 2nd line uses a single = in the POSIX shell even though it will work with double = in the bash shell.

We thought this was pretty strange since we are telling the script to run with the bash shell in the first line.

We eventually realised that the script was being spawned out to a POSIX shell by <cite>/root/.customization/post-customize-guest.sh</cite> which is the script that gets called on power on:


~~~text

 ((${SH} $POST_CUSTOMIZATION_TMP_SCRIPT_NAME "postcustomization" > /tmp/stdout.log) 2>&1 | ${TEE} -a /tmp/stderr.log)
~~~

I created a simple script to check the theory:


~~~text

#!/bin/bash

[ "mark" == "mark" ] && echo Mark 
~~~

Which works fine when called directly:


~~~text

$ ./mark.sh 
Mark
~~~

And throws the expected error when called with 'sh':


~~~text

$ sh mark.sh 
[: 3: mark: unexpected operator
~~~


We therefore needed to change our script to do the comparison with a single = like so:


~~~text

#!/bin/bash
if [ x$1 = x"postcustomization" ]; then
  echo post customization
fi
~~~
