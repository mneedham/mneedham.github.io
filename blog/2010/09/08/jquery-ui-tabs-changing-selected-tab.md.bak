+++
draft = false
date="2010-09-08 18:32:37"
title="jQuery UI Tabs: Changing selected tab"
tag=['jquery']
category=['jQuery']
+++

We're using the <a href="http://jqueryui.com/demos/tabs/">tabs part of the jQuery UI library</a> on the project I'm currently working on and one thing we wanted to do was change the default tab that was being selected. 

The documentation suggested that one way to do this was to give the index of the tab we wanted selected when calling the tabs function:


~~~javascript

$( ".selector" ).tabs({ selected: 3 });
~~~

Since we wanted to select the tab by name based on a value from the query string we thought it would probably be simpler if we could just set the selected tab using a css class.

Our initial thought was that we could put the 'ui-tabs-hide' class on the divs that we wanted to hide and then not put that class on the one that we wanted to show.

Unfortunately that didn't work and the first tab was still being selected...

We downloaded version <a href="http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.2/jquery-ui.js">1.8.2</a> of the library  via <a href="http://code.google.com/apis/libraries/devguide.html#jqueryUI">Google's CDN</a> (which seems really cool!) and were able to see that our class was actually intentionally being removed!


~~~javascript

if (o.selected >= 0 && this.anchors.length) { // check for length avoids error when initializing empty list
				this.panels.eq(o.selected).removeClass('ui-tabs-hide');
~~~

Luckily a little further down the file there is a comment which explains some other ways to manipulate the selected tab:


~~~javascript

			// Selected tab
			// use "selected" option or try to retrieve:
			// 1. from fragment identifier in url
			// 2. from cookie
			// 3. from selected class attribute on <li>
~~~

We need to put the class 'ui-tabs-selected' on the appropriate <li> and then that will be the one that gets selected.


