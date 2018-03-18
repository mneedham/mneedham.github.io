+++
draft = false
date="2009-06-29 00:28:14"
title="F#: Setting properties like named parameters"
tag=['f', 'objects']
category=['F#']
+++

One of the most frustrating things for me lately about interacting with C# libraries from F# has been setting up objects through the use of properties.

While I am against the use of setters to construct objects in the first place, that's the way that a lot of libraries work so it's a bit of a necessary evil!

In C# we would typically make use of the <a href="http://www.markhneedham.com/blog/2009/02/16/c-object-initializer-and-the-horse-shoe/">object initializer</a> syntax to do this, but in F# I've been writing code like this to do the same thing:


~~~ocaml

type MessageBuilder(?message:string, ?user:string) =              
	let buildMessage message user =
	   let twitterStatusBuilder = new TwitterStatus()
	      twitterStatusBuilder.Text <- message
	      twitterStatusBuilder.User <-
	      	let userBuilder = new TwitterUser()              
	         userBuilder.ScreenName <- user
	         userBuilder
	      twitterStatusBuilder

	member self.Build() = 
		buildMessage (if message.IsSome then message.Value else "") (if user.IsSome then user.Value else "")
~~~

This is more verbose than strictly necessary but I wanted to try and ensure all mutations to objects were being done within the function creating it rather than creating an object and then mutating it which feels strange to me in F# land.

I recently realised that it's actually possible to call properties <a href="http://msdn.microsoft.com/en-us/library/dd233192(VS.100).aspx">in the same way that we can create objects using named parameters</a>. 

We therefore end up with the following code:


~~~ocaml

type MessageBuilder(?message:string, ?user:string) =              
    let buildMessage message user = new TwitterStatus(Text = message, User = new TwitterUser(ScreenName = user))

    member self.Build() = 
        buildMessage (if message.IsSome then message.Value else "") (if user.IsSome then user.Value else "")
~~~

Which is much more concise and does the same thing.

