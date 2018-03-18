+++
draft = false
date="2012-09-23 22:46:09"
title="Java: Parsing CSV files"
tag=['java']
category=['Java']
+++

As I mentioned in a previous post I recently moved a <a href="http://www.markhneedham.com/blog/2012/09/23/neo4j-the-batch-inserter-and-the-sunk-cost-fallacy/">bunch of neo4j data loading code from Ruby to Java</a> and as part of that process I needed to parse some CSV files.

In Ruby I was using <a href="http://fastercsv.rubyforge.org/">FasterCSV</a> which became the <a href="http://stackoverflow.com/questions/5011395/what-is-ruby-1-9-standard-csv-library">standard CSV library from Ruby 1.9</a> but it's been a while since I had to parse CSV files in Java so I wasn't sure which library to use.

I needed a library which could parse a comma separated file where there might be commas in the values of one of the fields. I think that's fairly standard behaviour in any CSV library but my <a href="http://www.linuxquestions.org/questions/linux-general-1/parsing-a-comma-separated-csv-file-where-fields-have-commas-in-to-714332/">googling led me to OpenCSV</a>.

It can be <a href="http://downloads.sourceforge.net/project/opencsv/opencsv/2.3/opencsv-2.3-src-with-libs.tar.gz?r=&ts=1348439616&use_mirror=ignum">downloaded from here</a> and so far seems to do the job!

This is an example of how I'm using it:


~~~java

String filePath = "/Users/mneedham/data/awesome-csv-file.csv";
CSVReader reader = new CSVReader(new FileReader(filePath), ',');

List<String[]> csvEntries = reader.readAll();
Iterator<String[]> iterator = csvEntries.iterator();
        
while (iterator.hasNext()) {
    String[] row = iterator.next();
    System.out.println("field 1: " + row[0]);
}
~~~

There are more use cases described on the <a href="http://opencsv.sourceforge.net/">home page</a>.
