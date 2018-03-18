+++
draft = false
date="2012-06-10 23:30:23"
title="CSV parsing/UTF-8 encoding"
tag=['utf-8']
category=['Software Development']
+++

I was recently trying to parse a CSV file which I'd converted from an Excel spreadsheet but was having problems with characters beyond the standard character set.

This is <a href="http://stackoverflow.com/questions/1549139/ruby-cannot-parse-excel-file-exported-as-csv-in-os-x">an example</a> of what was going wrong:

~~~ruby

> require 'csv'
> people = CSV.open("sponsors.csv", 'r', ?,, ?\r).to_a
["Erik D\366rnenburg", "N/A"]

> people.each { |sponsee, sponsor| puts "#{sponsee} #{sponsor}" }
Erik D?rnenburg N/A
~~~

I came across a Ruby gem called <cite><a href="http://snippets.aktagon.com/snippets/159-Detecting-file-data-encoding-with-Ruby-and-the-chardet-RubyGem">chardet</a></cite> which allowed me to work out the character set of Erik's name like so:


~~~ruby

> require 'chardet'
> require 'UniversalDetector'

> UniversalDetector::chardet("Erik D\366rnenburg")
=> {"encoding"=>"ISO-8859-2", "confidence"=>0.879630020576305}
~~~

I'd forgotten that you can work out the same thing by making use of <cite>file</cite> like so:


~~~text

> file sponsors.csv 
sponsors.csv: ISO-8859 text, with CR line terminators
~~~

We can then make use of <cite><a href="http://docs.moodle.org/22/en/Converting_files_to_UTF-8">iconv</a></cite> to change the file encoding like this:


~~~text

> iconv -f iso-8859-2 -t utf-8 sponsors.csv > sponsors_conv.csv
~~~


~~~text

> file sponsors_conv.csv 
sponsors_conv.csv: UTF-8 Unicode text, with CR line terminators
~~~

Now if we parse the UTF-8 encoded file it doesn't ruin Erik's name!


~~~ruby

> people = CSV.open("sponsors.csv", 'r', ?,, ?\r).to_a
["Erik D\303\266rnenburg", "N/A"]

> people.each { |sponsee, sponsor| puts "#{sponsee} #{sponsor}" }
Erik Dörnenburg N/A
~~~

Hopefully I'll now remember what to do next time I come across this problem!
