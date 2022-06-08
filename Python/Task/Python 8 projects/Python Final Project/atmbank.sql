-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 08, 2022 at 05:32 PM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 8.1.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `atmbank`
--

-- --------------------------------------------------------

--
-- Table structure for table `atmcard`
--

CREATE TABLE `atmcard` (
  `accno` int(11) DEFAULT NULL,
  `fname` varchar(10) DEFAULT NULL,
  `lname` varchar(10) DEFAULT NULL,
  `qrname` varchar(20) DEFAULT NULL,
  `cvv` varchar(3) DEFAULT NULL,
  `dateexp` date DEFAULT NULL,
  `card1` int(11) DEFAULT NULL,
  `card2` int(11) DEFAULT NULL,
  `card3` int(11) DEFAULT NULL,
  `card4` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `atmcard`
--

INSERT INTO `atmcard` (`accno`, `fname`, `lname`, `qrname`, `cvv`, `dateexp`, `card1`, `card2`, `card3`, `card4`) VALUES
(36632, 'rahul', 'kanoj', '36632.png', '419', '2034-04-28', 548, 7751, 7642, 536),
(97163, 'vidhi', 'jadhav', '97163.png', '973', '2029-04-29', 6856, 770, 1212, 6699),
(95741, 'Prasad', 'Jadhav', '95741.png', '617', '2029-04-29', 562, 6237, 3221, 7237),
(72759, 'sunil', 'bhave', '72759.png', '813', '2029-04-30', 3306, 3198, 9041, 4135);

-- --------------------------------------------------------

--
-- Table structure for table `ministate`
--

CREATE TABLE `ministate` (
  `accno` int(11) DEFAULT NULL,
  `type` varchar(2) DEFAULT NULL,
  `amount` float(10,2) DEFAULT NULL,
  `date` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `ministate`
--

INSERT INTO `ministate` (`accno`, `type`, `amount`, `date`) VALUES
(34912, 'cr', 500.00, '2022-04-26'),
(14992, 'cr', 5000.00, '2022-04-28'),
(36632, 'cr', 5000.00, '2022-04-29'),
(97163, 'cr', 50000.00, '2022-04-29'),
(97163, 'cr', 6000.00, '2022-04-29'),
(97163, 'dr', 500.00, '2022-04-29'),
(97163, 'dr', 500.00, '2022-04-29'),
(97163, 'dr', 100.00, '2022-04-29'),
(97163, 'dr', 100.00, '2022-04-29'),
(97163, 'dr', 100.00, '2022-04-29'),
(97163, 'dr', 100.00, '2022-04-29'),
(97163, 'dr', 100.00, '2022-04-29'),
(97163, 'dr', 100.00, '2022-04-29'),
(97163, 'dr', 100.00, '2022-04-29'),
(97163, 'dr', 100.00, '2022-04-29'),
(97163, 'dr', 100.00, '2022-04-29'),
(97163, 'dr', 100.00, '2022-04-29'),
(97163, 'dr', 100.00, '2022-04-29'),
(97163, 'dr', 100.00, '2022-04-29'),
(97163, 'dr', 100.00, '2022-04-29'),
(97163, 'dr', 100.00, '2022-04-29'),
(97163, 'dr', 100.00, '2022-04-29'),
(97163, 'dr', 100.00, '2022-04-29'),
(97163, 'dr', 2500.00, '2022-04-29'),
(97163, 'dr', 2800.00, '2022-04-29'),
(95741, 'cr', 2500.00, '2022-04-29'),
(95741, 'cr', 25000.00, '2022-04-29'),
(95741, 'dr', 2800.00, '2022-04-29'),
(72759, 'cr', 5000.00, '2022-04-30'),
(72759, 'dr', 4800.00, '2022-04-30');

-- --------------------------------------------------------

--
-- Table structure for table `note`
--

CREATE TABLE `note` (
  `atm_id` varchar(4) DEFAULT NULL,
  `twoth` int(11) DEFAULT 0,
  `fivhun` int(11) DEFAULT 0,
  `twohun` int(11) DEFAULT 0,
  `onehun` int(11) DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `note`
--

INSERT INTO `note` (`atm_id`, `twoth`, `fivhun`, `twohun`, `onehun`) VALUES
('101', 3, 14, 60, 105);

-- --------------------------------------------------------

--
-- Table structure for table `staff`
--

CREATE TABLE `staff` (
  `fname` varchar(15) DEFAULT NULL,
  `lname` varchar(15) DEFAULT NULL,
  `usname` varchar(20) DEFAULT NULL,
  `password` varchar(20) DEFAULT NULL,
  `contact` varchar(13) DEFAULT NULL,
  `aadhar` varchar(16) DEFAULT NULL,
  `city` varchar(15) DEFAULT NULL,
  `dob` date DEFAULT NULL,
  `Position` varchar(15) DEFAULT NULL,
  `gender` varchar(8) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `staff`
--

INSERT INTO `staff` (`fname`, `lname`, `usname`, `password`, `contact`, `aadhar`, `city`, `dob`, `Position`, `gender`) VALUES
('tejas', 'jadhav', 'teja123', 'tejasj', '956235457', '4113562', 'Mulund', '2001-06-13', 'cashier', 'male');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `fname` varchar(15) DEFAULT NULL,
  `lname` varchar(15) DEFAULT NULL,
  `usname` varchar(20) DEFAULT NULL,
  `password` varchar(20) DEFAULT NULL,
  `contact` varchar(13) DEFAULT NULL,
  `aadhar` varchar(6) DEFAULT NULL,
  `city` varchar(15) DEFAULT NULL,
  `dob` date DEFAULT NULL,
  `acctype` varchar(10) DEFAULT NULL,
  `gender` varchar(8) DEFAULT NULL,
  `balance` float(10,2) DEFAULT NULL,
  `accno` int(7) NOT NULL,
  `cvv` int(4) DEFAULT NULL,
  `pin` int(4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`fname`, `lname`, `usname`, `password`, `contact`, `aadhar`, `city`, `dob`, `acctype`, `gender`, `balance`, `accno`, `cvv`, `pin`) VALUES
('ruchita', 'gurav', 'ruchi', 'ruchitag', '956616653', '756859', 'Karjat', '1999-10-12', 'saving', 'female', 5000.00, 14992, 663, NULL),
('bhavesh', 'ainkar', 'bhavesh123', 'bhavesha', '96562235', '45623', 'Karjat', '2001-01-19', 'saving', 'male', 4500.00, 34912, 923, NULL),
('rahul', 'kanoj', 'rahul123', 'rahulk', '95648766', '326541', 'kalyan', '2000-03-02', 'saving', 'male', 5000.00, 36632, 419, NULL),
('sunil', 'bhave', 'charlie', 'sunilb', '7709931296', '562664', 'Badlapur', '1999-04-02', 'saving', 'male', 200.00, 72759, 813, 482),
('Prasad', 'Jadhav', 'pvj1998', 'Prasad@123', '8975634953', '236', 'Nashik', '1998-03-13', 'saving', 'male', 24700.00, 95741, 617, 1680),
('vidhi', 'jadhav', 'soni2532000', '270121', '7045102996', '784589', 'kalyan', '2000-03-25', 'saving', 'female', 48100.00, 97163, 973, 482),
('rutuja', 'sawant', 'rutu123', 'rutujas', '956845623', '411689', 'Karjat', '2000-07-13', 'current', 'female', 12600.00, 99367, 556, NULL);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `atmcard`
--
ALTER TABLE `atmcard`
  ADD KEY `accno` (`accno`);

--
-- Indexes for table `ministate`
--
ALTER TABLE `ministate`
  ADD KEY `accno` (`accno`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`accno`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `atmcard`
--
ALTER TABLE `atmcard`
  ADD CONSTRAINT `atmcard_ibfk_1` FOREIGN KEY (`accno`) REFERENCES `user` (`accno`) ON DELETE CASCADE;

--
-- Constraints for table `ministate`
--
ALTER TABLE `ministate`
  ADD CONSTRAINT `ministate_ibfk_1` FOREIGN KEY (`accno`) REFERENCES `user` (`accno`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
