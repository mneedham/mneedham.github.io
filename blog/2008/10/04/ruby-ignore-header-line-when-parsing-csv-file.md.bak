+++
draft = false
date="2008-10-04 01:32:08"
title="Ruby: Ignore header line when parsing CSV file"
tag=['ruby', 'csv']
category=['Ruby']
+++

As my Ruby journey continues one of the things I wanted to do today was parse a CSV file.

<a href="http://www.rubytips.org/2008/01/06/csv-processing-in-ruby/">This article</a> proved to be very useful for teaching the basics but it didn't say how to ignore the header line that the CSV file contained.

The CSV file I was parsing was similar to this:


~~~text

name, surname, location
Mark, Needham, Sydney
David, Smith, London
~~~

I wanted to get the names of people originally to use them in my code. This was the first attempt:


~~~ruby

require 'csv'

def parse_csv_file_for_names(path_to_csv)
  names = []  
  csv_contents = CSV.read(path_to_csv)
  csv_contents.each do |row|
    names << row[0]
  end
  return names
end
~~~

I then printed out the names to see what was going on:


~~~ruby

names = parse_csv_file_for_names( "csv_file.csv" )
names.each do |name|
  puts name
end
~~~

This is what was printed:


~~~text

name
Mark
David
~~~

It turns out that the 'shift' method is what I was looking for to help me ignore the first line of the file. The new and improved method now looks like this:


~~~ruby

require 'csv'

def parse_csv_file_for_names(path_to_csv)
  names = []  
  csv_contents = CSV.read(path_to_csv)
  csv_contents.shift
  csv_contents.each do |row|
    names << row[0]
  end
  return names
end
~~~

Not a particularly complicated thing to do in the end although I had been expecting to find a method on CSV that would allow me to ignore the header line automatically. As far as I could tell there isn't one!
