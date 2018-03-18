+++
draft = false
date="2011-10-30 22:32:16"
title="Canonical Identifiers"
tag=['software-development']
category=['Software Development']
+++

<a href="http://duncan-cragg.org/blog/">Duncan</a> and I had an interesting problem recently where we had to make it possible to search within an 'item' to find possible sub items that exist inside it.

The <a href="http://en.wikipedia.org/wiki/Uniform_Resource_Identifier">URI</a> for the item was something like this:


~~~text

/items/234
~~~

Let's say Item 234 contains the following sub items:

<ul>
<li>Mark</li>
<li>duncan</li>
</ul>

We have a search box on the page which allows us to type in the name of a sub item and go the sub item's page if it exists or see an error message if it doesn't.

If the user types in the sub item name exactly right then there's no problem:


~~~text

items/234?subItem=Mark
~~~

redirects to:


~~~text

items/234/subItem/Mark
~~~

It becomes more interesting if the user gets the case of the sub item wrong e.g. they type 'mark' instead of 'Mark'.

It's not very friendly in terms of user experience to give the user an error message if they do that so I suggested that we just make the look up of the sub item case insensitive 


~~~text

items/234/subItem/mark
~~~

would therefore find us the 'Mark' sub item. 

Duncan pointed out that we'd now have more than 1 URI for the same document which isn't particularly great since theoretically there should be a one to one mapping between a URI and a given document.

He pointed out that we could do a look up to find the 'canonical identifier' before we did the redirect such that if you typed in 'mark':


~~~text

items/234?subItem=mark
~~~

would redirect to:


~~~text

items/234/subItem/Mark
~~~

The logic for checking the existence of a sub item would be the bit that's case insensitive and makes it more user friendly.
