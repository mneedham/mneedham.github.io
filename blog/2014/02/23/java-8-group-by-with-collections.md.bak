+++
draft = false
date="2014-02-23 19:16:27"
title="Java 8: Group by with collections"
tag=['java']
category=['Java']
+++

<p>In my continued reading of Venkat Subramaniam's '<a href="http://pragprog.com/book/vsjava8/functional-programming-in-java">Functional Programming in Java</a>' I've reached the part of the book where the <cite><a href="http://download.java.net/jdk8/docs/api/java/util/stream/Stream.html#collect-java.util.stream.Collector-">Stream#collect</a></cite> function is introduced.</p>


<p>We want to take a collection of people, group them by age and return a map of (age -> people's names) for which this comes in handy.</p>


<p>To refresh, this is what the Person class looks like:</p>



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

<p>And we can write the following code in Java 8 to get a map of people's names grouped by age:</p>




~~~java

Stream<Person> people = Stream.of(new Person("Paul", 24), new Person("Mark", 30), new Person("Will", 28));
Map<Integer, List<String>> peopleByAge = people
    .collect(groupingBy(p -> p.age, mapping((Person p) -> p.name, toList())));
System.out.println(peopleByAge);
~~~


~~~text

{24=[Paul], 28=[Will], 30=[Mark]}
~~~

<p>We're running the 'collect' function over the collection, grouping by the 'age' property as we go and grouping the names of people rather than the people themselves.</p>


<p>This is a little bit different to what you'd do in Ruby where there's a 'group_by' function which you can call on a collection:


~~~ruby

> people = [ {:name => "Paul", :age => 24}, {:name => "Mark", :age => 30}, {:name => "Will", :age => 28}]
> people.group_by { |p| p[:age] }
=> {24=>[{:name=>"Paul", :age=>24}], 30=>[{:name=>"Mark", :age=>30}], 28=>[{:name=>"Will", :age=>28}]}
~~~

<p>This gives us back lists of people grouped by age but we need to apply an additional 'map' operation to change that to be a list of names instead:</p>



~~~ruby

> people.group_by { |p| p[:age] }.map { |k,v| [k, v.map { |person| person[:name] } ] }
=> [[24, ["Paul"]], [30, ["Mark"]], [28, ["Will"]]]
~~~

<p>At this stage we've got an array of (age, names) pairs but luckily Ruby 2.1.0 has a function 'to_h' which we can call to get back to a hash again:</p>



~~~ruby

> people.group_by { |p| p[:age] }.map { |k,v| [k, v.map { |person| person[:name] } ] }.to_h
=> {24=>["Paul"], 30=>["Mark"], 28=>["Will"]}
~~~

<p>If we want to follow the Java approach of grouping by a property while running a reduce over the collection we'd have something like the following:</p>



~~~ruby

> people.reduce({}) { |acc, item| acc[item[:age]] ||=[]; acc[item[:age]] << item[:name]; acc }
=> {24=>["Paul"], 30=>["Mark"], 28=>["Will"]}
~~~

<p>If we're using Clojure then we might end up with something like this instead:</p>



~~~lisp

(def people
  [{:name "Paul", :age 24} {:name "Mark", :age 30} {:name "Will", :age 28}])

> (reduce (fn [acc [k v]] (assoc-in acc [k] (map :name v))) {} (group-by :age people))
{28 ("Will"), 30 ("Mark"), 24 ("Paul")}
~~~

<p>I thought the Java version looked a bit weird to begin with but it's actually not too bad having worked through the problem in a couple of other languages.</p>


<p>It'd be good to know whether there's a better way of doing this the Ruby/Clojure way though!</p>

