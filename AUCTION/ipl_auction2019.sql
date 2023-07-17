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
-- Table structure for table `auction2019`
--

DROP TABLE IF EXISTS `auction2019`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auction2019` (
  `Player` varchar(30) DEFAULT NULL,
  `Team` varchar(30) DEFAULT NULL,
  `Type` varchar(15) DEFAULT NULL,
  `Price` varchar(15) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auction2019`
--

LOCK TABLES `auction2019` WRITE;
/*!40000 ALTER TABLE `auction2019` DISABLE KEYS */;
INSERT INTO `auction2019` VALUES ('Mohit Sharma','Chennai Super Kings','Bowler','Rs 5,00,00,000'),('Ruturaj Gaikwad','Chennai Super Kings','Batsman','Rs 20,00,000'),('Colin Ingram','Delhi Capitals','Batsman','Rs 6,40,00,000'),('Axar Rajesh Patel','Delhi Capitals','All-Rounder','Rs 5,00,00,000'),('Hanuma Vihari','Delhi Capitals','Batsman','Rs 2,00,00,000'),('Sherfane Rutherford','Delhi Capitals','All-Rounder','Rs 2,00,00,000'),('Ishant Sharma','Delhi Capitals','Bowler','Rs 1,10,00,000'),('Keemo Paul','Delhi Capitals','All-Rounder','Rs 50,00,000'),('Jalaj Saxena','Delhi Capitals','All-Rounder','Rs 20,00,000'),('Ankush Bains','Delhi Capitals','Wicket Keeper','Rs 20,00,000'),('Nathu Singh','Delhi Capitals','Bowler','Rs 20,00,000'),('Bandaru Ayyappa','Delhi Capitals','Bowler','Rs 20,00,000'),('Varun Chakaravarthy','Kings XI Punjab','All-Rounder','Rs 8,40,00,000'),('Sam Curran','Kings XI Punjab','All-Rounder','Rs 7,20,00,000'),('Mohammad Shami','Kings XI Punjab','Bowler','Rs 4,80,00,000'),('Prabhsimran Singh','Kings XI Punjab','Wicket Keeper','Rs 4,80,00,000'),('Nicolas Pooran','Kings XI Punjab','Wicket Keeper','Rs 4,20,00,000'),('Moises Henriques','Kings XI Punjab','All-Rounder','Rs 1,00,00,000'),('Hardus Viljoen','Kings XI Punjab','Bowler','Rs 75,00,000'),('Darshan Nalkande','Kings XI Punjab','All-Rounder','Rs 30,00,000'),('Sarfaraz Naushad Khan','Kings XI Punjab','All-Rounder','Rs 25,00,000'),('Arshdeep Singh','Kings XI Punjab','Bowler','Rs 20,00,000'),('Agnivesh Ayachi','Kings XI Punjab','All-Rounder','Rs 20,00,000'),('Harpreet Brar','Kings XI Punjab','All-Rounder','Rs 20,00,000'),('M. Ashwin','Kings XI Punjab','Bowler','Rs 20,00,000'),('Carlos Brathwaite','Kolkata Knight Riders','All-Rounder','Rs 5,00,00,000'),('Lockie Ferguson','Kolkata Knight Riders','Bowler','Rs 1,60,00,000'),('Joe Denly','Kolkata Knight Riders','Batsman','Rs 1,00,00,000'),('Harry Gurney','Kolkata Knight Riders','Bowler','Rs 75,00,000'),('Nikhil Shankar Naik','Kolkata Knight Riders','Wicket Keeper','Rs 20,00,000'),('Shrikant Mundhe','Kolkata Knight Riders','All-Rounder','Rs 20,00,000'),('Prithvi Raj Yarra','Kolkata Knight Riders','Bowler','Rs 20,00,000'),('Anrich Nortje','Kolkata Knight Riders','Bowler','Rs 20,00,000'),('Barinder Singh Sran','Mumbai Indians','Bowler','Rs 3,40,00,000'),('Lasith Malinga','Mumbai Indians','Bowler','Rs 2,00,00,000'),('Yuvraj Singh','Mumbai Indians','All-Rounder','Rs 1,00,00,000'),('Anmolpreet Singh','Mumbai Indians','Batsman','Rs 80,00,000'),('Pankaj Jaswal','Mumbai Indians','All-Rounder','Rs 20,00,000'),('Rasikh Dar','Mumbai Indians','Bowler','Rs 20,00,000'),('Jaydev Unadkat','Rajasthan Royals','Bowler','Rs 8,40,00,000'),('Varun Aaron','Rajasthan Royals','Bowler','Rs 2,40,00,000'),('Oshane Thomas','Rajasthan Royals','Bowler','Rs 1,10,00,000'),('Ashton Turner','Rajasthan Royals','All-Rounder','Rs 50,00,000'),('Liam Livingstone','Rajasthan Royals','All-Rounder','Rs 50,00,000'),('Shashank Singh','Rajasthan Royals','All-Rounder','Rs 30,00,000'),('Riyan Parag','Rajasthan Royals','All-Rounder','Rs 20,00,000'),('Manan Vohra','Rajasthan Royals','Batsman','Rs 20,00,000'),('Shubham Ranjane','Rajasthan Royals','All-Rounder','Rs 20,00,000'),('Shivam Dube','Royal Challengers Bangalore','All-Rounder','Rs 5,00,00,000'),('Shimron Hetmyer','Royal Challengers Bangalore','Batsman','Rs 4,20,00,000'),('Akshdeep Nath','Royal Challengers Bangalore','All-Rounder','Rs 3,60,00,000'),('Prayas Ray Barman','Royal Challengers Bangalore','All-Rounder','Rs 1,50,00,000'),('Himmat Singh','Royal Challengers Bangalore','Batsman','Rs 65,00,000'),('Gurkeerat Singh Mann','Royal Challengers Bangalore','All-Rounder','Rs 50,00,000'),('Heinrich Klaasen','Royal Challengers Bangalore','Wicket Keeper','Rs 50,00,000'),('Devdutt Padikkal','Royal Challengers Bangalore','Batsman','Rs 20,00,000'),('Milind Kumar','Royal Challengers Bangalore','All-Rounder','Rs 20,00,000'),('Jonny Bairstow','Sunrisers Hyderabad','Wicket Keeper','Rs 2,20,00,000'),('Wriddhiman Saha','Sunrisers Hyderabad','Wicket Keeper','Rs 1,20,00,000'),('Martin Guptill','Sunrisers Hyderabad','Batsman','Rs 1,00,00,000');
/*!40000 ALTER TABLE `auction2019` ENABLE KEYS */;
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
