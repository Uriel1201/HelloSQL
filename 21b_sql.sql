/* 
21. Commonly Purchased Together.

Writing a query to return the names and purchase
frequency of the top three pairs of
products most often bought together. */

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
