+++
draft = false
date="2015-05-31 22:33:54"
title="Python: CSV writing - TypeError: 'builtin_function_or_method' object has no attribute '__getitem__'"
tag=['python']
category=['Python']
+++

<p>
When I'm working in Python I often find myself writing to CSV files using the <a href="https://docs.python.org/2/library/csv.html">in built library</a> and every now and then make a mistake when calling writerow:
</p>



~~~python

import csv
writer = csv.writer(file, delimiter=",")
writer.writerow["player", "team"]
~~~

<p>This results in the following error message:</p>



~~~text

TypeError: 'builtin_function_or_method' object has no attribute '__getitem__'
~~~

<p>The error message is a bit weird at first but it's basically saying that I've tried to do an <a href="http://stackoverflow.com/questions/13075632/typeerror-builtin-function-or-method-object-has-no-attribute-getitem">associative lookup on an object which doesn't support that operation</a>.</p>


<p>
The resolution is simply to include the appropriate parentheses instead of leaving them out!
</p>



~~~python

writer.writerow(["player", "team"])
~~~

<p>This one's for future Mark.</p>

