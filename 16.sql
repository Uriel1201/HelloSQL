/* 16. Customers Who didn't Buy a Product.

Writing a query to display the id and name of customers who
bought products A and B but didn't buy C */

create table customers_p16 (id integer, name varchar (20));
create table orders_p16 (order_id integer, customer_id integer, product_name char);

insert into customers_p16 with names as (
    select 1, 'Daniel'    from dual union all 
    select 2, 'Diana'     from dual union all 
    select 3, 'Elizabeth' from dual union all 
    select 4, 'John'      from dual
) select * from names;

insert into orders_p16 with names as (
    select 1 i, 1, 'A' from dual union all 
    select 2 i, 1, 'B' from dual union all 
    select 3 i, 2, 'A' from dual union all 
    select 4 i, 2, 'B' from dual union all 
    select 5 i, 2, 'C' from dual union all 
    select 6 i, 3, 'A' from dual union all 
    select 7 i, 3, 'A' from dual union all 
    select 8 i, 3, 'B' from dual union all 
    select 9 i, 3, 'D' from dual
) select * from names;

select * from customers_p16;
select * from orders_p16;

create table AB_but_noC as
select distinct customer_id 
    from orders_p16 
    where customer_id in (select customer_id 
                             from orders_p16 
                             where product_name = 'A') 
    and   customer_id in (select customer_id 
                             from orders_p16 
                             where product_name = 'B')
    and   customer_id not in (select customer_id 
                                 from orders_p16 
                                 where product_name = 'C')
;

select * from AB_but_noC;

select a.customer_id, b.name 
    from AB_but_noC a 
    left join customers_p16 b 
    on a.customer_id = b.id 
    order by 1;
