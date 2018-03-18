+++
draft = false
date="2010-08-18 10:07:42"
title="Database configuration: Just like any other change"
tag=['devops-2']
category=['DevOps']
+++

I've been flicking through <a href="http://www.amazon.com/Continuous-Delivery-Deployment-Automation-Addison-Wesley/dp/0321601912/ref=sr_1_1?ie=UTF8&s=books&qid=1282115440&sr=8-1">Continuous Deployment</a> and one section early on about changing configuration information in our applications particularly caught my eye:

<blockquote>
In our experience, it is an enduring myth that configuration information is somehow less risky to change than source code. Our bet is that, given access to both, we can stop your system at least as easily by changing the configuration as by changing the source code. </blockquote>

In many organisations where I've worked this is generally adhered to except when it comes to configuration which is controlled from the database!

If there was a change to be made to source code or configuration on the file system then the application would go through a series of regression tests (often manual) to ensure that the application would still work after the change. 

If it was a database change then that just be made and there would be no such process.

Making a change to database configuration is pretty much the same as making any other change and if we don't treat it the same way then we can run into all kinds of trouble as the authors point out:

<blockquote>
If we change the source code, there are a variety of ways in which we are protected from ourselves; the compiler will rule out nonsense, and automated tests should catch most other errors. On the other hand, most configuration information is free-form and untested.
</blockquote>

Alex recently wrote about his use of <a href="http://blog.m.artins.net/deployment-smoke-tests-is-anyone-being-slack/">deployment smoke tests</a> - another suggestion of the authors - to ensure that we don't break our application by making configuration changes.

Organisations often have painful processes for releasing software but I think it makes more sense to try and fix those rather than circumnavigating them and potentially making our application behave unexpectedly in production.
