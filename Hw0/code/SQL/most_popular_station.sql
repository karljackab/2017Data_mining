select id,sum(out_c+in_c)/2976 from iodata
group by id 
order by sum(out_c+in_c)/2976 desc
limit 1;