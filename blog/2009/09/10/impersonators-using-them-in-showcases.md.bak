+++
draft = false
date="2009-09-10 00:23:33"
title="Impersonators: Using them in showcases"
tag=['impersonators', 'showcases']
category=['Testing']
+++

Towards the end of <a href="http://blog.rufiao.com/2009/08/impersonator-pattern/">my colleague Julio Maia's blog post about the impersonator pattern</a> he suggests that the standalone environment that we can create through the use of impersonators can be quite useful for showcases and we actually had a recent occasion where we had to switch mid-showcase from using the integration environment to make use of an impersonator.

In this case part of the environment went down in the middle of the showcase so <strong>if we wanted to keep on going then that was our only option</strong> but in general the  expectation of the business is that our showcases show them the functionality of the application end to end.

We need to be careful when using a standalone environment that the business are aware of this because it's quite likely that the application is going to respond much more quickly than it would if it was fully integrated.

If people aren't aware of this then they will be very surprised when the application isn't quite as performant when we put it into a real environment and it has to retrieve and store real data instead of just getting pre-stored values from an in memory impersonator.

Another disadvantage of using a standalone environment is that we must ensure that we only enter data which we have previously entered otherwise we'll either go against the real environment if we're using a <a href="http://martinfowler.com/bliki/SelfInitializingFake.html">self initializing fake</a> or (I think) just get no response if we're using a record/replay type impersonator.

If we're letting a business user drive the application during a showcase then we'll need to ensure that they know which data they can enter.

As long as we're careful in those regards I think it can be quite a useful approach since <strong>we can make our showcase independent of factors that our outside of our control</strong> - for example in our most recent showcase we had to reschedule the time because one part of the server was going to be restarted at our initial showcase time.

I definitely like the idea of using the impersonator for the safety it brings although my thinking at the moment is that maybe it's best to use it as a backup option if the real environments aren't working.

I'd be interested to hear if others have experiences around this area.
