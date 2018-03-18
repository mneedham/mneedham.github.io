+++
draft = false
date="2008-09-24 05:11:20"
title="Testing with Joda Time"
tag=['testing', 'java', 'date', 'joda']
category=['Java']
+++

The alternative to dealing with java.util.Date which <a href="http://www.markhneedham.com/blog/2008/09/18/using-javautildate-safely/">I wrote about in a previous post</a> is to make use of the <a href="http://joda-time.sourceforge.net">Joda Time</a> library. I'm led to believe that a lot of the ideas from Joda Time will in fact be in <a href="http://jcp.org/en/jsr/detail?id=310">Java 7</a>.

Nevertheless when testing with Joda Time there are times when it would be useful for us to have control over the time our code is using. 

<h3>Why would we want to control the time?</h3>
There are a couple of situations that come to mind where it may be useful to be able to control the time in a system:
<ul>
<li>
There is a piece of code which only executes at a certain time of the day. To see if it executes correctly we need to be able to set the system time to be that time.
</li>
<li>
Date calculations - we want to do a calculation on a date and verify the result. We therefore need to be able to control the original date.
</li>
</ul>

Given that, there are two approaches which I have seen to allow us to do this:

<h3>Freezing time</h3>

Joda includes a DateTimeUtils class which allows us to <a href="http://joda-time.sourceforge.net/userguide.html#Change_the_Current_Time">change the current time</a>.

On the projects I've worked on we would typically wrap these calls in a more descriptive class. For example:


~~~java

import org.joda.time.DateTime;
import org.joda.time.DateTimeUtils;

public class JodaDateTime {
    public static void freeze(DateTime frozenDateTime) {
        DateTimeUtils.setCurrentMillisFixed(frozenDateTime.getMillis());
    }

    public static void unfreeze() {
        DateTimeUtils.setCurrentMillisSystem();
    }

}
~~~

This approach works better if DateTime is deeply engrained in the system and it is difficult for us to abstract dates behind another interface.

The benefit of taking this approach is that we can test for dates without having to change any of our code to add in another level of abstraction which leads to further complexity.

<h3>Time Provider</h3>

The alternative approach is to have a TimeProvider which we can pass around the system. This would typically be passed into the constructor of any classes which need to make use of time.

For example, we might have the following interface defined:


~~~java

import org.joda.time.DateTime;

public interface TimeProvider {
    public DateTime getCurrentDateTime() ;
}
~~~

We can then mock out getCurrentDate() to return whatever date we want in our tests.

The advantage of this approach is that it allows more flexibility around the implementation - it could be used to sync system and local machine dates for example - although at a cost of adding extra complexity.

This approach is similar to the<a href="http://martinfowler.com/eaaCatalog/plugin.html"> plugin pattern</a> Martin Fowler details in <a href="http://martinfowler.com/eaaCatalog/">Patterns of Enterprise Application Architecture</a> in that we use one implementation of TimeProvider in our application and then a different version for testing.

I generally favour this approach if possible although if a quick win is needed then the first approach is fine.
