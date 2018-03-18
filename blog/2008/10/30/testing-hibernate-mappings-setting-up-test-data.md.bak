+++
draft = false
date="2008-10-30 23:24:14"
title="Testing Hibernate mappings: Setting up test data"
tag=['testing', 'hibernate']
category=['Testing', 'Hibernate']
+++

Continuing with my mini Hibernate mappings series, this post talks about the different ways of <strong>setting up the test data</strong> for our Hibernate tests.

<ol>
<li><a href="http://www.markhneedham.com/blog/2008/10/27/testing-hibernate-mappings-where-to-test-from/">Where to test the mappings from?</a></li>
<li><a href="http://www.markhneedham.com/blog/2008/10/29/testing-hibernate-mappings-testing-equality/">How to test for equality?</a></li>
<li>How to setup the test data?</li>
</ol>

There are a couple of ways that we can setup data for Hibernate tests.

<h3>Insert Hibernate Object</h3>
This approach involves creating a new object and saving it to the database using the save method on the <a href="http://www.hibernate.org/hib_docs/v3/api/org/hibernate/Session.html">Hibernate session</a>.

The benefit of this approach is that our test is pretty clean. It looks like any old unit test where we create an object and then check that what we get back is the same object.

The problem is that we are effectively testing two things - the ability to save and then load our Hibernate object. We will be able to tell whether or not our Hibernate mappings are correct using this approach, but the failures we get when they do fail may not be that obvious - it could just be a database exception which makes the test fail.

<h3>SQL Insertion</h3>

The other approach I have seen is to write manual JDBC calls to insert data into the various tables in our database and then check that we can load our object from the database using Hibernate.

The advantage of this is that our test is now only testing the mappings when we load the data from the database which helps reduce our test's invariants or potential points of failure.

The disadvantage is that the tests can seem very brittle - if we make a small change to the column names in our tables then the test setup code may now fail to work anymore. 

I'm not really completely happy with either of these approaches - neither seems optimal to me but both can help us achieve our objective. It's just a matter of choosing which trade off we've prepared to accept.
