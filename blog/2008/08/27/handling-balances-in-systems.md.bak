+++
draft = false
date="2008-08-27 21:47:15"
title="Handling balances in systems"
tag=['software-development', 'finance', 'databases']
category=['Software Development']
+++

On one of my previous projects one of the problems that we had to solve was how to handle balances - we were working on a cash service for a financial services company.

The main discussion often centres around how often the balance should be updated. From my experience there are two main ways that we can go about this:

<h3>Real time update after every transaction</h3>

This is perhaps the most obvious approach and the implementation is fairly simple. After every transaction is executed the appropriate accounts should be debited/credited as part of that <a href="http://martinfowler.com/eaaCatalog/unitOfWork.html">unit of work</a>.

The benefit of doing it this way is that when we want to get the latest balance for an account we can easily do it without the need for any calculations. The balance stored in the database is always accurate.

The problems begin when the number of transactions being executed starts to increase. The likelihood is that most transactions will involve one of the bank's house accounts which means that you very quickly end up with severe database locking issues.

These can theoretically be solved by using row level locking but it's only a matter of time before the performance of the system is completely non existent.

<h3>Batch updates at varying intervals</h3>

The alternative is to not store the balance in real time and instead have a batch job running each night (for example) that updates it until the end of that day.

This approach was first shown to me by <a href="http://blog.halvard.skogsrud.com/">a colleague</a> who also pointed out <a href="http://blogs.msdn.com/pathelland/archive/2007/06/14/accountants-don-t-use-erasers.aspx">this article</a> by <a href="http://blogs.msdn.com/pathelland/default.aspx">Pat Helland</a> on the benefits of bringing the ideas of accountancy into software design.

The trade off that we incur as a result of taking this approach is that we now need to create a batch job to calculate how the balances have changed each day and update these in the database. 

Finding the current balance for an account also becomes more difficult as we now need to take the previous day's balance and apply the impact of today's transactions to come up with a real time balance.

The problems with database locking are removed, however, and this approach scales much more easily.

There are other interesting challenges around handling data like this in financial systems but balances strike me as particularly interesting since the most obvious solution is not necessarily the best one.

