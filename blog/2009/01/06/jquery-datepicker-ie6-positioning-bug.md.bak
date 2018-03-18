+++
draft = false
date="2009-01-06 21:57:06"
title="jQuery datepicker IE6 positioning bug"
tag=['jquery', 'ie6']
category=['jQuery']
+++

We've been using the <a href="http://docs.jquery.com/UI/Datepicker">jQuery datepicker</a> on my current project and came across some strange behaviour with regards to the positioning of the calendar in IE6.

The calendar was always positioning itself right at the top of the screen instead of just below the textbox it was hooked up to but in Firefox it was working fine.

After a bit of exploration in the jQuery code (<a href="http://ui.jquery.com/latest/ui/ui.datepicker.js">ui.datepicker.js</a>) we worked out that the 'document.documentElement.clientHeight' call in the '_checkOffset' function was always returning a value of 0 meaning that the position of the calendar was always right at the top of the screen.


~~~text

_checkOffset: function(inst, offset, isFixed) {
		var pos = inst.input ? this._findPos(inst.input[0]) : null;
		var browserWidth = window.innerWidth || document.documentElement.clientWidth;
		var browserHeight = window.innerHeight || document.documentElement.clientHeight;
...
~~~

It turned that we were missing the doctype at the top of the HTML page which make the page standards compliant and as a result document.documentElement.clientHeight returns the proper height.


~~~text

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"	"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">

~~~

Not having this set puts IE into Quirks Mode meaning that document.documentElement.clientHeight  always returns 0. 

We found a post on the Webmaster World Forum which helps explain <a href="http://www.webmasterworld.com/forum21/11096.htm">why this change makes a difference</a>.
