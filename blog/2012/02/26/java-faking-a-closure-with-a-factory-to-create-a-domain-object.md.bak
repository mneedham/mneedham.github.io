+++
draft = false
date="2012-02-26 00:09:03"
title="Java: Faking a closure with a factory to create a domain object"
tag=['java']
category=['Java']
+++

Recently we wanted to create a domain object which needed to have an external dependency in order to do a calculation and we wanted to be able to stub out that dependency in our tests.

Originally we were just new'ing up the dependency inside the domain class but that makes it impossible to control it's value in a test.

Equally it didn't seem like we should be passing that dependency into the constructor of the domain object since it's not a piece of state which defines the object, just something that it uses.

We ended up with something similar to the following code where we have our domain object as an inner class:


~~~java

public class FooFactory {
    private final RandomService randomService;

    public FooFactory(RandomService randomService) {
        this.randomService = randomService;
    }

    public Foo createFoo(String bar, int baz) {
        return new Foo(bar, baz);
    }

    class Foo {
        private String bar;
        private int baz;

        public Foo(String bar, int baz) {
            this.bar = bar;
            this.baz = baz;
        }

        public int awesomeStuff() {
            int random = randomService.random(bar, baz);
            return random * 3;
        }
    }
}
~~~

A test on that code could then read like this:


~~~java

public class FooFactoryTest {
    @Test
    public void createsAFoo() {
        RandomService randomService = mock(RandomService.class);
        when(randomService.random("bar", 12)).thenReturn(13);

        FooFactory.Foo foo = new FooFactory(randomService).createFoo("bar", 12);
        assertThat(foo.awesomeStuff(), equalTo(39));
    }
}
~~~

It's a bit of a verbose way of getting around the problem but it seems to work reasonably well.
