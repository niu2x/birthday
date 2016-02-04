drop database if exists birthday;

create database birthday default character set=utf8;

use birthday;

create table person(
	id int auto_increment,
	name varchar(256) not null,
	sex varchar(16) not null,
	birthday varchar(32) not null,
	calendar varchar(16) not null,
	mail varchar(256) not null,
	primary key(id)
);
