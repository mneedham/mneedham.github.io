+++
draft = false
date="2010-01-16 00:13:30"
title="Nant: Populating templates"
tag=['build', 'nant']
category=['Build']
+++

One of the common tasks that we need to do on every project I've worked on is ensure that we can create a web.config file for the different environments that we need to deploy our application to.

Nant has quite a neat task called '<a href="http://nant.sourceforge.net/release/0.85-rc3/help/filters/expandproperties.html">expandproperties</a>' which allows us to do this quite easily.

In our build file we would have the following:

build-file.build

~~~text

  <property name ="configFile" value="${environment}.properties" readonly="true"/>
  <if test="${not file::exists(configFile)}">
    <fail message="Configuration file '${configFile}' could not be found." />
  </if>
  <include buildfile ="${configFile}" />

  <target name="GenerateConfigFiles">
    <foreach item="File" property="TemplateFile">
      <in>
        <items>
          <include name="ProjectDirectory/**.template"/>
        </items>
      </in>
      <do>
        <copy file="${TemplateFile}" tofile="${string::replace(TemplateFile,'.template','')}" overwrite="true">
          <filterchain>
            <expandproperties />
          </filterchain>
        </copy>
      </do>
    </foreach>
  </target>
~~~

There would be corresponding '.template' and '.properties' files containing the various variables we want to set, like so:

dev.properties

~~~text

 <project>
	 <property name="SomeHost" value="http://my-host.com:8080"/>
 </project>
~~~

web.template.config

~~~text

<?xml version="1.0"?>
...
<configuration>
   <appSettings>
      <add key="SomeHost="${SomeHost}"/>
   </appSettings>
</configuration>
...
~~~


We would call the build file like so:


~~~text

nant -buildfile:build-file.build GenerateConfigFiles -D:environment=dev
~~~

We can then change that 'environment' variable depending which one we need to generate the configuration files for.

