+++
draft = false
date="2008-09-18 11:01:54"
title="Using java.util.Date safely"
tag=['javautildate', 'java', 'date']
category=['Java']
+++

Assuming that you are unable to use <a href="http://joda-time.sourceforge.net/faq.html">Joda Time</a> on your project, there are some simple ways that I have come across that allow you to not suffer at the hands of <a href="http://java.sun.com/j2se/1.4.2/docs/api/java/util/Date.html">java.util.Date</a>.

<h3>What's wrong with java.util.date in the first place?</h3>
First of all java.util.date is mutable. This means that if you create a java.util.date object its state can be modified after creation.

This means that you can do an operation like the following, for example:


~~~java

import java.util.Date;
import java.util.Calendar;

public class DateTest {
    public static void main(String[] args) {
        Date aDate = createDate(1, 0, 2008);
        System.out.println(aDate);
        aDate.setTime(createDate(1, 0, 2009).getTime());
        System.out.println(aDate);
    }

    private static Date createDate(int date, int month, int year) {
        Calendar calendar = Calendar.getInstance();
        calendar.set(Calendar.DATE, date);
        calendar.set(Calendar.MONTH, month);
        calendar.set(Calendar.YEAR, year);
        return new Date(calendar.getTimeInMillis());
    }
}

~~~
Ignoring the horridness of the zero based month on Calendar, the output of the above piece of code (when I ran it) is as follows.


~~~text

Tue Jan 01 23:41:50 GMT 2008
Thu Jan 01 23:41:50 GMT 2009
~~~

The 'aDate' object has actually had its value changed by this piece of code. Clearly this means that we have to be careful how we handle uses of java.util.Date in our code to ensure unexpected things don't happen.

<h3>The problems java.util.Date can cause</h3>
Often when looking at code we will notice dates being returned via a getter from a class:


~~~java

public class DateTest {
    private Date aDate;

    public Date getADate() {
        return aDate;
    }
}
~~~
Eventually we would like to get to a stage where aDate is encapsulated inside the DateTest class but for now we just want to ensure that clients of DateTest can't change the value of the 'aDate' field in DateTest. Right now this is what will happen if a client changed the value returned by getADate() because 'aDate' is a <a href="http://www.thehackademy.net/madchat/ebooks/Oreilly_Nutshells/books/javaenterprise/jnut/ch02_10.htm">reference type</a>.

If we want to return 'aDate' we need to ensure that the value in DateTest cannot be changed by clients of this class. We can do this by returning a copy of the value:


~~~java

public class DateTest {
    private Date aDate;

    public Date getADate() {
        return new Date(aDate.getTime());
    }
}
~~~

We have the same problem when setting dates - the reference which you set it to will still be changeable from outside the class.

e.g.

~~~java

import java.util.Date;
import java.util.Calendar;

public class DateTest {
	private Date aDate;

	public void setADate(Date aDate) {
		this.aDate = aDate;
	}

	public static void main(String[] args) {
		Date myDate = createDate(1,0,2008);
		new DateTest().setADate(myDate);	
	}

    private static Date createDate(int date, int month, int year) {
        Calendar calendar = Calendar.getInstance();
        calendar.set(Calendar.DATE, date);
        calendar.set(Calendar.MONTH, month);
        calendar.set(Calendar.YEAR, year);
        return new Date(calendar.getTimeInMillis());
    }
}
~~~

If we change myDate in this scenario the 'aDate' field in the DateTest object will also be changed. We can get around this the same way as before by creating a new date with the value passed in.


~~~java

import java.util.Date;

public class DateTest {
	private Date aDate;

	public void setADate(Date aDate) {
		this.aDate = new Date(aDate.getTime());
	}

	public static void main(String[] args) {
		Date myDate = someDate();
		new DateTest().setADate(myDate)	
	}
}
~~~

Joshua Bloch and Neal Gafter's <a href="http://www.amazon.co.uk/Java-Puzzlers-Traps-Pitfalls-Corner/dp/032133678X/ref=sr_1_1?ie=UTF8&s=books&qid=1221731947&sr=8-1">Java Puzzlers</a> has more on this topic and other interesting quirks in Java.
