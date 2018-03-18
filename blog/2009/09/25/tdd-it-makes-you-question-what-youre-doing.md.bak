+++
draft = false
date="2009-09-25 23:48:33"
title="TDD: It makes you question what you're doing"
tag=['tdd']
category=['Testing']
+++

My colleague Matt Dunn and I have been putting a lot of tests around some code over the last few days so that we can safely make some changes around that area and having finally created our safety net we've moved onto adding in the new functionality.

We're test driving the new bit of functionality whereas with the previous code only the code had been written with no unit tests and it's been quite interesting seeing the contrast in the style of code which seems to come out from these differing styles.

While we were writing the tests around the other code I found it quite surprising how often we came across code which wasn't actually needed - I guess if you only write the code then you need to make sure that all potential scenarios are covered even if it's impossible for them to happen.

In one case a null check was being done on a dependency of a class which always has its dependencies injected by a DI container and thus as far as I understand could never actually be null.

It seems to me that the outcome of this approach to coding can contribute greatly to what Fred Brooks coins 'Accidental Complexity' in '<a href="http://www.markhneedham.com/blog/2009/04/11/the-mythical-man-month-book-review/">The Mythical Man Month</a>'  - extra code which makes the code base more difficult to read as a whole but which adds no value apart from that. Essentially waste.

When test driving code I find that the process of coming up with examples/tests before you write any code leads you to question how the system actually works.

For example Matt and I had thought that the new piece of functionality we were working on would need to make a call to a repository to retrieve some data since that's what was being done for the existing functionality.

However, while writing our tests it become quite clear that we wouldn't need to do that.

On this occasion we wrote a test with an expectation for a call on the repository, then wrote the code to make that test to pass before moving onto our test where we would assert that the values retrieved from the repository would be populated into the appropriate object.

It was at this stage that we realised that there was actually no need to make that call because we already had the data available to us from another source. 

This has happened on quite a few occasions since and while I think pair programming helps put us in a state of mind where we are more inquisitive of the code being written, I think the TDD approach is quite useful as well.

I'm sure it's possible to avoid some of the problems I've described without a test driven approach but I certainly find it more difficult.
