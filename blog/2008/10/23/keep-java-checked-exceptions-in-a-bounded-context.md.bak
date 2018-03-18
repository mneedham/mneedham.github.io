+++
draft = false
date="2008-10-23 21:22:26"
title="Keep Java checked exceptions in a bounded context"
tag=['java', 'checked-exceptions']
category=['Java']
+++

One of the features that I dislike in Java compared to C# is <a href="http://radio.weblogs.com/0122027/stories/2003/04/01/JavasCheckedExceptionsWereAMistake.html">checked exceptions</a>.

For me an exception is about a situation which is <strong>exceptional</strong>, and if we know that there is a possibility of it happening and even have that possibility defined in our code then it doesn't seem all that exceptional to me.

Having said that they do at least provide information which you can't help but notice about what can go wrong when you make a call to a particular method.

The problem is that often these checked exceptions just get passed on - i.e. not handled - until we end up with an exception on the page the user sees which is completely irrelevant to the action they are trying to undertake.

To give an example, we have been using the <a href="http://www.ognl.org/">OGNL</a> library to hydrate some objects for testing using the builder pattern.

We have something like this:


~~~java

public class FooBuilder {
    private String bar;

    public FooBuilder setBar(String bar) {
        this.bar = bar;
        return this;
    }

    public Foo toFoo() {
        Foo foo = new Foo();
        setValue(foo, "bar", bar);
        return foo;
    }

    protected void setValue(Object object, String propertyName, Object propertyValue) {
        try {
            OgnlWrapper.setValue(object, propertyName, propertyValue);
        } catch (OgnlException e) {
            throw new RuntimeException(e);
        }
    }
}
~~~


~~~java

import ognl.DefaultMemberAccess;
import ognl.MemberAccess;
import ognl.Ognl;
import ognl.OgnlContext;
import ognl.OgnlException;

public class OgnlWrapper {

    public static void setValue(Object object, String propertyName, Object propertyValue) throws OgnlException {
        Ognl.setValue(propertyName, createOgnlContext(), object, propertyValue);
    }

    private static OgnlContext createOgnlContext() {
        MemberAccess memberAccess = new DefaultMemberAccess(true);
        OgnlContext ognlContext = new OgnlContext();
        ognlContext.setMemberAccess(memberAccess);
        return ognlContext;
    }
}
~~~

We can then build an instance of 'Foo' like so:


~~~java

Foo foo = new FooBuilder().setBar("barValue").toFoo();
~~~

What is interesting here is not the OGNL library in itself but the checked 'OgnlException' which the 'Ognl.setValue(...)' method defines.

If I am using the FooBuilder I don't care how the Foo object is created, all I care is that I get it. Therefore we don't want to bubble the implementation details of how we are creating the object upwards.

I only care about the OgnlException if I am calling the OgnlWrapper and therefore that is where the exception should be caught and then rethrown as a Runtime exception.

I like to refer to this area of OgnlWrapper callees as being a <a href="http://domaindrivendesign.org/discussion/messageboardarchive/BoundedContext.html">bounded context</a> - that exception should only be applicable in that particular area and beyond that it should not exist.

Doing this allows us more flexibility around the way we implement things. If I decide in the future to use a different library instead of OGNL to do the same job I don't need to worry that the callees of FooBuilder will all need to be updated. I can just make the change inside FooBuilder and that's it!
