select start_id,end_id,count(*)
from cbike
group by start_id,end_id
order by count(*) desc
limit 3;

select start_id,end_id,count(*)
from cbike
where
start_time like '2017-07-01%' or
start_time like '2017-07-02%' or
start_time like '2017-07-08%' or
start_time like '2017-07-09%' or
start_time like '2017-07-15%' or
start_time like '2017-07-16%' or
start_time like '2017-07-22%' or
start_time like '2017-07-23%' or
start_time like '2017-07-29%' or
start_time like '2017-07-30%'
group by start_id,end_id
order by count(*) desc
limit 3;