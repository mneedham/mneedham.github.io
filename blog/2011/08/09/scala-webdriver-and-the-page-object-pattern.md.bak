+++
draft = false
date="2011-08-09 00:54:23"
title="Scala, WebDriver and the Page Object Pattern"
tag=['scala', 'webdriver']
category=['Scala']
+++

We're using WebDriver on my project to automate our functional tests and as a result are using the <a href="http://code.google.com/p/selenium/wiki/PageObjects">Page Object pattern</a> to encapsulate each page of the application in our tests.

We've been trying to work out how to effectively reuse code since some of the pages have parts of them which work exactly the same as another page.

For example we had a test similar to this...


~~~scala

class FooPageTests extends Spec with ShouldMatchers with FooPageSteps {
  it("is my dummy test") {
    ...
    then(iShouldNotSeeAnyCommonLinks())
  }
}
~~~

...where <cite>FooPageSteps</cite> extends <cite>CommonSteps</cite> which contains the common assertions:


~~~scala

trait FooPageSteps extends CommonSteps {
  override val page = new FooPage(driver)
}
~~~


~~~scala

trait CommonSteps {
  val page : FooPage
  val driver: HtmlUnitDriver

  def iShouldNotSeeAnyCommonLinks() {
    page.allCommonLinks.isEmpty should equal(true)
  }
}
~~~

<cite>FooPage</cite> looks like this:


~~~scala

class FooPage(override val driver:WebDriver) extends Page(driver) with CommonSection {

}

abstract class Page(val driver: WebDriver) {
  def title(): String = driver.getTitle;
}

trait CommonSection {
  val driver:WebDriver
  def allCommonLinks:Seq[String] = driver.findElements(By.cssSelector(".common-links li")).map(_.getText)
}
~~~

We wanted to reuse <cite>CommonSteps</cite> for another page like so:


~~~scala

trait BarPageSteps extends CommonSteps {
  override val page = new BarPage(driver)
}

class BarPage(override val driver:WebDriver) extends Page(driver) with CommonSection {

}
~~~

But that means that we need to change the type of <cite>page</cite> in <cite>CommonSteps</cite> to make it a bit more generic so it will work for <cite>BarPageSteps</cite> too.

Making it of type <cite>Page</cite> is not enough since we still need to be able to call the <cite>allCommonLinks</cite> which is mixed into <cite>FooPage</cite> by <cite>CommonSection</cite>.

We therefore end up with the following:


~~~scala

trait CommonSteps {
  val page : Page with CommonSection
  val driver: HtmlUnitDriver

  def iShouldNotSeeAnyCommonLinks() {
    page.allCommonLinks.isEmpty should equal(true)
  }
}
~~~

We're able to mix in <cite>CommonSection</cite> just for this instance of <cite>Page</cite> which works pretty well for allowing us to achieve code reuse in this case!
