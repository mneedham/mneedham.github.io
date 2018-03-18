+++
draft = false
date="2010-04-14 22:53:07"
title="Agile: Slimming down stories"
tag=['lean']
category=['Agile']
+++

On the project I'm currently working on we have several stories around writing the code that does various different calculations based on user input and then shows the results on the screen.

The original assumption on these stories was that we would be looking up the data of the business rules from a local database. The data would be copied across from a central database into that one for this project.

After some discussion about one of the stories, <a href="http://twitter.com/christianralph">Christian</a> pointed out that the only reason that we needed to have that data in the database was so that it would be configurable in production without having to make code changes and redeploy the application.

I'd been working with the assumption that these stories could only be considered done when the data was coming from the database but we've extracted the 'configurability of data' out into another story which the business can choose to prioritise if that's more valuable than other features we're working on.

It didn't even occur to me that we could pull this type of thing out but it seems like a useful approach as part of our drive to deliver the core functionality of the application as quickly as possible.

If we then need to go back and put in the configurability of the data, the lookup of that data is all hidden behind an interface so we shouldn't see too much pain by choosing to delay doing that.
