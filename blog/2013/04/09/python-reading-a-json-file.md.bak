+++
draft = false
date="2013-04-09 07:23:59"
title="Python: Reading a JSON file"
tag=['python', 'json']
category=['Python']
+++

<p>I've been playing around with some code to spin up AWS instances using <a href="http://docs.fabfile.org/en/1.6/">Fabric</a> and <a href="https://github.com/boto/boto">Boto</a> and one thing that I wanted to do was define a bunch of default properties in a JSON file and then load this into a script.</p>


<p>I found it harder to work out how to do this than I expected to so I thought I'd document it for future me!</p>


<p>My JSON file looks like this:</p>


<em>config/defaults.json</em>

~~~json

{
	"region" : "eu-west-1",
	"instanceType": "m1.small"
}
~~~

<p>To read that file we can do the following:</p>



~~~python

>>> open('config/defaults.json').read()
'{\n\t"region" : "eu-west-1",\n\t"instanceType": "m1.small"\n}'
~~~

<p>We can then use the <a href="http://stackoverflow.com/questions/2835559/python-parsing-file-json">json.loads</a> function to convert that from a string into a Python object:</p>



~~~python

>>> import json
>>> config = json.loads(open('config/defaults.json').read())
>>> config
{u'region': u'eu-west-1', u'instanceType': u'm1.small'}
~~~

<p>We'd write the following code to get the region:</p>



~~~python

>>> config["region"]
u'eu-west-1'
~~~

<p>I guess we might want to use a different approach that didn't load the whole string into memory if we had a large JSON file but for my purposes this will do!</p>

