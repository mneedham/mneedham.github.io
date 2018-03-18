+++
draft = false
date="2010-02-10 00:02:02"
title="Javascript: File encoding when using string.replace"
tag=['javascript']
category=['Javascript']
+++

We ran into an interesting problem today when moving some Javascript code which was making use of the 'string.replace' function to strip out the £ sign from some text boxes on a form.

The code we had written was just doing this:


~~~javascript

var textboxValue = $("#fieldId").val().replace(/£/, '');
~~~

So having realised that we had this code all over the place we decided it would make sense to create a common function that strip the pound sign out. These common functions reside in a different js file to the original code.


~~~javascript

function Common() {
	this.stripPounds = function(value) {
		return value.replace(/£/, '');
	};
}
~~~

We replace the above code with a call to that instead:


~~~javascript

var textboxValue = new Common().stripPounds($("#fieldId").val());
~~~

Having done this we realised that the £ sign was no longer being replaced despite the fact that the code was pretty much identical.

After a lot of fiddling around <a href="http://twitter.com/gurrie09?utm_source=follow&utm_content=profile&utm_campaign=twitter20080331162631&utm_medium=email">Brian</a> eventually realised that the js file containing 'Common' was ANSI encoded when we actually needed it to be UTF-8 encoded, probably because we created it in Visual Studio. 

As a result the £ sign is presumably being read as some other character which means the replacement doesn't happen anymore.

Converting the file to UTF-8 encoding fixed the problem for us but it's certainly not something I'd have ever thought of.
