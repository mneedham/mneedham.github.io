+++
draft = false
date="2013-05-26 23:29:12"
title="Polyglot Persistence: The 'boring' relational option"
tag=['software-development']
category=['Software Development']
+++

<p>I was chatting with <a href="https://twitter.com/gurrie09">Brian Blignaut</a> last week after the <a href="http://nitetech230513.eventbrite.co.uk/?mkt_tok=3RkMMJWWfF9wsRoksq3BZKXonjHpfsX76uUtUaKg38431UFwdcjKPmjr1YAAT8R0aPyQAgobGp5I5FEPTbPYW69ut6ULXg%3D%3D">Equal Experts NoSQL event</a> and he made an interesting observation that in this age of <a href="http://martinfowler.com/bliki/PolyglotPersistence.html">Polyglot Persistence</a> we often rule out the relational database.</p>


<p>I think it's definitely better that we now have many different options for where we store our data - be it as key/value pairs, documents or as a network/graph.</p>


<p>Having these options forces us to think more about how we're going to read/write data in our application whereas previously our effort was focused around which tables we were going to pull out.</p>


<p>Having said that, I realised I'd fallen into the trap that Brian was referring to when thinking through how we could model the energy plans that users were selecting from a results table.</p>


<p>We wanted to run aggregate queries over the data to work out the most popular plans and suppliers on different days and then across different customer segments.</p>


<p>We represented each user selection as an event, stored as a document in <a href="http://www.mongodb.org/">MongoDB</a> which worked fine to start with but queries started to become much slower as the number of documents approached 500,000 or so.</p>


<p>I started thinking about whether we'd be better off storing the data in a different store which was better optimised for the types of queries that we wanted to run.</p>


<p>My initial thought was to use one of the flashier 'NoSQL' databases but <a href="https://twitter.com/a5HOK">Ashok</a> pointed out that the use case - slicing/dicing data at a scale (< 1 m rows) where everything would fit on disc - was perfect for something like <a href="http://www.postgresql.org/">PostgreSQL</a>.</p>


<p>I realised that he was absolutely right and I think it's important to remember that in future - when we talk about <strong>choosing the appropriate data store for our problem that doesn't mean we have to rule out the relational database</strong> even though it's probably more fun to use another store.</p>

