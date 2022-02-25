CREATE DATABASE IF NOT EXISTS db;
DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS post;


CREATE TABLE user (
  id int primary key auto_increment,
  username TEXT not null,
  password TEXT not null,
  UNIQUE (username)
);

-- CREATE TABLE post (
--   id int primary key auto_increment,
--   username varchar(30) not null,
--   password varchar(30) not null,
--   UNIQUE (username)
-- );