drop ----
DROP TABLE IF EXISTS `students`;

---- create ----
-- create table IF not exists `students`
-- (id carchar(30) not null primary key, name varchar(64) not null, email varchar(100)) DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ---- drop ----
-- DROP TABLE IF EXISTS `books`;

-- ---- create ----
-- create table IF not exists `books`
-- (id int auto_increment primary key, title varchar(64) not null, ISBN bigint(15) not null, author varchar(40), author_kana varchar(80), publisher varchar(60),  overview varchar(500), image_url varchar(500)) DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

DROP TABLE IF EXISTS `rent_hist`;

---- create ----
-- create table IF not exists `rent_hist`
-- (id int auto_increment primary key, bookid int, renterid int, return_date DATE,  rent_date DATE, returned boolean DEFAULT false, CONSTRAINT fk_renter_id FOREIGN KEY (renterid) REFERENCES students (id) ON DELETE RESTRICT ON UPDATE RESTRICT,CONSTRAINT fk_book_id FOREIGN KEY (bookid) REFERENCES books (id) ON DELETE RESTRICT ON UPDATE RESTRICT) DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

