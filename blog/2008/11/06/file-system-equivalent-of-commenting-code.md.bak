+++
draft = false
date="2008-11-06 21:51:09"
title="File system equivalent of commenting code"
tag=['software-development']
category=['Software Development']
+++

Last week I came across what I have decided is the file system equivalent of commenting out code - not deleting directories when we are no longer using them.

The specific situation we ran into was while trying to make some Tomcat configuration changes but everything we changed was having no effect on what we were seeing on the web site. 

Eventually we realised that we were actually changing the configuration in the wrong place - we actually had two Tomcat folder lying around. One for Tomcat 6 and one for Tomcat 5.5. We are running the former but were changing the configuration for the latter by mistake!

Of course the underlying problem was that we weren't paying enough attention to what we were changing, but if there had been only one possible place to make changes then we wouldn't have had a problem.

<strong>Lesson Learned:</strong> Treat the file system like the code - if something is not needed delete it straight away. It can always be retrieved from source control in the future if it's actually needed.
