+++
draft = false
date="2009-06-23 19:31:37"
title="Visual Studio/Resharper: Changing the order of arguments"
tag=['resharper', 'visual-studio']
category=['Software Development']
+++

We've recently run into some places in our tests where the expectation and actual values passed into <a href="http://nunit.org/index.php">NUnit</a>'s 'Assert.AreEqual' are the wrong way round, therefore meaning that the error messages we get when tests fail are somewhat confusing!


~~~csharp

Assert.AreEqual(theActualValue, "the expectation");
~~~

We can change the arguments around using Resharper by using the key combination 'Ctrl-Alt-Shift-ArrowKey' but you can only do this one line at a time which was a bit annoying as there were about 20 to change.

I got a bit bored of doing this after a while so I thought I'd look into whether it would be possible to do this with a 'Find & Replace'.

After a bit of trial and error this is what I've ended up with:

<ul>
<li>
Select all the areas of code that you want to change and press 'Ctrl-H'
</li>
<li>
In the find box type:

~~~text

\({.*}, {\".*\"}
~~~ 
</li>
<li>
And in the replace box type:

~~~text

(\2, \1
~~~
</li></ul>

The '{}' define a matching group of which we define two in this case and then switch them around. Visual Studio's regex seems a bit different than the one I'm used to - <a href="http://msdn.microsoft.com/en-us/library/2k3te2cs(VS.80).aspx">the reference list for the syntax is available on MSDN</a>.

It's not too complicated and I'm sure there are edge cases where it wouldn't work but for the little case I had it did the job reasonably well.
