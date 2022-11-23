# Write your MySQL query statement below
 select distinct pr.product_id, product_name from Product pr
 left join Sales sl on sl.product_id = pr.product_id
 group by sl.product_id
 having MIN(sale_date) >= '2019-01-01' AND MAX(sale_date) <= '2019-03-31' 