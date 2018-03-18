+++
draft = false
date="2014-03-23 21:18:36"
title="Functional Programming in Java - Venkat Subramaniam: Book Review"
tag=['book-review']
category=['Books']
+++

<p>I picked up Venkat Subramaniam's '<a href="http://pragprog.com/book/vsjava8/functional-programming-in-java">Functional Programming in Java: Harnessing the Power of Java 8 Lambda Expressions</a>' to learn a little bit more about Java 8 having struggled to find any online tutorials which did that.</p>


<p>A big chunk of the book focuses on lambdas, <a href="http://www.markhneedham.com/blog/2009/01/19/f-vs-c-vs-java-functional-collection-parameters/">functional collection parameters</a> and lazy evaluation  which will be familiar to users of C#, Clojure, Scala, Haskell, Ruby, Python, F# or libraries like <a href="https://code.google.com/p/totallylazy/">totallylazy</a> and <a href="https://code.google.com/p/guava-libraries/">Guava</a>.</p>


<p>Although I was able to race through the book quite quickly it was still interesting to see how Java 8 is going to reduce the amount of code we need to write to do simple operations on collections.</p>


<p>I wrote up my thoughts on <a href="http://www.markhneedham.com/blog/2014/02/26/java-8-lambda-expressions-vs-auto-closeable/">lambda expressions instead of auto closeable</a>, using <a href="http://www.markhneedham.com/blog/2014/02/23/java-8-group-by-with-collections/">group by on collections</a> and <a href="http://www.markhneedham.com/blog/2014/02/23/java-8-sorting-values-in-collections/">sorting values in collections</a> in previous blog posts.</p>


<p>I noticed a couple of subtle differences in the method names added to collection e.g. skip/limit are there instead of take/drop for grabbing a subset of said collection.</p>


<p>There are also methods such as 'mapToInt' and 'mapToDouble' where in other languages you'd just have a single 'map' and it would handle everything.</p>


<p>Over the last couple of years I've used totallylazy on Java projects to deal with collections and while I like the style of code it encourages you end up with a lot of code due to all the anonymous classes you have to create.</p>


<p>In Java 8 lambdas are a first class concept which should make using totallylazy even better.</p>


<p>In a previous blog post I showed how you'd go about sorted a collection of people by age. In Java 8 it would look like this:</p>



~~~java

List<Person> people = Arrays.asList(new Person("Paul", 24), new Person("Mark", 30), new Person("Will", 28));
people.stream().sorted(comparing(p -> p.getAge())).forEach(System.out::println)
~~~

<p>I find the 'comparing' function that we have to use a bit unintuitive and this is what we'd have using totallylazy pre Java 8:</p>



~~~java

Sequence<Person> people = sequence(new Person("Paul", 24), new Person("Mark", 30), new Person("Will", 28));
        
people.sortBy(new Callable1<Person, Integer>() {
    @Override
    public Integer call(Person person) throws Exception {
        return person.getAge();
    }
});
~~~

<p>Using Java 8 lambdas the code is much simplified:</p>



~~~java

Sequence<Person> people = sequence(new Person("Paul", 24), new Person("Mark", 30), new Person("Will", 28));
System.out.println(people.sortBy(Person::getAge));
~~~

<p>If we use 'forEach' to print out each person individually we end up with the following:</p>



~~~java

Sequence<Person> people = sequence(new Person("Paul", 24), new Person("Mark", 30), new Person("Will", 28));
people.sortBy(Person::getAge).forEach((Consumer<? super Person>) System.out::println);
~~~

<p>The compiler can't work out whether we want to use the forEach method from totallylazy or from Iterable so we end up having to cast which is a bit nasty.</p>


<p>I haven't yet tried converting the totallylazy code I've written but my thinking is that the real win of Java 8 will be making it easier to use libraries like totallylazy and Guava.</p>


<p>Overall the book describes Java 8's features very well but if you've used any of the languages I mentioned at the top it will all be very familiar - finally Java has caught up with the rest!</p>

