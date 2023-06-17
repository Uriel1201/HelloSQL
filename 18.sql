create table distances_p18 as
select a.states, a.city as city1, b.city as city2, round (sqrt (power (abs (a.latitude - b.latitude),2) + 
    power (abs (a.longitude - b.longitude),2)),2) as distances
    from stations_p17 a 
inner join stations_p17 b
 on a.states = b.states and a.id < b.id;

select * from distances_p18;

create table ranks_p18 as
select states, city1, city2, distances, rank () over  (partition by states order by distances desc) as rank
from distances_p18;

select * from ranks_p18;

select * from ranks_p18
    where rank = 1;
