+++
draft = false
date="2009-08-17 21:12:26"
title="Law of Demeter: Some thoughts"
tag=['coding', 'law-of-demeter']
category=['Coding']
+++

<a href="http://haacked.com/">Phil Haack</a> <a href="http://haacked.com/archive/2009/07/14/law-of-demeter-dot-counting.aspx">wrote a post a few weeks ago about the law of demeter</a> and how it's not just about reducing the number of dots that appear on one line.

This is a nice side effect of following the law of demeter but I often feel that the main benefit we get from following it is that code becomes <a href="http://www.markhneedham.com/blog/2009/03/12/oo-reducing-the-cost-oflots-of-stuff/">easier to change</a> since we haven't exposed the state of an object all over the place.

I think there are two parts to the law of demeter:

<ol>
<li>That we don't dig into the internals of objects to retrieve the data we want i.e. 'foo.bar.baz.qux' in Phil's example but instead create methods on the top level object which delegate to get us the data that we need. In this case we might have 'foo.bar_baz_qux' for example.</li>
<li>That we follow <a href="http://www.pragprog.com/articles/tell-dont-ask">tell don't ask</a> and never retrieve data from an object and then do something with that data, but instead tell the object to do something for us.</li>
</ol>

The second is harder to find fault with and is generally considered good design. <a href="http://www.dcmanges.com/blog/37">Dan Manges' post on this</a> is the best piece of writing I've seen on the subject - definitely worth reading.

The first definitely seems to be more contentious from what I've noticed and it seems like we mostly run into trouble when it comes to the boundaries of our domain layer e.g. interacting with a user interface or with another system.

<h3>Getting data onto the view</h3>

The user interface is an interesting place to start because the majority of applications we write have to interact with the user somehow and then we need to work out how we're going to display information to them.

Every web framework I've worked with makes use of template style pages to display data so we need to somehow get the data out of our domain objects and into these templates.

I've come across a few ways to do this:

<h4>Directly exposing domain objects</h4>
The first and perhaps most obvious way is to expose domain objects to the view directly but when we use this approach I think we need to be careful that we don't end up inadvertently putting domain logic into the view.

I think it's also quite important to make sure that we only expose read only versions of properties of our objects if we choose to take this approach otherwise our objects will become really difficult to understand. <a href="http://www.infoq.com/articles/dhanji-prasanna-concurrency">Dhanji Prasanna has an interesting article about immutability in our code</a> which I think applies here.

The other problem is that once you start exposing properties/getters on your objects then the temptation is there to make use of these properties from other places in our code whereby we run the risk of breaking the idea of tell don't ask.

Once we do this the difficulty of maintaining code seems to increase quite substantially so if we can avoid that happening it's a good thing.

<h4>View Data Container</h4>

An alternative is to make use of a 'ViewData' container which I mentioned briefly on <a href="http://www.markhneedham.com/blog/2009/03/10/oo-micro-types/">a post I wrote about micro types</a>. 

The idea here is that our objects can write themselves into the 'ViewData' container which is then made accessible from the view. The view can then take whichever data it is interested out of the container.

Although this approach reduces the explicit coupling between a view and a domain object it seems to create an implicit coupling between them since the view needs to know what names the domain object has given to each of the things it puts into the container.

I like this approach although I'm not sure how well it would work if we had a lot of data to display.

<h4>DTOs/View Model</h4>
We can also make use of <a href="http://en.wikipedia.org/wiki/Data_transfer_object">DTOs</a> which are weak objects with getters/setters where we can put data that we want to display on the view. 

An alternative we're using on my project which seems like a variation of this is to return a JSON object which generally only contains the fields that we are interested in seeing from a user perspective. We do have some places where we are making use of a JSON serializer to return an exact version of an object as JSON.

The problem when using DTOs is that we can end up writing a lot of translation code which is quite boring and which from my experience <a href="http://www.markhneedham.com/blog/2009/04/02/tdd-testing-mapping-code/">people are reluctant to test</a>. 

I guess tools like <a href="http://www.codeplex.com/AutoMapper">AutoMapper</a> and <a href="http://www.codeplex.com/json">JSON.NET</a> can help to remove this problem although a recent conversation with my colleague Lu Ning leads me to believe that we need to consider the value that we will get from using a DTO compared to just making use of a domain object directly from the view.

This is particularly true if there is not much difference between the domain model and the model of the domain that the user interacts with and if that is the case that it might make more sense to just expose the domain model directly.

Greg Young has taken this to the extreme with <a href="http://www.infoq.com/presentations/greg-young-unshackle-qcon08">his idea of Command Query Separation at the architecture level</a> whereby we would have a write only domain model on one side and then just fill DTOs effectively representing the user's view of the data on the other side. 

<h3>In summary</h3>
I'm not sure which is my favourite approach of the ones that I've come across - none of them seems quite right to me.

I quite like the idea of domain objects rendering themselves which can be done to some extent by using my colleague Alistair Jones' <a href="http://code.google.com/p/hypirinha/">Hyprinha</a> framework and in the Smalltalk <a href="http://www.seaside.st/">Seaside</a> framework although I would be interested how these frameworks would work with javascript intensive websites.
