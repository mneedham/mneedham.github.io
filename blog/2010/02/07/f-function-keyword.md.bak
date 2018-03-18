+++
draft = false
date="2010-02-07 02:54:13"
title="F#: function keyword"
tag=['f']
category=['F#']
+++

I've been browsing through Chris Smith's <a href="http://www.amazon.com/gp/product/0596153643?ie=UTF8&tag=marneesblo-20&linkCode=as2&camp=1789&creative=390957&creativeASIN=0596153643">Programming F#</a> book and in the chapter on pattern matching he describes the 'function' key word which I haven't used before.

It's used in pattern matching expressions when we want to match against one of the parameters passed into the function which contains the pattern match.

For example if we have this somewhat contrived example:


~~~ocaml

let isEven value = match value with 
                    | x when (x % 2) = 0 -> true
                    | _ -> false
~~~

That could be rewritten using the function keyword to the following:


~~~ocaml

let isEven  = function 
               | x when (x % 2) = 0 -> true
               | _ -> false
~~~

It's a relatively straight forward way to simplify code like this although one thing I noticed while looking back through some old code I've written is that if we use this syntax then we need to ensure that the parameter we want to pattern match against is passed as the last parameter to a function.

For example this function which is used to parse the arguments passed to  a script was originally written like this:


~~~ocaml

let GetArgs initialArgs  =
    let rec find args matches =
        match args with
        | hd::_ when hd = "--" -> List.to_array (matches)
        | hd::tl -> find tl (hd::matches) 
        | [] -> Array.empty
    find (List.rev (Array.to_list initialArgs) ) []
~~~
    
If we want to use 'function' then we'd need to put 'args' implicitly as the second argument passed to the recursive 'find' function:


~~~ocaml

let GetArgs initialArgs  =
    let rec find matches =
        function
        | hd::_ when hd = "--" -> List.to_array (matches)
        | hd::tl -> find (hd::matches) tl
        | [] -> Array.empty
    find [] (List.rev (Array.to_list initialArgs) )  
~~~

I'm not sure that the resulting code is necessarily more intention revealing if the function has more than one argument passed to it. The second version of this function could be very confusing if you didn't know what the 'function' keyword actually did.
