+++
draft = false
date="2012-01-08 20:56:45"
title="Learning Android: Getting android-support jar/compatability package as a Maven dependency"
tag=['android']
category=['Android']
+++

In the app I'm working on I make use of the <a href="http://android-developers.blogspot.com/2011/08/horizontal-view-swiping-with-viewpager.html">ViewPager class</a> which is only available in the compatibility package from revisions 3 upwards.

Initially I followed the <a href="http://developer.android.com/sdk/compatibility-library.html">instructions on the developer guide</a> to get hold of the jar but now that I'm trying to adapt my code to fit the <a href="https://github.com/pivotal/RobolectricSample#readme">RobolectricSample</a>, <a href="http://www.markhneedham.com/blog/2012/01/07/learning-android-java-lang-outofmemoryerror-java-heap-space-with-android-maven-plugin/">as I mentioned in my previous post</a>, I needed to hook it up as a Maven dependency.

I added the dependency to my pom.xml like this:


~~~xml

<dependency>
  <groupId>android.support</groupId>
  <artifactId>compatibility-v4</artifactId>
  <version>r6</version>
</dependency>
~~~

But when I tried to resolve the dependencies (via 'mvn test') I ended up with this error:


~~~text

Downloading: http://repo1.maven.org/maven2/android/support/compatibility-v4/r6/compatibility-v4-r6.pom
[WARNING] The POM for android.support:compatibility-v4:jar:r6 is missing, no dependency information available
Downloading: http://repo1.maven.org/maven2/android/support/compatibility-v4/r6/compatibility-v4-r6.jar
[INFO] ------------------------------------------------------------------------
[INFO] BUILD FAILURE
[INFO] ------------------------------------------------------------------------
[INFO] Total time: 1.878s
[INFO] Finished at: Sun Jan 08 20:42:17 GMT 2012
[INFO] Final Memory: 8M/554M
[INFO] ------------------------------------------------------------------------
[ERROR] Failed to execute goal on project tweetboard: Could not resolve dependencies for project com.markhneedham:tweetboard:apk:1.0.0-SNAPSHOT: Could not find artifact android.support:compatibility-v4:jar:r6 in central (http://repo1.maven.org/maven2) -> [Help 1]
~~~

A bit of googling led me to <a href="https://github.com/jayway/maven-android-plugin-samples/tree/master/support4demos">a demo project</a> showing how to hook up the compatibility package. It linked to the <a href="https://github.com/mosabua/maven-android-sdk-deployer">Maven Android SDK Deployer</a> which is:

<blockquote>
The Maven Android SDK Deployer is a helper maven project that can be used to install the libraries necessary to build Android applications with Maven and the Android Maven Plugin directly from your local Android SDK installation.
</blockquote>

I had to first clone that git repository:


~~~text

git clone git://github.com/mosabua/maven-android-sdk-deployer.git
~~~

And then find the compatability-v4 package and install it:


~~~text

$ cd maven-android-sdk-deployer
$ cd extras/compatibility-v4
$ mvn clean install
~~~

I initially made the mistake of not setting <cite>$ANDROID_HOME</cite> to the location of the Android SDK on my machine, which led to the following error:


~~~text

[INFO] ------------------------------------------------------------------------
[INFO] BUILD FAILURE
[INFO] ------------------------------------------------------------------------
[INFO] Total time: 0.484s
[INFO] Finished at: Sun Jan 08 20:51:07 GMT 2012
[INFO] Final Memory: 3M/81M
[INFO] ------------------------------------------------------------------------
[ERROR] Failed to execute goal org.codehaus.mojo:properties-maven-plugin:1.0-alpha-2:read-project-properties (default) on project android-extras: Properties file not found: /Users/mneedham/github/maven-android-sdk-deployer/extras/${env.ANDROID_HOME}/extras/android/support/source.properties -> [Help 1]
~~~

Setting it solves the problem:


~~~text

$ export ANDROID_HOME=/Users/mneedham/github/android/android-sdk-macosx
~~~

There are more detailed instructions on the <a href="https://github.com/mosabua/maven-android-sdk-deployer">home page of the github project</a>.
