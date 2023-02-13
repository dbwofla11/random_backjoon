-- create database if not exists random_problem;

create table if not exists url_table(
    ploblem_url varchar(50) not null,
    primary key(ploblem_url)
);


create table if not exists ploblem(
    num int(11) not null auto_increment,
    title varchar(50),
    problem_text varchar(500),
    ploblem_url varchar(50),
    primary key(num)
);

