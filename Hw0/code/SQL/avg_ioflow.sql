select id,sum(out_c)/1488 from iodata
group by id 
order by sum(out_c)/1488 desc
limit 3;

select id,sum(in_c)/1488 from iodata
group by id 
order by sum(in_c)/1488 desc
limit 3;