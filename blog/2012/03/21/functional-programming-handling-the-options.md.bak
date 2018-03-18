+++
draft = false
date="2012-03-21 00:50:37"
title="Functional Programming: Handling the Options"
tag=['functional-programming', 'totallylazy']
category=['Java']
+++

A couple of weeks ago <a href="https://twitter.com/#!/channingwalton/status/177662437905010688">Channing Walton tweeted the following</a>:

<blockquote>
Every time you call get on an Option a kitten dies.
</blockquote>

As Channing points out in the comments he was referring to unguarded calls to 'get' which would lead to an exception if the Option was empty, therefore pretty much defeating the point of using an Option in the first place!

We're using Dan Bodart's <a href="http://code.google.com/p/totallylazy/">totallylazy</a> library on the application I'm currently working on and in fact were calling 'get' on an Option so I wanted to see if we could get rid of it.

The code in question is used to work out a price based on a base value and an increment value, both of which are optional.

I've re-created some tests to show roughly how it works:


~~~java

@Test
public void myOptionsExample() {
    Assert.assertThat(calculate(Option.<Double>none(), Option.<Double>none(), 20), is(Option.<Double>none()));
    Assert.assertThat(calculate(Option.<Double>none(), Option.some(12.0), 20), is(Option.some(240.0)));
    Assert.assertThat(calculate(Option.some(50.0), Option.some(12.0), 20), is(Option.some(290.0)));
    Assert.assertThat(calculate(Option.some(50.0), Option.<Double>none(), 20), is(Option.some(50.0)));
}
~~~


~~~java

private Option<Double> calculate(Option<Double> base, final Option<Double> increment, final int multiplier) {
    if(base.isEmpty() && increment.isEmpty()) {
        return Option.none();
    }

    if(increment.isEmpty()){
        return base;
    }

    double baseBit = base.getOrElse(0.0);
    double incrementBit = increment.get() * multiplier;

    return Option.some(baseBit + incrementBit);
}
~~~

We can get rid of the 'increment.isEmpty()' line by making use of a 'getOrElse' a few lines later like so:


~~~java

private Option<Double> calculate(Option<Double> base, final Option<Double> increment, final int multiplier) {
    if(base.isEmpty() && increment.isEmpty()) {
        return Option.none();
    }

    double baseBit = base.getOrElse(0.0);
    double incrementBit = increment.getOrElse(0.0) * multiplier;

    return Option.some(baseBit + incrementBit);
}
~~~

In Scala we can often make use of a for expression when combining Options but I'm not sure it would help in this case because we want to return a 'Some' if either of the Options has a value and only return a 'None' if they're both empty.

I can't figure out how to get rid of that opening if statement - I tried pushing the options into a list and then calling 'foldLeft' on that to sum up the components but we still have the problem of how to deal with returning a 'None' when the list is empty.

If you know how to simplify that code either using totallylazy or another language please let me know in the comments!
