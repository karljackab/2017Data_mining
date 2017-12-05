select tm%48,sum(out_c)
from iodata
group by tm%48
order by sum(out_c) desc;

select tm%48,sum(in_c)
from iodata
group by tm%48
order by sum(in_c) desc;

select tm,sum(out_c)
from iodata
group by tm
order by sum(out_c) desc
limit 20;

select tm,sum(in_c)
from iodata
group by tm
order by sum(in_c) desc
limit 20;