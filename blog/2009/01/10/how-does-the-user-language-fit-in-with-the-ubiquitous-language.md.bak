+++
draft = false
date="2009-01-10 15:38:01"
title="How does the user language fit in with the ubiquitous language?"
tag=['ddd', 'domain-driven-design']
category=['Domain Driven Design']
+++

We've been doing some work this week around trying to ensure that we have a <a href="http://domaindrivendesign.org/discussion/messageboardarchive/UbiquitousLanguage.html">ubiquitous language</a> to describe aspects of the domain across the various different systems on my project.

It's not easy as there are several different teams involved but one thing we realised while working on the language is that the <strong>language of the business is not the same as the language of the user</strong>.

Although this is the first time that I recall working on a project where the language of the user is different to the language of the domain I'm sure there must be other domains where this is the case as well.

In our case the language is simplified so that it makes sense to the user - the terms used by the business make sense in that context but would be completely alien if we used it on the interfaces from which our users interact with the system.

At the moment our domain model represents the business terminology and then when we show the data to the user we refer to it by a different name. The problem with this approach is that there is a mental translation step in trying to remember which business term maps to which user term.

We can probably solve this problem somewhat by having the user terms represented in our Presentation Model but this still doesn't help remove the translation problem when it comes to discussions away from the code.

At the moment there aren't that many terms which differ but I'm not sure what the approach should be if there become more in the future, should we have a whole user language as well as a business specific ubiquitous one or should our ubiquitous language be the user language?
