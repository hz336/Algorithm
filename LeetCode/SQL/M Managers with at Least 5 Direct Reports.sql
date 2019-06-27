/*
The Employee table holds all employees including their managers. Every employee has an Id, and there is also a column for the manager Id.

+------+----------+-----------+----------+
|Id    |Name 	  |Department |ManagerId |
+------+----------+-----------+----------+
|101   |John 	  |A 	      |null      |
|102   |Dan 	  |A 	      |101       |
|103   |James 	  |A 	      |101       |
|104   |Amy 	  |A 	      |101       |
|105   |Anne 	  |A 	      |101       |
|106   |Ron 	  |B 	      |101       |
+------+----------+-----------+----------+

Given the Employee table, write a SQL query that finds out managers with at least 5 direct report. For the above table, your SQL query should return:

+-------+
| Name  |
+-------+
| John  |
+-------+
*/


select name
from Employee e1
inner join (
    select ManagerId
    from Employee
    group by ManagerId
    having count(*) >= 5
) as e2
on e1.Id = e2.ManagerId


/*
If the interviewee doesn't differentiate null vs empty, below answer is simpler to understand.
-- select e2.Name
-- from Employee e1
-- left join Employee e2
-- on e1.ManagerId = e2.Id
-- group by e2.ManagerId
-- having count(*) >= 5
*/



