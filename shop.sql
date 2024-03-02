-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               10.4.11-MariaDB - mariadb.org binary distribution
-- Server OS:                    Win64
-- HeidiSQL Version:             9.3.0.4984
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

-- Dumping database structure for shop2
DROP DATABASE IF EXISTS `shop2`;
CREATE DATABASE IF NOT EXISTS `shop2` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;
USE `shop2`;


-- Dumping structure for table shop2.catogary
DROP TABLE IF EXISTS `catogary`;
CREATE TABLE IF NOT EXISTS `catogary` (
  `Cid` varchar(5) NOT NULL,
  `Discription` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`Cid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table shop2.catogary: ~4 rows (approximately)
/*!40000 ALTER TABLE `catogary` DISABLE KEYS */;
REPLACE INTO `catogary` (`Cid`, `Discription`) VALUES
	('B', 'Bakery'),
	('E23', 'hello'),
	('P', 'primary'),
	('S', 'Stationary');
/*!40000 ALTER TABLE `catogary` ENABLE KEYS */;


-- Dumping structure for table shop2.item
DROP TABLE IF EXISTS `item`;
CREATE TABLE IF NOT EXISTS `item` (
  `ID` int(11) NOT NULL,
  `Name` varchar(15) NOT NULL,
  `Price` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table shop2.item: ~61 rows (approximately)
/*!40000 ALTER TABLE `item` DISABLE KEYS */;
REPLACE INTO `item` (`ID`, `Name`, `Price`) VALUES
	(1000, 'Fried Rice', 230.00),
	(1001, 'Parata', 50.00),
	(1002, 'Koththu', 150.00),
	(1003, 'Hoppers', 25.00),
	(1004, 'Red Rice', 250.00),
	(1005, 'Pittu', 600.00),
	(1006, 'Biscute', 55.00),
	(1007, 'Suger', 130.00),
	(1008, 'Flur', 110.00),
	(1009, 'Cake', 230.00),
	(1010, 'Daal', 260.00),
	(1011, 'Beans', 145.00),
	(1012, 'Itly', 35.00),
	(1013, 'Potato', 45.00),
	(1014, 'Cracker', 70.00),
	(1015, 'Samaposha', 80.00),
	(1016, 'Ball', 60.00),
	(1017, 'Battery', 35.00),
	(1018, 'Tea', 15.00),
	(1019, 'Pencil', 20.00),
	(1020, 'Pen', 20.00),
	(1021, 'Book', 80.00),
	(1022, 'Sunlight', 50.00),
	(1023, 'Lux', 62.00),
	(1024, 'Velvet', 65.00),
	(1025, 'Life Buoy', 58.00),
	(1026, 'Pepermint', 0.50),
	(1027, 'Toffee', 2.00),
	(1028, 'Chocalate', 10.00),
	(1029, 'Eno', 25.00),
	(1030, 'Panadol', 24.00),
	(1031, 'Center Fruit', 3.00),
	(1032, 'Anchor', 240.00),
	(1033, 'Raththi', 250.00),
	(1034, 'Horliks', 320.00),
	(1035, 'Viva', 310.00),
	(1036, 'Pathola', 35.00),
	(1037, 'Dunhil', 70.00),
	(1038, 'Gold Leaf', 65.00),
	(1039, 'Bristal', 40.00),
	(1040, 'Astra', 10.00),
	(1041, 'Jam', 30.00),
	(1042, 'Newdale', 35.00),
	(1043, 'Salt', 70.00),
	(1044, 'Sprite', 110.00),
	(1045, 'Coca Cola', 130.00),
	(1046, 'Egg', 23.00),
	(1047, 'Maggi Soup', 50.00),
	(1048, 'Koththumee', 55.00),
	(1049, 'Milk Maid', 360.00),
	(1050, 'Stepler', 210.00),
	(1051, 'Ice Cream', 30.00),
	(1052, 'Broom', 165.00),
	(1053, 'Pastal', 90.00),
	(1054, 'Chicken Cube', 25.00),
	(1055, 'Tipitip', 10.00),
	(1056, 'Soya Meet', 40.00),
	(1058, 'Saman', 100.00),
	(1059, 'Bulbs', 120.00),
	(1060, 'Koththamalli', 75.00),
	(2147483647, 'tttttt', 4443.00);
/*!40000 ALTER TABLE `item` ENABLE KEYS */;


-- Dumping structure for table shop2.sale_det
DROP TABLE IF EXISTS `sale_det`;
CREATE TABLE IF NOT EXISTS `sale_det` (
  `bill_index` int(11) NOT NULL,
  `id` int(11) NOT NULL,
  `price` decimal(10,2) DEFAULT NULL,
  `quentity` float DEFAULT NULL,
  `discount` float DEFAULT NULL,
  KEY `FK_sale_det_item` (`id`),
  KEY `FK_sale_det_sale_sum` (`bill_index`),
  CONSTRAINT `FK_sale_det_item` FOREIGN KEY (`id`) REFERENCES `item` (`ID`),
  CONSTRAINT `FK_sale_det_sale_sum` FOREIGN KEY (`bill_index`) REFERENCES `sale_sum` (`bill_index`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table shop2.sale_det: ~93 rows (approximately)
/*!40000 ALTER TABLE `sale_det` DISABLE KEYS */;
REPLACE INTO `sale_det` (`bill_index`, `id`, `price`, `quentity`, `discount`) VALUES
	(1, 1000, 10.00, 2, 2),
	(1, 1014, 5.00, 4, 1),
	(2, 1001, 50.00, 1, 50),
	(2, 1014, 70.00, 2, 140),
	(3, 1005, 600.00, 3, 20.5),
	(3, 1015, 80.00, 1, 20.5),
	(3, 1026, 0.50, 1, 20.5),
	(3, 1042, 35.00, 12, 20.5),
	(3, 1054, 25.00, 2, 20.5),
	(3, 1045, 130.00, 1, 20.5),
	(3, 1055, 10.00, 2, 20.5),
	(4, 1006, 55.00, 3, 5),
	(4, 1013, 45.00, 2, 5),
	(5, 1005, 600.00, 3, 80),
	(5, 1021, 80.00, 1, 80),
	(5, 1029, 25.00, 4, 80),
	(6, 1010, 260.00, 2, 40),
	(6, 1015, 80.00, 4, 40),
	(7, 1010, 260.00, 3, 4),
	(7, 1023, 62.00, 2, 4),
	(8, 1007, 130.00, 3, 25),
	(8, 1016, 60.00, 4, 25),
	(8, 1024, 60.00, 2, 25),
	(8, 1029, 25.00, 3, 25),
	(9, 1005, 600.00, 1, 50),
	(9, 1010, 260.00, 2, 50),
	(9, 1019, 20.00, 10, 50),
	(9, 1036, 30.00, 2, 50),
	(9, 1040, 10.00, 3, 50),
	(9, 1038, 65.00, 1, 50),
	(9, 1017, 30.00, 4, 50),
	(9, 1048, 55.00, 1, 50),
	(10, 1005, 600.00, 2, 65),
	(10, 1010, 260.00, 4, 65),
	(10, 1017, 35.00, 5, 65),
	(10, 1022, 50.00, 1, 65),
	(0, 1004, 250.00, 2, 2),
	(0, 1009, 200.00, 2, 2),
	(11, 1004, 250.00, 2, 0),
	(12, 1008, 110.00, 2, 25),
	(12, 1012, 35.00, 3, 25),
	(12, 1015, 75.00, 12, 25),
	(13, 1008, 110.00, 3, 40),
	(13, 1012, 35.00, 2, 40),
	(13, 1020, 20.00, 12, 40),
	(13, 1025, 50.00, 4, 40),
	(14, 1012, 35.00, 40, 60),
	(14, 1021, 80.00, 2, 60),
	(14, 1050, 200.00, 5, 60),
	(15, 1013, 45.00, 3, 15),
	(15, 1024, 65.00, 2, 15),
	(15, 1000, 230.00, 3, 15),
	(15, 1045, 130.00, 4, 15),
	(15, 1032, 240.00, 1, 15),
	(16, 1040, 10.00, 5, 21),
	(16, 1016, 55.00, 10, 21),
	(16, 1024, 65.00, 2, 21),
	(16, 1031, 3.00, 20, 21),
	(16, 1053, 90.00, 1, 21),
	(16, 1042, 35.00, 3, 21),
	(16, 1048, 53.00, 12, 21),
	(17, 1008, 110.00, 4, 5),
	(17, 1017, 35.00, 5, 5),
	(17, 1032, 240.00, 3, 5),
	(17, 1038, 60.00, 4, 5),
	(17, 1000, 230.00, 2, 5),
	(17, 1045, 130.00, 1, 5),
	(17, 1033, 245.00, 12, 5),
	(18, 1019, 20.00, 2, 6),
	(18, 1022, 50.00, 1, 6),
	(18, 1036, 30.00, 2, 6),
	(18, 1041, 30.00, 3, 6),
	(18, 1031, 3.00, 2, 6),
	(19, 1059, 120.00, 2, 4),
	(19, 1022, 47.00, 2, 4),
	(20, 1004, 250.00, 2, 30),
	(20, 1014, 70.00, 3, 30),
	(20, 1000, 210.00, 2, 30),
	(21, 1012, 35.00, 1, 0),
	(22, 1013, 45.00, 2, 15),
	(22, 1003, 25.00, 5, 15),
	(22, 1028, 10.00, 7, 15),
	(22, 1042, 30.00, 12, 15),
	(22, 1037, 70.00, 1, 15),
	(23, 1060, 70.00, 2, 20),
	(23, 1037, 70.00, 4, 20),
	(24, 1040, 10.00, 6, 5),
	(24, 1026, 0.50, 7, 5),
	(24, 1000, 230.00, 45, 5),
	(25, 1060, 75.00, 44, 10000),
	(25, 1043, 70.00, 66, 10000),
	(26, 1032, 240.00, 7, 64),
	(26, 1012, 35.00, 8, 64);
/*!40000 ALTER TABLE `sale_det` ENABLE KEYS */;


-- Dumping structure for table shop2.sale_sum
DROP TABLE IF EXISTS `sale_sum`;
CREATE TABLE IF NOT EXISTS `sale_sum` (
  `bill_index` int(5) NOT NULL,
  `date` varchar(50) DEFAULT NULL,
  `discount` float DEFAULT NULL,
  PRIMARY KEY (`bill_index`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table shop2.sale_sum: ~27 rows (approximately)
/*!40000 ALTER TABLE `sale_sum` DISABLE KEYS */;
REPLACE INTO `sale_sum` (`bill_index`, `date`, `discount`) VALUES
	(0, '2020.1.28', 2),
	(1, '2020.1.26', 6),
	(2, '2020.1.26', 90),
	(3, '2020.1.27', 20.5),
	(4, '2020.1.27', 5),
	(5, '2020.1.27', 80),
	(6, '2020.1.27', 40),
	(7, '2020.1.27', 4),
	(8, '2020.1.27', 25),
	(9, '2020.1.27', 50),
	(10, '2020.1.28', 65),
	(11, '2020.4.13', 0),
	(12, '2020.4.13', 25),
	(13, '2020.4.13', 40),
	(14, '2020.4.13', 60),
	(15, '2020.5.5', 15),
	(16, '2020.5.5', 21),
	(17, '2020.5.13', 5),
	(18, '2020.5.13', 6),
	(19, '2020.5.13', 4),
	(20, '2020.5.16', 30),
	(21, '2020.5.16', 0),
	(22, '2020.6.2', 15),
	(23, '2020.6.2', 20),
	(24, '2020.6.20', 5),
	(25, '2022.1.30', 10000),
	(26, '2022.3.25', 64);
/*!40000 ALTER TABLE `sale_sum` ENABLE KEYS */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
