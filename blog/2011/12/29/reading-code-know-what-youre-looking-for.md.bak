+++
draft = false
date="2011-12-29 02:43:34"
title="Reading Code: Know what you're looking for"
tag=['reading-code']
category=['Reading Code']
+++

In the last week or so before Christmas I got the chance to spend some time pairing with my colleague <a href="http://www.linkedin.com/pub/alex-harin/13/40b/716">Alex Harin</a> while trying to understand how an existing application which we were investigating was written.

We knew from watching a demo of the application that the user was able to send some processing off to be done in the background and that they would be emailed once that had happened.

Our starting point was therefore to work backwards from the labels on the UI and finding which code got executed when the user submitted the task.

My initial approach was to find the entry point and then follow the method calls line by line, slowly building my knowledge of how the application actually worked.

Alex used a much quicker approach whereby he <strong>thought about how the code would be designed</strong> and then looked for the bit of code which proved his belief.

In this case we knew that the application had a 2 tier architecture and that it didn't use any middleware which meant that it would more than likely be using the database as a queue to store the tasks to be processed.

Another colleague and I were then able to make use of this approach when looking at another piece of code.

It was being used to do pricing and we knew that there were different algorithms depending on which country you were in, which meant that we needed to look for anything country related to answer our questions.

Effectively we're looking at the code with a hypothesis in hand and then trying to see whether or not what we see proves or disproves that hypotheses.

I need to practice a bit more but it seems to let you navigate code much more quickly and makes you much less likely to dive down a rabbit hole.
