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
-- Table structure for table `auction2021`
--

DROP TABLE IF EXISTS `auction2021`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auction2021` (
  `Player` varchar(30) DEFAULT NULL,
  `Team` varchar(30) DEFAULT NULL,
  `Type` varchar(15) DEFAULT NULL,
  `Price` varchar(15) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auction2021`
--

LOCK TABLES `auction2021` WRITE;
/*!40000 ALTER TABLE `auction2021` DISABLE KEYS */;
INSERT INTO `auction2021` VALUES ('Krishnappa Gowtham','Chennai Super Kings','All-Rounder','Rs 9,25,00,000'),('Moeen Ali','Chennai Super Kings','All-Rounder','Rs 7,00,00,000'),('Cheteshwar Pujara','Chennai Super Kings','Batsman','Rs 50,00,000'),('K.Bhagath Varma','Chennai Super Kings','All-Rounder','Rs 20,00,000'),('C Hari Nishaanth','Chennai Super Kings','Batsman','Rs 20,00,000'),('M. Harisankar Reddy','Chennai Super Kings','Bowler','Rs 20,00,000'),('Nathan Coulter-Nile','Mumbai Indians','Bowler','Rs 5,00,00,000'),('Adam Milne','Mumbai Indians','Bowler','Rs 3,20,00,000'),('Piyush Chawla','Mumbai Indians','Bowler','Rs 2,40,00,000'),('James Neesham','Mumbai Indians','All-Rounder','Rs 50,00,000'),('Yudhvir Charak','Mumbai Indians','All-Rounder','Rs 20,00,000'),('Marco Jansen','Mumbai Indians','All-Rounder','Rs 20,00,000'),('Tom Curran','Delhi Capitals','All-Rounder','Rs 5,25,00,000'),('Steven Smith','Delhi Capitals','Batsman','Rs 2,20,00,000'),('Sam Billings','Delhi Capitals','Wicket Keeper','Rs 2,00,00,000'),('Umesh Yadav','Delhi Capitals','Bowler','Rs 1,00,00,000'),('Ripal Patel','Delhi Capitals','All-Rounder','Rs 20,00,000'),('Vishnu Vinod','Delhi Capitals','Wicket Keeper','Rs 20,00,000'),('Lukman Hussain Meriwala','Delhi Capitals','Bowler','Rs 20,00,000'),('M Siddharth','Delhi Capitals','Bowler','Rs 20,00,000'),('Shakib Al Hasan','Kolkata Knight Riders','All-Rounder','Rs 3,20,00,000'),('Harbhajan Singh','Kolkata Knight Riders','Bowler','Rs 2,00,00,000'),('Ben Cutting','Kolkata Knight Riders','All-Rounder','Rs 75,00,000'),('Karun Nair','Kolkata Knight Riders','Batsman','Rs 50,00,000'),('Pawan Negi','Kolkata Knight Riders','All-Rounder','Rs 50,00,000'),('Venkatesh Iyer','Kolkata Knight Riders','All-Rounder','Rs 20,00,000'),('Sheldon Jackson','Kolkata Knight Riders','Wicket Keeper','Rs 20,00,000'),('Vaibhav Arora','Kolkata Knight Riders','Bowler','Rs 20,00,000'),('Arjun Tendulkar','Mumbai Indians','All-Rounder','Rs 20,00,000'),('Jhye Richardson','Punjab Kings','Bowler','Rs 14,00,00,000'),('Riley Meredith','Punjab Kings','Bowler','Rs 8,00,00,000'),('Shahrukh Khan','Punjab Kings','All-Rounder','Rs 5,25,00,000'),('Moises Henriques','Punjab Kings','All-Rounder','Rs 4,20,00,000'),('Dawid Malan','Punjab Kings','All-Rounder','Rs 1,50,00,000'),('Fabian Allen','Punjab Kings','All-Rounder','Rs 75,00,000'),('Jalaj Saxena','Punjab Kings','All-Rounder','Rs 30,00,000'),('Saurabh Kumar','Punjab Kings','All-Rounder','Rs 20,00,000'),('Utkarsh Singh','Punjab Kings','All-Rounder','Rs 20,00,000'),('Christopher Morris','Rajasthan Royals','All-Rounder','Rs 16,25,00,000'),('Shivam Dube','Rajasthan Royals','All-Rounder','Rs 4,40,00,000'),('Chetan Sakariya','Rajasthan Royals','Bowler','Rs 1,20,00,000'),('Mustafizur Rahman','Rajasthan Royals','Bowler','Rs 1,00,00,000'),('Liam Livingstone','Rajasthan Royals','All-Rounder','Rs 75,00,000'),('K.C Cariappa','Rajasthan Royals','Bowler','Rs 20,00,000'),('Akash Singh','Rajasthan Royals','Bowler','Rs 20,00,000'),('Kuldip Yadav','Rajasthan Royals','Bowler','Rs 20,00,000'),('Kyle Jamieson','Royal Challengers Bangalore','All-Rounder','Rs 15,00,00,000'),('Glenn Maxwell','Royal Challengers Bangalore','All-Rounder','Rs 14,25,00,000'),('Dan Christian','Royal Challengers Bangalore','All-Rounder','Rs 4,80,00,000'),('Sachin Baby','Royal Challengers Bangalore','Batsman','Rs 20,00,000'),('Rajat Patidar','Royal Challengers Bangalore','Batsman','Rs 20,00,000'),('Mohammed Azharudeen','Royal Challengers Bangalore','Wicket Keeper','Rs 20,00,000'),('Suyash Prabhudesai','Royal Challengers Bangalore','All-Rounder','Rs 20,00,000'),('Kona Srikar Bharat','Royal Challengers Bangalore','Wicket Keeper','Rs 20,00,000'),('Kedar Jadhav','Sunrises Hyderabad ','All-Rounder','Rs 2,00,00,000'),('Mujeeb Zadran','Sunrises Hyderabad ','Bowler','Rs 1,50,00,000'),('J Suchith','Sunrises Hyderabad ','Bowler','Rs 30,00,000');
/*!40000 ALTER TABLE `auction2021` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-07-17 20:26:46
