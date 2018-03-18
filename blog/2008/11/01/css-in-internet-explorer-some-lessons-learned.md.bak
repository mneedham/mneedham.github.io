+++
draft = false
date="2008-11-01 01:24:51"
title="CSS in Internet Explorer - Some lessons learned"
tag=['css']
category=['Software Development']
+++

I've spent the last few days working with CSS, and in particular trying to make a layout which works perfectly fine in Firefox work properly in Internet Explorer 6.

I'm far from an expert when it comes to this but I've picked up a few lessons from our attempts to get identical layouts in both browsers.

<ul>
<li>
Internet Explorer seems to do some crazy stuff when it comes to <a href="http://www.webcredible.co.uk/user-friendly-resources/css/internet-explorer.shtml">padding and margins</a> - we were often ending up with huge margins where we hadn't even specified any. A useful approach pointed out by <a href="http://www.workingwithrails.com/person/8781-josh-price">Josh</a> was <strong>resetting the margin and padding for the whole page</strong> so that IE's default padding was removed.

Putting the following code in your style sheet will do this:


~~~css

* {padding:0;margin:0}
~~~
</li>
<li>Despite the fact that we start with IE and Firefox on an even keel, there were still differences in how they rendered some spacings that we tried to apply. I don't think this is necessarily a good long term fix but it seems that <strong>if you start a property name with an underscore IE will respect it but Firefox will ignore it</strong>. This is known as the <a href="http://www.wellstyled.com/css-underscore-hack.html">MSIE underscore hack</a>, which describes it fairly accurately! We can therefore set up IE only CSS properties like this:


~~~css

_margin: 0 0 2px 0;  
~~~
</li>
<li>One of the other problems we came across was the <a href="http://www.positioniseverything.net/explorer/peekaboo.html">hidden text bug</a> - sometimes when we refreshed the page text inside a floating div would just disappear until you selected it with the mouse when it would reappear. We found a <a href="http://www.satzansatz.de/cssd/onhavinglayout.html">couple</a> of <a href="http://plone.org/documentation/how-to/internet-explorer-invisible-text">posts</a> which explained that the problem was being caused by IE not correctly setting the element size for floating elements on the page. 

The other posts go into more detail, but the fix that worked for us involved <strong>forcing IE into layout mode</strong> by applying a small height to the element that was being hidden:


~~~css

.visualIEFloatFix {
    height: 0.01%; 
}
~~~

</li>
</ul>

I'm sure there will be further learnings on my CSS travels - I've been trying to find some resources which describe good patterns to use with CSS but I've only come across a book called <a href="http://cssdesignpatterns.com/">Pro CSS and HTML Design Patterns</a> so far. 

Anyone know if this book is any good or if not what a better alternative is?
