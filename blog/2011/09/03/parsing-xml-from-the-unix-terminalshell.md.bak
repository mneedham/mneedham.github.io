+++
draft = false
date="2011-09-03 23:42:11"
title="Parsing XML from the unix terminal/shell"
tag=['software-development', 'xml']
category=['Software Development']
+++

I spent a bit of time today trying to put together a quick script which would allow me to grab story numbers from the commits in our Git repository and then work out which functional areas those stories were in by querying mingle.

Therefore I wanted to make a <cite>curl</cite> request to the mingle and then pipe that result somewhere and run an xpath expression to get my element.

I didn't want to have to write code in another script file and then reference that file from the shell and in my search to achieve that I came across <cite><a href="http://xmlstar.sourceforge.net/docs.php">XMLStarlet</a></cite> on <a href="http://stackoverflow.com/questions/29004/parsing-xml-using-unix-terminal">stackoverflow</a>. 

It's installable via mac ports:


~~~text

sudo port install xmlstarlet
~~~

And I was then able to pipe the results of my mingle request and locate the following bit of XML:


~~~text

<property type_description="Managed text list" hidden="false">
<name>Functional Area</name>
<value>Our Functional Area</value>
</property>
~~~


~~~text

curl -s http://user:password@mingleurl:8888/api/v2/projects/project_name/cards/1.xml  | xmlstarlet sel -t -v "//property/name[. = 'Functional Area']/../value"
~~~

There's much more you can do with the command which is listed on the <a href="http://xmlstar.sourceforge.net/doc/xmlstarlet.txt">documentation page</a>.
