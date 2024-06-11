/* 
16. Customers Who didn't Buy a Product.

Writing a query to display the id and name of customers who
bought products A and B but didn't buy C. */

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
