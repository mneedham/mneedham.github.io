+++
draft = false
date="2013-02-28 22:23:27"
title="Vertical/Horizontal Slicing"
tag=['software-development']
category=['Software Development']
+++

<p>A few years ago I wrote a bunch of posts <a href="http://www.markhneedham.com/blog/2010/03/02/riskiest-thing-first-vs-outside-in-development/">exploring</a> <a href="http://www.markhneedham.com/blog/2010/04/18/coding-another-outside-in-example/">my experiences</a> <a href="http://www.markhneedham.com/blog/2009/12/19/coding-an-outside-in-observation/">of outside in development</a> eventually coming to the conclusion that it seemed to make sense to drive out functionality from the UI and work back from there.</p>


<p>i.e. we take a vertical slice of functionality and then drive it end to end.</p>


<p>On the team I'm working on there's been success using an approach where the functionality is still split vertically but we work across a horizontal layer for all the cards before moving onto the next layer.</p>


<p>The advantage of this approach is that <strong>we can do all the work in one layer without context switching</strong> and then move onto the next layer.</p>


<p>In our case this meant adding a bunch of text and check boxes to a backend CMS and then making sure that the values entered there bubbled their way up to a service used by the front end.</p>


<p>This was counter to my previous experience so I was curious why we weren't seeing the problems that I'd seen before where we'd model things incorrectly in the backend and only realise when we tried to call them from the front end.</p>
 

<p><a href="http://www.linkedin.com/search/fpsearch?fname=Jae&lname=Lee&keepFacets=Y&facet_G=gb%3A0&pplSearchOrigin=TSEO_SN&trk=TSEO_SN">Jae</a> pointed out that you don't necessarily run into this problem <strong>if you can hold the model of how the whole system fits together in your head</strong>.</p>


<p>Since we have a few people who are able to do that and have knowledge of how the data flows through the different applications that is indeed the case!</p>


<p>I'm sure there are some other cases where this approach makes more sense so if you find success writing code in this style do let me know!</p>

