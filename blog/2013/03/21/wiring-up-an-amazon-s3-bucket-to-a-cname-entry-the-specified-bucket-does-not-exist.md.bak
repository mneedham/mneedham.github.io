+++
draft = false
date="2013-03-21 22:39:02"
title="Wiring up an Amazon S3 bucket to a CNAME entry - The specified bucket does not exist"
tag=['software-development', 'aws']
category=['Software Development']
+++

<p><a href="https://twitter.com/jasonneylon">Jason</a> and I were setting up an internal static website using an <a href="http://aws.amazon.com/s3/">S3</a> bucket a couple of days ago and wanted to point a more friendly domain name at it.</p>


<p>We initially called our bucket 'static-site' and then created a <a href="http://en.wikipedia.org/wiki/CNAME_record">CNAME</a> entry using <a href="http://www.zerigo.com/">zerigo</a> to point our sub domain at the bucket.</p>


<p>The mapping was something like this:</p>



~~~text

our-subdomain.somedomain.com -> static-site.s3-website-eu-west-1.amazonaws.com
~~~

<p>When we tried to access the site through our-subdomain.somedomain.com we got the following error:</p>



~~~text

<Error>
<Code>NoSuchBucket</Code>
<Message>The specified bucket does not exist</Message>
<BucketName></BucketName>
<RequestId></RequestId>
<HostId>
~~~

<p>A bit of googling led us to <a href="https://forums.aws.amazon.com/message.jspa?messageID=237562">this thread</a> which suggested that we needed to ensure that our bucket was named after the sub domain that we wanted to serve the site from.</p>


<p>In this case we needed to rename our bucket to 'our-subdomain.somedomain.com" and then our CNAME entry to:</p>



~~~text

our-subdomain.somedomain.com -> our-subdomain.somedomain.com.s3-website-eu-west-1.amazonaws.com
~~~

<p>And then everything was happy.</p>

