DROP TABLE IF EXISTS `user`;
CREATE TABLE IF NOT EXISTS user
(
  `id`               INTEGER(20)  AUTO_INCREMENT,
 `username`          TEXT NOT NULL ,
 `password`          TEXT NOT NULL,
    PRIMARY KEY (`id`)
);

