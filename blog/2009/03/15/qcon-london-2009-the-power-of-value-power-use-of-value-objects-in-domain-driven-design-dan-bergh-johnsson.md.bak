+++
draft = false
date="2009-03-15 09:45:19"
title="QCon London 2009: The Power of Value - Power Use of Value Objects in Domain Driven Design - Dan Bergh Johnsson"
tag=['qconlondon', 'qcon', 'infoq']
category=['QCon']
+++

The final <a href="http://qconlondon.com/london-2009/tracks/show_track.jsp?trackOID=228">Domain Driven Design</a> talk I attended at <a href="http://qconlondon.com/london-2009">QCon</a> was by <a href="http://dearjunior.blogspot.com/">Dan Bergh Johnsson</a> about the <a href="http://qconlondon.com/london-2009/presentation/The+Power+of+Value+-+Power+Use+of+Value+Objects+in+Domain+Driven+Design">importance of value objects in our code</a>.

I thought this session fitted in really well as a couple of the previous speakers had spoken of the under utilisation of value objects.

The slides for the presentation are <a href="http://qconlondon.com/london-2009/file?path=/qcon-london-2009/slides/DanBerghJohnsson_ThePowerOfValuePowerUseOfValueObjectsInDomainDrivenDesign.pdf">here</a>.

<h4>What did I learn?</h4>

<ul>
<li>Dan started the talk by outlining the goal for the presentation which was to 'show how power use of value objects can radically change design and code, hopefully for the better'. A lot of the presentation was spent refactoring code written without value objects into shape.</li>
<li>We started out with a brief description of what value objects are not which I found quite amusing. To summarise,<strong>they are not DTOS, not Java beans and not objects with public fields</strong>. The aim with value objects is to <strong>swallow computational complexity</strong> from our entities. Creating what Dan termed 'compound value objects' provides a way to do this. The benefits of doing this are reduced complexity in entities and code which is <strong>more extensible, more testable and has less concurrency issues</strong>.</li>
<li>I found myself quite intrigued as to how you would be able to spot an opportunity in your code to introduce a value object and almost as soon as I wrote down the question Dan covered it! Some opportunities include strings with format limitations, integers with limitations or arguments/results in service methods. The example used was a phone number which was being passed all over the place as a string - refactoring this allowed the code to become <strong>explicit</strong> - before the concept existed but it was never properly spelled out - and it <strong>pulled all the functionality into one place</strong>.</li>
<li>Dan's term for this was '<strong>data as centres of gravity</strong>' - once you have the value object anything related to that data will be drawn towards the object until you have a very useful reusable component. He pointed out that '<strong>your API has 10-30 seconds to direct a programmer to the right spot before they implement it [the functionality] themselves</strong>'. I think this was a fantastic reason for encouraging us to name these objects well as we pretty much only have the amount of time it takes to hit 'Ctrl-N' in IntelliJ, for example, and to type in a potential class name.</li>
<li>Another interesting point which was being <a href="http://twitter.com/rbanks54/statuses/1316885410">discussed</a>	 <a href="http://twitter.com/rbanks54/statuses/1316738208">on</a> <a href="http://search.twitter.com/search?q=&ands=&phrase=&ors=&nots=&tag=&lang=all&from=rbanks54&to=caseycharlton&ref=&near=&within=15&units=mi&since=&until=&source=&rpp=15">twitter</a> as the presentation was going on was whether we should be <strong>going to our domain expert after discovering these value objects and asking them whether these objects made sense to them</strong>. Dan said that this is indeed the best way to go about it. I have to say that what struck me the most across all the presentations was the massive emphasis on getting the domain expert involved all the time.</li>
<li>Seemingly randomly Dan pointed out an approach called <a href="http://www.qi4j.org/">composite oriented programming</a> which is all about using DDD terminology but inside a framework to drive development. I've only had a brief look at the website so I'm not sure if it's anything worth shouting about.</li>
<li>In the second half of the session <strong>compound value objects</strong> were introduced - these basically encapsulate other value objects to come up with even more explicitly named objects. The examples in the <a href="http://qconlondon.com/london-2009/file?path=/qcon-london-2009/slides/DanBerghJohnsson_ThePowerOfValuePowerUseOfValueObjectsInDomainDrivenDesign.pdf">slides</a> are very useful for understanding the ideas here so I'd recommend having a look from slide 44 onwards. The underlying idea is to encapsulate multi object behaviour and context and make implicit context explicit. This idea is certainly one that is new to me so I'm going to be looking at our code base to see if there's an opportunity to introduce the ideas I learnt in this talk.</li>
<li>To close Dan rounded up the benefits we get from introducing value objects into our code - <strong>context aware client code, smart services and a library with an API</strong>.</li>
</ul>
