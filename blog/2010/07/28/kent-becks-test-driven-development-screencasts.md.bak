+++
draft = false
date="2010-07-28 10:44:05"
title="Kent Beck's Test Driven Development Screencasts"
tag=['tdd']
category=['Testing']
+++

Following the recommendations of <a href="http://twitter.com/coreyhaines/status/19490859095">Corey Haines</a>, <a href="http://twitter.com/mguterl/status/19527458401">Michael Guterl</a>, <a href="http://twitter.com/jmrtn/status/19491323181">James Martin</a> and <a href="http://twitter.com/mesirii/status/19489106768">Michael Hunger</a> I decided to get <a href="http://www.pragprog.com/screencasts/v-kbtdd/test-driven-development">Kent Beck's screencasts on Test Driven Development</a> which have been published by the Pragmatic Programmers.

I read Kent's '<a href="http://www.markhneedham.com/blog/2008/10/07/test-driven-development-by-example-book-review/">Test Driven Development By Example</a>' book a couple of years ago and remember enjoying that so I was intrigued as to what it would be like to see some of those ideas put into practice in real time.

As I expected a lot of Kent's approach wasn't that surprising to me but there were a few things which stood out: 

<ul>
<li>Kent <strong>wrote the code inside the first test</strong> and didn't pull that out into its own class until the first test case was working. I've <a href="http://www.markhneedham.com/blog/2009/04/30/coding-dojo-13-tdd-as-if-you-meant-it/">only used</a> <a href="http://www.markhneedham.com/blog/2009/05/15/coding-dojo-14-rock-scissors-paper-tdd-as-if-you-meant-it/">this approach</a> <a href="http://www.markhneedham.com/blog/2009/08/08/coding-dojo-21-tdd-as-if-you-meant-it-revisited/">in coding dojos</a> when we followed Keith Braithwaite's '<a href="http://gojko.net/2009/02/27/thought-provoking-tdd-exercise-at-the-software-craftsmanship-conference/">TDD as if you meant it</a>' idea. Kent wasn't as stringent about writing all the code inside the test though - he only did this when he was getting started with the problem.

The goal seemed to be to <a href="http://www.markhneedham.com/blog/2009/07/20/coding-quick-feedback/">keep the feedback loop as tight as possible</a> and this was approach was the easiest way to achieve that when starting out.
</li>
<li>He reminded me of the '<a href="http://www.markhneedham.com/blog/2010/07/28/tdd-call-your-shots/">calling the shots</a>' technique when test driving a piece of code. We should predict what's going to happen when we run the test rather than just blindly running it. Kent pointed out that <strong>this is a good way for us to learn something</strong> - if the test doesn't fail/pass the way that we expect it to then we have a gap in our understanding of how the code works. We can then do something about closing that gap. </li>
<li>I was quite surprised that <strong>Kent copied and pasted part of an existing test almost every time he created a new one</strong> - I thought that was just something that we did because we're immensely lazy!

I'm still unsure about this practice because although <a href="http://blog.iancartwright.com/2009/04/test-code-is-just-code.html">Ian Cartwright points out the dangers of doing this</a> it does seem to  make for better pairing sessions. The navigator doesn't have to wait twiddling their thumbs while their pair types out what is probably a fairly similar test to one of the others in the same file. Having said that it could be argued that if your tests are that similar then perhaps there's a better way to write them.

For me the main benefit of not copy/pasting is that it puts us in a mindset where we have to think about the next test that we're going to write. I got the impression that Kent was doing that anyway so it's probably not such a big deal.</li>
<li>Kent used the 'present tense' in his test names rather than prefixing each test with 'should'. This is an approach I came across when working with <a href="http://raphscallion.com/">Raph</a> at the end of last year.

To use <a href="http://blog.orfjackal.net/2010/02/three-styles-of-naming-tests.html">Esko Luontola's lingo</a> I think the tests follow the specification style as each of them seems to describe a particular behaviour for part of the API.

I found it interesting that he includes the method name as part of the test name. For some reason I've tried to avoid doing this and often end up with really verbose test names when a more concise name with the method name included would have been way more readable.

A couple of examples are 'getRetrievesWhatWasPut' and 'getReturnsNullIfKeyNotFound' which both describe the intent of their test clearly and concisely. The <a href="http://www.pragprog.com/screencasts/v-kbtdd/source_code">code and tests are available to download from the Prag Prog website</a>.
</li>
<li>One thing which I don't think I quite yet grasp is something Kent pointed out in his summary at the end of the 4th screencast. To paraphrase, he suggested that the order in which we write our tests/code can have quite a big impact on the way that the code evolves.

He described the following algorithm to help find the best order:

<ul>
<li>Write some code
	<ul>
		<li>erase it</li>
			<ul>
				<li>write it in a different order</li>
			</ul>
	</ul>
</ul>
And repeat.

I'm not sure if Kent intended for that cycle to be followed just when practicing or if it's something he'd do with real code too. An interesting idea either way and since I haven't ever used that technique I'm intrigued as to how it would impact the way code evolved.
</li>
<li>There were also a few good reminders across all the episodes:
<ul>
<li>Don't parameterise code until you actually need to.</li>
<li>Follow the Test - Code - Cleanup cycle.</li>
<li>Keep a list of tests to write and cross them off as you go.</li>
</ul>
</li></ul>

Overall it was an interesting series of videos to watch and there were certainly some good reminders and ideas for doing TDD more effectively.
