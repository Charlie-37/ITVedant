-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 02, 2022 at 12:32 PM
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
-- Database: `dbhospital`
--

-- --------------------------------------------------------

--
-- Table structure for table `bill_table`
--

CREATE TABLE `bill_table` (
  `Bill_No` varchar(50) NOT NULL,
  `P_ID` varchar(10) NOT NULL,
  `Doctor_Charge` int(11) NOT NULL,
  `Medicine_Charge` int(11) NOT NULL,
  `Room_Charge` int(11) NOT NULL,
  `Operation_Charge` int(11) DEFAULT 0,
  `No_Of_Days` int(11) DEFAULT 0,
  `Nursing_Charge` int(11) DEFAULT 0,
  `Advance` int(11) DEFAULT 0,
  `Lab_Charge` int(11) DEFAULT 0,
  `Bill` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `bill_table`
--

INSERT INTO `bill_table` (`Bill_No`, `P_ID`, `Doctor_Charge`, `Medicine_Charge`, `Room_Charge`, `Operation_Charge`, `No_Of_Days`, `Nursing_Charge`, `Advance`, `Lab_Charge`, `Bill`) VALUES
('10001', '1001', 600, 2500, 100, 0, 0, 0, 0, 1200, 4400),
('10002', '1002', 700, 1500, 100, 0, 0, 0, 0, 1900, 4200),
('10003', '1003', 400, 1000, 100, 0, 0, 0, 0, 200, 1700),
('10004', '1006', 500, 700, 100, 0, 0, 0, 0, 1900, 3200),
('10005', '1005', 600, 1100, 100, 0, 0, 0, 0, 1100, 2900),
('10006', '1004', 1200, 2000, 300, 0, 0, 600, 500, 900, 4500),
('10007', '1008', 2900, 1500, 700, 0, 0, 900, 1000, 800, 5800),
('10008', '1007', 4900, 1400, 700, 0, 0, 1400, 600, 1200, 9000);

-- --------------------------------------------------------

--
-- Table structure for table `dr_table`
--

CREATE TABLE `dr_table` (
  `Dr_Id` int(11) NOT NULL CHECK (`Dr_Id` >= 101),
  `Dr_Name` varchar(30) NOT NULL,
  `Contact` varchar(20) NOT NULL,
  `Dr_Dept` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `dr_table`
--

INSERT INTO `dr_table` (`Dr_Id`, `Dr_Name`, `Contact`, `Dr_Dept`) VALUES
(101, 'Dr.Rajendra J.', '954622812', 'Thyrorid Specialist'),
(102, 'Dr.Vikrant N..', '9124826322', 'Dermatologist'),
(103, 'Dr. Sujay K', '823147616', 'Ophthalmologist'),
(104, 'Dr. Narayan S.', '7314261394', 'M.B.B.S'),
(105, 'Dr.M.R.Tiwari', '861321562', 'General Practitioner'),
(106, 'Dr.Kavita B.', '7956266192', 'Dentist'),
(107, 'Dr.Kailash K.', '814657946', 'General Surgeon');

-- --------------------------------------------------------

--
-- Table structure for table `inpat_table`
--

CREATE TABLE `inpat_table` (
  `In_Id` varchar(10) NOT NULL,
  `P_Id` varchar(10) DEFAULT NULL,
  `Room_No` varchar(10) NOT NULL,
  `Date_of_Admis yyyy-mm-dd` varchar(30) NOT NULL,
  `Date_of_Disc yyyy-mm-dd` varchar(30) NOT NULL,
  `Lab_No` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `inpat_table`
--

INSERT INTO `inpat_table` (`In_Id`, `P_Id`, `Room_No`, `Date_of_Admis yyyy-mm-dd`, `Date_of_Disc yyyy-mm-dd`, `Lab_No`) VALUES
('101', '1004', '201', '2021/12/31', '2022/1/2', '10006'),
('102', '1009', '203', '2022/1/11', '2022/2/21', '10010'),
('103', '1010', '202', '2022/1/2', '2022/3/3', '10007');

-- --------------------------------------------------------

--
-- Table structure for table `lab_table`
--

CREATE TABLE `lab_table` (
  `Lab_No` varchar(10) NOT NULL,
  `P_Id` varchar(10) NOT NULL,
  `Weight` int(11) NOT NULL,
  `Doc_Id` int(11) DEFAULT NULL,
  `Date` varchar(20) NOT NULL,
  `Category` varchar(20) NOT NULL,
  `Amount` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `lab_table`
--

INSERT INTO `lab_table` (`Lab_No`, `P_Id`, `Weight`, `Doc_Id`, `Date`, `Category`, `Amount`) VALUES
('10001', '1001', 90, 101, '2021/12/21', 'Thyorid Report', 1200),
('10002', '1003', 65, 103, '2021/12/22', 'Eye Report', 200),
('10003', '1006', 77, 105, '2021/12/27', 'Teeth Report', 900),
('10004', '1002', 75, 102, '2021/12/30', 'Fungal Infection Rep', 1900),
('10005', '1005', 72, 104, '2021/12/30', 'Full Body Check', 1100),
('10006', '1004', 88, 104, '2021/12/31', 'Bone X-Ray', 900),
('10007', '1010', 85, 107, '2022/1/2', 'Full Heart Scan', 3900),
('10008', '1008', 86, 106, '2022/1/4', 'Upper Jaw Scan', 800),
('10009', '1007', 82, 106, '2022/1/7', 'Full Tooth Scan', 1200),
('10010', '1009', 76, 107, '2022/1/11', 'Full Liver Scan', 3700);

-- --------------------------------------------------------

--
-- Table structure for table `outpat_table`
--

CREATE TABLE `outpat_table` (
  `Out_Id` varchar(10) NOT NULL,
  `P_Id` varchar(10) DEFAULT NULL,
  `Date yyyy-mm-dd` varchar(20) NOT NULL,
  `Lab_No` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `outpat_table`
--

INSERT INTO `outpat_table` (`Out_Id`, `P_Id`, `Date yyyy-mm-dd`, `Lab_No`) VALUES
('101', '1001', '2021/12/21', '10001'),
('102', '1003', '2021/12/23', '10002'),
('103', '1006', '2021/12/27', '10003'),
('104', '1002', '2021/12/30', '10004'),
('105', '1005', '2021/12/30', '10005'),
('106', '1008', '2021/1/4', '10008'),
('107', '1007', '2021/1/7', '10009');

-- --------------------------------------------------------

--
-- Table structure for table `pt_table`
--

CREATE TABLE `pt_table` (
  `P_Id` varchar(5) NOT NULL,
  `Name` varchar(20) NOT NULL,
  `Age` int(11) NOT NULL,
  `Weight` int(11) NOT NULL,
  `Gender` varchar(10) NOT NULL,
  `Address` varchar(30) NOT NULL,
  `Phone_No` varchar(20) NOT NULL,
  `Disease` varchar(30) NOT NULL,
  `Doctor_Id` varchar(10) NOT NULL
) ;

--
-- Dumping data for table `pt_table`
--

INSERT INTO `pt_table` (`P_Id`, `Name`, `Age`, `Weight`, `Gender`, `Address`, `Phone_No`, `Disease`, `Doctor_Id`) VALUES
('1001', 'Savita', 45, 90, 'F', 'Badlapur', '956146255', 'Thyroid', '101'),
('1002', 'Swati', 22, 75, 'F', 'Badlapur', '95951255', 'Fungal', '102'),
('1003', 'Rahul', 25, 65, 'M', 'Thane', '8215951255', 'Eye Check', '103'),
('1004', 'Mahesh S', 55, 88, 'M', 'Mumbai', '851221962', 'Bone Crack', '104'),
('1005', 'Anjali', 30, 72, 'F', 'Andheri', '95564235', 'Fever', '104'),
('1006', 'Suresh', 32, 77, 'M', 'Thane', '832512511', 'Common Flu', '105'),
('1007', 'Prasad', 28, 82, 'M', 'Kalyan', '9123475622', 'Teeth Replace', '106'),
('1008', 'Sneha', 33, 86, 'F', 'Borivali', '96214562', 'Root Cannel', '106'),
('1009', 'Vijay', 65, 76, 'F', 'Colaba', '784623145', 'Lever Operation', '107'),
('1010', 'Sahil', 79, 85, 'M', 'Mumbra', '796545123', 'Heart Operation', '107');

-- --------------------------------------------------------

--
-- Table structure for table `room_table`
--

CREATE TABLE `room_table` (
  `R_No` varchar(10) NOT NULL,
  `R_type` varchar(30) NOT NULL,
  `R_Status` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `room_table`
--

INSERT INTO `room_table` (`R_No`, `R_type`, `R_Status`) VALUES
('201', 'Genereal Ward', '6/10'),
('202', 'Private Room', 'Occupied'),
('203', 'Private Room', 'Occupied'),
('204', 'Private Room', 'Idle'),
('205', 'Premium Room', 'Idle'),
('206', 'General Ward', '0/12');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `bill_table`
--
ALTER TABLE `bill_table`
  ADD PRIMARY KEY (`Bill_No`),
  ADD KEY `P_ID` (`P_ID`);

--
-- Indexes for table `dr_table`
--
ALTER TABLE `dr_table`
  ADD PRIMARY KEY (`Dr_Id`);

--
-- Indexes for table `inpat_table`
--
ALTER TABLE `inpat_table`
  ADD PRIMARY KEY (`In_Id`),
  ADD KEY `Lab_No` (`Lab_No`),
  ADD KEY `P_Id` (`P_Id`);

--
-- Indexes for table `lab_table`
--
ALTER TABLE `lab_table`
  ADD PRIMARY KEY (`Lab_No`),
  ADD KEY `Doc_Id` (`Doc_Id`);

--
-- Indexes for table `outpat_table`
--
ALTER TABLE `outpat_table`
  ADD PRIMARY KEY (`Out_Id`),
  ADD KEY `Lab_No` (`Lab_No`),
  ADD KEY `P_Id` (`P_Id`);

--
-- Indexes for table `pt_table`
--
ALTER TABLE `pt_table`
  ADD PRIMARY KEY (`P_Id`);

--
-- Indexes for table `room_table`
--
ALTER TABLE `room_table`
  ADD PRIMARY KEY (`R_No`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `bill_table`
--
ALTER TABLE `bill_table`
  ADD CONSTRAINT `bill_table_ibfk_1` FOREIGN KEY (`P_ID`) REFERENCES `pt_table` (`P_Id`);

--
-- Constraints for table `inpat_table`
--
ALTER TABLE `inpat_table`
  ADD CONSTRAINT `inpat_table_ibfk_1` FOREIGN KEY (`Lab_No`) REFERENCES `lab_table` (`Lab_No`),
  ADD CONSTRAINT `inpat_table_ibfk_2` FOREIGN KEY (`P_Id`) REFERENCES `pt_table` (`P_Id`);

--
-- Constraints for table `lab_table`
--
ALTER TABLE `lab_table`
  ADD CONSTRAINT `lab_table_ibfk_1` FOREIGN KEY (`Doc_Id`) REFERENCES `dr_table` (`Dr_Id`);

--
-- Constraints for table `outpat_table`
--
ALTER TABLE `outpat_table`
  ADD CONSTRAINT `outpat_table_ibfk_1` FOREIGN KEY (`Lab_No`) REFERENCES `lab_table` (`Lab_No`),
  ADD CONSTRAINT `outpat_table_ibfk_2` FOREIGN KEY (`P_Id`) REFERENCES `pt_table` (`P_Id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
