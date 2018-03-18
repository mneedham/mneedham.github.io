+++
draft = false
date="2017-04-27 20:59:56"
title="Python: Flask - Generating a static HTML page"
tag=['python']
category=['Python']
description="Learn how to generate a static HTML page using Python's Flask library."
+++

<p>
Whenever I need to quickly spin up a web application Python's <a href="http://flask.pocoo.org">Flask</a> library is my go to tool but I recently found myself wanting to generate a static HTML to upload to S3 and wondered if I could use it for that as well.</p>


<p>
It's actually not too tricky. If we're in <a href="http://stackoverflow.com/questions/31830663/how-to-render-template-in-flask-without-using-request-context">the scope of the app context</a> then we have access to the template rendering that we'd normally use when serving the response to a web request.</p>


<p>The following code will generate a HTML file based on a template file</a> <cite>templates/blog.html<cite>:
</p>




~~~python

from flask import render_template
import flask

app = flask.Flask('my app')

if __name__ == "__main__":
    with app.app_context():
        rendered = render_template('blog.html', \
            title = "My Generated Page", \
            people = [{"name": "Mark"}, {"name": "Michael"}])
        print(rendered)
~~~

<p>
<cite>templates/blog.html</cite>
</p>



~~~html

<!doctype html>
<html>
  <head>
	<title>{{ title }}</title>
  </head>
  <body>
	<h1>{{ title }}</h1>
  <ul>
  {% for person in people %}
    <li>{{ person.name }}</li>
  {% endfor %}
  </ul>
  </body>
</html>
~~~

<p>If we execute the Python script it will generate the following HTML:</p>



~~~bash

$ python blog.py 
<!doctype html>
<html>
  <head>
	<title>My Generated Page</title>
  </head>
  <body>
	<h1>My Generated Page</h1>
  <ul>
  
    <li>Mark</li>
  
    <li>Michael</li>
  
  </ul>

  </body>
</html>
~~~

<P>
And we can finish off by redirecting that output into a file:
</P>


~~~bash

$ python blog.py  > generated_blog.html
~~~

<p>
We could also write to the file from Python but this seems just as easy!
</p>

