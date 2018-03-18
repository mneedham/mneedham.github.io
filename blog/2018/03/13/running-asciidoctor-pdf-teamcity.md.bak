+++
draft = false
date="2018-03-13 21:57:14"
title="Running asciidoctor-pdf on TeamCity"
tag=['ruby', 'asciidoc', 'asciidoctor', 'asciidoctor-pdf', 'gemfile']
category=['Software Development']
+++

<p>
I've been using <a href="https://asciidoctor.org/docs/asciidoctor-pdf/">asciidoctor-pdf</a> to generate PDF and while I was initially running the tool locally I eventually decided to setup a build on TeamCity. 
</p>


<p>
It was a bit trickier than I expected, mostly because I'm not that familiar with deploying Ruby applications, but I thought I'd capture what I've done for future me.
</p>


<p>
I have the following <cite>Gemfile</cite> that installs asciidoctor-pdf and its dependencies:
</p>


<p><cite>Gemfile</cite></p>



~~~text

source 'https://rubygems.org'

gem 'prawn'
gem 'addressable'
gem 'prawn-svg'
gem 'prawn-templates'
gem 'asciidoctor-pdf'
~~~

<p>
I don't have permissions to install gems globally on the build agents so I'm bundling those up into the <cite>vendor</cite> directory. It's been a long time since I worked on a Ruby application so perhaps that's par for the course.
</p>



~~~bash

bundle install --path vendor/
bundle package
~~~

<p>
On the build agent I'm running the following script:
</p>



~~~bash

export PATH="$PATH:/home/teamcity/.gem/ruby/2.3.0/bin"
mkdir $PWD/gems
export GEM_HOME="$PWD/gems"
gem install bundler --user-install --no-rdoc --no-ri && bundle install
./vendor/ruby/2.3.0/bin/asciidoctor-pdf -a allow-uri-read blog.adoc
~~~

<p>
I override where gems should be installed and then execute the <cite>asciidoctor-pdf</cite> executable from the vendor directory.
</p>


<p>
It all seems to work quite nicely but if there's a better approach that I should be taking so let me know in the comments.
</p>

