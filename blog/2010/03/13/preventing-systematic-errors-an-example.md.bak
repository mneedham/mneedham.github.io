+++
draft = false
date="2010-03-13 23:26:23"
title="Preventing systematic errors: An example"
tag=['testing']
category=['Testing']
+++

James Shore has <a href="http://jamesshore.com/Blog/Alternatives-to-Acceptance-Testing.html">an interesting recent blog post where he describes some alternatives to over reliance on acceptance testing</a> and one of the ideas that he describes is fixing the process whenever a bug is found in exploratory testing.

He describes two ways of preventing bugs from making it through to exploratory testing:

<ul>
<li>Make the bug impossible</li>
<li>Catch the bug automatically</li>
</ul>

<blockquote>
Sometimes we can prevent defects by changing the design of our system so that type of defect is impossible. For example, if find a defect that's caused by mismatch between UI field lengths and database field lengths, we might change our build to automatically generate the UI field lengths from database metadata.

When we can't make defects impossible, we try to catch them automatically, typically by improving our build or test suite. For example, we might create a test that looks at all of our UI field lengths and checks each one against the database.
</blockquote>

We had an example of the latter this week around some code which loads rules out of a database and then tries to map those rules to classes in the code through use of reflection.

For example a rule might refer to a specific property on an object so if the name of the property in the database doesn't match the name of the property on the object then we end up with an exception.

This hadn't happened before because we hadn't been making many changes to the names of those properties and when we did people generally remembered that if they changed the object then they should change the database script as well.

Having that sort of manual step always seems a bit risky to me since it's prone to human error, so having worked out what was going on we wrote a couple of integration tests to ensure that every property in the database matched up with those in the code.

We couldn't completely eliminate this type of bug in this case because the business wanted to have the rules configurable on the fly via the database.

It perhaps seems quite obvious that we should look to write these types of tests to shorten the feedback loop and allow us to catch problems earlier than we otherwise would but it's easy to forget to do this so James' post provides a good reminder!
