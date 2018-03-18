+++
draft = false
date="2013-07-30 16:20:16"
title="s3cmd: put fails with “Connection reset by peer” for large files"
tag=['aws', 's3']
category=['Software Development']
+++

<p>I recently wanted to copy some large files from an AWS instance into an S3 bucket using <a href="http://s3tools.org/">s3cmd</a> but ended up with the following error when trying to use the 'put' command:</p>



~~~bash

$ s3cmd put /mnt/ebs/myfile.tar s3://mybucket.somewhere.com
/mnt/ebs/myfile.tar -> s3://mybucket.somewhere.com/myfile.tar  [1 of 1]
     1077248 of 12185313280     0% in    1s   937.09 kB/s  failed
WARNING: Upload failed: /myfile.tar ([Errno 104] Connection reset by peer)
WARNING: Retrying on lower speed (throttle=0.00)
WARNING: Waiting 3 sec...
/mnt/ebs/myfile.tar -> s3://mybucket.somewhere.com/myfile.tar  [1 of 1]
     1183744 of 12185313280     0% in    1s  1062.18 kB/s  failed
WARNING: Upload failed: /myfile.tar ([Errno 104] Connection reset by peer)
WARNING: Retrying on lower speed (throttle=0.01)
WARNING: Waiting 6 sec...
/mnt/ebs/myfile.tar -> s3://mybucket.somewhere.com/myfile.tar  [1 of 1]
      417792 of 12185313280     0% in    1s   378.75 kB/s  failed
WARNING: Upload failed: /myfile.tar ([Errno 104] Connection reset by peer)
WARNING: Retrying on lower speed (throttle=0.05)
WARNING: Waiting 9 sec...
/mnt/ebs/myfile.tar -> s3://mybucket.somewhere.com/myfile.tar  [1 of 1]
       94208 of 12185313280     0% in    1s    81.04 kB/s  failed
WARNING: Upload failed: /myfile.tar ([Errno 32] Broken pipe)
WARNING: Retrying on lower speed (throttle=0.25)
WARNING: Waiting 12 sec...
/mnt/ebs/myfile.tar -> s3://mybucket.somewhere.com/myfile.tar  [1 of 1]
       28672 of 12185313280     0% in    1s    18.40 kB/s  failed
WARNING: Upload failed: /myfile.tar ([Errno 32] Broken pipe)
WARNING: Retrying on lower speed (throttle=1.25)
WARNING: Waiting 15 sec...
/mnt/ebs/myfile.tar -> s3://mybucket.somewhere.com/myfile.tar  [1 of 1]
       12288 of 12185313280     0% in    2s     4.41 kB/s  failed
ERROR: Upload of '/mnt/ebs/myfile.tar' failed too many times. Skipping that file.
~~~

<p>I tried with a smaller file just to make sure I wasn't doing anything stupid syntax wise and that transferred without a problem which lead me to believe the problem might be when uploading larger files - the one I was uploading was around ~10GB in size.</p>


<p>I eventually came across <a href="http://serverfault.com/questions/514861/s3put-fails-with-connection-reset-by-peer-for-large-files">this StackOverflow thread</a> which suggested that files >5GB in size need to make use of the 'multi part method' which was released in <a href="http://s3tools.org/s3cmd-110b2-released">version 1.1.0 of s3cmd</a>.</p>


<p>The Ubuntu repository comes with version 1.0.0 so I needed to find a way of getting a newer version onto the machine.</p>


<p>I eventually ended up downloading <a href="http://sourceforge.net/projects/s3tools/files/s3cmd/1.5.0-alpha3/">version 1.5.0 from sourceforge</a> but I couldn't get a direct URI to download it so I ended up downloading it to my machine, uploading to the S3 bucket through the web UI and then pulling it back down again using a 's3cmd get'. #epic</p>


<p>In retrospect the <a href="https://launchpad.net/ubuntu/+source/s3cmd">s3cmd PPA</a> might have been a better option.</p>


<p>Anyway, when I used this s3cmd it uploaded using multi part fine:</p>



~~~bash

...
/mnt/ebs/myfile.tar -> s3://mybucket.somewhere.com/myfile.tar  [part 761 of 775, 15MB]
 15728640 of 15728640   100% in    3s     4.12 MB/s  done
/mnt/ebs/myfile.tar -> s3://mybucket.somewhere.com/myfile.tar  [part 762 of 775, 15MB]
...
~~~
