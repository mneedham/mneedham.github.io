+++
draft = false
date="2008-12-02 22:54:52"
title="jQuery Validation & Firefox Refresh Behaviour"
tag=['software-development', 'browsers', 'jquery']
category=['jQuery']
+++

We've been working quite a bit with <a href="http://jquery.com/">jQuery</a> and cross browser compatibility and one of the interesting differences we came across today was the behaviour of Firefox and Internet Explorer when it comes to refreshing a page.

When you press refresh in Internet Explorer the page gets refreshed to the state that it was in when you first loaded the URL, meaning that the state of the data in forms is returned to its original state.

Doing the same in Firefox doesn't have the same behaviour - the page refreshes but it keeps the most recent data that was entered into the form. In theory this is quite nice behaviour because it means if you accidentally hit refresh it keeps all your data.

For us it was quite annoying as we had hooked up a <a href="http://docs.jquery.com/Plugins/Validation">validator</a> and some other custom code which declared certain parts of the page invalid if any data had changed from what was on the page when it first loaded.

The way we got around the problem was to fire the validation events on jQuery's document ready as well as firing them on the change events for each of the form elements.


~~~javascript

$(document).ready(function(){
   // validation code here as well as on change events for form elements
 });

~~~

Although it does mean that we are calling the validation in more places it has helped us to get around the problem.
