select count(*) from
(
    select distinct start_id from cbike
    union
    select distinct end_id from cbike
) as a;