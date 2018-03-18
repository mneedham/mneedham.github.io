+++
draft = false
date="2008-11-28 21:32:28"
title="Html.RadioButton setting all values to selected value workaround"
tag=['aspnet', 'mvc']
category=['.NET']
+++

While working with the Html.RadioButton() UI helper for ASP.NET MVC we came across an interesting problem whereby when you submitted the form, all the values for that particular group of radio buttons was set to the value of the one that was selected.

For example, given a form like this:


~~~csharp

<%= Html.RadioButton("option1", true) %>Yes
<%= Html.RadioButton("option2", false)%>No   
~~~

When we first load the page, this is the HTML it generated:


~~~csharp

<input type="radio" name="option1" value="true" />Yes
<input type="radio" name="option1" value="false" />No
~~~

When we post the form having selected the 'Yes' option for example, this is what the HTML looks like now:


~~~csharp

<input type="radio" name="option1" value="true" checked="checked" />Yes
<input type="radio" name="option1" value="true" />No
~~~

A bit of Googling revealed that <a href="http://stackoverflow.com/questions/277607/htmlradiobutton-sets-all-values-to-selected-value">others</a> have come across this same problem and that it is a <a href="http://forums.asp.net/t/1338576.aspx">bug in the code</a>.

The solution suggested on Stack Overflow was to write a custom RadioButton helper which does a regex replacement on the 'value=' part of the HTMl generated.

We started working down the path to using a similar approach before <a href="http://jamescrisp.org/">James</a> pointed out that we might be able to achieve the same outcome by passing in the value as one of the htmlAttributes.

We changed our original Html.RadioButton() code to take in 'new { value = true }' and 'new { value = false }' respectively and it solved the problem.
