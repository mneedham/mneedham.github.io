+++
draft = false
date="2008-11-08 02:46:59"
title="Hamcrest Matchers - Make the error message clear"
tag=['java', 'hamcrest']
category=['Java']
+++

We have been making good use of <a href="http://code.google.com/p/hamcrest/">Hamcrest</a> matchers on my current project for making assertions, and have moved almost entirely away from the more traditional JUnit assertEquals approach.

There are several reasons why I find the Hamcrest matcher approach to be more productive - it's more flexible, more expressive and when an assertion fails we have a much better idea about why it has failed than if we use a JUnit assertion for example.

This applies especially when we get a test failing as part of the build as compared to running a test from the IDE where the source code is close at hand and non descriptive error messages may not be such a problem.

It therefore makes sense when writing custom Hamcrest matchers to ensure that we do indeed provide a clear error message so that it is obvious how to fix the test.

The convention seems to be that we should first state the static method name of the matcher and then in brackets list the expected arguments.

To give an example from a matcher we wrote yesterday:


~~~java

import org.hamcrest.Description;
import org.hamcrest.Factory;
import org.hamcrest.TypeSafeMatcher;

public class ContainsAllOf<T> extends TypeSafeMatcher<T> {
    private String[] messages;

    public ContainsAllOf(String... messages) {
        this.messages = messages;
    }

    public void describeTo(Description description) {
        description.appendText("containsAllOf(");
        for (String message : messages) {
            description.appendText(",");
            description.appendValue(message);
        }
        description.appendText(")");
    }

    @Factory
    public static <T> ContainsAllOf containsAllOf(String... messages) {
        return new ContainsAllOf(messages);
    }

    public boolean matchesSafely(T t) {
        return contains(t, messages);
    }

    private boolean contains(T t, String[] messages) {
        boolean containsAllMessages = true;
        for (String message : messages) {
            if (!t.toString().contains(message)) {
                return false;
            }
        }
        return containsAllMessages;
    }

}
~~~

If we call this in our test with a value that doesn't exist:


~~~java

assertThat("mark's cool message", containsAllOf("mark", "cool", "message", "notThere"));
~~~

Running the test results in the following error:


~~~text

java.lang.AssertionError: 
Expected: containsAllOf(,"mark","cool","message","notThere")
     got: "mark's cool message"
~~~

We can easily see what the problem is and how to go about fixing it, which I feel is the most important thing when it comes to test assertions.
