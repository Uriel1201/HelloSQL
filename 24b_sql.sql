/* 24. Taxi Cancel Rate.

Writing a query to return the
cancellation rate in the first two days in
October. */

select * from trips_p24;
select * from users_p24;

create table noBanned_p24 as 
select request_date, status 
    from trips_p24 
    where rider_id not in 
        (select user_id from users_p24 
             where banned = 'yes') and 
          driver_id not in 
         (select user_id from users_p24 
             where banned = 'yes')
          order by 1;

select * from noBanned_p24;

select request_date, 1 - avg (case when status = 'completed' then 1 else 0 end) as cancellation_rate
   from noBanned_p24 
    group by request_date
    having extract(day from request_date) <= 2
    order by 1;
