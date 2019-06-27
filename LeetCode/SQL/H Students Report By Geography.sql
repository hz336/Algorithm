/*
A U.S graduate school has students from Asia, Europe and America. The students' location information are stored in table student as below.
| name   | continent |
|--------|-----------|
| Jack   | America   |
| Pascal | Europe    |
| Xi     | Asia      |
| Jane   | America   |

Pivot the continent column in this table so that each name is sorted alphabetically and displayed underneath its corresponding continent. The output
headers should be America, Asia and Europe respectively. It is guaranteed that the student number from America is no less than either Asia or Europe.

For the sample input, the output is:
| America | Asia | Europe |
|---------|------|--------|
| Jack    | Xi   | Pascal |
| Jane    |      |        |

*/

select America, Asia, Europe
from
	(select @as:=0, @am:=0, @eu:=0) t,
	(
		select @as:=@as + 1 as asid, name as Asia
		from student
		where continent = 'Asia'
		order by Asia
	) as t1
	right join
	(
		select @am:=@am + 1 as amid, name as America
		from student
		where continent = 'America'
		order by America
	) as t2
	on asid = amid
    left join
	(
		select @eu:=@eu + 1 as euid, name as Europe
		from student
		where continent = 'Europe'
		order by Europe
	) as t3
	on euid = amid


	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	