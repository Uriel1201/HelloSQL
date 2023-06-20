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

select * from orders_p21;
select * from products_p21;

create table pairs_p21 as
select a.order_id, a.product_id as product1, b.product_id as product2
    from orders_p21 a 
    inner join orders_p21 b 
    on a.order_id = b.order_id and 
a.product_id  < b.product_id;

select * from pairs_p21;

create table PairNames_p21 as 
select a.product1, a.product2, concat (b.name, c.name) as pairs 
    from pairs_p21 a 
inner join products_p21 b
on a.product1 = b.id 
inner join products_p21 c
on a.product2 = c.id;

select * from PairNames_p21;

select * from (
select pairs, count(*) as freq
    from PairNames_p21 
group by pairs 
order by 2 desc) 
    where rownum <= 3;
