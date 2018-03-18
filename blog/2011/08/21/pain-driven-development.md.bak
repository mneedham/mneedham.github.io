+++
draft = false
date="2011-08-21 17:33:07"
title="Pain Driven Development"
tag=['software-development']
category=['Software Development']
+++

My colleague <a href="http://twitter.com/#!/patforna">Pat Fornasier</a> has been using an interesting spin on the idea of making decisions at the last responsible moment by encouraging our team to 'feel the pain' before introducing any constraint in our application.

These are some of the decisions which we've been delaying/are still delaying:

<h3>Dependency Injection</h3>
Everyone in our team comes from a Java/C# background and one of the first technical decisions that gets made on applications in those languages is which dependency injection container to use.

We decided to just create a trait where we wired up the dependencies ourself and then inject that trait into the entry point of our application. Effectively it acts as the ApplicationContext that a framework like Spring would provide.

I was fairly sure that we'd need to introduce a container fairly quickly but it's been 10 weeks and we still haven't felt the need to do that and our application is simpler as a result.

<h3>Data Ingestion</h3>
As I mentioned in an earlier post we have to import around 5 million documents into our database by the time the application goes live.

Our initial attempt at writing this code was single threaded and it was clear that there were many places where performance optimisations could be made.

Since we were only ingesting a few thousand documents at that stage it still ran pretty quickly so Pat encouraged us to wait until we felt the pain before making any changes.

That duly happened once the number of documents increased and it started taking 3/4 hours to run the job in our QA environment.

We then spent a couple of days <a href="http://www.markhneedham.com/blog/2011/07/29/performance-tuning-our-data-import-gather-precise-data/">working out how to make it possible to process the documents more quickly</a>.

<h3>Complex markup in documents</h3>

<a href="http://www.markhneedham.com/blog/2011/06/26/coding-light-weight-wrapper-vs-serialisationdeserialisation/">As I mentioned a couple of months ago </a>the application we're working on is mainly about taking data from a database and applying some transformations on it before showing it to the user.

We decided to incrementally add different types of documents into the database.

This meant that initially all our transformations involved just getting a text representation of XML nodes even though we knew that eventually we'd need to do more processing on the data depending on which tags appeared.

These data transformations actually turned out to be more complicated than we'd imagined so we might have delayed the pain here a little bit too long. 

On the other hand we were able to show early progress to our business stakeholders which probably wouldn't have been the case if we'd tried to take on the complex markup all at once.

<h3>N.B.</h3>

One thing to note with this approach is that we need to make sure there is a feedback mechanism to recognise when we are feeling pain otherwise we'll end up going beyond the last responsible moment more frequently.

There will probably also be more complaints about things not being done 'properly' since we're waiting for longer until we actually do that.

We have a code review that the whole team attends for an hour each week which acts as the feedback mechanism and we recently starting using <a href="http://fabiopereira.me/blog/2009/09/01/technical-debt-retrospective/">Fabio's effort/pain wall</a> to work out which things were causing us most pain.
