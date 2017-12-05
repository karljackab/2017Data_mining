create table station(
id varchar(10),
name varchar(100),
latitude float,
longitude float,
primary key(id),
index(id)
);

load data local infile './station_data.csv'
into table station
fields terminated by ','
enclosed by '"'
lines terminated by '\n'
ignore 1 lines;