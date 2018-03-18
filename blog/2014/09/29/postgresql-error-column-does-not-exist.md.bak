+++
draft = false
date="2014-09-29 22:40:31"
title="PostgreSQL: ERROR:  column does not exist"
tag=['software-development']
category=['Software Development']
+++

<p>I've been playing around with PostgreSQL recently and in particular <a href="https://code.google.com/p/northwindextended/downloads/detail?name=northwind.postgre.sql&can=2&q=">the Northwind dataset</a> typically used as an introductory data set for relational databases.</p>


<p>Having imported the data I wanted to take a quick look at the employees table:</p>



~~~sql

postgres=# select * from employees limit 1;
 EmployeeID | LastName | FirstName |        Title         | TitleOfCourtesy | BirthDate  |  HireDate  |           Address           |  City   | Region | PostalCode | Country |   HomePhone    | Extension | Photo |                                                                                      Notes                                                                                      | ReportsTo |              PhotoPath               
------------+----------+-----------+----------------------+-----------------+------------+------------+-----------------------------+---------+--------+------------+---------+----------------+-----------+-------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+--------------------------------------
          1 | Davolio  | Nancy     | Sales Representative | Ms.             | 1948-12-08 | 1992-05-01 | 507 - 20th Ave. E.\nApt. 2A | Seattle | WA     | 98122      | USA     | (206) 555-9857 | 5467      | \x    | Education includes a BA in psychology from Colorado State University in 1970.  She also completed "The Art of the Cold Call."  Nancy is a member of Toastmasters International. |         2 | http://accweb/emmployees/davolio.bmp
(1 row)
~~~

<p>That works fine but what if I only want to return the 'EmployeeID' field?</p>



~~~sql

postgres=# select EmployeeID from employees limit 1;
ERROR:  column "employeeid" does not exist
LINE 1: select EmployeeID from employees limit 1;
~~~

<p>I hadn't realised (or had forgotten) that <a href="http://stackoverflow.com/questions/20878932/are-postgresql-column-names-case-sensitive">field names get lower cased</a> so we need to quote the name if it's been stored in mixed case:</p>



~~~sql

postgres=# select "EmployeeID" from employees limit 1;
 EmployeeID 
------------
          1
(1 row)
~~~

<p>From my reading the suggestion seems to be to have your field names lower cased to avoid this problem but since it's just a dummy data set I guess I'll just put up with the quoting overhead for now.</p>

