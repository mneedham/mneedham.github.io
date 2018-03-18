+++
draft = false
date="2008-11-12 23:50:33"
title="Technical/Code Base Retrospective"
tag=['learning', 'technical-retrospective']
category=['Learning']
+++

We decided to run a technical retrospective on our code base yesterday afternoon but apart from one <a href="http://www.scottlilly.com/?p=6">blog post</a> on the subject and a <a href="http://www.thekua.com/atwork/2007/11/onboarding-strategy-airing-of-grievances/">brief mention on Pat Kua's blog</a> I couldn't find much information with regards to how to run one.

We therefore decided to take a fairly similar approach to our weekly <a href="http://www.thekua.com/atwork/category/retrospective/">retrospectives</a> in terms of having one column for <strong>'Like'</strong> and one for <strong>'Dislike'</strong>. In addition we had columns for <strong>'Want To Know More About'</strong> and <strong>'Patterns'</strong>. We kept this retrospective purely about the code base because we tend to cover development best practices and process in our normal retrospectives.

Since the code base is only a couple of months old and has been kept in fairly good shape with regular paying off of technical debt, there weren't that many areas of the code best that people didn't like.

We did have some interesting discussions around the best way to get data onto the page. 

We are currently getting domain objects to render themselves into a ViewData object which is then available for consumption from our <a href="http://freemarker.org/">Freemarker</a> templates.

The problem expressed with this approach is that when we are writing the code in the Freemarker template we need to know exactly how the domain object has rendered itself to the ViewData object in order to display the data on the page.

The alternative approach is to expose the data by adding getters to the domain objects but this seems wrong to me because it means breaking encapsulation and even if we mean to only use these getters from the view, the fact that the data is now exposed increases the chance of it being misused elsewhere.

The majority of the retrospective was taken up discussing the items in the 'Want To Know More About Column'. Although we have been pairing rotating quite frequently there are still some areas of the code base where some people are stronger than others so this gave them an opportunity to share their knowledge.

One useful thing about this discussion was that a pair were able to explain why they had done something in the code base rather than just what they had done which is often the case when explaining things in stand ups for example. Hopefully this will help to create a greater understanding of the code base.

I don't tend to notice patterns in code bases so I put that column into the retrospective more out of intrigue to see what others had noticed. We managed to come up with 5 or 6 although a lot of them were around the use of Pico Container, Servlet Filters and Restlet Filters although we do have some of the <a href="http://domaindrivendesign.org/discussion/messageboardarchive/MessagesByTopic.html">Domain Driven Design patterns</a> appearing in the code as well.

Overall this was an interesting exercise to have undertaken and one which I first came across from <a href="http://sarahtaraporewalla.com/thoughts/uncategorized/retrospectives-for-the-code-base/">Sarah Taraporewalla</a>. It will be interesting to see how things change in the code base if another one is run in a month's time.
