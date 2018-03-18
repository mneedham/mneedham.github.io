+++
draft = false
date="2010-11-18 18:40:37"
title="Capistrano, sed, escaping forward slashes and 'p' is not 'puts'!"
tag=['ruby', 'sed', 'capistrano']
category=['Ruby']
+++

<a href="http://twitter.com/priyaaank">Priyank</a> and I have been working on automating part of our deployment process and one task we needed to do as part of this is replace some variables used in one of our shell scripts.

All the variables in the script refer to production specific locations but we needed to change a couple of them in order to run the script in our QA environment.

We're therefore written a sed command, which we call from <a href="https://github.com/capistrano/capistrano">Capistrano</a>, to allow us to do this.

The Capistrano script looks a little like this:


~~~ruby

task :replace_in_shell do
	directory = "/my/directory/path"
	sed_command = "sed 's/^some_key.*$/#{directory}/' shell_script.sh > shell_script_with_qa_variables.sh"
	run sed_command
end
~~~

Unfortunately this creates the following sed command which isn't actually valid syntactically:


~~~text

sed 's/^some_key.*$//my/directory/path/' shell_script.sh > shell_script_with_qa_variables.sh
~~~

We decided to use 'gsub' to escape all the forward slashes in the directory path and to work out which parameters we needed to pass to 'gsub' we started using irb.

Executing gsub with the appropriate parameters leads us to believe that 2 backslashes will be added:


~~~ruby

ruby-1.8.7-p299 > "/my/directory/path".gsub("/", "\\/")
 => "\\/my\\/directory\\/path" 
~~~

This is because there IRB is implicitly called 'inspect' on the result which shows a different string than what we would actually get.

While writing this blog post I've also learnt (thanks to <a href="http://twitter.com/ashwinraghav">Ashwin</a>) that 'p' is not the same as 'puts' which is what I originally thought and has been driving me crazy as I try to understand why everything I print includes an extra backslash!

The following code:


~~~ruby

p "/mark/dir/".gsub("/", "\\/")
~~~

is the same as typing:


~~~ruby

puts "/mark/dir/".gsub("/", "\\/").inspect
~~~

We were able to change our Capistrano script to escape forward slashes like so:


~~~ruby

task :replace_in_shell do
	directory = "/my/directory/path"
	sed_command = "sed 's/^some_key.*$/#{directory.gsub("/", "\\/"}/' shell_script.sh > shell_script_with_qa_variables.sh"
	run sed_command
end
~~~




