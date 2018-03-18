+++
draft = false
date="2013-04-10 07:03:15"
title="awk: Parsing 'free -m' output to get memory usage/consumption"
tag=['unix']
category=['Shell Scripting']
+++

<p>Although I know this problem is already solved by <a href="http://collectd.org/">collectd</a> and <a href="http://newrelic.com/">New Relic</a> I wanted to write a little shell script that showed me the memory usage on a bunch of VMs by parsing the output of <cite><a href="http://linux.about.com/library/cmd/blcmdl1_free.htm">free</a></cite>.</p>


<p>The output I was playing with looks like this:</p>



~~~text

$ free -m
             total       used       free     shared    buffers     cached
Mem:           365        360          5          0         59         97
-/+ buffers/cache:        203        161
Swap:          767         13        754
~~~

<p>I wanted to find out what % of the memory on the machine was being used and as I understand it the numbers that we would use to calculate this are the 'total' value on the 'Mem' line and the 'used' value on the 'buffers/cache' line.</p>


<p>I initially thought that the 'used' value I was interested in should be the one on the 'Mem' line but this number includes memory that <a href="http://www.linuxatemyram.com/index.html">Linux has borrowed for disk caching</a> so it isn't the true number.</p>
 

<p>There's another <a href="http://www.linuxatemyram.com/play.html">quite interesting article showing some experiments you can do</a> to prove this.</p>


<p>So what I wanted to do was get the result of the calculation '203/365' which I wasn't sure how to do until I realised you can match multiple regular expressions with awk like so:</p>



~~~text

$ free -m | awk '/Mem:/ { print $2 } /buffers\/cache/ { print $3 }'                                                        
365
203
~~~

<p>We've now filtered the output down to just our two numbers but another neat thing you can do with awk is change what it uses as its field and record separator.</p>


<p>In this case we want to change the field separator to be the new line character and we'll set the record separator to be nothing because otherwise it defaults to the new line character which will mess with our field separator.</p>


<p>Those two values are set by using <a href="http://www.thegeekstuff.com/2010/01/8-powerful-awk-built-in-variables-fs-ofs-rs-ors-nr-nf-filename-fnr/">the 'RS' and 'FS' variables</a>:</p>



~~~text

$ free -m | 
  awk '/Mem:/ { print $2 } /buffers\/cache/ { print $3 }' | 
  awk 'BEGIN { RS = "" ; FS = "\n" } { print $2 / $1 }'
0.556164
~~~

<p>This is still sub optimal because we're using two awk commands rather than one! We can get around that by storing the two memory values in variables and printing them out in an END block:</p>



~~~text

$ free -m | 
  awk '/Mem:/ { total=$2 } /buffers\/cache/ { used=$3 } END { print used/total}'
0.556164
~~~
