+++
draft = false
date="2016-06-01 05:53:38"
title="Unix parallel: Populating all the USB sticks"
tag=['shell-scripting-2']
category=['Shell Scripting']
+++

<p>
The day before Graph Connect Europe 2016 we needed to create a bunch of USB sticks containing Neo4j and the training materials and eventually iterated our way to a half decent approach which made use of the <a href="https://www.gnu.org/software/parallel/parallel_tutorial.html">GNU parallel command</a> which I've always wanted to use!
</p>


<P>
But first I needed to get a USB hub so I could do lots of them at the same time. I bought the <a href="https://www.amazon.co.uk/gp/product/B00ID270ZU/ref=oh_aui_detailpage_o08_s00?ie=UTF8&psc=1">EasyAcc USB 3.0</a> but there are lots of other ones that do the same job.
</p>


<p>
Next I mouunted all the USB sticks and then renamed the volumes to be NEO4J1 -> NEO4J7:
</p>



~~~bash

for i in 1 2 3 4 5 6 7; do diskutil renameVolume "USB DISK" NEO4J${i}; done
~~~

<p>
I then created a bash function called 'duplicate' to do the copying work:
</p>



~~~bash

function duplicate() {
  i=${1}
  echo ${i}
  time rsync -avP --size-only --delete --exclude '.*' --omit-dir-times /Users/markneedham/Downloads/graph-connect-europe-2016/ /Volumes/NEO4J${i}/
}
~~~

<p>We can now call this function in parallel like so:</p>



~~~bash

seq 1 7 | parallel duplicate
~~~

<p>
And that's it. We didn't get a 7x improvement in the throughput of USB creation from doing 7 in parallel but it took ~ 9 minutes to complete 7 compared to 5 minutes each. Presumably there's still some part of the copying that is sequential further down - <a href="https://en.wikipedia.org/wiki/Amdahl%27s_law">Amdahl's law</a> #ftw.
</p>


<p>I want to go and find other things that I can use pipe into parallel now!</p>

