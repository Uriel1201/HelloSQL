/* 
24. Taxi Cancel Rate.

Writing a query to return the
cancellation rate in the first two days in
October. */

create table trips_p24 (trip_id integer, rider_id integer, driver_id integer, status varchar(25), request_date date);
create table users_p24 (user_id integer, banned varchar(3), type varchar(7));

insert into trips_p24 with names as (
    select 1 t, 1, 10, 'completed',           '01-OCT-20' from dual union all 
    select 2 t, 2, 11, 'cancelled_by_driver', '01-OCT-20' from dual union all 
    select 3 t, 3, 12, 'completed',           '01-OCT-20' from dual union all 
    select 4 t, 4, 10, 'cancelled_by_rider',  '02-OCT-20' from dual union all 
    select 5 t, 1, 11, 'completed',           '02-OCT-20' from dual union all 
    select 6 t, 2, 12, 'completed',           '02-OCT-20' from dual union all 
    select 7 t, 3, 11, 'completed',           '03-OCT-20' from dual 
) select * from names;

insert into users_p24 with names as (
    select 1,  'no',  'rider'  from dual union all 
    select 2,  'yes', 'rider'  from dual union all 
    select 3,  'no',  'rider'  from dual union all 
    select 4,  'no',  'rider'  from dual union all 
    select 10, 'no',  'driver' from dual union all 
    select 11, 'no',  'driver' from dual union all 
    select 12, 'no',  'driver' from dual
) select * from names;
