+++
draft = false
date="2009-07-02 12:04:34"
title="Book Club: Logging - Release It (Michael Nygaard)"
tag=['book-club', 'logging', 'release-it']
category=['Book Club']
+++

Our latest technical book club session was a discussion of the logging section in Michael Nygard's <a href="http://www.pragprog.com/titles/mnee/release-it">Release It</a>.

I recently listened to <a href="http://se-radio.net/podcast/2009-05/episode-134-release-it-michael-nygard">an interview with Michael Nygard on Software Engineering Radio</a> so I was interested in reading more of his stuff and <a href="http://camswords.wordpress.com/">Cam</a> suggested that the logging chapter would be an interesting one to look at as it's often something which we don't spend a lot of time thinking about on software development teams.

These are some of my thoughts and our discussion of the chapter:

<ul>
<li>An idea which <a href="http://pilchardfriendly.wordpress.com/">Nick</a> introduced on a project I worked on last year was the idea of having a '<strong>SupportTeam</strong>' class that could be used to do any logging of information that would be useful to the operations/support team that looked after our application once it was in production.

This is an approach also suggested by Steve Freeman/Nat Pryce in <a href="http://www.mockobjects.com/book/listening-to-the-tests.html">Growing Object Oriented software</a> (in the 'Logging is a feature' section) and the idea is that we will then focus more on logging the type of information that is actually useful to them rather than just logging what we think is needed.

One thing which <a href="http://twitter.com/davcamer">Dave</a> pointed out is that it's often difficult to get access to the operations team to try and get their requirements for the type of logging and monitoring they need and so often ends up being something that's done very late on. On projects I've worked on there has often been a story card for logging and I think this is a good way to go as they are a stakeholder of the system so logging shouldn't just be dealt with as a nice extra.</li>
<li>Something which I hadn't considered until reading this book is the idea of <strong>making logs human readable and machine parseable</strong> as well. The default format of most of the logging tools is not actually that useful when you're trying to scan through hundreds of lines of data and it was intriguing how a little indentation could improve this so dramatically with the added benefit of making it much easier to create a regular expression to find what you want. </li>
<li>One thing I'm interested in understanding is <strong>how we work out what's too much logging and what's too little</strong> since it seems that it seems that the answer to this question is fairly context sensitive. For example on a recent project we logged all unhandled exceptions that came from the system as well as any exceptions that happened when retrieving data from the service layer. In general the data we've had available has been enough to solve problems but we could probably have done more, just working out what would be useful doesn't seem obvious.</li>
<li>I think it was <a href="http://blog.m.artins.net/">Alex</a> who pointed out that it's often useful to have an explicit <strong>step in the build to remove any debug logging</strong> from the code so that it doesn't end up in production by mistake. This seems like a pretty neat idea although I haven't seen it done yet - it also leads towards the idea that logging is for the operations team which I think is correct although it is often suggested	 that logging is actually for developers since it is assumed that they would be the ones to eventually solve any problems that arise.</li>
<li>The idea of having <strong>message codes for specific errors messages</strong> seems like a really cool idea for allowing easy searching of log files - we've done this on some projects I've worked on and not on others. I guess the key here is to ensure we don't end up with too many different error codes otherwise it's just as confusing as not having them at all.</li>
</ul>
