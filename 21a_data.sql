/* 
21. Commonly Purchased Together.

Writing a query to return the names and purchase
frequency of the top three pairs of
products most often bought together. */

create table orders_p21 (order_id integer, customer_id integer, product_id integer); 
create table products_p21 (id integer, name char);

insert into orders_p21 with names as (
    select 1 o, 1 c, 1 from dual union all 
    select 1 o, 1 c, 2 from dual union all 
    select 1 o, 1 c, 3 from dual union all 
    select 2 o, 2 c, 1 from dual union all 
    select 2 o, 2 c, 2 from dual union all 
    select 2 o, 2 c, 4 from dual union all 
    select 3 o, 1 c, 5 from dual
) select * from names;

insert into products_p21 with names as (
    select 1, 'A' from dual union all
    select 2, 'B' from dual union all 
    select 3, 'C' from dual union all 
    select 4, 'D' from dual union all 
    select 5, 'E' from dual
) select * from names;
