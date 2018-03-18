+++
draft = false
date="2009-06-22 23:39:07"
title="F#: Continuation Passing Style"
tag=['f', 'continuation-passing-style', 'continuations']
category=['F#']
+++

I recently came across the idea of continuations while reading <a href="http://www.markhneedham.com/blog/2009/05/24/real-world-functional-programming-book-review/">Real World Functional Programming</a> and Wes Dyer has <a href="http://blogs.msdn.com/wesdyer/archive/2007/12/22/continuation-passing-style.aspx">a blog post where he explains continuations in more detail and also talks about the idea of using a continuation passing style in languages</a> which don't support Call/CC (Call with Current continuation).

As I understand it we can achieve a continuation passing style of programming by passing in the bit of code that we went executed next (i.e. the continuation) as an argument to a function. 

Wes has a series of examples in C# so I thought I'd see what they look like in F#:

The first example is a function 'Identity' which originally returns the value it is given before the calling function prints it to the screen.


~~~ocaml

let identity value = value
printfn "%s" (identity "mark") 
~~~

In CPS the function 'identity' would take in the printfn statement as a continuation:


~~~ocaml

let identity value k = k value
identity "mark" (printfn "%s")  
~~~

The type of identity has change from "'a -> 'a" to "'a -> ('a -> 'b) -> 'b" which in our example is "string -> (string -> unit) -> unit). 

The next example is to convert a 'Max' function to CPS style:


~~~ocaml

let max m n = if m > n then m else n
printfn "%d" (max 2 3)
~~~

That would become:


~~~ocaml

let max m n k = if m > n then k m else k n
max 2 3 (printfn "%d")
~~~

In both of these cases the "printfn.." part of the statement implicitly defines a function which takes in a value of 'string' in the first case and 'int' in the second.

We could just have easily written the code like this:


~~~ocaml

let max m n k = if m > n then k m else k n
max 2 3 (fun number -> printfn "%d" number)
~~~

I found the next example a bit tricky as it involves passing the continuation on to another function. 

We originally have the following:


~~~ocaml

let g n = n + 1    
let f n = g(n + 1) + 1    
printfn "%d" (f(1) + 1)
~~~

This becomes:


~~~ocaml

let g n k = k(n+1)
let f n k = g (n + 1) (fun x -> k(x + 1))
f 1 (fun n -> printfn "%d" (n + 1))
~~~

The thing I found strange when trying to think about how to do this is that anything which would happen after the initial function call needs to be passed into the continuation instead.

You need to always think about what happens next instead of just thinking about the result that needs to be calculated. At the moment I think I'm more used to a sequential flow of operations but I'm sure that will change.

The same applied for the last example, factorial:


~~~ocaml

let rec factorial n = 
	if n = 0 
	then 1 
	else n * factorial (n-1) 
~~~

Apply the same idea of putting any additional calculations outside the function call into the continuation we end up with:


~~~ocaml

let rec factorial n k =
	if n = 0 
	then k(1)
	else factorial (n-1) (fun x -> k(n*x)) 
~~~

The first factorial I define here is <a href="http://cs.hubfs.net/forums/permalink/8022/8022/ShowThread.aspx#8022">not tail recursive</a> as we still need to multiply the result of all the recursive calls by n at the end, meaning that the compiler can't optimise this code to just keep the latest call to the function on the stack.

The usual way I've seen to get around this is to thread an accumulator to an inner function inside factorial which would keep the running total of the factorial calculation but passing continuations is another way of doing this as we are passing on all the data needed to factorial every time we call it.

Looking at the C# via IL code version of these two functions we get the following:


~~~csharp

public static int factorial(int n)
{
    if (n == 0)
    {
        return 1;
    }
    return (n * factorial(n - 1));
}
~~~


~~~csharp

public static a factorial2<a>(int n, FastFunc<int, a> k)
{
    while (n != 0)
    {
        k = new factorial2@103<a>(n, k);
        n--;
    }
    return k.Invoke(1);
}
~~~

The second one has been converted into a while loop which I hadn't realised was what happened with tail recursive calls until I came across <a href="http://blogs.msdn.com/jomo_fisher/archive/2007/09/19/adventures-in-f-tail-recursion-in-three-languages.aspx">Jomo Fisher's post about tail recursion</a>.

I'm still getting the hang of this and would definitely agree with Wes' comment:

<blockquote>
CPS turns a program inside-out.  In the process, the programmer may feel that his brain has been turned inside-out as well.
</blockquote>

When I first read about continuations they sounded a bit similar to callbacks and Wes defines a callback as being an 'explicity-passed continuation' which is effectively what we are doing here. The difference for me is that we are passing the continuation around whereas when I've used a callback it's typically executed straight away.

<a href="http://www.williamcaputo.com/archives/000285.html">William Caputo has also been playing around with continuations in C#</a> and has some interesting thoughts as well.
