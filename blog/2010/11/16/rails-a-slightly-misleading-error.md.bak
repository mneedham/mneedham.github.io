+++
draft = false
date="2010-11-16 21:17:00"
title="Rails: A slightly misleading error"
tag=['ruby', 'rails']
category=['Ruby']
+++

We recently created a new project to handle the reporting part of our application and as with all our projects we decided not to checkin any configuration ".yml' files but rather '.yml.example' files which people can then customise for their own environments.

So in our config directory would look something like this when you first checkout the project:

<ul>
<li>config
<ul>
<li>database.yml.example</li>
<li>some.yml.example</li></ul>
</ul>

And we'd need to copy those files to get '.yml' versions, changing any parameters that we need to for our local environment.

The disadvantage of this approach is that you have an extra step on using a project for the first time, a step that I've been meaning to automate.

Several people ran into a somewhat confusing error message when running our rake file after forgetting to create these '.yml' files which looked like this:


~~~text

> rake db:migrate
(in /Users/mneedham/SandBox/project)
rake aborted!
uninitialized constant ActiveRecord

(See full trace by running task with --trace)
~~~

Running with --trace didn't reveal our mistake but interestingly launching 'script/console' did!


~~~text

script/console
Loading development environment (Rails 2.3.5)
/Users/mneedham/SandBox/project/config/environment.rb:4:in `initialize':Errno::ENOENT: No such file or directory - /Users/mneedham/SandBox/project/config/some.yml
/Users/mneedham/SandBox/project/vendor/rails/railties/lib/rails/backtrace_cleaner.rb:2:NameError: uninitialized constant ActiveSupport::BacktraceCleaner
/Users/mneedham/SandBox/project/vendor/rails/railties/lib/console_with_helpers.rb:5:NameError: uninitialized constant ApplicationController
ruby-1.8.7-p299 > 
~~~

This is the environment.rb file in which we were loading that yml file:

config/environment.rb

~~~ruby

....
require 'yaml'
some_file = File.join(File.dirname(__FILE__), "some.yml")
...
~~~

It's a relatively simple mistake to make so I was surprised that rake didn't tell us that the file didn't exist rather than failing when trying to require ActiveRecord.

