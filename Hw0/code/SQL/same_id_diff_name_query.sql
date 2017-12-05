select * from
(
	select distinct end_id,end_name
	from cbike
)as a,
(
	select distinct end_id,end_name
	from cbike
)as b
where (a.end_id=b.end_id and a.end_name!=b.end_name);


select * from
(
	select distinct start_id,start_name
	from cbike
)as a,
(
	select distinct start_id,start_name
	from cbike
)as b
where (a.start_id=b.start_id and a.start_name!=b.start_name);
