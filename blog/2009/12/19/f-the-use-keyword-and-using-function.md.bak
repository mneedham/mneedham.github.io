+++
draft = false
date="2009-12-19 10:33:57"
title="F#: The use keyword and using function"
tag=['f']
category=['F#']
+++

While I was playing around with <a href="http://www.markhneedham.com/blog/2009/12/18/f-word-count-a-somewhat-failed-attempt/">the little F# script that I wrote to try and solve the word count problem</a> I noticed that in a couple of places I had used the '<a href="http://msdn.microsoft.com/en-us/library/dd233240(VS.100).aspx">use</a>' keyword when dealing with resources that needed to be released when they'd been used.

Using the 'use' keyword means that the 'Dispose' method will be called on the resource when it goes out of scope.

The two examples were 'StreamWriter' and 'StreamReader':


~~~ocaml

let writeTo (path:string) f = 
    use writer = new StreamWriter(path)
    f writer
~~~


~~~ocaml

let download path = 
    use streamReader = new StreamReader(File.OpenRead path)
    streamReader.ReadToEnd() 
~~~

I found it quite annoying that those bits of code needed to take up three lines despite the fact I don't really need to have the class construction assigned.

Luckily there is a 'using' function available which allows us to make these bits of code more concise.

'using' takes in 2 arguments - the object to be created and a function which takes in that object and does something with it.

If we make use of that function instead of the 'use' keyword we end up with the following function definitions:


~~~ocaml

let writeTo (path:string) f = using (new StreamWriter(path)) (fun writer -> f writer)
~~~


~~~ocaml

let download path = using (new StreamReader(File.OpenRead path)) (fun reader -> reader.ReadToEnd())
~~~

When we're just doing one thing with the resource, as I am here, then I think this reads better. If we're using it for multiple different operations then perhaps the use keyword is more appropriate.
