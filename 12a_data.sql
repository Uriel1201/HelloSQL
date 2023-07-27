
/* 
12. Hacker Scores.

Writing  a
query to return the hacker ID, name, and
total score (the sum of maximum scores
for each challenge completed) ordered by descending score, and by ascending
hacker ID in the case of score tie. Do not
display entries for hackers with a score
of zero. */ 

create table hackers_p12 (hacker_id integer, name varchar(10));

insert into hackers_p12 with names as (
    select 1, 'John' from dual union all
    select 2, 'Jane' from dual union all
    select 3, 'Joe'  from dual union all
    select 4, 'Jim'  from dual
) select * from names;

create table submissions_p12 (sub_id integer, hacker_id integer, challenge_id integer, score integer);

insert into submissions_p12 with names as (
    select 101 s, 1 h, 1 ch, 10 sc from dual union all 
    select 102 s, 1 h, 1 ch, 12 sc from dual union all 
    select 103 s, 2 h, 1 ch, 11 sc from dual union all 
    select 104 s, 2 h, 1 ch, 9  sc from dual union all 
    select 105 s, 2 h, 2 ch, 13 sc from dual union all 
    select 106 s, 3 h, 1 ch, 9  sc from dual union all 
    select 107 s, 3 h, 2 ch, 12 sc from dual union all 
    select 108 s, 3 h, 2 ch, 15 sc from dual union all 
    select 109 s, 4 h, 1 ch, 0  sc from dual
) select * from names;
