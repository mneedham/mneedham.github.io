+++
draft = false
date="2015-06-15 22:53:33"
title="Northwind: Finding direct/transitive Reports in SQL and Neo4j's Cypher"
tag=['neo4j']
category=['neo4j']
+++

<p>
Every few months we run a <a href="http://www.meetup.com/graphdb-london/events/222398828/">relational to graph meetup</a> at the Neo London office where we go through how to take your data from a relational database and into the graph.
</p>


<p>
We use the <a href="https://code.google.com/p/northwindextended/downloads/detail?name=northwind.postgre.sql">Northwind dataset</a> which often comes as a demo dataset on relational databases and come up with some queries which seem graph in nature. 
</p>


<p>
My favourite query is one which finds out how employees are organised and who reports to whom. I thought it'd be quite interesting to see what it would look like in Postgres SQL as well, just for fun.
</p>


<p>
We'll start off by getting a list of employees and the person they report to:
</p>



~~~sql

SELECT e."EmployeeID", e."ReportsTo"
FROM employees AS e
WHERE e."ReportsTo" is not null;

 EmployeeID | ReportsTo
------------+-----------
          1 |         2
          3 |         2
          4 |         2
          5 |         2
          6 |         5
          7 |         5
          8 |         2
          9 |         5
(8 rows)
~~~

<p>In cypher we'd do this:</p>



~~~cypher

MATCH (e:Employee)<-[:REPORTS_TO]-(sub)
RETURN sub.EmployeeID, e.EmployeeID 

+-------------------------------+
| sub.EmployeeID | e.EmployeeID |
+-------------------------------+
| "4"            | "2"          |
| "5"            | "2"          |
| "1"            | "2"          |
| "3"            | "2"          |
| "8"            | "2"          |
| "9"            | "5"          |
| "6"            | "5"          |
| "7"            | "5"          |
+-------------------------------+
8 rows
~~~

<p>
Next let's find the big boss who doesn't report to anyone. First in SQL:
</p>



~~~sql

SELECT e."EmployeeID" AS bigBoss
FROM employees AS e
WHERE e."ReportsTo" is null

 bigboss
---------
       2
(1 row)
~~~

<p>And now cypher:</p>



~~~cypher

MATCH (e:Employee)
WHERE NOT (e)-[:REPORTS_TO]->()
RETURN e.EmployeeID AS bigBoss

+---------+
| bigBoss |
+---------+
| "2"     |
+---------+
1 row
~~~

<p>We still don't need to join anything so the query isn't that interesting yet. Let's bring in some more properties from the manager record so we have to self join on the employees table:
</p>



~~~sql

SELECT e."FirstName", e."LastName", e."Title", manager."FirstName", manager."LastName", manager."Title"
FROM employees AS e
JOIN employees AS manager ON e."ReportsTo" = manager."EmployeeID"
WHERE e."ReportsTo" is not null

 FirstName | LastName  |          Title           | FirstName | LastName |         Title
-----------+-----------+--------------------------+-----------+----------+-----------------------
 Nancy     | Davolio   | Sales Representative     | Andrew    | Fuller   | Vice President, Sales
 Janet     | Leverling | Sales Representative     | Andrew    | Fuller   | Vice President, Sales
 Margaret  | Peacock   | Sales Representative     | Andrew    | Fuller   | Vice President, Sales
 Steven    | Buchanan  | Sales Manager            | Andrew    | Fuller   | Vice President, Sales
 Michael   | Suyama    | Sales Representative     | Steven    | Buchanan | Sales Manager
 Robert    | King      | Sales Representative     | Steven    | Buchanan | Sales Manager
 Laura     | Callahan  | Inside Sales Coordinator | Andrew    | Fuller   | Vice President, Sales
 Anne      | Dodsworth | Sales Representative     | Steven    | Buchanan | Sales Manager
(8 rows)
~~~


~~~cypher

MATCH (e:Employee)<-[:REPORTS_TO]-(sub)
RETURN sub.FirstName, sub.LastName, sub.Title, e.FirstName, e.LastName, e.Title

