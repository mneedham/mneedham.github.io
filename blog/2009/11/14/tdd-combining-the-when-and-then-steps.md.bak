+++
draft = false
date="2009-11-14 00:17:57"
title="TDD: Combining the when and then steps"
tag=['testing']
category=['Testing']
+++

I've written before about <a href="http://www.markhneedham.com/blog/2009/04/13/tdd-balancing-dryness-and-readability/">my favoured approach of writing tests in such a way that they have clear 'Given/When/Then' sections</a> and something which I come across quite frequently is tests where the latter steps have been combined into one method call which takes care of both of these.

An example of this which I came across recently was roughly like this:


~~~java

@Test
public void shouldCalculatePercentageDifferences() {
	verifyPercentage(50, 100, 100);
	verifyPercentage(100, 100, 0);
	verifyPercentage(100, 50, -50);
}
~~~


~~~java

private void verifyPercentage(int originalValue, int newValue, int expectedValue) {
	assertEquals(expectedValue, new PercentageCalculator().calculatePercentage(originalValue, newValue));
}
~~~

This code is certainly adhering to the DRY principle although it took us quite a while to work out what the different numbers being passed into 'verifyPercentage' were supposed to represent.

With this type of test I think it makes more sense to have a bit of duplication to make it easier for us to understand the test.

We changed this test to have its assertions inline and make use of the <a href="http://code.google.com/p/hamcrest/">Hamcrest</a> library to do those assertions:


~~~java

@Test
public void shouldCalculatePercentageDifferences() {
	assertThat(new PercentageCalculator().calculatePercentage(50, 100), is(100));
	assertThat(new PercentageCalculator().calculatePercentage(100, 100), is(0));
	assertThat(new PercentageCalculator().calculatePercentage(100, 50), is(-50));
}
~~~

I think we may have also created a field to instantiate 'PercentageCalculator' so that we didn't have to instantiate that three times.

Although we end up writing more code than in the first example I don't think it's a problem because it's now easier to understand and we'll be able to resolve any failures more quickly than we were able to previously.

As Michael Feathers points out during Jay Fields' '<a href="http://blog.jayfields.com/2009/06/developer-testing-welcome-to-beta-test.html">Beta Test</a>' presentation we need to remember why we try and adhere to the <a href="http://en.wikipedia.org/wiki/Don%27t_repeat_yourself">DRY principle</a> in the first place.

To paraphrase his comments:

<blockquote>
In production code if we don't adhere to the DRY principle then we might make a change to a piece of code and we won't know if there's another place where we need to make a change as well.

In test code the tests always tell us where we need to make changes because the tests will break.
</blockquote>
