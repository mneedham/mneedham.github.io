+++
draft = false
date="2010-07-25 11:48:51"
title="Bundler: Don't forget to call 'source'"
tag=['ruby', 'bundler']
category=['Ruby']
+++

<a href="http://twitter.com/bguthrie">Brian</a>, <a href="http://twitter.com/tdinkar">Tejas</a> and I (well mainly them) have been working on <a href="http://developer.yahoo.com/hacku/hackuhandler.php?appid=hacku&op=showhack&hackid=1094">an application to give badges to people based on their GitHub activity at the Yahoo Open Hack Day</a> in Bangalore and we've been making use of <a href="http://gembundler.com/">Bundler</a> to pull in our dependencies.

Our Gemfile was originally like this:


~~~ruby

gem "sinatra", "1.0"
gem "haml", "3.0.13"
gem "activesupport", "3.0.0.beta4", :require => false
gem "tzinfo", "0.3.22"
gem "nokogiri", "1.4.2"
...
~~~

For quite a while we were wondering why 'bundle install' wasn't actually resolving anything at all before we <a href="http://en.wikipedia.org/wiki/RTFM">RTFM</a> and realised that we needed to call 'source' at the top so that bundler knows where to pull the dependencies from.

Changing the file to look like this solved that problem:


~~~ruby

source "http://rubygems.org"

gem "sinatra", "1.0"
gem "haml", "3.0.13"
gem "activesupport", "3.0.0.beta4", :require => false
gem "tzinfo", "0.3.22"
gem "nokogiri", "1.4.2"
...
~~~

bundler still seemed to have problems resolving 'nokogiri' whereby I was getting various error messages, eventually ending up with this one:


~~~text

Installing nokogiri (1.4.2) from .gem files at /Users/mneedham/.rvm/gems/ruby-1.8.7-p299/cache with native extensions /Library/Ruby/Site/1.8/rubygems/installer.rb:482:in `build_extensions': ERROR: Failed to build gem native extension. (Gem::Installer::ExtensionBuildError)

/System/Library/Frameworks/Ruby.framework/Versions/1.8/usr/bin/ruby extconf.rb
checking for iconv.h... yes
checking for libxml/parser.h... yes
checking for libxslt/xslt.h... yes
checking for libexslt/exslt.h... yes
checking for gzopen() in -lz... no
-----
zlib is missing.  please visit http://nokogiri.org/tutorials/installing_nokogiri.html for help with installing dependencies.
~~~

I had to <a href="http://nokogiri.org/tutorials/installing_nokogiri.html">follow the instructions on their website</a> to get that working which isn't ideal as it means not everything is being resolved through bundler. 

I'm not sure if there's a way to get around having to do that so if anyone know a way let me know!
