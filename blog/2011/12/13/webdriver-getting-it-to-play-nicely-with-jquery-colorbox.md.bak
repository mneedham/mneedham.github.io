+++
draft = false
date="2011-12-13 23:31:02"
title="WebDriver: Getting it to play nicely with jQuery ColorBox"
tag=['webdriver']
category=['Software Development']
+++

As I <a href="http://www.markhneedham.com/blog/2011/12/05/continuous-delivery-removing-manual-scenarios/">mentioned in an earlier post about removing manual test scenarios</a> we've been trying to automate some parts of our application where a user action leads to a <a href="http://jacklmoore.com/colorbox/">jQuery ColorBox</a> powered overlay appearing.

With this type of feature there tends to be some sort of animation which accompanies the overlay so we have to wait for an element inside the overlay to become visible on the screen before trying to do any assertions on the overlay.

We have a simple method to do that:


~~~scala

def iWaitUntil(waitingFor: => Boolean) {
  for (i <- 1 to 5) {
    if(waitingFor) {
      return
    }
   Thread.sleep(200)
  }
}
~~~

It can then be called like this in our tests:


~~~scala

def driver: WebDriver = new FirefoxDriver()

iWaitUntil(driver.findElements(By.cssSelector(".i-am .inside-the-colorbox h3")).nonEmpty)
driver.findElement(By.cssSelector(".i-am .inside-the-colorbox h3")).getText should equal("Awesome Title")
~~~

Annoyingly what we noticed was that this wasn't enough and although the h3 element was coming back as being visible it was then failing the following assertion because 'getText' was returning nothing despite the fact that it clearly had text inside it!

<a href="http://twitter.com/#!/uday_rayala">Uday</a> came up with the neat idea of adding an additional wait clause which would wait until the text was non empty so we now have something like this...


~~~scala

def driver: WebDriver = new FirefoxDriver()

iWaitUntil(driver.findElements(By.cssSelector(".i-am .inside-the-colorbox h3")).nonEmpty)
driver.findElement(By.cssSelector(".i-am .inside-the-colorbox h3")).getText should equal("Awesome Title")
iWaitUntil(driver.findElement(By.cssSelector(".i-am .inside-the-colorbox h3")).getText != "")
~~~

...which seems to do the job nicely.

An alternative approach would have been to disable the animation of jQuery ColorBox just for our tests but the approach we took was a much quicker win at the time.

We did realise later on that we didn't need to write our own wait method since <a href="http://seleniumhq.org/docs/04_webdriver_advanced.html">WebDriver has one built into the API</a> but I guess they both do similar things so it's not such a big problem.
