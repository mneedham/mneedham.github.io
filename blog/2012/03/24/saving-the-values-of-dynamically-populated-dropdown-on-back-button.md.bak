+++
draft = false
date="2012-03-24 00:40:34"
title="Saving the values of dynamically populated dropdown on back button"
tag=['software-development']
category=['Software Development']
+++

We wanted to be able to retain the value of a drop down menu that was being dynamically populated (via an AJAX call) when the user hit the back button but the AJAX request re-runs when we go hit back therefore losing our selection.

Our initial thinking was that we might be able to store the value of the dropdown in a hidden field and then restore it into the dropdown using jQuery on page load but that approach didn't work since hidden fields don't seem to retain their values when you hit back.

Another approach would be to update the URL with a new # value on each change of the dropdown and then parse the URL on page load to figure out which value should be selected.

That would probably work but it seemed a bit too complicated.

Eventually we realised that we could create an extra text box, 'hide' it by use of 'display:none' in our CSS and then copy the dropdown value into that every time it changed.

We ended up with code something like this to capture the selected value:


~~~javascript

$("#dropdown-menu").live('change', function() {
  $("#hidden-field').val($(this).val());
});
~~~

And then we populated the dropdown with the saved value on the callback from the AJAX call:


~~~javascript

$.ajax({
  url: 'url/to/populate_dropdown',
  success: function(data) {
    $("#dropdown-menu").html(data);
	$("#dropdown-menu").val($("#hidden-field").val());
  }
});
~~~

It seems to work pretty well and it's a simple technique as well so it worked in all the browsers that we tested it in.
