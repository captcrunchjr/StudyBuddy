#Create database userAccount;
USE userAccount;

CREATE TABLE user_info(
ID INT AUTO_INCREMENT,
username varchar(100),
password varchar(100),
email varchar(100),
UNIQUE (username),
UNIQUE (email)
);

CREATE TABLE users(
name varchar(100)
);

CREATE TABLE user_account(
major varchar(100),
classes_enrolled varchar(200),
classes_taken varchar(1000),
year varchar(50),
GPA DOUBLE
);


CREATE TABLE colleges(
name varchar(200)
);

CREATE TABLE college_computing(
name varchar(200)
);

CREATE table classes(
name varchar(100)
);