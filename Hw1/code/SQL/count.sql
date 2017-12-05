select count(*)
from station
group by cast((latitude-40.655399322509766)/0.001 as int),
cast((longitude+73.89659881591797)/0.001 as int)
order by count(*) desc;