+----------------------------------------------------------------------------------------------------------------+
| sub.FirstName | sub.LastName | sub.Title                  | e.FirstName | e.LastName | e.Title                 |
+----------------------------------------------------------------------------------------------------------------+
| "Margaret"    | "Peacock"    | "Sales Representative"     | "Andrew"    | "Fuller"   | "Vice President, Sales" |
| "Steven"      | "Buchanan"   | "Sales Manager"            | "Andrew"    | "Fuller"   | "Vice President, Sales" |
| "Nancy"       | "Davolio"    | "Sales Representative"     | "Andrew"    | "Fuller"   | "Vice President, Sales" |
| "Janet"       | "Leverling"  | "Sales Representative"     | "Andrew"    | "Fuller"   | "Vice President, Sales" |
| "Laura"       | "Callahan"   | "Inside Sales Coordinator" | "Andrew"    | "Fuller"   | "Vice President, Sales" |
| "Anne"        | "Dodsworth"  | "Sales Representative"     | "Steven"    | "Buchanan" | "Sales Manager"         |
| "Michael"     | "Suyama"     | "Sales Representative"     | "Steven"    | "Buchanan" | "Sales Manager"         |
| "Robert"      | "King"       | "Sales Representative"     | "Steven"    | "Buchanan" | "Sales Manager"         |
+----------------------------------------------------------------------------------------------------------------+
8 rows
~~~

<p>
Now let's see how many direct reports each manager has:
</p>



~~~sql

SELECT manager."EmployeeID" AS manager, COUNT(e."EmployeeID") AS reports
FROM employees AS manager
LEFT JOIN employees AS e ON e."ReportsTo" = manager."EmployeeID"
GROUP BY manager
ORDER BY reports DESC;

 manager | reports
---------+---------
       2 |       5
       5 |       3
       1 |       0
       3 |       0
       4 |       0
       9 |       0
       6 |       0
       7 |       0
       8 |       0
(9 rows)
~~~


~~~cypher

MATCH (e:Employee)
OPTIONAL MATCH (e)<-[rel:REPORTS_TO]-(report)
RETURN e.EmployeeID AS employee, COUNT(rel) AS reports

+--------------------+
| employee | reports |
+--------------------+
| "2"      | 5       |
| "5"      | 3       |
| "8"      | 0       |
| "7"      | 0       |
| "1"      | 0       |
| "4"      | 0       |
| "6"      | 0       |
| "9"      | 0       |
| "3"      | 0       |
+--------------------+
9 rows
~~~

<p>
Things start to get more interesting if we find the transitive reporting relationships that exist. I'm not an expert at Postgres but one way to achieve this is by writing <a href="http://www.postgresql.org/docs/current/static/queries-with.html">a recursive WITH query</a> like so:
</p>




~~~sql

WITH RECURSIVE recursive_employees("EmployeeID", "ReportsTo") AS (
        SELECT e."EmployeeID", e."ReportsTo"
        FROM employees e
      UNION ALL
        SELECT e."EmployeeID", e."ReportsTo"
        FROM employees e, recursive_employees re
        WHERE e."EmployeeID" = re."ReportsTo"
)
SELECT re."ReportsTo", COUNT(*) AS count
FROM recursive_employees AS re
WHERE re."ReportsTo" IS NOT NULL
GROUP BY re."ReportsTo";

 ReportsTo | count
-----------+-------
         2 |     8
         5 |     3
(2 rows)
~~~

<p>If there's a simpler way let me know in the comments.</p>


<p>
In cypher we only need to add one character, '*', after the 'REPORTS_TO' relationship to get it to recurse as far as it can. We'll also remove the 'OPTIONAL MATCH' so that we only get back people who have people reporting to them:
</p>



~~~cypher

MATCH (e:Employee)<-[rel:REPORTS_TO*]-(report)
RETURN e.EmployeeID AS employee, COUNT(rel) AS reports

+--------------------+
| employee | reports |
+--------------------+
| "2"      | 8       |
| "5"      | 3       |
+--------------------+
2 rows
~~~

<p>
Now I need to find some relational datasets with more complicated queries to play around with. If you have any ideas do let me know.
</p>

