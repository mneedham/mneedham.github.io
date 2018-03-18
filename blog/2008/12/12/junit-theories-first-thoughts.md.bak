+++
draft = false
date="2008-12-12 00:34:17"
title="JUnit Theories: First Thoughts"
tag=['theory', 'junit']
category=['Java']
+++

One of my favourite additions to <a href="http://www.testingreflections.com/node/view/5736">JUnit 4.4</a> was the @Theory annotation which allows us to write parameterised tests rather than having to recreate the same test multiple times with different data values or creating one test and iterating through our own collection of data values.

Previously, as far as I'm aware, it was only possible to parameterise tests by using the <a href="http://testng.org/doc/">TestNG</a> library which has some nice ideas around grouping tests but had horrible reporting the last time I used it.

To create parameterisable tests using Theories we need to write some code like the following:


~~~java

import org.junit.Test;
import org.junit.experimental.theories.DataPoints;
import org.junit.experimental.theories.Theories;
import org.junit.experimental.theories.Theory;
import org.junit.runner.RunWith;

@RunWith(Theories.class)
public class SomeTest {
	@Theory
	public void testTheNewTheoriesStuff(int value) {
		// test which involves int value	
	}

	public static @DataPoints int[] values = {1,2,3,4,5};
}
~~~

The 'testTheNewTheoriesStuff' Theory is then executed with each of the values defined in the values array decorated with the @DataPoints annotation.

The error message reported for a failure is reasonably good and makes it quite easy to figure out which one of the data points causes the problem. 

An example error message for an assertion which failed inside a theory might look like this:


~~~text

org.junit.experimental.theories.internal.ParameterizedAssertionError: testTheNewTheoriesStuff(values[1])
~~~

It's 0 indexed so this error message tells us that there was an error when running the theory with the 2nd data point, therefore allowing us to go and work out why that's the case and fix it.

This approach is actually particularly useful for testing the scope in which classes we pull from a dependency injection container are available from in our application.

Another potential use for this would be to test the edge cases of our classes - perhaps this would work best if we can randomise the data it uses.

This seems to be more the approach Microsoft are taking with the the <a href="http://research.microsoft.com/Pex/">Pex</a> framework, a similar idea in the .NET space.
