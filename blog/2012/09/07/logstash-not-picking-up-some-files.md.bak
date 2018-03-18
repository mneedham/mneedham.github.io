+++
draft = false
date="2012-09-07 23:49:41"
title="logstash not picking up some files"
tag=['software-development', 'logstash']
category=['Software Development']
+++

We're using <a href="http://logstash.net/">logstash</a> to collect all the logs across the different machines that we use in various environments and had noticed that on some of the nodes log files which we'd told the logstash-client to track weren't being collected.

We wanted to check what the open file descriptors of logstash-client were so we first had to grab its process id:

~~~text

$ ps aux | grep logstash
logstash     19896  134  9.1 711404 187768 ?       Ssl  09:13   0:06 java -Xms128m -Xmx256m -jar /var/apps/logstash/logstash-1.1.1-rc2-monolithic.jar agent -f /etc/logstash/logstash-client.conf
root     19910  0.0  0.0   7624   936 pts/1    S+   09:13   0:00 grep --color=auto logstash
~~~

And then list the open file descriptors:


~~~text

$ ls -alh /proc/19896/fd
lr-x------ 1 root root 64 2012-09-07 09:16 9 -> /var/log/syslog
...
~~~

That seemed to be restricted to 50 files for some reason so we also tried 'lsof':


~~~text

$ lsof -p 19896
COMMAND   PID USER   FD      TYPE             DEVICE SIZE/OFF    NODE NAME
root    20230 root  txt       REG                8,1    39584   22895 /var/log/syslog
...
~~~

Either way we weren't seeing most of the files we were supposed to be tracking so we put some print statements into the <a href="https://github.com/jordansissel/ruby-filewatch">ruby-filewatch</a> gem (which is included in the logstash jar) and redeployed the jar to see if we could figure out what was going on.

Eventually we narrowed it down to the <cite>watch.rb</cite> file's <cite><a href="https://github.com/jordansissel/ruby-filewatch/blob/master/lib/filewatch/watch.rb#L114">_discover_file</a></cite> method which was making a call to <cite>Dir.glob</cite> and returning an empty array even for some paths which definitely existed.


~~~ruby

    def _discover_file(path, initial=false)
      Dir.glob(path).each do |file| # if Dir.glob is empty the file doesn't get watched!
        next if @files.member?(file)
        next unless File.file?(file)
~~~

logstash 1.1.1 uses the JRuby 1.6.7 interpreter so we installed that locally to check if we could replicate the problem but we didn't really end up getting anywhere so we ended up <a href="https://github.com/alphagov/ruby-filewatch/commit/9daaab8381719188af6158acc13996235075df75">writing some code to work around the problem</a>.

The beginning of the <cite>_discover_file</cite> method now looks like this:


~~~ruby

    def _discover_file(path, initial=false)
      globbed_dirs = Dir.glob(path)
      @logger.debug("_discover_file_glob: #{path}: glob is: #{globbed_dirs}")
      if globbed_dirs.empty? && File.file?(path)
        globbed_dirs = [path]
        @logger.debug("_discover_file_glob: #{path}: glob is: #{globbed_dirs} because glob did not work")
      end
      globbed_dirs.each do |file|
        next if @files.member?(file)
        next unless File.file?(file)

        @logger.debug("_discover_file: #{path}: new: #{file} (exclude is #{@exclude.inspect})")
    ...
~~~

With this hack we can still ensure that a file will be watched even if <cite>Dir.glob</cite> returns an empty array.
