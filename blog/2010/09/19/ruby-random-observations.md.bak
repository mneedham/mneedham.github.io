+++
draft = false
date="2010-09-19 11:35:28"
title="Ruby: Random Observations"
tag=['ruby']
category=['Ruby']
+++

I thought it'd be interesting to write down some of my observations after working with Ruby and Rails for a couple more weeks so here are some more things I've come across and others that I've got confused with...

<h3>The :: operator</h3>
(apparently also known as the leading double colon operator)

I came across this while looking at some of the <a href="http://github.com/hassox/rails_warden/blob/master/lib/rails_warden.rb">rails_warden code</a> to try to  understand how that gem opens the ActionController::Base class to add helper methods to it.

The code reads as follows:


~~~ruby

 Rails.configuration.after_initialize do
    class ::ActionController::Base
      include RailsWarden::Mixins::HelperMethods
      include RailsWarden::Mixins::ControllerOnlyMethods
    end

    module ::ApplicationHelper
      include RailsWarden::Mixins::HelperMethods
    end
  end
~~~

The '::' operator is used on line 78 and it means that Ruby will look in the global scope for the constant which follows the operator - in this case ActionController::Base. Marcos Ricardo <a href="http://marcricblog.blogspot.com/2007/11/ruby-double-colon.html">explains this in more detail on his blog</a>.

In this case I'm not entirely sure why the operator is necessary since there doesn't seem to be another constant defined with the same name in the local scope.

<h3>The !! operator</h3>

This is another operator that I came across while reading the <a href="http://github.com/hassox/warden/blob/master/lib/warden/strategies/base.rb">Warden code</a>. 


~~~ruby

      def halted?
        !!@halted
      end
~~~

<a href="http://twitter.com/ponnappa">Sidu</a> explained that this operator ensures that true or false will be returned rather than a truish/falish value.

For example:


~~~ruby

ruby-1.8.7-p299 > !!nil
 => false 
~~~


~~~ruby

ruby-1.8.7-p299 > !!1
 => true 
~~~

<h3>Single '=' in if statements</h3>

A mistake I've made a few times now is using '=' in if statements instead of '==' which means that the code tends to fail in a somewhat confusing way.

I'm not sure if this is because I've been playing around with Clojure a bit recently and in Clojure you use '=' for comparison or if I do this anyway and usually get saved by the compiler.

Either way it's very frustrating!

<h3>Open classes</h3>
I'm used to being able to see exactly what is defined on a class in one place but in Ruby it's possible to open a class from anywhere and add to it or change the existing behaviour.

I still don't know all of the hooks that Rails provides for opening classes so it's still a big magical for me at the moment.

