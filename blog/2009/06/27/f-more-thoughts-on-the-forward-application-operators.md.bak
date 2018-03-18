+++
draft = false
date="2009-06-27 22:55:02"
title="F#: More thoughts on the forward & application operators"
tag=['f']
category=['F#']
+++

I've been spending a bit of time reading through the <a href="http://code.google.com/p/fake/source/checkout">Fake source code</a> to try and understand how it works and one of the things which I quite like about it is the way the authors have made use of different F# operators to make expressions easier to read by reducing the number of brackets that need to be written and reordering the functions/values depending on the particular context.

One which I hadn't seen before is the <a href="http://codebetter.com/blogs/matthew.podwysocki/archive/2009/04/27/functional-c-reverse-functional-composition.aspx">application operator</a> which is the opposite of the <a href="http://www.markhneedham.com/blog/2009/01/06/f-forward-operator/">forward operator</a> which I have previously written about. 

The application operator (<|) applies a value to a function, the function being on the left and the value on the right. 

It is used in <a href="http://code.google.com/p/fake/source/browse/trunk/src/app/FakeLib/FileHelper.fs">FileHelper.fs</a> as part of the DeleteFile function:


~~~ocaml

let DeleteFile x =   
  let file = new FileInfo(x)    
  if file.Exists then 
    log <| sprintf "Deleting %s" file.FullName
    file.Delete()
  else
    log <| sprintf "%s does not exist." file.FullName
~~~

The log function is of type 'string -> unit' and the sprintf call helps create that string. Without the application operator we would have to put in extra parentheses:


~~~ocaml

log (sprintf "Deleting %s" file.FullName)
~~~

The code also makes use of the forward operator which I think panders more to the object oriented style of programming whereby you have have some data/object and then apply a method/function to that. I find that code written in this way reads more intuitively to me at the moment.

One example of this is the SetDirReadOnly function in FileHelper.fs


~~~ocaml

  let rec SetDirReadOnly readOnly (dir:DirectoryInfo) =
    dir.GetDirectories() |> Seq.iter (fun dir ->
      SetDirReadOnly readOnly dir
      setDirectoryReadOnly readOnly dir)
    dir.GetFiles() |> Seq.iter (fun file -> file.IsReadOnly <- readOnly)    
~~~

In this case if we didn't have the forward operator then in theory we should be able to just put the 'dir.GetFiles()' can be passed as the second argument to 'Seq.iter':


~~~ocaml

  let rec SetDirReadOnly readOnly (dir:DirectoryInfo) =
    dir.GetDirectories() |> Seq.iter (fun dir ->
      SetDirReadOnly readOnly dir
      setDirectoryReadOnly readOnly dir)
    Seq.iter (fun file -> file.IsReadOnly <- readOnly)  dir.GetFiles()  
~~~

In fact what we get is a compilation error:


~~~text

Successive arguments should be separated by spaces or tupled, and arguments involving function or method applications should be parenthesized.
~~~

In this case we need to paranthesise the 'dir.GetFiles()' method call:


~~~ocaml

  let rec SetDirReadOnly readOnly (dir:DirectoryInfo) =
    dir.GetDirectories() |> Seq.iter (fun dir ->
      SetDirReadOnly readOnly dir
      setDirectoryReadOnly readOnly dir)
    Seq.iter (fun file -> file.IsReadOnly <- readOnly)  (dir.GetFiles())  
~~~

Which leads to another compilation error:


~~~text

Lookup on object of indeterminate type based on information prior to this program point. A type annotation may be needed prior to this program point to constrain the type of the object. This may allow the lookup to be resolved
~~~

In this case what we're being told is that the compiler is unable to work out the type of 'file' in the function being passed to 'Seq.iter'. We can fix this by specifically stating its type:


~~~ocaml

  let rec SetDirReadOnly readOnly (dir:DirectoryInfo) =
    dir.GetDirectories() |> Seq.iter (fun dir ->
      SetDirReadOnly readOnly dir
      setDirectoryReadOnly readOnly dir)
    Seq.iter (fun (file:FileInfo) -> file.IsReadOnly <- readOnly)  (dir.GetFiles())  
~~~

It works but it seems to miss the point of getting the F# compiler to infer which types you're talking about - the forward operator simplifies the code a lot. I also think the code is more readable having 'files' at the beginning as it seems more obvious that the function is being applied to the sequence of files when written this way.

These operators are pretty cool and I've found it quite useful to look at the <a href="http://research.microsoft.com/en-us/um/cambridge/projects/fsharp/manual/FSharp.Core/Microsoft.FSharp.Core.Operators.html">full list of the F# operators available on the Microsoft Research website</a> as there may well be even more built in functions that can help simplify our code further.
