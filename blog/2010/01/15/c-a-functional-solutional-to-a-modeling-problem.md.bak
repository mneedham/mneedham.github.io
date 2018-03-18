+++
draft = false
date="2010-01-15 23:23:58"
title="C#: A functional solution to a modeling problem"
tag=['coding']
category=['Coding']
+++

We were working on some refactoring today where we <a href="http://www.markhneedham.com/blog/2009/11/11/coding-pushing-the-logic-back/">pushed some logic back</a> from a service and onto a domain object and I noticed that we were able to use functions quite effectively to reduce the amount of code we had to write while still describing differences in behaviour.

The class we want to write needs to take in two integers which represent two different situations related to Foo. Depending upon whether we have 'Situation 1', 'Situation 2' or both situations we will display the results slightly differently.


~~~csharp

    public class Foo
    {
        private readonly int situationOneValue;
        private readonly int situationTwoValue;
        private readonly Func<int, string> situationOneDisplayFunc;
        private readonly Func<int, string> situationTwoDisplayFunc;

        private Foo(int situationOneValue, int situationTwoValue, Func<int, string> situationOneDisplayFunc, Func<int, string> situationTwoDisplayFunc)
        {
            this.situationOneValue = situationOneValue;
            this.situationTwoValue = situationTwoValue;
            this.situationOneDisplayFunc = situationOneDisplayFunc;
            this.situationTwoDisplayFunc = situationTwoDisplayFunc;
        }

        public static Foo ForSituation1(int situationOneValue, int situationTwoValue)
        {
            return new Foo(situationOneValue, situationTwoValue, Format, _ => "Irrelevant value");
        }

        public static Foo ForSituation2(int situationOneValue, int situationTwoValue)
        {
            return new Foo(situationOneValue, situationTwoValue, _ => "Irrelevant value", Format);
        }

        public static Foo ForSituation1And2(int situationOneValue, int situationTwoValue)
        {
            return new Foo(situationOneValue, situationTwoValue, Format, Format);
        }

        public string Situation1()
        {
            return situationOneDisplayFunc(situationOneValue);
        }

        public string Situation2()
        {
            return situationTwoDisplayFunc(situationTwoValue);
        }

        private string Format(int value)
        {
            return string.Format("Formatted Value {0}");
        }
    }

~~~ 

The way that it's used is that we get a value coming in from another system as a string which represents which situation we have to deal with.

As a result in the code which processes this data we have a dictionary which maps from these strings to the corresponding static method defined above:


~~~csharp

private static Dictionary<string, Func<int, int, Foo>> Foos = 
    new Dictionary<string, Func<int, int, Foo>> 
    { { "Situation 1", Foo.ForSituation1 }, 
      { "Situation 2", Foo.ForSituation2 }.
      { "Situation 1 and 2", Foo.ForSituation1And2 };
~~~

This is a neat little idea which I learnt from some Scala code that my colleague <a href="http://elhumidor.blogspot.com/">John Hume</a> posted on an internal mailing list a few weeks ago where he'd done something similar.

In our code which parses the incoming data we have something like the following:


~~~csharp

var foo = Foos[incomingMessage.Situation](incomingMessage.Situation1Value, incomingMessage.Situation2Value);
// and so on
~~~ 

If we wanted to solve this without using functions then for the first part I think we would probably need to use inheritance to create three different Foos, probably with a common interface, and then define the different behaviour on those classes.

The second part of the solution might end up being solved with some if statements or something similar.

I was a bit unsure of how easy it was to understand this code when we first came up with it but it's growing on me.
