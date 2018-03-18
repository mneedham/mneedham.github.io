+++
draft = false
date="2009-03-31 23:15:28"
title="Pair Programming: Slowly but surely"
tag=['pair-programming']
category=['Pair Programming']
+++

I recently watched a <a href="http://devlicio.us/blogs/sergio_pereira/archive/2009/02/14/video-xp-after-10-years-why-are-we-still-talking-about-it.aspx">video recorded by Uncle Bob at the Chicago Alt.NET meeting</a> where amongst other things he talked about the importance of <strong>going slowly but surely when we're developing code</strong> i.e. spending the time to get it right first time instead of rushing through and having to go back and fix our mistakes.

While pairing with a colleague recently it became clear to me that pair programming, when done well, drives you towards a state where you are being much more careful about the work being produced.

Two particular parts of our pairing session made this stand out for me.

<ol>
<li>We were trying to work out the best way to get some data from the UI into our application. I had an idea of the best way to do this but my pair pointed out an alternative which I originally thought would might our tasks more difficult.


After talking through the different approaches and trying out the alternative approach in code it actually turned out that my colleagues' approach led to a much simpler solution and we were able to get that part of our task done much more quickly than I had anticipated.
</li>
<li>A bit later we were writing some tests for getting this data into our application using an <a href="">ASP.NET MVC binder</a>. Not not knowing exactly how to do this I decided to go for the obvious implementation and then triangulate this with the second test. 

It was a bit painful putting this hardcoding in to make the test pass and I was starting to wonder whether just going ahead and implementing the binding properly would have been preferable.

As we got to the fifth field we needed to bind we realised that we had no way of getting an additional piece of data that we needed. Luckily we hadn't gone too far down the route we were heading so it was quite easy to go and make the changes to the UI to ensure we could get the extra bit of data that we needed.

As a result of us having to stop and actually look back at what we'd just coded it became clear that we could simplify our approach further, so we did! 

The resulting code was much different and eventually cleaner than the original solution we were driving to.</li>
</ol>

Taking our time over our code is something which is invaluable - nearly every time I take a short cut or try to do something without thinking about it properly it ends up taking longer than it would if done properly - the somewhat ironic outcome that Uncle Bob points out in the video.

When we are pairing if we want to take one of these shortcuts we need to convince our pair as well as ourself and from my experience we tend to realise that what we're suggesting doesn't make sense and end up coding a better solution.

That's not to say that we sometimes don't have to take the pragmatic approach and not do a bit of refactoring until later so we can get features completed. After all that is what we are being paid to do.

Software development for me is a lot more about thinking through our options than coding the first thing that comes to mind and pair programming helps drive this approach to problem solving.
