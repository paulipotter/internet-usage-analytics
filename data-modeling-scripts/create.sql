-- ****************** SqlDBM: MySQL ******************;
-- ***************************************************;

DROP TABLE `smartphone_recurrence`;


DROP TABLE `laptop_recurrence`;


DROP TABLE `pc_recurrence`;


DROP TABLE `scams`;


DROP TABLE `smartphones`;


DROP TABLE `cellphones`;


DROP TABLE `tablets`;


DROP TABLE `laptops`;


DROP TABLE `pcs`;


DROP TABLE `entries`;


DROP TABLE `City`;


DROP TABLE `age_group`;


DROP TABLE `gender`;


DROP TABLE `devices`;


DROP TABLE `trust_level`;


DROP TABLE `scam_type`;


DROP TABLE `news_source`;


DROP TABLE `social_media`;


DROP TABLE `recurrence`;


DROP TABLE `binary_entries`;


DROP TABLE `department`;



-- ************************************** `age_group`

CREATE TABLE `age_group`
(
 `group_id` INT NOT NULL ,
 `group`    VARCHAR(50) NOT NULL ,

PRIMARY KEY (`group_id`)
) COMMENT='checked';





-- ************************************** `gender`

CREATE TABLE `gender`
(
 `gender_id` INT NOT NULL ,
 `gender`    VARCHAR(50) NOT NULL ,

PRIMARY KEY (`gender_id`)
) COMMENT='checked';





-- ************************************** `devices`

CREATE TABLE `devices`
(
 `device_id` INT NOT NULL ,
 `name`      VARCHAR(50) NOT NULL ,

PRIMARY KEY (`device_id`)
) COMMENT='checked';





-- ************************************** `trust_level`

CREATE TABLE `trust_level`
(
 `trust_level_id` INT NOT NULL ,
 `level`          VARCHAR(50) NOT NULL ,

PRIMARY KEY (`trust_level_id`)
) COMMENT='checked';





-- ************************************** `scam_type`

CREATE TABLE `scam_type`
(
 `scam_type_id` INT NOT NULL ,
 `type`         VARCHAR(50) NOT NULL ,

PRIMARY KEY (`scam_type_id`)
) COMMENT='checked';





-- ************************************** `news_source`

CREATE TABLE `news_source`
(
 `news_source_id` INT NOT NULL ,
 `name`           VARCHAR(50) NOT NULL ,

PRIMARY KEY (`news_source_id`)
) COMMENT='checked
1 - tv
2 - radio
3 - printed media
4 - online news
5 - Social media';





-- ************************************** `social_media`

CREATE TABLE `social_media`
(
 `social_media_id` INT NOT NULL ,
 `name`            VARCHAR(50) NOT NULL COMMENT '1 - Facebook
2 - Instagram
3 - Twitter
4 - Snapchat
5 - Telegram
6 - Youtube' ,

PRIMARY KEY (`social_media_id`)
) COMMENT='checked
1 - Facebook
2 - Instagram
3 - Twitter
4 - Snapchat
5 - Telegram
6 - Youtube';





-- ************************************** `recurrence`

CREATE TABLE `recurrence`
(
 `recurrence_id` INT NOT NULL ,
 `recurrence`    VARCHAR(50) NOT NULL COMMENT 'P03

1 - every day
2 - couple times a week
3 - once a week
4 - once in a while' ,

PRIMARY KEY (`recurrence_id`)
) COMMENT='checked';





-- ************************************** `binary_entries`

CREATE TABLE `binary_entries`
(
 `bin_id` INT NOT NULL ,
 `answer` VARCHAR(50) NOT NULL ,

PRIMARY KEY (`bin_id`)
) COMMENT='checked';





-- ************************************** `department`

CREATE TABLE `department`
(
 `department_id` INT NOT NULL COMMENT 'ZO
' ,
 `name`          VARCHAR(50) NOT NULL ,

PRIMARY KEY (`department_id`)
) COMMENT='checked';





-- ************************************** `City`

CREATE TABLE `City`
(
 `city_id`       INT NOT NULL ,
 `name`          VARCHAR(50) NOT NULL COMMENT 'ciudad' ,
 `department_id` INT NOT NULL ,

PRIMARY KEY (`city_id`),
KEY `fkIdx_23` (`department_id`),
CONSTRAINT `FK_23` FOREIGN KEY `fkIdx_23` (`department_id`) REFERENCES `department` (`department_id`)
) COMMENT='checked';





-- ************************************** `entries`

