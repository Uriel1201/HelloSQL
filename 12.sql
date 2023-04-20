/* 12. Hacker Scores.

Writing a query to return the hacker ID, name, and
total score (the sum of maximum scores
for each challenge completed). */

create table hackers_p12  (hacker_id integer, name varchar (10));

create table submissions_p12  (sub_id integer, hacker_id integer, challenge_id integer, score integer);

insert into hackers_p12 with names as (
    select 1, 'John' from dual union all 
    select 2, 'Jane' from dual union all 
    select 3, 'Joe'  from dual union all 
    select 4, 'Jim'  from dual
) select * from names;

insert into submissions_p12 with names as  (
    select 101, 1 h, 1 c, 10 from dual union all 
    select 102, 1 h, 1 c, 12 from dual union all 
    select 103, 2 h, 1 c, 11 from dual union all 
    select 104, 2 h, 1 c, 9  from dual union all 
    select 105, 2 h, 2 c, 13 from dual union all 
    select 106, 3 h, 1 c, 9  from dual union all 
    select 107, 3 h, 2 c, 12 from dual union all 
    select 108, 3 h, 2 c, 15 from dual union all 
    select 109, 4 h, 1 c, 0  from dual    
) select * from names;

select * from hackers_p12;
select * from submissions_p12;

create table allscores_p12 as
select hacker_id, max (score) as max_score
       from submissions_p12
       group by hacker_id, challenge_id
       order by 1;

select * from allscores_p12;

select a.hacker_id, h.name, sum (a.max_score) as total
       from allscores_p12 a
       inner join hackers_p12 h
        on a.hacker_id = h.hacker_id
        group by a.hacker_id, h.name
            having sum (a.max_score) > 0
        order by 3 desc, 1;
