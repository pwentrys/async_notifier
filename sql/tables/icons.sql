CREATE TABLE `icons` (
  `id` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `datetime_create` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `datetime_update` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `path` VARCHAR (100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  UNIQUE KEY `path_UNIQUE` (`path`),
  UNIQUE KEY `idpath_UNIQUE` (`id`, `path`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8