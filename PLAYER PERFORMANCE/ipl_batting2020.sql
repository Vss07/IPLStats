-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: localhost    Database: ipl
-- ------------------------------------------------------
-- Server version	8.0.27

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `batting2020`
--

DROP TABLE IF EXISTS `batting2020`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `batting2020` (
  `POS` text,
  `Player` text,
  `Team` varchar(30) DEFAULT NULL,
  `Matches` bigint DEFAULT NULL,
  `Innings` bigint DEFAULT NULL,
  `NotOut` bigint DEFAULT NULL,
  `Runs` bigint DEFAULT NULL,
  `BallsFaced` bigint DEFAULT NULL,
  `Centuries` bigint DEFAULT NULL,
  `Fifties` bigint DEFAULT NULL,
  `StrikeRate` bigint DEFAULT NULL,
  `Average` decimal(5,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `batting2020`
--

LOCK TABLES `batting2020` WRITE;
/*!40000 ALTER TABLE `batting2020` DISABLE KEYS */;
INSERT INTO `batting2020` VALUES ('1','KL Rahul','Kings XI Punjab',14,14,2,670,518,1,5,129,55.83),('2','Shikhar Dhawan','Delhi Capitals',17,17,3,618,427,2,4,145,44.14),('3','David Warner','Sunrisers Hyderabad',16,16,2,548,407,0,4,135,39.14),('4','Shreyas Iyer','Delhi Capitals',17,17,2,519,421,0,3,123,34.60),('5','Ishan Kishan','Mumbai Indians',14,13,4,516,354,0,4,146,57.33),('6','Quinton de Kock','Mumbai Indians',16,16,2,503,358,0,4,140,35.93),('7','Suryakumar Yadav','Mumbai Indians',16,15,3,480,331,0,4,145,40.00),('8','Devdutt Padikkal','Royal Challengers Bangalore',15,15,0,473,379,0,5,125,31.53),('9','Virat Kohli','Royal Challengers Bangalore',15,15,4,466,384,0,3,121,42.36),('10','AB de Villiers','Royal Challengers Bangalore',15,14,4,454,286,0,5,159,45.40),('11','Faf du Plessis','Chennai Super Kings',13,13,2,449,319,0,4,141,40.82),('12','Shubman Gill','Kolkata Knight Riders',14,14,1,440,373,0,3,118,33.85),('13','Manish Pandey','Sunrisers Hyderabad',16,15,2,425,333,0,3,128,32.69),('14','Mayank Agarwal','Kings XI Punjab',11,11,0,424,271,1,2,156,38.55),('15','Eoin Morgan','Kolkata Knight Riders',14,14,4,418,302,0,1,138,41.80),('16','Sanju Samson','Rajasthan Royals',14,14,1,375,236,0,3,159,28.85),('17','Ambati Rayudu','Chennai Super Kings',12,11,2,359,282,0,1,127,39.89),('18','Nicholas Pooran','Kings XI Punjab',14,14,4,353,208,0,2,170,35.30),('19','Nitish Rana','Kolkata Knight Riders',14,14,0,352,254,0,3,139,25.14),('20','Marcus Stoinis','Delhi Capitals',17,17,3,352,237,0,3,149,25.14),('21','Jonny Bairstow','Sunrisers Hyderabad',11,11,0,345,272,0,3,127,31.36),('22','Rishabh Pant','Delhi Capitals',14,14,3,343,301,0,1,114,31.18),('23','Rohit Sharma','Mumbai Indians',12,12,0,332,260,0,3,128,27.67),('24','Jos Buttler','Rajasthan Royals',13,12,2,328,227,0,2,144,32.80),('25','Kane Williamson','Sunrisers Hyderabad',12,11,4,317,237,0,3,134,45.29),('26','Steve Smith','Rajasthan Royals',14,14,2,311,237,0,3,131,25.92),('27','Shane Watson','Chennai Super Kings',11,11,1,299,247,0,2,121,29.90),('28','Chris Gayle','Kings XI Punjab',7,7,0,288,210,0,3,137,41.14),('29','Ben Stokes','Rajasthan Royals',8,8,1,285,200,1,1,142,40.71),('30','Hardik Pandya','Mumbai Indians',14,13,5,281,157,0,1,179,35.13),('31','Aaron Finch','Royal Challengers Bangalore',12,12,0,268,241,0,1,111,22.33),('32','Kieron Pollard','Mumbai Indians',16,12,7,268,140,0,1,191,53.60),('33','Rahul Tewatia','Rajasthan Royals',14,11,5,255,183,0,1,139,42.50),('34','Ravindra Jadeja','Chennai Super Kings',14,11,6,232,135,0,1,172,46.40),('35','Rahul Tripathi','Kolkata Knight Riders',11,11,1,230,181,0,1,127,23.00),('36','Prithvi Shaw','Delhi Capitals',13,13,0,228,167,0,2,137,17.54),('37','Wriddhiman Saha','Sunrisers Hyderabad',4,4,1,214,153,0,2,140,71.33),('38','Ruturaj Gaikwad','Chennai Super Kings',6,6,2,204,169,0,3,121,51.00),('39','MS Dhoni','Chennai Super Kings',14,12,4,200,172,0,0,116,25.00),('40','Robin Uthappa','Rajasthan Royals',12,12,0,196,164,0,0,120,16.33),('41','Sam Curran','Chennai Super Kings',14,11,3,186,141,0,1,132,23.25),('42','Shimron Hetmyer','Delhi Capitals',12,11,3,185,125,0,0,148,23.13),('43','Dinesh Karthik','Kolkata Knight Riders',14,14,2,169,134,0,1,126,14.08),('44','Pat Cummins','Kolkata Knight Riders',14,11,4,146,114,0,1,128,20.86),('45','Priyam Garg','Sunrisers Hyderabad',14,10,1,133,111,0,1,120,14.78),('46','Mandeep Singh','Kings XI Punjab',7,7,1,130,109,0,1,119,21.67),('47','Shivam Dube','Royal Challengers Bangalore',11,9,2,129,105,0,0,123,18.43),('48','Sunil Narine','Kolkata Knight Riders',10,9,0,121,85,0,1,142,13.44),('49','Andre Russell','Kolkata Knight Riders',10,9,0,117,81,0,0,144,13.00),('50','Axar Patel','Delhi Capitals',15,9,1,117,85,0,0,138,14.63),('51','Ajinkya Rahane','Delhi Capitals',9,8,0,113,107,0,1,106,14.13),('52','Jofra Archer','Rajasthan Royals',14,10,4,113,63,0,0,179,18.83),('53','Abdul Samad','Sunrisers Hyderabad',12,8,3,111,65,0,0,171,22.20),('54','Washington Sundar','Royal Challengers Bangalore',15,9,3,111,95,0,0,117,18.50),('55','Krunal Pandya','Mumbai Indians',16,12,6,109,92,0,0,118,18.17),('56','Glenn Maxwell','Kings XI Punjab',13,11,4,108,106,0,0,102,15.43),('57','Saurabh Tiwary','Mumbai Indians',7,5,0,103,80,0,0,129,20.60),('58','Deepak Hooda','Kings XI Punjab',7,5,4,101,71,0,1,142,101.00),('59','Vijay Shankar','Sunrisers Hyderabad',7,5,1,97,96,0,1,101,24.25),('60','Riyan Parag','Rajasthan Royals',12,8,1,86,77,0,0,112,12.29),('61','Tom Curran','Rajasthan Royals',5,4,3,83,62,0,1,134,83.00),('62','Josh Philippe','Royal Challengers Bangalore',5,5,1,78,77,0,0,101,19.50),('63','Abhishek Sharma','Sunrisers Hyderabad',8,7,2,71,56,0,0,127,14.20),('64','Gurkeerat Mann Singh','Royal Challengers Bangalore',8,5,5,71,80,0,0,89,0.00),('65','Jason Holder','Sunrisers Hyderabad',7,4,2,66,53,0,0,125,33.00),('66','Kedar Jadhav','Chennai Super Kings',8,5,2,62,66,0,0,94,20.67),('67','Mahipal Lomror','Rajasthan Royals',3,3,0,59,54,0,0,109,19.67),('68','Kagiso Rabada','Delhi Capitals',17,8,4,56,49,0,0,114,14.00),('69','Lockie Ferguson','Kolkata Knight Riders',5,2,2,43,29,0,0,148,0.00),('70','Krishnappa Gowtham','Kings XI Punjab',2,2,1,42,27,0,0,156,42.00),('71','Yashasvi Jaiswal','Rajasthan Royals',3,3,0,40,44,0,0,91,13.33),('72','Shreyas Gopal','Rajasthan Royals',14,5,1,37,39,0,0,95,9.25),('73','Ravichandran Ashwin','Delhi Capitals',15,6,3,37,34,0,0,109,12.33),('74','Rashid Khan','Sunrisers Hyderabad',16,7,3,35,30,0,0,117,8.75),('75','Chris Morris','Royal Challengers Bangalore',9,5,1,34,21,0,0,162,8.50),('76','Narayan Jagadeesan','Chennai Super Kings',5,2,0,33,29,0,0,114,16.50),('77','Sarfaraz Khan','Kings XI Punjab',5,3,1,33,29,0,0,114,16.50),('78','Alex Carey','Delhi Capitals',3,3,1,32,29,0,0,110,16.00),('79','Murali Vijay','Chennai Super Kings',3,3,0,32,43,0,0,74,10.67),('80','Chris Jordan','Kings XI Punjab',9,5,2,29,31,0,0,94,9.67),('81','Navdeep Saini','Royal Challengers Bangalore',13,3,2,27,27,0,0,100,27.00),('82','Nathan Coulter-Nile','Mumbai Indians',7,2,1,25,15,0,0,167,25.00),('83','Kamlesh Nagarkoti','Kolkata Knight Riders',10,6,3,22,31,0,0,71,7.33),('84','Harshal Patel','Delhi Capitals',5,2,0,21,24,0,0,88,10.50),('85','Tushar Deshpande','Delhi Capitals',5,2,1,21,12,0,0,175,21.00),('86','Jimmy Neesham','Kings XI Punjab',5,3,1,19,18,0,0,106,9.50),('87','Tom Banton','Kolkata Knight Riders',2,2,0,18,20,0,0,90,9.00),('88','Mohammed Siraj','Royal Challengers Bangalore',9,3,2,17,14,0,0,121,17.00),('89','Karun Nair','Kings XI Punjab',4,3,1,16,14,0,0,114,8.00),('90','Prabhsimran Singh','Kings XI Punjab',2,2,0,15,15,0,0,100,7.50),('91','Isuru Udana','Royal Challengers Bangalore',10,4,1,15,11,0,0,136,5.00),('92','James Pattinson','Mumbai Indians',10,2,1,15,13,0,0,115,15.00),('93','Imran Tahir','Chennai Super Kings',3,1,1,13,10,0,0,130,0.00),('94','Kuldeep Yadav','Kolkata Knight Riders',5,2,1,13,21,0,0,62,13.00),('95','Moeen Ali','Royal Challengers Bangalore',3,3,0,12,16,0,0,75,4.00),('96','Shardul Thakur','Chennai Super Kings',9,2,1,12,21,0,0,57,12.00),('97','Sandeep Sharma','Sunrisers Hyderabad',13,5,3,12,15,0,0,80,6.00),('98','Mohammad Nabi','Sunrisers Hyderabad',1,1,1,11,8,0,0,138,0.00),('99','Rinku Singh','Kolkata Knight Riders',1,1,0,11,11,0,0,100,11.00),('100','Shivam Mavi','Kolkata Knight Riders',8,3,1,10,14,0,0,71,5.00),('101','Varun Chakaravarthy','Kolkata Knight Riders',13,3,1,10,15,0,0,67,5.00),('102','Ankit Rajpoot','Rajasthan Royals',6,2,1,9,10,0,0,90,9.00),('103','Jaydev Unadkat','Rajasthan Royals',7,1,0,9,13,0,0,69,9.00),('104','Pravin Dubey','Delhi Capitals',3,1,1,7,13,0,0,54,0.00),('105','Dwayne Bravo','Chennai Super Kings',6,2,0,7,6,0,0,117,3.50),('106','Shahbaz Nadeem','Sunrisers Hyderabad',7,2,1,7,8,0,0,88,7.00),('107','Deepak Chahar','Chennai Super Kings',14,3,2,7,12,0,0,58,7.00),('108','Ravi Bishnoi','Kings XI Punjab',14,3,2,7,12,0,0,58,7.00),('109','Anrich Nortje','Delhi Capitals',16,5,4,7,6,0,0,117,7.00),('110','Andrew Tye','Rajasthan Royals',1,1,0,6,6,0,0,100,6.00),('111','Jasprit Bumrah','Mumbai Indians',15,1,1,5,3,0,0,167,0.00),('112','Murugan Ashwin','Kings XI Punjab',9,1,0,4,4,0,0,100,4.00),('113','Kartik Tyagi','Rajasthan Royals',10,3,2,4,6,0,0,67,4.00),('114','Dhawal Kulkarni','Mumbai Indians',1,1,1,3,2,0,0,150,0.00),('115','T Natarajan','Sunrisers Hyderabad',16,3,3,3,5,0,0,60,0.00),('116','Prasidh Krishna','Kolkata Knight Riders',6,2,2,2,4,0,0,50,0.00),('117','Mohammad Shami','Kings XI Punjab',14,3,2,2,3,0,0,67,2.00),('118','Rahul Chahar','Mumbai Indians',15,1,1,2,4,0,0,50,0.00),('119','Nikhil Naik','Kolkata Knight Riders',1,1,0,1,3,0,0,33,1.00),('120','Mujeeb Ur Rahman','Kings XI Punjab',2,1,0,1,3,0,0,33,1.00),('121','Shahbaz Ahmed','Royal Challengers Bangalore',2,1,1,1,1,0,0,100,0.00),('122','Dale Steyn','Royal Challengers Bangalore',3,1,1,1,2,0,0,50,0.00),('123','Varun Aaron','Rajasthan Royals',3,2,1,1,10,0,0,10,1.00),('124','Yuzvendra Chahal','Royal Challengers Bangalore',15,2,1,1,3,0,0,33,1.00),('125','Mitchell Marsh','Sunrisers Hyderabad',1,1,0,0,1,0,0,0,0.00),('126','Shreevats Goswami','Sunrisers Hyderabad',2,2,0,0,4,0,0,0,0.00),('127','Umesh Yadav','Royal Challengers Bangalore',2,1,0,0,2,0,0,0,0.00),('128','Daniel Sams','Delhi Capitals',3,1,0,0,2,0,0,0,0.00),('129','Bhuvneshwar Kumar','Sunrisers Hyderabad',4,1,0,0,2,0,0,0,0.00),('130','Sheldon Cottrell','Kings XI Punjab',6,1,0,0,2,0,0,0,0.00),('131','Khaleel Ahmed','Sunrisers Hyderabad',7,1,0,0,2,0,0,0,0.00),('132','Arshdeep Singh','Kings XI Punjab',8,1,0,0,3,0,0,0,0.00),('133','Trent Boult','Mumbai Indians',15,1,0,0,1,0,0,0,0.00);
/*!40000 ALTER TABLE `batting2020` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-07-17 20:26:47
