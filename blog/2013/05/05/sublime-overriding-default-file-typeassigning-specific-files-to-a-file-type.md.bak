+++
draft = false
date="2013-05-05 00:03:17"
title="Sublime: Overriding default file type/Assigning specific files to a file type"
tag=['sublime']
category=['Software Development']
+++

<p>I've been using <a href="">Sublime</a> a bit recently and one thing I wanted to do was put <a href="">neo4j cypher</a> queries into files with arbitrary extensions and have them recognised as cypher files every time I open them.</p>


<p>I'm using the <a href="">cypher Sublime plugin</a> to get the syntax highlighting but since I've got my cypher in a .haml file it only remembers that it should have cypher highlighting as long as the file is open.</p>


<p>As soon as I close and then re-open the file it goes back to being highlighted as HAML.</p>


<p>I initially thought that the way around this would be to write a plugin which kept track of files that you'd manually assigned a syntax to but then I came across the <a href="https://github.com/facelessuser/ApplySyntax">ApplySyntax</a> plugin which seems even better.</p>


<p>ApplySyntax allows you to assign syntaxes to files based on regular expression matching on the file name or on the first line of the file.</p>


<p>At the moment, the easiest way to detect that a file is a cypher query is that the first line will begin with 'START' so I wrote the following in my user settings file:</p>


<em>~/Library/Application Support/Sublime Text 2/Packages/User/ApplySyntax.sublime-settings</em>


~~~json

{
	"reraise_exceptions": false,
	"new_file_syntax": false,
	"syntaxes": [
		{			
			"name": "Cypher",
			"rules": [
				{"first_line": "^START"}
			]
		}	
	]
}
~~~

<p>ApplySyntax is a pretty neat plugin, worth having a look if you have this problem to solve!</p>

