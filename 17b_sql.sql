/* 
17. Median Latitude. 

Writint a query to return the median
latitude of weather stations from each
state. */ 

select * from stations_p17;

create table N_p17 as
select states, latitude, 
    row_number () over (partition by states order by latitude) as orders,
    count (*) over (partition by states) as n
    from stations_p17;

select * from N_p17;

select states, avg(latitude) as median
    from N_p17 
    where orders <= (1.0 * n / 2) + 1 
    and   orders >= 1.0 * n / 2 
    group by states;
