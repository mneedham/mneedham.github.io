+++
draft = false
date="2011-01-10 15:28:44"
title="Failure of integration point doesn't have to stop the user: A real life example"
tag=['software-development']
category=['Software Development']
+++

<a href="">Ashwin</a> and I were recently discussing integration points in software systems and in particular how many systems are designed in such a way that they will stop the user from going any further if one of those integration points is down.

The main point in favour of designing systems in this way is that it's logically very simple - all operations are synchronous and we don't have to worry about any offline processing.

That doesn't mean that it gives the best user experience though and the more integration points that we have the more likely the user will experience a problem at some stage.

I vaguely remember hearing/reading someone (I think by <a href="http://www.michaelnygard.com/">Michael Nygaard</a> but if anyone knows please let me know!) point out that we often don't need all of the integration points to be up in order to continue the user's journey.

Of course there might be some user interactions with integration points where we do need that system to be online but for others, which play a more supporting role, we can just keep going and then process anything related to that system offline later on.

'<a href="http://www.damninteresting.com/the-baader-meinhof-phenomenon">Coincidentally</a>' later that day I was using an RBS ATM which informed me that the receipt printer wasn't working and asked me if I'd like to continue with my transaction.

The receipt in a cash withdrawal transaction is effectively a supporting 'feature' so it's reasonable that I should be able to continue with what I was doing.

Obviously if the machine was out of money then it wouldn't make sense to allow me to continue with a cash withdrawal transaction but it would still be fine for me to do a balance enquiry for example.

I haven't been at the ATM when it was out of money to check whether it actually does!
