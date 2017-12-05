create table cbike(
    trip_duration int,
    start_time datetime,
    stop_time datetime,
    start_id varchar(10),
    start_name varchar(100),
    start_latitude float,
    start_longitude float,
    end_id varchar(10),
    end_name varchar(100),
    end_latitude float,
    end_longitude float,
    bike_id varchar(10),
    user_type varchar(20),
    birth_year int,
    gender varchar(5),
    index(start_id,start_time,stop_time,end_id)
);

load data local infile './201707-citibike-tripdata.csv'
into table cbike
fields terminated by ','
enclosed by '"'
lines terminated by '\n'
ignore 1 lines;