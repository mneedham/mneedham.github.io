+++
draft = false
date="2012-11-13 12:19:30"
title="Web Operations: Feature flags to turn off failing parts of infrastructure"
tag=['devops-2']
category=['DevOps']
+++

On most of the projects I've worked on over the last couple of years we've made use of <a href="http://martinfowler.com/bliki/FeatureToggle.html">feature toggles</a> that we used to turn pending features on and off while they were still being built but while reading <a href="http://www.amazon.co.uk/Web-Operations-Keeping-Data-ebook/dp/B0043M4Z34/ref=sr_1_2?ie=UTF8&qid=1352804969&sr=8-2">Web Operations</a> I came across another usage.

In the chapter titled 'Dev and Ops Collaboration and Cooperation' <a href="https://twitter.com/ph">Paul Hammond</a> suggests the following:

<blockquote>
Eventually some of your infrastructure will fail in an unexpected way. When that happens, you'll want the ability to disable just the features that rely on it, and keep the rest of the site running. Feature flags make this possible.
</blockquote> 

We'd mainly use this approach to disable peripheral functionality such as the ability to comment on a site whose main purpose is to deliver news.

From what I understand this means we'd permanently have if statements (or some equivalent) in the appropriate places in our code base which could be dynamically toggled if we start experiencing problems.

This differs slightly from the feature toggle approach we've used because those toggles would eventually be removed when the feature was running successfully in production.

Hammond goes on to suggest using feature flags for any external services that we rely on e.g. Flickr relies on the Yahoo address book, del.icio.us and last.fm but can gracefully disable that functionality if needs be.

He also points out that it's useful to think hard about what features are absolutely core to serving your site e.g. Flickr can disable photo uploads but still allow people to continue viewing photos.

Overall this sounds like a pretty neat idea and apart from the slight complexity of having the conditionals in the code I can't really think of any reasons why you wouldn't want to do it. Happy to hear opposing views though!
