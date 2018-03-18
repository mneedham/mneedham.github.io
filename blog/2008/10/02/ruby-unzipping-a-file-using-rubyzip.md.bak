+++
draft = false
date="2008-10-02 00:04:22"
title="Ruby: Unzipping a file using rubyzip"
tag=['ruby', 'rubyzip']
category=['Ruby']
+++

In the world of Ruby I've been working on a script which needs to unzip a file and then run an installer which is only available after unpacking it.

We've been using the <a href="http://rubyzip.sourceforge.net/">rubyzip</a> gem to do so but so far it hasn't felt intuitive to me coming from the Java/C# world.

<a href="http://rubyzip.sourceforge.net/classes/Zip/ZipFile.html">ZipFile</a> is the class we need to use and at first glance I had thought that it would be possible to just pass the zip file name to the 'extract' method and have it do all the work for me!

Turns out you actually need to open the zip file and then create the directory location for each file in the zip before extracting them all individually.

We eventually ended up with this little method:


~~~ruby

require 'rubygems'
require 'zip/zip'

def unzip_file (file, destination)
  Zip::ZipFile.open(file) { |zip_file|
   zip_file.each { |f|
     f_path=File.join(destination, f.name)
     FileUtils.mkdir_p(File.dirname(f_path))
     zip_file.extract(f, f_path) unless File.exist?(f_path)
   }
  }
end
~~~

Which we can then call with the zip file and the destination where we want to unzip the file.


~~~ruby

unzip_file("my.zip", "marks_zip")
~~~

Is there a better way to do this? It feels a bit clunky to me at the moment.
