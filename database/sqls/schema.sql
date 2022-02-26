CREATE DATABASE IF NOT EXISTS db;
DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS post;
use db;

CREATE TABLE user (
  id int primary key auto_increment,
  username varchar(200) not null,
  password TEXT not null,
  UNIQUE (username)
);

-- CREATE TABLE post (
--   id int primary key auto_increment,
--   username varchar(30) not null,
--   password varchar(30) not null,
--   UNIQUE (username)
-- );