CREATE TABLE `entries`
(
 `entry_id`       INT NOT NULL COMMENT 'numero' ,
 `city`           INT NOT NULL ,
 `household_size` INT NOT NULL COMMENT 'P01' ,
 `social_media`   INT NOT NULL ,
 `news_source`    INT NOT NULL ,
 `internet_trust` INT NOT NULL ,
 `device_id`      INT NOT NULL ,
 `gender_id`      INT NOT NULL ,
 `age`            INT NOT NULL ,
 `age_group`      INT NOT NULL ,

PRIMARY KEY (`entry_id`),
KEY `fkIdx_190` (`social_media`),
CONSTRAINT `FK_190` FOREIGN KEY `fkIdx_190` (`social_media`) REFERENCES `social_media` (`social_media_id`),
KEY `fkIdx_199` (`news_source`),
CONSTRAINT `FK_199` FOREIGN KEY `fkIdx_199` (`news_source`) REFERENCES `news_source` (`news_source_id`),
KEY `fkIdx_242` (`internet_trust`),
CONSTRAINT `FK_242` FOREIGN KEY `fkIdx_242` (`internet_trust`) REFERENCES `trust_level` (`trust_level_id`),
KEY `fkIdx_273` (`city`),
CONSTRAINT `FK_273` FOREIGN KEY `fkIdx_273` (`city`) REFERENCES `City` (`city_id`),
KEY `fkIdx_314` (`device_id`),
CONSTRAINT `FK_314` FOREIGN KEY `fkIdx_314` (`device_id`) REFERENCES `devices` (`device_id`),
KEY `fkIdx_334` (`gender_id`),
CONSTRAINT `FK_334` FOREIGN KEY `fkIdx_334` (`gender_id`) REFERENCES `gender` (`gender_id`),
KEY `fkIdx_344` (`age_group`),
CONSTRAINT `FK_344` FOREIGN KEY `fkIdx_344` (`age_group`) REFERENCES `age_group` (`group_id`)
) COMMENT='checked';





-- ************************************** `smartphone_recurrence`

CREATE TABLE `smartphone_recurrence`
(
 `entry_id`      INT NOT NULL ,
 `recurrence_id` INT NOT NULL ,

PRIMARY KEY (`entry_id`),
KEY `fkIdx_320` (`recurrence_id`),
CONSTRAINT `FK_320` FOREIGN KEY `fkIdx_320` (`recurrence_id`) REFERENCES `recurrence` (`recurrence_id`),
KEY `fkIdx_324` (`entry_id`),
CONSTRAINT `FK_324` FOREIGN KEY `fkIdx_324` (`entry_id`) REFERENCES `entries` (`entry_id`)
);





-- ************************************** `laptop_recurrence`

CREATE TABLE `laptop_recurrence`
(
 `entry_id`      INT NOT NULL ,
 `recurrence_id` INT NOT NULL ,

PRIMARY KEY (`entry_id`),
KEY `fkIdx_300` (`entry_id`),
CONSTRAINT `FK_300` FOREIGN KEY `fkIdx_300` (`entry_id`) REFERENCES `entries` (`entry_id`),
KEY `fkIdx_305` (`recurrence_id`),
CONSTRAINT `FK_305` FOREIGN KEY `fkIdx_305` (`recurrence_id`) REFERENCES `recurrence` (`recurrence_id`)
);





-- ************************************** `pc_recurrence`

CREATE TABLE `pc_recurrence`
(
 `entry_id`      INT NOT NULL ,
 `recurrence_id` INT NOT NULL ,

PRIMARY KEY (`entry_id`),
KEY `fkIdx_285` (`recurrence_id`),
CONSTRAINT `FK_285` FOREIGN KEY `fkIdx_285` (`recurrence_id`) REFERENCES `recurrence` (`recurrence_id`),
KEY `fkIdx_294` (`entry_id`),
CONSTRAINT `FK_294` FOREIGN KEY `fkIdx_294` (`entry_id`) REFERENCES `entries` (`entry_id`)
) COMMENT='checked';





-- ************************************** `scams`

CREATE TABLE `scams`
(
 `entry_id`  INT NOT NULL ,
 `reported`  INT NOT NULL ,
 `scam_type` INT NOT NULL ,

PRIMARY KEY (`entry_id`),
KEY `fkIdx_209` (`entry_id`),
CONSTRAINT `FK_209` FOREIGN KEY `fkIdx_209` (`entry_id`) REFERENCES `entries` (`entry_id`),
KEY `fkIdx_213` (`reported`),
CONSTRAINT `FK_213` FOREIGN KEY `fkIdx_213` (`reported`) REFERENCES `binary_entries` (`bin_id`),
KEY `fkIdx_222` (`scam_type`),
CONSTRAINT `FK_222` FOREIGN KEY `fkIdx_222` (`scam_type`) REFERENCES `scam_type` (`scam_type_id`)
) COMMENT='checked';





-- ************************************** `smartphones`

