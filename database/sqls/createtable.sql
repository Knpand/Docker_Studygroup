CREATE DATABASE IF NOT EXISTS docker_db;
DROP TABLE IF EXISTS user;

CREATE TABLE user
(
    id int auto_increment primary key,
    name varchar(10) not null,
    pass varchar not null
);