+++
draft = false
date="2013-02-28 00:00:03"
title="Micro Services: Where does the complexity go?"
tag=['micro-services-2']
category=['Micro Services']
+++

<p>For the past year every system that I've worked on has been designed around a micro services architecture and while there are <a href="http://www.infoq.com/presentations/Micro-Services">benefits with this approach</a> there is an inherent complexity in software which has to go somewhere!</p>


<p>I thought it'd be interesting to run through some of the new complexities that I've noticed in what may well be an acknowledgement of the difficulty of designing distributed systems.</p>


<h4>Interactions between components</h4>

<p>One of the advantages of having lots of small applications is that each one is conceptually easier to understand and we only need to keep the mental model of how that one application works when we're working on it.</p>


<p>With the big monolithic application all the code is together which makes it more difficult to make that separation and completely different concepts can end up getting mashed together.</p>


<p>On the other hand there is now complexity in the interactions between the applications which will often communicate with each other over HTTP using JSON/XML messages.</p>


<p>We now need to be careful how you go about changing these messages because we can easily break a client of out service if we change the name of a field for example.</p>


<p>That can be solved by running two versions of the service but that means we have the burden of maintaining two versions of the service!</p>


<h4>Understanding how everything fits together</h4>

<p>Despite the fact that you can choose to focus on one component at a time there are occasions where you need to know how everything works together.</p>


<p>For example we recently wanted to make changes to the way data is displayed on our results page.</p>
 

<p>This involved making changes to a backend CMS, making sure those propagated to a database which another service used, making sure the service's client could handle the new fields we added and handling the new fields on the web front end.</p>


<p>In a big monolithic system we might use an IDE to help us navigate around the code and see how everything fitted together whereas when we have separate applications the only tool we have is text search!</p>


<h4>Deployment</h4>

<p>Although in some ways deployment is easier because we don't have to deploy everything when we make a small change, in some ways it's more complicated because we have more moving parts.</p>


<p>We need to deploy components in the right order otherwise we'll end up deploying a component which relies on getting a certain value from another component which it doesn't get because the other component's out of date.</p>


<p>Another thing to look out for is that we don't make our services too fine grained otherwise we'll end up being overwhelmed by how many applications we actually have to deploy.</p>


<h4>Micro services are still cool!</h4>

<p>Despite these disadvantages it wouldn't have been possible to have our teams setup the way they are without splitting capabilities in this way.</p>


<p>We have 10 developers in 3 teams working across ~25 different applications. There's some overlap between the applications but each team owns about 1/3 of the repositories and they tend to dominate the commits on there.</p>


<p>Another neat thing about the micro services approach is that it's very easy to see which things need to happen in real time on the web application and which can be processed offline at a later stage.</p>


<p>I'm sure there are many more things to watch out for when choosing to design a distributed system but these are the things I've picked up in my short amount of time working in this area!</p>

