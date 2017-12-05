create table iodata(
    id varchar(10),
    tm int,
    in_c int,
    out_c int,
    primary key(id,tm),
    index(id)
);

load data local infile './inout_flow_data.csv'
into table iodata
fields terminated by ','
enclosed by '"'
lines terminated by '\n'
ignore 1 lines;