+++
draft = false
date="2009-06-07 08:19:01"
title="F#: Explicit interface implementation"
tag=['f', 'interfaces']
category=['F#']
+++

I've been writing some code to map between CouchDB documents and F# objects and something which I re-learned while doing this is the way that interfaces work in F#.

In F# when you have a class which implements an interface that class makes use of explicit interface implementation. 

This means that in order to access any members of the interface that the class implements you need to specifically refer to the interface by upcasting the value using the ':>' operator.

Given the following interface and class definitions:


~~~ocaml

type CouchDBDocument =  
    abstract DocType : string
        
type UserDocument = 
    { UserName:string; FirstName:string; Surname:string }
    interface CouchDBDocument with member x.DocType = "User"
~~~

If we had the following value:


~~~ocaml

let mark = { UserName = "mneedham"; FirstName = "Mark"; Surname = "Needham" }
~~~

In order to access the 'DocType' member of 'mark' we would need to do the following:


~~~ocaml

(mark :> CouchDBDocument).DocType
~~~

Coming from the world of C# I had expected that it would be possible to define a value as being of type 'CouchDBDocument' and then pass in a value of UserDocument like this:


~~~ocaml

let mark : CouchDBDocument = { UserName = "mneedham"; FirstName = "Mark"; Surname = "Needham" };;
~~~

But that doesn't actually compile:


~~~text

error FS0191: The type CouchDBDocument does not contain a field UserName
~~~

It is possible to do this in C# as well although the implementation would be implicit in C# unless we explicitly declare it to be explicit like so:


~~~csharp

public interface CouchDBDocument
{
    string DocType { get; }
}

public class UserDocument : CouchDBDocument
{
     string CouchDBDocument.DocType
    {
        get { return "User"; }
    }
}
~~~

To access the 'DocType' property in this case we would need to be explicitly referring to the 'CouchDBDocument':


~~~csharp

CouchDBDocument mark = new UserDocument();
Console.WriteLine(mark.DocType);
~~~

Mauricio Scheffer has an <a href="http://bugsquash.blogspot.com/2009/01/implementing-interfaces-in-f.html">interesting post where he talks about rewriting a piece of C# code in F#</a> which required him to use interfaces in F# and <a href="http://cs.hubfs.net/forums/permalink/7579/7586/ShowThread.aspx#7586">Brian McNamara explains on hubfs why explicit interface implementation can actually be quite useful</a>.

The <a href="http://www.markhneedham.com/blog/2009/05/24/real-world-functional-programming-book-review/">Real World Functional Programming book</a> also has a chapter which describes interfaces in C# and F# and the way they differ very clearly.
