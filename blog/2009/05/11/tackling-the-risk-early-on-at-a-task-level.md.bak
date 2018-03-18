+++
draft = false
date="2009-05-11 23:54:12"
title="Tackling the risk early on at a task level"
tag=['risk']
category=['Software Development']
+++

I <a href="http://www.markhneedham.com/blog/2008/11/10/agile-putting-the-risk-up-front/">wrote previously about the idea of tackling the risky tasks in a project early on</a> - an idea that I learnt about when reading Alistair Cockburn's <a href="http://www.markhneedham.com/blog/2008/11/05/crystal-clear-book-review/">Crystal Clear</a>.

Towards the end of the post I wondered whether we could apply this idea at a story level whereby we would identify the potentially risky parts of a story and make sure that we addressed those risks before they became problematic to us.

I define risk in this sense to mean something that we don't know a lot about and therefore don't know how long it is going to take, something which we think might be difficult to do or something which is likely to cause us problems.

From my experience I've noticed that there tends to be risk around any boundaries with other systems which are likely to be a black box to us and in areas which we lack information about the best approach and therefore need to do some research/spiking first.

I've been trying to apply this approach and in a recent example my pair and I needed to fix a bug whereby some values on the website weren't being correctly updated when the user changed a value in a particular field.

We started by informally working out the different changes we might need to make in order to fix this problem:

<ul>
<li>Javascript to handle the page refreshing with the new values</li>
<li>C# mapping data from service into JSON object</li>
<li>Service call to get back the new values</li>
</ul>

We had quite a tight timeframe to make this fix and it seemed clear that the call to the service was probably the biggest area of risk in fixing this bug - we had done some investigation which indicated that we hadn't been sending a particular piece of data to the service and we weren't sure what would happen when we did.

As it turned out when we did pass this data we weren't quite getting the response that we expected but we were able to communicate with the other team and get the problem resolved really quickly.

The only thing I would have changed about our approach to this problem was that we tested whether or not the service was working by making a call to it through the UI having ensured that we were passing the correct data through to it. 

We would have been able to find out whether our integration was working much more quickly if we had just written an automated test directly hitting the service and made some assertions on the results. This only became apparent to me while watching an <a href="http://railsconf.blip.tv/file/2089545/">Uncle Bob presentation which included a section about the value of testing</a>. 
