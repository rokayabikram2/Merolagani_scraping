-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 26, 2024 at 02:06 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `garima bank`
--

-- --------------------------------------------------------

--
-- Table structure for table `company_detail`
--

CREATE TABLE `company_detail` (
  `Sector` varchar(1000) NOT NULL,
  `Share_Out` int(11) NOT NULL,
  `Market_Price` int(11) NOT NULL,
  `Changes` int(11) NOT NULL,
  `Last_Trade_On` int(11) NOT NULL,
  `52_Weeks_High_Low` int(11) NOT NULL,
  `120_Day_Average` int(11) NOT NULL,
  `1_Year_Yield` int(11) NOT NULL,
  `EPS` int(11) NOT NULL,
  `P_E_Ratio` int(11) NOT NULL,
  `Book_Value` int(11) NOT NULL,
  `PBV` int(11) NOT NULL,
  `Dividend` int(11) NOT NULL,
  `Bonus` int(11) NOT NULL,
  `Right_Share` int(11) NOT NULL,
  `30_Day_Avg_Volume` int(11) NOT NULL,
  `Market_Capitalization` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `company_detail`
--

INSERT INTO `company_detail` (`Sector`, `Share_Out`, `Market_Price`, `Changes`, `Last_Trade_On`, `52_Weeks_High_Low`, `120_Day_Average`, `1_Year_Yield`, `EPS`, `P_E_Ratio`, `Book_Value`, `PBV`, `Dividend`, `Bonus`, `Right_Share`, `30_Day_Avg_Volume`, `Market_Capitalization`) VALUES
('', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
('', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
('', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
('', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
('', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
('', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
