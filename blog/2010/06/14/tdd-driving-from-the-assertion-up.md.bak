+++
draft = false
date="2010-06-14 22:46:00"
title="TDD: Driving from the assertion up"
tag=['testing']
category=['Testing']
+++

About a year ago I wrote a post about <a href="http://www.markhneedham.com/blog/2009/06/20/book-club-the-readability-of-tests-growing-object-oriented-software-steve-freemannat-pryce/">a book club we ran in Sydney covering 'The readability of tests'</a> from Steve Freeman and Nat Pryce's book in which they suggest that their preferred way of writing tests is to drive them from the assertion up:

<blockquote>
Write Tests Backwards

Although we stick to a canonical format for test code, we don't necessarily write tests from top to bottom. What we often do is: write the test name, which helps us decide what we want to achieve; write the call to the target code, which is the entry point for the feature; write the expectations and assertions, so we know what effects the feature should have; and, write the setup and teardown to define the context for the test. Of course, there may be some blurring of these steps to help the compiler, but this sequence reflects how we tend to think through a new unit test. Then we run it and watch it fail.
</blockquote>

At the time I wasn't necessarily convinced that this was the best way to drive but we came across an interesting example today where that approach might have been beneficial.

The test in question was an integration test and we were following the approach of <a href="http://www.markhneedham.com/blog/2008/10/30/testing-hibernate-mappings-setting-up-test-data/">saving the test object directly through the NHibernate session</a> and then loading it again through a repository.

We started the test from the setup of the data and decided to get the mappings and table setup in order to successfully persist the test object first. We didn't write the assertion or repository call in the test initially.

Having got that all working correctly we got back to our test and wrote the rest of it only to realise as we drove out the repository code that we actually needed to create a new object which would be a composition of several objects including our original test object.

We wanted to retrieve a 'Foo' by providing a key and a date - we would retrieve different values depending on the values we provided for those parameters.

This is roughly what the new object looked like:


~~~csharp

public class FooRecord
{
   public Foo Foo { get; set; }
   public FooKey FooKey { get; set; }
   public DateTime OnDate { get; set; } 
}
~~~

'FooRecord' would need to be saved to the session although we would still retrieve 'Foo' from the repository having queried the database for the appropriate one.


~~~csharp

public class FooRepository
{
   public Foo Find(Date onDate, FooKey fooKey)
   {
      // code to query NHibernate which retrieves FooRecords
      // and then filters those to find the one we want
   }
}
~~~

We wouldn't necessarily have discovered this more quickly if we'd driven from the assertion because we'd still have had to start driving the implementation with an incomplete test to avoid any re-work.

I think it would have been more likely that we'd have seen the problem though.
