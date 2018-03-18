+++
draft = false
date="2013-07-22 22:37:28"
title="Lessons from supporting production code"
tag=['software-development']
category=['Software Development']
+++

<p>Until I started working on the <a href="http://www.uswitch.com/">uSwitch</a> energy website around 8 months ago I had not really done any support of a production system so I learnt some interesting lessons in my time there.</p>


<h3>Look at the new code first</h3>

<p>We had our application wired up to <a href="http://airbrakeapp.com/pages/home">Airbrake</a> so whenever a user did anything which resulted in an exception being thrown we received a report with the stack trace, environment variables and which page they were on.</p>


<p>When trying to work out what had happened I initially started from scratch and tried to work backwards from the source and create a scenario in my head of what they might have done to get that error.</p>


<p>After a few times of doing this it became clear that there was a reasonable chance that if a user was experiencing a problem it was probably because of some new code that we'd just introduced.</p>


<p>We therefore tweaked our bug hunting algorithm to initially check code that had been changed recently and only after ruling that out did we work back from first principles.</p>


<h3>It may never have worked</h3>

<p>Sometimes it became clear that new code wasn't to blame but it seemed implausible that the error could have actually happened.</p>


<p>There was a tendency to assume that the user must be deliberately doing something to make the application break but it soon became clear that they had just managed to hit a code path that had not been hit before.</p>


<p>Even if you've done extensive testing on a system users still seem to find paths through the code that haven't failed previously so it seems best to just assume that is going to happen at some stage.</p>


<h3>Log all the things</h3>

<p>As I mentioned earlier we were using a 3rd party service to collect errors and other helpful information which was really useful for helping us find the root cause of problems.</p>


<p>The type of logging that you need varies so for a product like <a href="http://www.neo4j.org/">neo4j</a> as well as logging exceptions we also log system information and memory settings.</p>


<p>Obviously I'm quite new to this type of work so I'm sure others will have useful bits of advice to share as well.</p>

