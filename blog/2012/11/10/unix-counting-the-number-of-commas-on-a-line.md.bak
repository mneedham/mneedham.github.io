+++
draft = false
date="2012-11-10 16:30:48"
title="Unix: Counting the number of commas on a line"
tag=['unix']
category=['Shell Scripting']
+++

A few weeks ago I was playing around with some data stored in a CSV file and wanted to do a simple check on the quality of the data by making sure that <a href="http://unix.stackexchange.com/questions/18736/how-to-count-the-number-of-a-specific-character-in-each-line">each line had the same number of fields</a>.

One way this can be done is with <cite>awk</cite>:


~~~text

awk -F "," ' { print NF-1 } ' file.csv
~~~

Here we're specifying the file separator <cite>-F</cite> as ',' and then using the <cite>NF</cite> (number of fields) variable to print how many commas there are on the line.

Another slightly more complicated way is to combine <cite>tr</cite> and <cite>awk</cite> like so:


~~~text

tr -d -c ",\n" < file.csv | awk ' { print length } '
~~~

Here we're telling <cite>tr</cite> to delete any characters except for a comma or new line.

If we pass just a comma to the '-d' option like so...


~~~text

tr -d "," < file.csv
~~~

...that would delete all the commas from a line but we can use the '-c' option to complement the comma i.e. delete everything except for the comma.


~~~text

tr -d -c "," < file.csv
~~~

Unfortunately that puts all the commas onto the same line so we need to complement the new line character as well:


~~~text

tr -d -c ",\n" < file.csv
~~~

We can then use the <cite>length</cite> variable of awk to print out the number of commas on each line.

We can achieve the same thing by making use of <cite>sed</cite> instead of <cite>tr</cite> like so:


~~~text

sed 's/[^,]//g' file.csv | awk ' { print length } '
~~~

Since sed operates on a line by line basis we just need to tell it to substitute anything which isn't a comma with nothing and then pipe the output of that into awk and use the <cite>length</cite> variable again.

I thought it might be possible to solve this problem using <cite>cut</cite> as well but I can't see any way to get it to output the total number of fields.

If anyone knows any other cool ways to do the same thing let me know in the comments - it's always interesting to see how different people wield the unix tools!
