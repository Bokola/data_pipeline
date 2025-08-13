-- check if item discount always > 0
select *
from 
    {{ref('fct_orders')}}
where item_discount_amount > 0