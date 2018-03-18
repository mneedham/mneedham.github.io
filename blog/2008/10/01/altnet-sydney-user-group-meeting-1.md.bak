+++
draft = false
date="2008-10-01 22:09:53"
title="Alt.NET Sydney User Group Meeting #1"
tag=['ruby', 'altdotnet', 'altnet', 'altnetsyd', 'ironruby']
category=['.NET']
+++

<a href="http://jamescrisp.org/">James Crisp</a> and <a href="http://richardsbraindump.blogspot.com/">Richard Banks</a> arranged the first <a href="http://sydneyaltdotnet.blogspot.com/">Alt.NET Sydney User Group</a> meeting held on Tuesday night at the ThoughtWorks office.

The first thing to say is thanks to James and Richard for getting this setup so quickly - it was less than a month ago that Richard suggested the idea of creating a group on the Alt.NET mailing list. 

Richard and James have already <a href="http://sydneyaltdotnet.blogspot.com/2008/09/and-we-away.html">written summaries</a> <a href="http://richardsbraindump.blogspot.com/2008/10/rhino-mocks-35-presentation-at-altnet.html">of</a> <a href="http://jamescrisp.org/2008/09/30/sydney-altnet-launched-ruby-slides/">what went on</a> but I thought I'd give some of my thoughts as well.

The meeting was split into three parts with a retrospective on proceedings at the end:

<h3>.NET News</h3>
Richard opened the meeting by talking about some of the latest news in the .NET community in the last month or so.

I thought this worked very well and helped to get some discussion going very early on. One of my comments from the <a href="http://www.markhneedham.com/blog/2008/09/14/altnet-uk-conference-20/">London Alt.NET Conference</a> was that very few people seemed to get involved - that certainly wasn't the case last night and there was a very collaborative feel about the whole event.

The first news was that the much talked about <a href="http://www.hanselman.com/blog/jQueryToShipWithASPNETMVCAndVisualStudio.aspx">jQuery is going to ship with ASP.NET MVC and Visual Studio</a> and that Microsoft intend to provide Product Support Services for it and contribute any changes they make to it back into the community. It was suggested that this is a bit strange as jQuery is effectively a competitor to <a href="http://silverlight.net/">Silverlight</a> - Microsoft's plugin for developing rich applications for the web. Apparently <a href="http://jquery.com/blog/2008/09/28/jquery-microsoft-nokia/">Nokia are also intending to get involved</a>.

Another thing which I hadn't heard about was the <a href="http://devsta.microsoft.com.au/">DevSta coding competition</a> which was mentioned at <a href="http://www.microsoft.com.au/teched/">Tech Ed</a> earlier in the year. I haven't read exactly what the competition is all about but you get 200 hours and 8 minutes to prove your skills with Visual Studio 2008. The challenge is <a href="http://devsta.microsoft.com.au/about.aspx">here</a> for those that are interested.

Richard also pointed out some open source projects which I hadn't come across, notably <a href="http://www.codeplex.com/CloneDetectiveVS">CloneDetectiveVS</a> - a duplicate code finder plugin for Visual Studio - and <a href="http://www.codeplex.com/SnippetDesigner">SnippetDesigner</a> - another plugin to create code snippets. Not sure how different this would be to <a href="http://www.jetbrains.com/resharper/features/code_templates.html">Resharper's code templates</a> but it's another option.

A new language which runs on the CLR called <a href="http://cobra-language.com/">Cobra</a> was mentioned. It has support for <a href="http://cobra-language.com/how-to/DeclareContracts/">contracts</a> and testing so it could be a contender - probably needs someone high profile to run with it for that to happen I would imagine.

<a href="http://gocosmos.org/index.en.aspx">gocosmos</a> was also discussed - an operating system project implemented completely in CIL compliant languages.

The <a href="http://www.webdirections.org/">WebDirections</a> conference was also mentioned - the <a href="http://www.microsoft.com/surface/index.html">Microsoft Surface</a> seemed to be the most interesting thing to come out of this.


<h3>Ruby and Rails From a .NET Perspective</h3>
James opened the second half of the evening with <a href="http://jamescrisp.org/2008/09/30/sydney-altnet-launched-ruby-slides">a talk about using Ruby in the world of .NET</a>.

He opened with <a href="http://www.artima.com/intv/ruby.html">a brief history of the Ruby language</a> going through some of the ideas that Ruby brings to the table - <a href="http://en.wikipedia.org/wiki/Principle_of_least_astonishment">principle of least surprise</a> being the most intriguing one to me - before covering some of the Ruby compilers currently available - <a href="http://en.wikipedia.org/wiki/Ruby_MRI">MRI</a>, <a href="http://www.atdot.net/yarv/">YARV</a> <a href="http://jruby.codehaus.org/">JRuby</a> and <a href="http://www.ironruby.net/">IronRuby</a>. The last one was the focus for the talk - being a .NET implementation of the Ruby language.

James went through some demos using the Interactive IronRuby Console to start with but later showing how to create a simple application using <a href="http://www.rubyonrails.org/">Rails</a>.

There was an interesting discussion around testing - James pointed out that the Ruby/Rails world is much more test focused than the .NET one and unit testing is available right out the box. 

I haven't worked with Ruby enough to know if everyone in the Ruby world unit tests but as a general feeling I would say this is probably accurate.

<a href="http://rspec.info/">RSpec</a> was covered briefly as an alternative to the Test::Unit framework that comes baked in with Rails. I haven't played around with it before but as I'm working a bit in the world of Ruby at the moment it is something that I hope to use in the near future.

Finally build and deployment tools from the Ruby world such as <a href="http://www.capify.org/">Capistrano</a> and <a href="http://rake.rubyforge.org/">Rake</a> were mentioned. I can see the latter having some influence but as the former is meant for Unix I can't see it being heavily used in the .NET world.

<h3>Rhino Mocks</h3>
Richard closed the evening with a <a href="http://richardsbraindump.blogspot.com/2008/10/rhino-mocks-35-presentation-at-altnet.html">presentation on Rhino Mocks</a>.

I went into this presentation with the belief that <a href="http://code.google.com/p/moq/">Moq</a> was the way to go when it comes to .NET mocking frameworks.

The Arrange Act Assert or <a href="http://code.google.com/p/mockito/">Mockito</a> approach to mocking is one which makes it much easier to do and leads to far less clutter in tests. 

I thought this was only possible in Moq and that <a href="http://ayende.com/projects/rhino-mocks.aspx">Rhino Mocks</a> encourage the Record/Replay approach. As Richard pointed out, <a href="http://ayende.com/Blog/archive/2008/05/16/Rhino-Mocks--Arrange-Act-Assert-Syntax.aspx">this is no longer the case</a>.

Richard gave a demonstration on several of the ways that you can use Rhino Mocks in your testing efforts - covering simple interaction testing, event testing and several other clever techniques that Rhino Mocks allows.

An interesting statement was made that 'Mocking = Genuine Unit Testing', a statement that I tend to agree with. Several people mentioned that they now realised their unit tests were actually functional tests - this is a problem which mocking can help to reduce.

<h3>Overall</h3>
Overall it was again interesting to meet up with the .NET crowd and hear the different ways that people are doing - I was impressed with the turn out given the short notice - there were over 30 people in attendance.

The next meeting is on 28th October 2008, ThoughtWorks Sydney Office, <a href="http://maps.google.com.au/maps?f=q&hl=en&geocode=&q=pitt+street&sll=-25.335448,135.745076&sspn=39.413301,93.164063&ie=UTF8&ll=-33.863467,151.209812&spn=0.00898,0.022745&z=16">51 Pitt Street</a> again.
