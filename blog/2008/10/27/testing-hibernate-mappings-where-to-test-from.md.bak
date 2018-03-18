+++
draft = false
date="2008-10-27 22:55:15"
title="Testing Hibernate mappings: Where to test from?"
tag=['tdd', 'testing', 'hibernate']
category=['Testing', 'Hibernate']
+++

I've had the opportunity to work with <a href="http://www.hibernate.org/">Hibernate</a> and it's .NET twin <a href="http://sourceforge.net/projects/nhibernate">NHibernate</a> on several of my projects and one of the more interesting decisions around its use is working out the best way to test the hibernate mappings that hook together our domain model and the database.

There are three decisions to make around how best to do this:

<ol>
<li>Where to test the mappings from?</li>
<li>How to test for equality?</li>
<li>How to setup the test data?</li>
</ol>

This post will focus on the ways I have seen with regards to choosing <strong>where to test the mappings from</strong>.

<h3>Functional Tests</h3>

This approach advocates only testing whether we have setup the mappings correctly when we run our acceptance or functional tests - we do not write tests specifically for testing hibernate mappings.

The benefit of this approach is that we are more likely to have acceptance tests in place, so this is just another thing that they can be used to catch.

While this approach is better than not testing at all, from my experiences the test feedback cycle is too slow - it takes too long to change one of the hibernate mappings and then run the test to check if it worked or not.

<h3>Repository Tests</h3>

With this approach we test whether our hibernate mappings are working as part of our <a href="http://domaindrivendesign.org/discussion/messageboardarchive/Repositories.html">repository</a> tests.

The tricky thing with testing our hibernate mappings this way is that typically we only want to set up one object in the database and then test that Hibernate hydrates it correctly, but our repository doesn't necessarily need a method for finding a single object.

We either end up adding on a method just for testing or we have to try and find our object from a list of other objects and then test it.

On the other hand, this approach does seem to work quite well when we have quite chatty repositories which provide a degree of flexibility around how we can retrieve our objects.

<h3>Direct Tests</h3>

This approach is my current favourite and involves loading the object directly from the <a href="http://www.hibernate.org/hib_docs/v3/api/org/hibernate/Session.html">Hibernate session</a> and then testing it.

I was introduced to this idea by a <a href="http://www.flickr.com/photos/adsphoto/">colleague</a> of mine and it seems to fit the idea of testing just one thing more closely than the other two approaches.

The strange thing about this approach is that we are testing directly with an API that is hidden from our system beyond the Repository.

In terms of simplicity with regards to testing hibernate mappings, however, this is the best approach I have seen.

---

I did a quick survey of some people last week and the most popular way of testing the mappings expressed was using Repository tests.

This post covers the other ways I have seen - are there any others people have come across or are using?
