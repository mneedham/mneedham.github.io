+++
draft = false
date="2010-02-14 01:03:34"
title="F#: Unexpected identifier in implementation file"
tag=['f']
category=['F#']
+++

I've been playing around with some F# code this evening and one of the bits of code needs to make a HTTP call and return the result.

I wrote this code and then tried to make use of the 'Async.RunSynchronously' function to execute the call.

The code I had looked roughly like this:


~~~ocaml

namespace Twitter

module RetrieveLinks
    open System.Net
    open System.IO
    open System.Web
    open Microsoft.FSharp.Control
    
    let AsyncHttp (url:string) = async {
        let request =  HttpWebRequest.Create(url)
        let! response = request.AsyncGetResponse()
        let stream = response.GetResponseStream()
        use reader = new StreamReader(stream  )
        return! reader.AsyncReadToEnd() }

    let getData =
        let request = "http://some.url"
        AsyncHttp <| request

	Async.RunSynchronously getData
~~~

The problem was I was getting the following error on the last line:


~~~text

Error	3	Unexpected identifier in implementation file
~~~

I've seen that error before and it often means that you haven't imported a reference correctly and hence the compiler doesn't know what you're trying to refer to.

In this case I was fairly sure all my references were correct and I was still getting the same error when I used the full namespace to 'Async.RunSynchronously' which seemed to suggest I'd done something else wrong.

After comparing this file with another one which was quite similar but didn't throw this error I realised that I'd left of the '=' after the module definition. Putting that in solved the problem.


~~~ocaml

namespace Twitter

module RetrieveLinks = 
	// and so on
~~~

As I understand it if we don't use the '=' then we've created a top level module declaration and if we do use the '=' then we've created a local module declaration.

<a href="http://msdn.microsoft.com/en-us/library/dd233221(VS.100).aspx">From MSDN</a>:

<blockquote>
You do not have to indent declarations in a top-level module. You do have to indent all declarations in local modules. In a local module declaration, only the declarations that are indented under that module declaration are part of the module.
</blockquote>

Given this understanding another way to solve my problem would be to remove the indentation of the functions inside the module like so:


~~~ocaml

module RetrieveLinks
open System.Net
open System.IO
open System.Web
open Microsoft.FSharp.Control
    
// and so on until...
        
Async.RunSynchronously getData
~~~

That compiles as expected.

From reading the MSDN page it would suggest that in my first example I'd created a top level module declaration but indenting the code inside that module somehow meant that the 'Async.RunSynchronously' function wasn't recognised. 

I don't quite understand why that is so if anyone can enlighten me that would be cool!
