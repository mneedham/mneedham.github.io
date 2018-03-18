+++
draft = false
date="2009-12-25 22:25:57"
title="Roy Osherove's TDD Kata: My first attempt"
tag=['tdd']
category=['Coding']
+++

I recently came across <a href="http://weblogs.asp.net/rosherove/archive/2009/12/23/comments-on-corey-haines-string-calculator-tdd-kata-implementation.aspx">Roy Osherove's commentary</a> on <a href="http://katas.softwarecraftsmanship.org/?p=80">Corey Haines' attempt</a> at <a href="http://osherove.com/tdd-kata-1/">Roy's TDD Kata</a> so I thought I'd try it out in C#.

<a href="http://www.21apps.com/agile/tdd-kata-by-example-video/">Andrew Woodward has recorded his version of the kata</a> where he avoids using the mouse for the whole exercise so I tried to avoid using the mouse as well and it was surprisingly difficult!

I've only done the first part of the exercise so far which is as follows:

<ol>
<li>Create a simple String calculator with a method <strong>int Add(string numbers)</strong> <ol>
<li>The method can take 0, 1 or 2 numbers, and will return their sum (for an empty string it will return 0) for example<strong> &#8220;&#8221; or &#8220;1&#8221; or &#8220;1,2&#8221;</strong></li>
<li>Start with the simplest test case of an empty string and move to 1 and two numbers</li>
<li>Remember to solve things as simply as possible so that you force yourself to write tests you did not think about</li>

<li>Remember to refactor after each passing test</li>
</ol></li>
<li>Allow the Add method to handle an unknown amount of numbers</li>
<li>Allow the Add method to handle new lines between numbers (instead of commas). <ol>
<li>the following input is ok:&nbsp; &#8220;1\n2,3&#8221;&nbsp; (will equal 6)</li>
<li>the following input is NOT&nbsp;ok:&nbsp; &#8220;1,\n&#8221;&nbsp;</li>

<li>Make sure you only test for correct inputs. there is no need to test for invalid inputs for these katas</li>
</ol></li>
<li>Allow the Add method to handle a different delimiter: <ol>
<li>to change a delimiter, the beginning of the string will contain a separate line that looks like this:&nbsp;&nbsp; &#8220;//[delimiter]\n[numbers&#8230;]&#8221; for example &#8220;//;\n1;2&#8221; should return three where the default delimiter is &#8216;;&#8217; . </li>

<li>the first line is optional. all existing scenarios should still be supported</li>
</ol></li>
<li>Calling Add with a negative number will throw an exception &#8220;negatives not allowed&#8221; - and the negative that was passed.if there are multiple negatives, show all of them in the</li> </ol>
<h4>Mouseless coding</h4>

I know a lot of the <a href="http://www.jetbrains.com/resharper/">Resharper</a> shortcuts but I found myself using the mouse mostly to switch to the solution explorer and run the tests.

These are some of the shortcuts that have become more obvious to me from trying not to use the mouse:

<ul>
<li>I'm using a Mac and VMWare so I followed <a href="http://chriskchew.wordpress.com/2008/10/28/developing-net-on-a-mac-–-resharper-altinsert/">the instructions on Chris Chew's blog</a> to setup the key binding for 'Alt-Insert'. I also setup a key binding for 'Ctrl-~' to map to 'Menu' to allow me to right click on the solution explorer menu to create my unit tests project, to add references and so on. I found that I needed to use VMWare 2.0 to get those key bindings setup - I couldn't work out how to do it with the earlier versions.</li>
<li>I found that I had to use '<strong>Ctrl-Tab</strong>' to get to the various menus such as Solution Explorer and the Unit Test Runner. '<strong>Ctrl-E</strong>' also became useful for switching between the different code files.</li>
</ul>

<h4>Simplest thing possible</h4>

The first run through of the exercise I made use of a <a href="http://www.markhneedham.com/blog/2008/08/17/returning-from-methods/">guard block</a> for the empty string case and then went straight to 'String.Split' to get each of the numbers and then add them together.

It annoyed me that there had to be a special case for the empty string so I changed my solution to make use of a regular expression instead:


~~~csharp

Regex.Matches(numbers, "\\d").Cast<Match>().Select(x => int.Parse(x.Value)).Aggregate(0, (acc, num) => acc + num);
~~~

That works for nearly all of the cases provided but it's not incremental at all and it doesn't even care if there are delimeters between each of the numbers or not, it just gets the numbers!

It eventually came unstuck when trying to work out if there were negative numbers or not. I considered trying to work out how to do that with a regular expression but it did feel as if I'd totally missed the point of the exercise:

<blockquote>
Remember to solve things as simply as possible so that you force yourself to write tests you did not think about
</blockquote>

I decided to watch Corey's video to see how he'd achieved this and I realised he was doing much smaller steps than me.

I started again following his lead and found it interesting that <strong>I wasn't naturally seeing the smallest step but more often than not the more general solution to a problem</strong>.

For example the first part of the problem is to add together two numbers separated by a comma.

Given an input of "1,2" we should get a result of 3.

I really wanted to write this code to do that:

~~~csharp

if(number == "") return 0;
return number.Split(',').Aggregate(0, (acc, num) => acc + int.Parse(num));
~~~

But a simpler version would be this (assuming that we've already written the code for handling a single number):


~~~csharp

if (number == "") return 0;
if (number.Length == 1) return int.Parse(number); 
return int.Parse(number.SubString(0,1)) + int.Parse(number.SubString(2, 1));
~~~

After writing a few more examples we do eventually end up at something closer to that first solution.

<h4>Describing the relationships in code</h4>

I'm normally a fan of doing simple incremental steps but for me the first solution expresses the intent of our solution much more than the second one does and the step from using 'SubString' to using 'Split' doesn't seem that incremental to me. It's a <a href="http://www.markhneedham.com/blog/2009/12/10/tdd-big-leaps-and-small-steps/">bit of a leap</a>. 

This exercise reminds me a bit of a post by Reg Braithwaite where he talks about <a href="http://weblog.raganwald.com/2007/12/golf-is-good-program-spoiled.html">programming golf</a>. In this post he makes the following statement:

<blockquote>The goal is readable code that expresses the underlying relationships.</blockquote>

In the second version of this we're describing the relationship very specifically and then we'll generalise that  relationship later when we have an example which forces us to do that. I think that's a good thing that the incremental approach encourages.

<h4>Programming in the large/medium/small</h4>

In this exercise I found that the biggest benefit of only coding what you needed was that the code was easier to change when a slightly different requirement was added. If we've already generalised our solution then it can be quite difficult to add that new requirement.

I recently read a post by Matt Podwysocki <a href="http://weblogs.asp.net/podwysocki/archive/2009/12/14/going-hybrid-implementing-a-shopping-cart-in-f.aspx">where he talks about three different types of programming</a>:

<ul>
<li>Programming in the large: a high level that affects as well as crosscuts multiple classes and functions
<li>Programming in the medium: a single API or group of related APIs in such things as classes, interfaces, modules</li>
<li>Programming in the small: individual function/method bodies</li>
</li>
</ul>

From my experience generalising code prematurely hurts us the most when we're programming in the large/medium and it's really difficult to recover once we've done that.

I'm not so sure where the line is when programming in the small. I feel like generalising code inside small functions is not such a bad thing although based on this experience perhaps that's me just trying to justify my currently favoured approach!
