+++
draft = false
date="2010-03-19 18:06:51"
title="TDD: Expressive test names"
tag=['tdd']
category=['Testing']
+++

Towards the end of <a href="http://www.markhneedham.com/blog/2009/01/30/tdd-test-dryness/">a post I wrote just over a year ago</a> I suggested that I wasn't really bothered about test names anymore because I could learn what I wanted from reading the test body.

Recently, however, I've come across several tests that I wrote previously which were testing the wrong thing and had such generic test names that it wasn't obvious that it was happening.

The tests in question were around code which partially clones an object but doesn't copy some fields for various reasons.

Instead of documenting these reasons I had written tests with names like this:


~~~csharp

[Test]
public void ShouldCloneFooCorrectly() { }
~~~


~~~csharp

[Test]
public void ShouldSetupFooCorrectly() { }
~~~

When we realised that the code wasn't working correctly, which didn't happen until QA testing, these test names were really useless because they didn't express the intent of what we were trying to test at all.

<a href="http://foldingair.blogspot.com/">Damian</a> and i spent some time writing more fine grained tests which described <strong>why</strong> the code was written the way it was.

We also changed the name of the test fixture to be more descriptive as well:


~~~csharp

[TestFixture]
public class WhenCloningFooTests
{
	[Test]
	public void ShouldNotCloneIdBecauseWeWantANewOneAssignedInTheDatabase() { }

	[Test]
	public void ShouldNotCopyCompletedFlagBecauseWeWantTheFooCompletionJobToPickItUp() { 	
}
~~~

It seems to me that these new tests names are more useful as <a href="http://blog.orfjackal.net/2010/02/three-styles-of-naming-tests.html">specifications of the system behaviour</a> although we didn't go as far as you can with some frameworks where you can create base classes and separate methods to describe the different parts of a test.

Despite that I think naming tests in this way can be quite useful so I'm going to try and write more of my tests like this.

Of course it's still possible to test the wrong thing even if you are using more expressive names but I think it will make it less likely.
