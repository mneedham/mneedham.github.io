+++
draft = false
date="2009-02-08 09:10:39"
title="Refactoring: Comment it out vs small steps removal"
tag=['coding']
category=['Coding', 'Incremental Refactoring']
+++

One refactoring I was doing last week was to try and remove the use of some getters/setters on one of our objects so that it was better encapsulated and all the behaviour related to it happened in one place.

The change involved introducing a constructor to initialise the object rather than doing so using the new object initialiser syntax and initalising it using the properties. 

My initial approach was to <strong>find all the usages of these properties and then remove each usage one by one</strong>, running our suite of tests against the code after each change to ensure that nothing had broken as a result of the change.

While we were doing this my colleague pointed out that it would probably be quicker to just <strong>comment out the properties code and then recompile the code</strong> - the list of errors would then point out the areas which relied on the properties and we could then fix the code that way.

It's a technique I've used previously and it worked out reasonably well because there were only 10 or so usages, meaning we were able to make all those changes and run the tests in under ten minutes.

I think if there had been bigger changes to make - for example if the properties had been being used to expose the data all over the application (luckily we only had one case of this) then the smaller steps approach may have been preferable.

Getting the balance between taking small steps and getting rapid feedback was also a consideration here. 

We were running our unit and javascript tests as we made the changes since we were uncertain exactly what impact the changes would have. It took around 70 seconds to run these tests, which I think encouraged slightly bigger steps so that we weren't sitting around waiting too often.

Both of these approaches are useful and it seems to me that maybe a combination of them, at different stages of our refactoring, would prove to be most useful.
