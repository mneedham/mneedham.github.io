+++
draft = false
date="2011-12-15 23:19:31"
title="WebDriver: Getting it to play nicely with Xvfb"
tag=['webdriver']
category=['Software Development']
+++

Another thing we've been doing with WebDriver is having it run with the FirefoxDriver while redirecting the display output into the <a href="http://en.wikipedia.org/wiki/Xvfb">Xvfb framebuffer</a> so that we can run it on our continuous integration agents which don't have a display attached.

The first thing we needed to do was set the environment property 'webdriver.firefox.bin' to our own script which would point the display to Xvfb before starting Firefox:


~~~scala

import java.lang.System._
lazy val firefoxDriver: FirefoxDriver = {
  setProperty("webdriver.firefox.bin", "/our/awesome/starting-firefox.sh")
  new FirefoxDriver()
}
~~~


Our first version of the script looked like this:

/our/awesome/starting-firefox.sh

~~~text

#!/bin/bash

rm -f ~/.mozilla/firefox/*/.parentlock
rm -rf /var/go/.mozilla


XVFB=`which xVfb`
if [ "$?" -eq 1 ];
then
    echo "Xvfb not found."
    exit 1
fi

$XVFB :99 -ac &


BROWSER=`which firefox`
if [ "$?" -eq 1 ];
then
    echo "Firefox not found."
    exit 1
fi

export DISPLAY=:99
$BROWSER &
~~~

The mistake we made here was that we started Xvfb in the background which meant that sometimes it hadn't actually started by the time Firefox tried to connect to the display and we ended up with this error message:


~~~text

No Protocol specified
Error cannot open display :99
~~~

We really wanted to keep Xvfb running regardless of whether the Firefox instances being used by WebDriver were alive or not so we moved the starting of Xvfb out into a separate script which we run as one of the earlier steps in the build.

We also struggled to get the FirefoxDriver to kill itself after each test as calling 'close' or 'quit' on the driver didn't seem to kill off the process.

We eventually resorted to putting a 'pkill firefox' statement at the start of our firefox starting script:

/our/awesome/starting-firefox.sh

~~~text

#!/bin/bash

rm -f ~/.mozilla/firefox/*/.parentlock
rm -rf /var/go/.mozilla

pkill firefox

BROWSER=`which firefox`
if [ "$?" -eq 1 ];
then
    echo "Firefox not found."
    exit 1
fi

export DISPLAY=:99
$BROWSER &
~~~

It's a bit hacky but it does the job more deterministically than anything else we've tried previously.