CREATE TABLE `smartphones`
(
 `entry_id` INT NOT NULL ,
 `utilize`  INT NOT NULL COMMENT 'P2E1
' ,
 `quantity` INT NOT NULL COMMENT 'P2E3' ,
 `home`     INT NOT NULL COMMENT 'P2E2
' ,

PRIMARY KEY (`entry_id`),
KEY `fkIdx_106` (`entry_id`),
CONSTRAINT `FK_106` FOREIGN KEY `fkIdx_106` (`entry_id`) REFERENCES `entries` (`entry_id`),
KEY `fkIdx_131` (`home`),
CONSTRAINT `FK_131` FOREIGN KEY `fkIdx_131` (`home`) REFERENCES `binary_entries` (`bin_id`),
KEY `fkIdx_135` (`utilize`),
CONSTRAINT `FK_135` FOREIGN KEY `fkIdx_135` (`utilize`) REFERENCES `binary_entries` (`bin_id`)
) COMMENT='checked';





-- ************************************** `cellphones`

CREATE TABLE `cellphones`
(
 `entry_id` INT NOT NULL ,
 `utilize`  INT NOT NULL COMMENT 'P2D1
' ,
 `home`     INT NOT NULL COMMENT 'P2D2
' ,
 `quantity` INT NOT NULL COMMENT 'P2D3
' ,

PRIMARY KEY (`entry_id`),
KEY `fkIdx_101` (`entry_id`),
CONSTRAINT `FK_101` FOREIGN KEY `fkIdx_101` (`entry_id`) REFERENCES `entries` (`entry_id`),
KEY `fkIdx_123` (`home`),
CONSTRAINT `FK_123` FOREIGN KEY `fkIdx_123` (`home`) REFERENCES `binary_entries` (`bin_id`),
KEY `fkIdx_127` (`utilize`),
CONSTRAINT `FK_127` FOREIGN KEY `fkIdx_127` (`utilize`) REFERENCES `binary_entries` (`bin_id`)
) COMMENT='checked';





-- ************************************** `tablets`

CREATE TABLE `tablets`
(
 `entry_id` INT NOT NULL ,
 `utilize`  INT NOT NULL COMMENT 'P2C1
' ,
 `home`     INT NOT NULL ,
 `quantity` INT NOT NULL COMMENT 'P2C3' ,

PRIMARY KEY (`entry_id`),
KEY `fkIdx_96` (`entry_id`),
CONSTRAINT `FK_96` FOREIGN KEY `fkIdx_96` (`entry_id`) REFERENCES `entries` (`entry_id`),
KEY `fkIdx_119` (`utilize`),
CONSTRAINT `FK_119` FOREIGN KEY `fkIdx_119` (`utilize`) REFERENCES `binary_entries` (`bin_id`),
KEY `fkIdx_174` (`home`),
CONSTRAINT `FK_174` FOREIGN KEY `fkIdx_174` (`home`) REFERENCES `binary_entries` (`bin_id`)
) COMMENT='checked';





-- ************************************** `laptops`

CREATE TABLE `laptops`
(
 `entry_id` INT NOT NULL ,
 `utilize`  INT NOT NULL COMMENT 'P2B1
' ,
 `home`     INT NOT NULL COMMENT 'P2B2
' ,
 `quantity` INT NOT NULL COMMENT 'P2B3
' ,

PRIMARY KEY (`entry_id`),
KEY `fkIdx_62` (`entry_id`),
CONSTRAINT `FK_62` FOREIGN KEY `fkIdx_62` (`entry_id`) REFERENCES `entries` (`entry_id`),
KEY `fkIdx_79` (`home`),
CONSTRAINT `FK_79` FOREIGN KEY `fkIdx_79` (`home`) REFERENCES `binary_entries` (`bin_id`),
KEY `fkIdx_83` (`utilize`),
CONSTRAINT `FK_83` FOREIGN KEY `fkIdx_83` (`utilize`) REFERENCES `binary_entries` (`bin_id`)
) COMMENT='checked';





-- ************************************** `pcs`

CREATE TABLE `pcs`
(
 `entry_id` INT NOT NULL ,
 `utilize`  INT NOT NULL COMMENT 'P2A1
' ,
 `home`     INT NOT NULL COMMENT 'P2A2' ,
 `quantity` INT NOT NULL COMMENT 'P2A3
' ,

PRIMARY KEY (`entry_id`),
KEY `fkIdx_48` (`entry_id`),
CONSTRAINT `FK_48` FOREIGN KEY `fkIdx_48` (`entry_id`) REFERENCES `entries` (`entry_id`),
KEY `fkIdx_71` (`utilize`),
CONSTRAINT `FK_71` FOREIGN KEY `fkIdx_71` (`utilize`) REFERENCES `binary_entries` (`bin_id`),
KEY `fkIdx_75` (`home`),
CONSTRAINT `FK_75` FOREIGN KEY `fkIdx_75` (`home`) REFERENCES `binary_entries` (`bin_id`)
) COMMENT='checked';
