+++
draft = false
date="2010-03-25 08:09:26"
title="Selenium, Firefox and HTTPS pages"
tag=['selenium', 'firefox']
category=['Testing']
+++

A fairly common scenario that we come across when building automated test suites using Selenium is the need to get past the security exception that Firefox pops up when you try to access a self signed HTTPS page.

Luckily there is quite a cool plugin for Firefox called '<a href="https://addons.mozilla.org/en-US/firefox/addon/10246">Remember Certificate Exception</a>' which automatically clicks through the exception and allows the automated tests to keep running and not get stuck on the certificate exception page.

One other thing to note is that if the first time you hit a HTTPS page is on a HTTP POST then the automated test will still get stuck because after the plugin has accepted the certificate exception it will try to refresh the page which leads to the 'Do you want to resend the data' pop up.

We've previously got around this by writing a script using <a href="http://www.autoitscript.com/autoit3/index.shtml">AutoIt</a> which waits for that specific pop up and then 'presses the spacebar' but another way is to ensure that you hit a HTTPS page with a GET request at the beginning of the build so that the certificate exception is accepted for the rest of the test run.

To use the plugin in the build we need to add it to the Firefox profile that we use to run the build.

In Windows you need to run this command (having first ensured that all instances of Firefox are closed):


~~~text

firefox.exe --ProfileManager
~~~

We then need to create a profile which points to the '/path/to/selenium/profile' directory that we will use when launching Selenium Server. There is a much more detailed description of how to do that on <a href="http://girliemangalo.wordpress.com/2009/02/05/creating-firefox-profile-for-your-selenium-rc-tests/">this blog post</a>.

After that we need to launch Firefox with that profile and then add the plugin to the profile.

Having done that we need to tell Selenium Server to use that profile whenever it runs any tests which can be done like so:


~~~text

java -jar selenium-server.jar -firefoxProfileTemplate /path/to/selenium/profile
~~~
