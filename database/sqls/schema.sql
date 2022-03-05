CREATE DATABASE IF NOT EXISTS docker_db;
DROP TABLE IF EXISTS user;
use docker_db;

CREATE TABLE user (
  id int primary key auto_increment,
  username varchar(200) not null,
  password TEXT not null
);