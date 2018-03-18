+++
draft = false
date="2010-04-25 17:27:25"
title="Iron Ruby: 'unitialized constant...NameError'"
tag=['ruby', 'net', 'ironruby']
category=['.NET', 'Ruby']
+++

I've been playing around a bit with Iron Ruby and cucumber following <a href="http://blog.webintellix.com/2009/10/how-to-use-cucumber-with-net-and-c.html">Rupak Ganguly's tutorial</a> and I tried to change the .NET example provided in the <a href="http://github.com/aslakhellesoy/cucumber/tree/v0.4.2/examples/">0.4.2 release of cucumber</a> to call a class wrapping Castle's WindsorContainer.

The feature file now looks like this:


~~~ruby

# 'MyAssembly.dll' is in the 'C:/Ruby/lib/ruby/gems/1.8/gems/cucumber-0.6.4/examples/cs' folder
require 'MyAssembly'
...
Before do
  @container = Our::Namespace::OurContainer.new.Container
end
~~~

The class is defined roughly like this:


~~~csharp

public class OurContainer : IContainerAccessor
    {
        private WindsorContainer container = new WindsorContainer();

        public SwintonContainer()
        {
            container.RegisterControllers(Assembly.GetExecutingAssembly()).AddComponent<IFoo, Foo>();
           // and so on
        }

        public IWindsorContainer Container
        {
            get { return container; }
        }
    }
~~~

When I tried to run the feature like so:


~~~text

icucumber features
~~~

I kept getting the following error:


~~~text

uninitialized constant Our::Namespace::OurContainer (NameError)
C:/Ruby/lib/ruby/gems/1.8/gems/cucumber-0.6.4/examples/cs/features/step_definitons/calculator_steps.rb:13:in `Before'
~~~

I've come across a few posts where <a href="http://blog.benhall.me.uk/2009/01/rubygems-ironruby-and-systemnet.html">people described the same error</a> and they all suggested that IronRuby was unable to find the class that I was trying to call in the code.

I decided to try calling another class from the assembly to see if that was the problem but that worked fine so there wasn't a problem with locating the class.

Somewhat by coincidence I was looking at the assembly again in Reflector and tried to look at the constructor of the 'OurContainer' class and was asked to give the location of the 'Castle.Windsor' assembly which it uses internally.

I didn't have that assembly or any of its dependencies in the 'C:/Ruby/lib/ruby/gems/1.8/gems/cucumber-0.6.4/examples/cs' folder but once I'd included those it all worked fine again!
