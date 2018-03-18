+++
draft = false
date="2010-06-30 10:46:20"
title="jQuery: Dynamically updating a drop down list"
tag=['jquery']
category=['jQuery']
+++

We recently had a requirement to dynamically update a drop down list based on how the user had filled in other parts of the page.

Our initial approach was to populate the drop down with all potential options on page load and then add CSS selectors to the options that we wanted to hide. That worked fine in Chrome and Firefox but Internet Explorer seems to ignore CSS selectors inside a drop down list so none of the options were being hidden.

We therefore had to try and dynamically add and remove options from the drop down list instead.

The list that we initially loaded onto the page was like this:


~~~html

<select id="foo" name="foo">
<option value="A" selected="selected">A</option>
<option value="B">B</option>
<option value="C">C</option>
<option value="Not applicable">Not applicable</option>
</select>
~~~

<a href="http://twitter.com/christianralph">Christian</a> eventually came up with the following solution to hide/show those options and select the appropriate one after several hours of trial and error:


~~~javascript

// captured on page load
var originalFooOptions = $("#foo > option"); 
~~~


~~~javascript

var foo = $("#foo");
var dependentField = $("#fieldFooIsDependentOn");

if(notApplicable()) {
	foo.children("option[value!='Not applicable']").remove();
	foo.val("Not applicable");
} else {
	foo.empty();
	$(originalFooOptions).each(function() {
		var newOption = $(this).clone();
		if ($(this).val() === dependentField.val()) {
			newOption.attr("selected", "selected");
		}
		newOption.appendTo(foo);
	});	
}
~~~



Another approach we tried was to try and dynamically update 'foo' rather than removing all the items and then adding them back.

Unfortunately we kept getting an 'unspecified error' on Internet Explorer 6 when we tried to set the selected value with that approach.
