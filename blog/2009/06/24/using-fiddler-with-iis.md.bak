+++
draft = false
date="2009-06-24 17:46:23"
title="Using Fiddler with IIS"
tag=['software-development', 'fiddler']
category=['.NET']
+++

We've been using <a href="http://www.fiddler2.com/fiddler2/">Fiddler</a> to debug the requests and responses sent via web services to a service layer our application interacts with and it works pretty well when you run the application using <a href="http://en.wikipedia.org/wiki/UltiDev_Cassini_Web_Server">Cassini</a> but by default won't work when you run the website through IIS.

The key to this as one of my colleagues (who gives credit to <a href="http://erik.doernenburg.com">Erik</a>) showed me today is to ensure that IIS is running under the same user that Fiddler is running under which in our case is the 'Administrator' account.

The default user for IIS is 'Network Service' but as far as I'm aware you can't actually launch an application such as Fiddler from that account.

We therefore changed IIS to run under the 'Administrator' account on local development machines since this is where we typically use Fiddler.

To do this we need to:

<ul>
<li>Create a new application pool by going to the 'Application Pool' menu in IIS Manager and setting the 'Identity' of the new pool to be the Administrator account.
</li>
<li>Change the application pool for our application to match that new application pool.</li>
<li>Go to 'Computer Management > Local Users and Groups > IIS_WPG' and add the Administrator as a user of that group.</li></ul>

Fiddler should now capture requests/responses!

I'm not sure running IIS as the Administrator account is such a great idea although it's only on the local development environment so maybe it's a reasonable trade off for the benefits we get from being able to debug web service communication.
