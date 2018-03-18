+++
draft = false
date="2010-10-29 04:27:41"
title="Ruby: Getting Active Record validation errors twice"
tag=['ruby', 'active-record']
category=['Ruby']
+++

I managed to create an interesting problem for myself while playing around with some code whereby I was ending up with validation errors appearing twice every time I called 'valid?' on a specific model.

I figured I was probably doing something stupid and in fact a few replies by Aaron Baldwin on <a href="http://groups.google.com/group/rubyonrails-talk/browse_thread/thread/a848f697dd7eba61?pli=1">a mailing list thread on 'rubyonrails-talk'</a> helped explain exactly what I'd done:

<blockquote>
Are you calling require 'employee' anywhere?  If so you are likely 
causing the model to load twice which causes duplicate errors because 
the validates_presence_of method gets called twice. 
</blockquote>

I'd put the following code into a controller elsewhere somewhat unnecessarily since it didn't seem to be picking up the location of my model at the time:

code_submissions_controller.rb

~~~ruby

require 'models/code_submission'

class CodeSubmissionsController < ApplicationController
  def new
    CodeSubmission.new  
  end
end
~~~

<a href="http://ruby-doc.org/core/classes/Kernel.html#M005941">require</a> doesn't load a file if it's already been included but Aaron points out why it does on this occasion:

<blockquote>
You are right that "require" will only load the file once.  But if you load the class another way calling "require" will load it again. 
</blockquote>

As I understand it that controller code would also implicitly require 'code_submission' by the convention of inserting an underscore between the 'CodeSubmission' constant's names.

We therefore effectively have the following two requires:


~~~ruby

require 'code_submission'
require 'models/code_submission'
~~~

Which explain how the file gets loaded twice and therefore why the validation method fires twice and therefore creates two errors!
