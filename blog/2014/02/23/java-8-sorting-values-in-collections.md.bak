+++
draft = false
date="2014-02-23 14:43:47"
title="Java 8: Sorting values in collections"
tag=['java']
category=['Java']
+++

<p>Having realised that Java 8 is <a href="http://openjdk.java.net/projects/jdk8/">due for its GA release within the next few weeks</a> I thought it was about time I had a look at it and over the last week have been reading <a href="http://pragprog.com/book/vsjava8/functional-programming-in-java">Venkat Subramaniam's book</a>.</p>


<p>I'm up to chapter 3 which covers sorting a collection of people. The Person class is defined roughly like so:</p>



~~~java

static class Person {
    private String name;
    private int age;

    Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    @Override
    public String toString() {
        return String.format("Person{name='%s', age=%d}", name, age);
    }
}
~~~

<p>In the first example we take a list of people and then sort them in ascending age order:</p>



~~~java

List<Person> people = Arrays.asList(new Person("Paul", 24), new Person("Mark", 30), new Person("Will", 28));
people.stream().sorted((p1, p2) -> p1.age - p2.age).forEach(System.out::println);
~~~


~~~text

Person{name='Paul', age=24}
Person{name='Will', age=28}
Person{name='Mark', age=30}
~~~

<p>If we were to write a function to do the same thing in Java 7 it'd look like this:</p>



~~~java

Collections.sort(people, new Comparator<Person>() {
    @Override
    public int compare(Person o1, Person o2) {
        return o1.age - o2.age;
    }
});

for (Person person : people) {
    System.out.println(person);
}
~~~

<p>Java 8 has reduced the amount of code we have to write although it's still more complicated than what we could do in Ruby:</p>



~~~ruby

> people = [ {:name => "Paul", :age => 24}, {:name => "Mark", :age => 30}, {:name => "Will", :age => 28}]
> people.sort_by { |p| p[:age] }
=> [{:name=>"Paul", :age=>24}, {:name=>"Will", :age=>28}, {:name=>"Mark", :age=>30}]
~~~

<p>A few pages later Venkat shows how you can get close to this by using the <cite><a href="http://download.java.net/jdk8/docs/api/java/util/Comparator.html#comparing-java.util.function.Function-">Comparator#comparing</a></cite> function:</p>



~~~java

Function<Person, Integer> byAge = p -> p.age ;
people.stream().sorted(comparing(byAge)).forEach(System.out::println);
~~~

<p>I thought I could make this simpler by inlining the 'byAge' lambda like this:</p>



~~~java

people.stream().sorted(comparing(p -> p.age)).forEach(System.out::println);
~~~

<p>This seems to compile and run correctly although IntelliJ 13.0 suggests there is a '<a href="http://youtrack.jetbrains.com/issue/IDEA-101788">cyclic inference</a>' problem. IntelliJ is happy if we explicitly cast the lambda like this:</p>



~~~java

people.stream().sorted(comparing((Function<Person, Integer>) p -> p.age)).forEach(System.out::println);
~~~

<p>IntelliJ also seems happy if we explicitly type 'p' in the lambda, so I think I'll go with that for the moment:</p>



~~~java

people.stream().sorted(comparing((Person p) -> p.age)).forEach(System.out::println);
~~~
