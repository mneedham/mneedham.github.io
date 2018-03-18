+++
draft = false
date="2008-10-26 20:54:18"
title="buildr - using another project's dependencies"
tag=['buildr']
category=['Build']
+++

Through my continued use of <a href="http://incubator.apache.org/buildr">buildr</a> on my current project one thing we wanted to do last week was to run our production code tests using some code from the test-utilities project along with its dependencies.

I thought this would be the default behaviour but it wasn't. Looking at the <a href="http://incubator.apache.org/buildr/building.html">documentation</a> suggested we could achieve this by calling 'compile.dependencies' on the project, but from what I can tell you still need to explicitly state that you want to use the main test utilities code as well.

The following code in our buildfile does the job:


~~~text

DEPENDENCY_JAR='depedency:dependency:jar:1.0' # change this to whatever the path to the dependency is
...
define "test.utilities" do
  compile.with DEPENDENCY_JAR
  package(:jar)
end

define "main.code" do
  # Some other code
  test.with project("test.utilities"), project("test.utilities").compile.dependencies
  package(:jar)
end
~~~

It seems a bit verbose but it achieves our objective in a cleaner way than having to repeat test-utilities dependencies when we run main.code's tests. 

I'm sure there must be an even cleaner way than this but I'm not yet aware of it!
