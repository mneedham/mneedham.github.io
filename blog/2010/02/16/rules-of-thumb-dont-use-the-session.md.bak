+++
draft = false
date="2010-02-16 23:19:09"
title="Rules of Thumb: Don't use the session"
tag=['coding']
category=['Coding']
+++

A while ago I wrote about some <a href="http://www.markhneedham.com/blog/2009/10/04/coding-rules-of-thumb/">rules of thumb</a> that I'd been taught by my colleagues with respect to software development and I was reminded of one of them - don't put anything in the session - during a presentation my colleague <a href="http://www.lucagrulla.it/blog/">Luca Grulla</a> gave at our client on scaling applications by making use of the infrastructure of the web.	

The problem with putting state in the session is that it means that requests from a specific user have to be tied to a specific server i.e. we have to use a <a href="http://stackoverflow.com/questions/1040025/difference-between-session-affinity-and-sticky-session">sticky session/session affinity</a>.

This reduces our ability to scale our system horizontally (scale out) i.e. by adding more servers to handle requests.

If, for example, we have a small amount of users (whose first request went to the same server) making a lot of requests (perhaps through AJAX calls) then we may quickly put one of our servers under load while the others are sitting there idle.

In addition we have increased complexity around our deployment process.

If we want to do an incremental deployment of a new version of our website across some of our servers then we need to ensure that we create a copy of any sessions on those servers and copy them to the ones we're not updating so that any users still on the system don't experience loss of data.

There are no doubts products which can allow us to do this more easily but it seems to me to be an unnecessary product in the first place since we can just design our application to not rely on the session.

As I understand it the web was designed to be stateless i.e. each request is independent and all the information is contained within that request and the idea of the session was only something which was added in later on.

<h3>How does the way we code change if we don't use the session?</h3>

One thing we've often used the session for on projects that I've worked on is to store the current state of a form that the user is filling in.

When they've completed the form then we would probably store some representation of what they've entered in a database.

If we don't use the session then we need to store this intermediate data somewhere and include a key to load it in the request. 

On the project I'm working on at the moment we're storing that data in a database but then clearing out that data every other day since it's not needed once the user has completed the form.

An alternative perhaps could be to store it in a cache since in reality all we have is a key/value pair which we need to keep for a relatively short amount of time.

<h3>Advantages/disadvantages of this approach</h3>

The disadvantage of this approach is that we have to make more reads and writes to the database to deal with this temporary data.

Apart from the advantages I outlined initially, we are also more protected if a server handling a user's request goes down.

If we were using the session to store intermediate state then that information would be lost and they would have to start over.

In the approach we've using this isn't a problem and when the request is sent to another server we can still query the database and get whatever data the user had already saved.

As with most things there's a trade off to be made but in this case it seems a fair one to me.

<h3>Alternative approaches</h3>
I've come across some alternative approaches where we avoid using the session but don't store intermediate state in a database.

One way is to store that state in hidden fields on the form and another is to send it in the request parameters.

Neither of these approaches seem particularly clean to me and they give the user an easier way to change the intermediate data in ways that the form might not allow them to do.

From my experience our server side code becomes more complicated since we're always writing all of the data entered so far back into the page.

In addition the url becomes a complete mess with the second approach.
