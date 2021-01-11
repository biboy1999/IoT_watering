-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: db
-- Generation Time: Jan 05, 2021 at 03:12 AM
-- Server version: 10.5.8-MariaDB-1:10.5.8+maria~focal
-- PHP Version: 7.4.11

SET FOREIGN_KEY_CHECKS=0;
SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `auto_water`
--
CREATE DATABASE IF NOT EXISTS `auto_water` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `auto_water`;

-- --------------------------------------------------------

--
-- Table structure for table `record`
--
-- Creation: Jan 05, 2021 at 03:11 AM
-- Last update: Jan 05, 2021 at 03:11 AM
--

CREATE TABLE `record` (
  `ID` int(11) NOT NULL,
  `IOT_ID` int(11) DEFAULT NULL,
  `air_temp` float DEFAULT NULL,
  `air_hum` float DEFAULT NULL,
  `dirt_hum` float NOT NULL,
  `ts` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `record`
--

INSERT INTO `record` (`ID`, `IOT_ID`, `air_temp`, `air_hum`, `dirt_hum`, `ts`) VALUES
(1, 1, 32.8, 58.3, 32.5, '2021-01-05 03:11:27'),
(2, 1, 33.2, 56.4, 55.6, '2021-01-05 03:11:31'),
(3, 1, 33.8, 55.3, 87.6, '2021-01-05 03:11:36'),
(4, 1, 34, 50.3, 23.8, '2021-01-05 03:11:39'),
(5, 1, 33.1, 48.2, 56.4, '2021-01-05 03:11:42');

-- --------------------------------------------------------

--
-- Table structure for table `setting`
--
-- Creation: Dec 22, 2020 at 03:01 AM
--

CREATE TABLE `setting` (
  `IOT_ID` int(11) DEFAULT NULL,
  `water_schedule` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `setting`
--

INSERT INTO `setting` (`IOT_ID`, `water_schedule`) VALUES
(1, '00:00;7:00;17:00;21:00');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `record`
--
ALTER TABLE `record`
  ADD PRIMARY KEY (`ID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `record`
--
ALTER TABLE `record`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
SET FOREIGN_KEY_CHECKS=1;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
