+++
draft = false
date="2009-07-30 00:59:18"
title="Book Club: Hexagonal Architecture (Alistair Cockburn)"
tag=['book-club', 'hexagonal-architecture']
category=['Book Club']
+++

In our latest book club we discussed Alistair Cockburn's <a href="http://alistair.cockburn.us/Hexagonal+architecture">Hexagonal Architecture</a> which I first heard about <a href="http://www.markhneedham.com/blog/2008/09/01/my-software-development-journey-so-far/">around a year ago</a> and was another of <a href="http://intwoplacesatonce.com/">Dave Cameron</a>'s recommendations.

As I understand it, the article describes an architecture for our systems where the domain sits in the centre and other parts of the system depend on the domain while the domain doesn't depend on anything concrete but is interacted with by various adapters.

These are some of my thoughts and our discussion of the article:

<ul>
<li>It seems like the collection of adapters that Cockburn describes as interacting with the 'application' form lots of different <a href="http://www.markhneedham.com/blog/2009/07/07/domain-driven-design-anti-corruption-layer/">anti corruption layers</a> in Domain Driven Design language. 

I think tools like <a href="http://www.codeplex.com/AutoMapper">Automapper</a> and <a href="http://www.codeplex.com/Json">JSON.NET</a> might be useful when writing some of these adaptors although <a href="http://intwoplacesatonce.com/">Dave</a> pointed out that we need to be careful that we're not just copying every bit of data between different representations of our model otherwise we are indirectly creating the coupling that we intended to avoid.</li>
<li>I was intrigued as to how rich user interfaces which have a lot of javascript in them would fit into the idea of mainly testing the application via the API and from our discussion we came to the conclusion that perhaps the javascript code would be an application by itself which server side code would interact with by using an adaptor. 

This seems to lead towards an understanding of code as consisting of <strong>lots of different hexagons which interact with each other</strong> through pipes and filters.</li>
<li>Dave described how designing our code according to the hexagonal architecture can help us <strong>avoid the zone of pain</strong> whereby we have lots of concrete classes inside a package and a lot of other packages depending on us. Scott Hanselman <a href="http://www.hanselman.com/blog/ExitingTheZoneOfPainStaticAnalysisWithNDepend.aspx">discusses this concept as part of a post on the different graphs & metrics NDepend provides</a>.

From my understanding the idea seems to be to try not to have our application depending on unstable packages such as the data layer which we might decide to change and will have great difficulty in doing so if it is heavily coupled to our business code. Instead we should look to rely on an abstraction which sits inside the domain package and is implemented by one of the adaptors. I haven't read the whole paper but it sounds quite similar to Uncle Bob's <a href="http://www.objectmentor.com/resources/articles/stability.pdf">Stable Dependencies Principle</a>.</li>
<li>I'm not sure whether these applications are following the hexagonal architecture but <a href="http://apiwiki.twitter.com/">twitter</a>, <a href="http://code.google.com/apis/maps/">Google Maps</a> and <a href="http://codex.wordpress.org/Plugin_API">WordPress</a> all have APIs which provide us with the ability to drive at least some part of their applications using adaptors that we need to write. This seems to be the way that quite a few applications are going which I imagine would influence the way that they organise their code in some way. In twitter's case the external adaptors that drive their application are the main source of use. </li>
</ul>

