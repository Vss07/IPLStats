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
-- Table structure for table `auction2020`
--

DROP TABLE IF EXISTS `auction2020`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auction2020` (
  `Player` varchar(30) DEFAULT NULL,
  `Team` varchar(30) DEFAULT NULL,
  `Type` varchar(15) DEFAULT NULL,
  `Price` varchar(15) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auction2020`
--

LOCK TABLES `auction2020` WRITE;
/*!40000 ALTER TABLE `auction2020` DISABLE KEYS */;
INSERT INTO `auction2020` VALUES ('Piyush Chawla','Chennai Super Kings','Bowler','Rs 6,75,00,000'),('Sam Curran','Chennai Super Kings','All-Rounder','Rs 5,50,00,000'),('Josh Hazlewood','Chennai Super Kings','Bowler','Rs 2,00,00,000'),('R. Sai Kishore','Chennai Super Kings','Bowler','Rs 20,00,000'),('Shimron Hetmyer','Delhi Capitals','Batsman','Rs 7,75,00,000'),('Marcus Stoinis','Delhi Capitals','All-Rounder','Rs 4,80,00,000'),('Alex Carey','Delhi Capitals','Wicket Keeper','Rs 2,40,00,000'),('Jason Roy','Delhi Capitals','Batsman','Rs 1,50,00,000'),('Chris Woakes','Delhi Capitals','All-Rounder','Rs 1,50,00,000'),('Mohit Sharma','Delhi Capitals','Bowler','Rs 50,00,000'),('Tushar Deshpande','Delhi Capitals','Bowler','Rs 20,00,000'),('Lalit Yadav','Delhi Capitals','All-Rounder','Rs 20,00,000'),('Glenn Maxwell','Kings XI Punjab','All-Rounder','Rs 10,75,00,000'),('Sheldon Cottrell','Kings XI Punjab','Bowler','Rs 8,50,00,000'),('Chris Jordan','Kings XI Punjab','All-Rounder','Rs 3,00,00,000'),('Ravi Bishnoi','Kings XI Punjab','Bowler','Rs 2,00,00,000'),('Prabhsimran Singh','Kings XI Punjab','Wicket Keeper','Rs 55,00,000'),('Deepak Hooda','Kings XI Punjab','All-Rounder','Rs 50,00,000'),('James Neesham','Kings XI Punjab','All-Rounder','Rs 50,00,000'),('Tajinder Dhillon','Kings XI Punjab','All-Rounder','Rs 20,00,000'),('Ishan Porel','Kings XI Punjab','Bowler','Rs 20,00,000'),('Pat Cummins','Kolkata Knight Riders','All-Rounder','Rs 15,50,00,000'),('Eoin Morgan','Kolkata Knight Riders','Batsman','Rs 5,25,00,000'),('Varun Chakaravarthy','Kolkata Knight Riders','All-Rounder','Rs 4,00,00,000'),('Tom Banton','Kolkata Knight Riders','Batsman','Rs 1,00,00,000'),('Rahul Tripathi','Kolkata Knight Riders','Batsman','Rs 60,00,000'),('Chris Green','Kolkata Knight Riders','All-Rounder','Rs 20,00,000'),('Nikhil Shankar Naik','Kolkata Knight Riders','Wicket Keeper','Rs 20,00,000'),('Pravin Tambe','Kolkata Knight Riders','Bowler','Rs 20,00,000'),('M Siddharth','Kolkata Knight Riders','Bowler','Rs 20,00,000'),('Nathan Coulter-Nile','Mumbai Indians','Bowler','Rs 8,00,00,000'),('Chris Lynn','Mumbai Indians','Batsman','Rs 2,00,00,000'),('Saurabh Tiwary','Mumbai Indians','Batsman','Rs 50,00,000'),('Digvijay Deshmukh','Mumbai Indians','All-Rounder','Rs 20,00,000'),('Prince Balwant Rai Singh','Mumbai Indians','All-Rounder','Rs 20,00,000'),('Mohsin Khan','Mumbai Indians','Bowler','Rs 20,00,000'),('Robin Uthappa','Rajasthan Royals','Batsman','Rs 3,00,00,000'),('Jaydev Unadkat','Rajasthan Royals','Bowler','Rs 3,00,00,000'),('Yashasvi Jaiswal','Rajasthan Royals','All-Rounder','Rs 2,40,00,000'),('Kartik Tyagi','Rajasthan Royals','Bowler','Rs 1,30,00,000'),('Tom Curran','Rajasthan Royals','All-Rounder','Rs 1,00,00,000'),('Andrew Tye','Rajasthan Royals','Bowler','Rs 1,00,00,000'),('Anuj Rawat','Rajasthan Royals','Wicket Keeper','Rs 80,00,000'),('David Miller','Rajasthan Royals','Batsman','Rs 75,00,000'),('Oshane Thomas','Rajasthan Royals','Bowler','Rs 50,00,000'),('Anirudha Ashok Joshi','Rajasthan Royals','All-Rounder','Rs 20,00,000'),('Akash Singh','Rajasthan Royals','Bowler','Rs 20,00,000'),('Christopher Morris','Royal Challengers Bangalore','All-Rounder','Rs 10,00,00,000'),('Aaron Finch','Royal Challengers Bangalore','Batsman','Rs 4,40,00,000'),('Kane Richardson','Royal Challengers Bangalore','Bowler','Rs 4,00,00,000'),('Dale Steyn','Royal Challengers Bangalore','Bowler','Rs 2,00,00,000'),('Isuru Udana','Royal Challengers Bangalore','All-Rounder','Rs 50,00,000'),('Shahbaz Ahamad','Royal Challengers Bangalore','Wicket Keeper','Rs 20,00,000'),('Joshua Philippe','Royal Challengers Bangalore','Wicket Keeper','Rs 20,00,000'),('Pavan Deshpande','Royal Challengers Bangalore','All-Rounder','Rs 20,00,000'),('Mitchell Marsh','Sunrisers Hyderabad','All-Rounder','Rs 2,00,00,000'),('Priyam Garg','Sunrisers Hyderabad','Batsman','Rs 1,90,00,000'),('Virat Singh','Sunrisers Hyderabad','Batsman','Rs 1,90,00,000'),('Fabian Allen','Sunrisers Hyderabad','All-Rounder','Rs 50,00,000'),('Sandeep Bavanaka','Sunrisers Hyderabad','All-Rounder','Rs 20,00,000'),('Sanjay Yadav','Sunrisers Hyderabad','All-Rounder','Rs 20,00,000'),('Abdul Samad','Sunrisers Hyderabad','All-Rounder','Rs 20,00,000');
/*!40000 ALTER TABLE `auction2020` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-07-17 20:26:45
