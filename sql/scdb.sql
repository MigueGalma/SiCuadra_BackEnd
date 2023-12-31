-- MySQL Script generated by MySQL Workbench
-- Fri Dec 15 23:36:04 2023
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema scdb
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `scdb` ;

-- -----------------------------------------------------
-- Schema scdb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `scdb` DEFAULT CHARACTER SET utf8 ;
USE `scdb` ;

-- -----------------------------------------------------
-- Table `scdb`.`Codigos`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `scdb`.`Codigos` ;

CREATE TABLE IF NOT EXISTS `scdb`.`Codigos` (
  `idCodigos` INT NOT NULL,
  `orientacion` VARCHAR(45) NOT NULL,
  `medidas` VARCHAR(45) NOT NULL,
  `precio` INT NOT NULL,
  PRIMARY KEY (`idCodigos`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `scdb`.`Registros`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `scdb`.`Registros` ;

CREATE TABLE IF NOT EXISTS `scdb`.`Registros` (
  `idRegistros` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  `apellido` VARCHAR(45) NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  `direccion` VARCHAR(45) NOT NULL,
  `localidad` VARCHAR(45) NOT NULL,
  `provincia` VARCHAR(45) NOT NULL,
  `codigopostal` VARCHAR(45) NOT NULL,
  `tematica` VARCHAR(45) NOT NULL,
  `codigo` INT NOT NULL,
  PRIMARY KEY (`idRegistros`))
ENGINE = InnoDB;



SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

-- -----------------------------------------------------
-- Data for table `scdb`.`Codigos`
-- -----------------------------------------------------
START TRANSACTION;
USE `scdb`;
INSERT INTO `scdb`.`Codigos` (`idCodigos`, `orientacion`, `medidas`, `precio`) VALUES (1090060, 'Individual', '90 cm x 60 cm', 6000);
INSERT INTO `scdb`.`Codigos` (`idCodigos`, `orientacion`, `medidas`, `precio`) VALUES (2075070, 'Horizontal', '75 cm x 70 cm', 9000);
INSERT INTO `scdb`.`Codigos` (`idCodigos`, `orientacion`, `medidas`, `precio`) VALUES (2100070, 'Horizontal', '100 cm x 70 cm', 12000);
INSERT INTO `scdb`.`Codigos` (`idCodigos`, `orientacion`, `medidas`, `precio`) VALUES (2150070, 'Horizontal', '150 cm x 70 cm', 15000);
INSERT INTO `scdb`.`Codigos` (`idCodigos`, `orientacion`, `medidas`, `precio`) VALUES (3075070, 'Vertical', '75 cm x 70 cm', 9000);
INSERT INTO `scdb`.`Codigos` (`idCodigos`, `orientacion`, `medidas`, `precio`) VALUES (3100070, 'Vertical', '100 cm x 70 cm', 12000);
INSERT INTO `scdb`.`Codigos` (`idCodigos`, `orientacion`, `medidas`, `precio`) VALUES (3150070, 'Vertical', '150 cm x 70 cm', 15000);

COMMIT;

