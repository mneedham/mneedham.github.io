+++
draft = false
date="2010-05-03 00:28:04"
title="Coding: The Kestrel"
tag=['coding']
category=['Coding']
+++

Reg Braithwaite has a <a href="http://github.com/raganwald/homoiconic">cool series of posts where he covers the different combinators</a> from Raymond Smullyan's 'To Mock a Mockingbird' book and one of my favourites is the <a href="http://github.com/raganwald/homoiconic/blob/master/2008-10-29/kestrel.markdown#readme">'Kestrel' or 'K Combinator' </a> which describes a function that returns a constant function.

It's described like so:


~~~text

Kxy = x
~~~

The Kestrel function would take in 2 arguments and return the value of the first one. The second argument would probably be a function that takes in the first argument and then performs some side effects with that value.

Braithwaite descirbes the 'returning' function from Rails as an example of this combinator whereby instead of writing code like this:


~~~ruby

def registered_person(params = {})
  person = Person.new(params.merge(:registered => true))
  Registry.register(person)
  person.send_email_notification
  person
end

~~~

We can write this:


~~~ruby

def registered_person(params = {})
  returning Person.new(params.merge(:registered => true)) do |person|
    Registry.register(person)
    person.send_email_notification
  end
end
~~~

i.e. we can group all the side effects together and it's more obvious to the reader that we're returning the value of 'Person.new(...)' from this method.

I've been writing a bit of code in F# to generate some test objects and I realised that I had code like this in a few places:


~~~ocaml

let build (t:Type) =
      let theType = Activator.CreateInstance(t)
      theType.GetType().GetProperties() |> Array.iter (fun p -> p.SetValue(t, createValueFor p, null))
      theType  
~~~

We're creating 'theType' and then mutating it straight away using reflection before returning the value.

We can implement a 'returning' function like so to simplify the code a little:


~~~ocaml

let returning t f = f(t); t 
~~~


~~~ocaml

let build (t:Type) =
    returning (Activator.CreateInstance(t)) (fun t -> 
        t.GetType().GetProperties() |> Array.iter (fun p -> p.SetValue(t, createValueFor p, null)))
~~~

I think this is the same as what Martin Fowler refers to as a <a href="http://martinfowler.com/dslwip/NestedClosure.html">nested closure</a> and it seems quite a neat way of encapsulating side effects and making the code a bit more expressive. 

