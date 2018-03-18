+++
draft = false
date="2008-10-15 00:09:05"
title="Java vs .NET: An Overview"
tag=['coding', 'net', 'java']
category=['.NET', 'Java']
+++

A couple of months ago my colleague Mark Thomas posted about <a href="http://markthomas.info/blog/?p=47">working on a C# project after 10 years working in Java</a>, and being someone who has worked on projects in both languages fairly consistently (3 Java projects, 2 .NET projects) over the last two years I thought it would be interesting to do a comparison between the two.

The standard ThoughtWorks joke is that you just need to remember to capitalise the first letter of method names in C# and then you're good to go but I think there's more to it than that.

<h3>The Language & Framework</h3>
There is really not much difference between the syntax of Java and C# and I'm not that interested in going into it it massive detail here. There are <a href="http://www.javacamp.org/javavscsharp/">other</a> <a href="http://www.25hoursaday.com/CsharpVsJava.html">websites</a> which cover it in more detail.

Language features wise C# seems to be marginally ahead - the introduction of lambda expressions, implicitly typed local variables and extension methods in <a href="http://www.developer.com/net/csharp/article.php/3561756">C# 3.0</a> is something not yet matched in Java.

From my experience C#/.NET has much better support for front end rich GUI applications (WinForms, WPF) while Java is probably better for back end work. When it comes to web applications Java probably holds a marginal edge although the soon to be production released <a href="http://www.asp.net/mvc/">ASP.NET MVC framework</a> is a very nice piece of kit.

I have no data to justify saying that, merely thoughts based on experience, but from conversations with friends who work in investment banking I have learned that this is the way the two languages are used there as well.

<h3>Other language support</h3>

If you are looking for language support on the respective platforms beyond Java/C#, Java probably has a slight edge.

<a href="http://groovy.codehaus.org/">Groovy</a> is a dynamic lanuage with a Java style syntax and should therefore be easier for Java developers to pick up. I'm not aware of a dynamic language with C# style syntax for .NET although <a href="http://boo.codehaus.org/">Boo</a> is an alternative which compiles to run on the <a href="http://boo.codehaus.org/Common+Language+Infrastructure">Common Language Infrastructure</a>.

If you need Ruby support Java has <a href="http://jruby.codehaus.org/">JRuby</a> while .NET has <a href="http://www.ironruby.net/">IronRuby</a>. JRuby is the more mature of the two options here. If Python is what you need then both contenders compete here too with Java's offering of <a href="http://www.jython.org/Project/">Jython</a> and .NET's <a href="http://www.codeplex.com/IronPython">IronPython</a>.

Functional language wise .NET has a CTP release of <a href="http://research.microsoft.com/fsharp/fsharp.aspx">F#</a>, while Java has support for <a href="http://www.scala-lang.org/">Scala</a>.

<h3>Use of 3rd party APIs/Open Source Software</h3>

I've found that in the Java projects that I've worked on use significantly more open source software than the .NET ones. I'm yet to be convinced that this is necessarily a good thing although my Java colleagues are confident that it is.

To give an example, there are multiple different Java libraries for Xml parsing  whereas in C# everyone just uses the default one that's provided.

This provides the opportunity to learn new and better ways of doing things on the one hand, but the potential to spend serious amounts of time evaluating which tool to use instead of just getting on with it on the other.

From a Java perspective it certainly provides extra challenges in trying to get your applications integrated with the range of different application and web servers on the market. In .NET it would simply be a case of getting it to work on IIS - of course easier said than done!

<h3>IDEs</h3>

I think Java clearly leads in this area with <a href="http://www.jetbrains.com/idea/">IntelliJ</a> out ahead of anything else I've ever worked with. <a href="http://www.eclipse.org/">Eclipse</a> is a popular open source alternative but for me it is far less intuitive to use than IntelliJ.

Visual Studio only becomes usable once <a href="http://www.jetbrains.com/resharper/">Resharper</a> is installed but when that's done it becomes better than eclipse if not quite as usable as IntelliJ. My colleague Pat Kua also <a href="http://www.thekua.com/atwork/2007/05/31/speeding-up-visual-studio-2005/">listed some ideas to make it run even better</a>. <a href="http://www.icsharpcode.net/OpenSource/SD/">SharpDevelop</a> is a free IDE for .NET development although I haven't used it so I'm not sure how good it is.

<h3>Build and Deployment</h3>
Partly due to its better support of Ruby, Java has a much wider range of tools for working with the build. 

In .NET <a href="http://nant.sourceforge.net/">NAnt</a> is the only serious contender, and although <a href="http://msdn.microsoft.com/en-us/library/0k6kkbsd.aspx">msbuild</a> is often used to handle the compiling of the code its verbosity of non intuitive approach means I can't imagine recommending it for a whole build file.

Java wise we have <a href="http://ant.apache.org/">Ant</a>, <a href="http://maven.apache.org/">Maven</a>, a Groovy based wrapper around Ant called <a href="http://gant.codehaus.org/">Gant</a>, the Ruby based <a href="http://incubator.apache.org/buildr/">buildr</a> and the dependency management tool <a href="http://ant.apache.org/ivy/">Ivy</a>.

<h3>Communities</h3>

From my experience the community around .NET is more accessible to your average developer than what I've noticed in the Java world.

The <a href="http://altdotnet.org/">Alt.NET</a> group is an initiative <a href="http://www.infoq.com/news/2007/10/fowler-alt.net">started last year</a> by several of the leading lights in the .NET world and aims to make the world of .NET development a better and more productive place.

Java has the <a href="http://jcp.org/en/home/index">Java Community Process</a> driving it forward from a community perspective and perhaps due to the lower reliance on the drag and drop tools which are encouraged by Microsoft tools, the standard of your average Java developer may in fact be higher.

When it comes to finding the answers to questions both are mainstream enough that this is fairly easy.

<h3>Overall</h3>

I've tried to cover some of the areas which I considered important when using these two approaches. I'm sure there are some comparisons I have missed out so it would be interesting to hear from others who have worked on both platforms.

This is all written from my knowledge (and a bit of research) so if I've missed anything please mention it in the comments.

*Updated*
The paragraph about 'Other Language Support' was updated to reflect Robin Clowers' comments.
