+++
draft = false
date="2015-03-09 23:00:56"
title="Python: Streaming/Appending to a file"
tag=['python']
category=['Python']
+++

<p>
I've been playing around with Twitter's API (via the <a href="https://github.com/tweepy/tweepy">tweepy</a> library) and due to the rate limiting it imposes I wanted to stream results to a CSV file rather than waiting until my whole program had finished.
</p>


<p>
I wrote the following program to simulate what I was trying to do:
</p>



~~~python

import csv
import time

with open("rows.csv", "a") as file:
    writer = csv.writer(file, delimiter = ",")

    end = time.time() + 10
    while True:
        if time.time() > end:
            break
        else:
            writer.writerow(["mark", "123"])
            time.sleep(1)

~~~

<p>
The program will run for 10 seconds and append one line to 'rows.csv' once a second. Although I have used the 'a' flag in my call to 'open' if I poll that file before the 10 seconds is up it's empty:
</p>



~~~bash

$ date && wc -l rows.csv
Mon  9 Mar 2015 22:54:27 GMT
       0 rows.csv

$ date && wc -l rows.csv
Mon  9 Mar 2015 22:54:31 GMT
       0 rows.csv

$ date && wc -l rows.csv
Mon  9 Mar 2015 22:54:34 GMT
       0 rows.csv

$ date && wc -l rows.csv
Mon  9 Mar 2015 22:54:43 GMT
      10 rows.csv
~~~

<p>
I thought the flushing of the file was completely controlled by the with block but lucky for me there's actually a <cite><a href="https://docs.python.org/2/library/io.html#io.IOBase.flush">flush()</a></cite> function which allows me to force writes to the file whenever I want.
</p>


<p>Here's the new and improved sample program:</p>



~~~python

import csv
import time

with open("rows.csv", "a") as file:
    writer = csv.writer(file, delimiter = ",")

    end = time.time() + 10
    while True:
        if time.time() > end:
            break
        else:
            writer.writerow(["mark", "123"])
            time.sleep(1)
            file.flush()
~~~

<p>And if we poll the file while the program's running:</p>



~~~python

$ date && wc -l rows.csv
Mon  9 Mar 2015 22:57:36 GMT
      14 rows.csv

$ date && wc -l rows.csv
Mon  9 Mar 2015 22:57:37 GMT
      15 rows.csv

$ date && wc -l rows.csv
Mon  9 Mar 2015 22:57:40 GMT
      18 rows.csv

$ date && wc -l rows.csv
Mon  9 Mar 2015 22:57:45 GMT
      20 rows.csv
~~~

<p>Much easier than I expected - I ♥ python!</p>

