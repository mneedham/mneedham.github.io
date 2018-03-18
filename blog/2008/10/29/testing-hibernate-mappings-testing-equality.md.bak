+++
draft = false
date="2008-10-29 18:03:36"
title="Testing Hibernate mappings: Testing Equality"
tag=['testing', 'hibernate']
category=['Testing', 'Hibernate']
+++

I started a mini Hibernate series with <a href="http://www.markhneedham.com/blog/2008/10/27/testing-hibernate-mappings-where-to-test-from/">my last post</a> where I spoke of there being three main areas to think about when it comes to testing:

<ol>
<li><a href="http://www.markhneedham.com/blog/2008/10/27/testing-hibernate-mappings-where-to-test-from/">Where to test the mappings from?</a></li>
<li>How to test for equality?</li>
<li>How to setup the test data?</li>
</ol>

Once we have worked out where to test the mappings from, if we have decided to test them through either our repository tests or directly from the Hibernate session then we have some choices to make around how to test for equality.

I've seen this done in several ways:

<h3>Override equals</h3>
This was the first approach I saw and in a way it does make some sort of sense to test like this.

We don't have to expose any of the internals of the class and we can get feedback on whether our objects have the same fields values or not. In addition we can normally get the IDE to generate the code for the equals method so it doesn't require much extra effort on our behalf. 

Typically an equality test along these lines would look something like this:


~~~java

@Entity
public class Foo {
	@Column(name="BAR")
	private String bar;

	public Foo(String bar) {
		this.bar = bar;
	}

    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;

        Foo foo = (Foo) o;

        return !(bar != null ? !bar.equals(foo.bar) : foo.bar != null);

    }
}
~~~


~~~java

import static org.hamcrest.MatcherAssert.assertThat;
...
Foo expectedFoo = new Foo("barValue");
Foo foo = getFooFromHibernate();

assertThat(foo, equalTo(expectedFoo));
~~~

The problem with this approach is that objects which are in Hibernate are likely to be <a href="http://domaindrivendesign.org/discussion/messageboardarchive/Entities.html">entities</a> and therefore their equality really depends on whether or not they have the same identity, not whether they have the same values. Therefore our equals method on the object should only compare the id value of the object to determine equality.

Implementing the equals method just for testing purposes may also be considered a code smell.

<h3>Getters</h3>

This approach involves adding getters to our objects to check that the values of each field have been set correctly.

While this approach is marginally better than not testing the mappings at all, the temptation to then use these getters in other pieces of the code can lead to us having <a href="http://www.martinfowler.com/bliki/AnemicDomainModel.html">objects with no behaviour at all</a> with our logic spread all over the application.


~~~java

@Entity
public class Foo {
	@Column(name="BAR")
	private String bar;

	public Foo(String bar) {
		this.bar = bar;
	}

	public getBar() {
		return this.bar;
	}
}
~~~


~~~java

import static org.hamcrest.MatcherAssert.assertThat;
...
String bar = "barValue";
Foo foo = getFooFromHibernate();

assertThat(foo.getBar(), equalTo(bar));
~~~

<h3>Reflection</h3>
An approach I was introduced to recently involves using reflection to check that Hibernate has hydrated our objects correctly.

We initially rolled our own 'Encapsulation Breaker' to achieve this before realising that the <a href="http://www.ognl.org/">OGNL</a> library did exactly what we wanted to do.

By adding a custom <a href="http://code.google.com/p/hamcrest/wiki/Tutorial">Hamcrest</a> matcher into the mix we end up with quite a nice test for verifying whether our mappings are working correctly.


~~~java

@Entity
public class Foo {
	@Column(name="BAR")
	private String bar;
}
~~~


~~~java

import static org.hamcrest.MatcherAssert.assertThat;
...
Foo foo = getFooFromHibernate();
assertThat(foo, hasMapping("bar", equalTo("someValue")));
~~~


~~~java

public class HasMapping<T> extends BaseMatcher<T> {
    private String mapping;
    private Matcher<T> mappingValueMatcher;

    public HasMapping(String mapping, Matcher<T> mappingValueMatcher) {
        this.mapping = mapping;
        this.mappingValueMatcher = mappingValueMatcher;
    }

    public void describeTo(Description description) {
        description.appendText("A mapping from ");
        description.appendText(mapping);
        description.appendText(" that matches ");
        valueMatcher.describeTo( description );
    }

    @Factory
    public static <T> HasMapping hasMapping(String mapping, Matcher<T> mappingValueMatcher) {
        return new HasMapping(mapping, mappingValueMatcher);
    }

    public boolean matches(Object o) {
        try {
            Object value = OgnlWrapper.getValue(mapping, o);
            return mappingValueMatcher.matches(value);
        } catch (OgnlException e) {
            return false;
        }
    }

}
~~~

The drawback of this approach is that if we change the names of the fields on our objects we need to make a change to our test to reflect the new names.

I ran into the <a href="http://blog.jayfields.com/2008/03/example-dilemma.html">example dilemma</a> a bit while writing this but hopefully the ideas have been expressed in the code presented. I didn't want to put too much code in this post but if you're interested in what the OgnlWrapper does I posted more about this on my post about <a href="http://www.markhneedham.com/blog/2008/10/23/keep-java-checked-exceptions-in-a-bounded-context/">Java checked exceptions</a>.
