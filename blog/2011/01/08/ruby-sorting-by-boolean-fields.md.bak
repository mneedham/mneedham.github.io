+++
draft = false
date="2011-01-08 13:15:19"
title="Ruby: Sorting by boolean fields"
tag=['ruby']
category=['Ruby']
+++

We were doing a bit of work on <a href="http://rapidftr.com/">RapidFTR</a> in the ThoughtWorks Pune office today and one problem my pair and I were trying to solve was how to sort a collection of objects by a boolean field.

Therefore given the following array of values:


~~~ruby

form_sections = [FormSection.new(:enabled => false, :name => "a", :order => 1), 
                 FormSection.new(:enabled => true, :name => "b", :order => 2)]
~~~

We wanted to display those form sections which were disabled at the bottom of the page.

We originally tried the following:


~~~ruby

form_sections.sort_by { |row| [row.enabled, row.order] }
~~~

But got the following error:


~~~ruby

undefined method `<=>' for true:TrueClass
~~~

We figured we'd need to convert the true and false values to equivalent values which is demonstrated on <a href="http://stackoverflow.com/questions/903877/sort-objects-by-boolean-values-in-ruby">this Stack Overflow post</a>:


~~~ruby

form_sections.sort_by { |row| [row.enabled ? 0 : 1, row.order] }
~~~

I didn't realise it would be that simple to do - it's pretty neat.

