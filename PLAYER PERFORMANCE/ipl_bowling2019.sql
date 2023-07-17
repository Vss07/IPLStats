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
-- Table structure for table `bowling2019`
--

DROP TABLE IF EXISTS `bowling2019`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bowling2019` (
  `POS` int DEFAULT NULL,
  `Player` varchar(30) DEFAULT NULL,
  `Team` varchar(30) DEFAULT NULL,
  `Matches` int DEFAULT NULL,
  `Innings` int DEFAULT NULL,
  `Overs` decimal(4,1) DEFAULT NULL,
  `Runs` int DEFAULT NULL,
  `Wickets` int DEFAULT NULL,
  `Econ` decimal(4,2) DEFAULT NULL,
  `SR` decimal(5,2) DEFAULT NULL,
  `Average` decimal(5,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bowling2019`
--

LOCK TABLES `bowling2019` WRITE;
/*!40000 ALTER TABLE `bowling2019` DISABLE KEYS */;
INSERT INTO `bowling2019` VALUES (1,'Imran Tahir','Chennai Super Kings',17,17,64.2,431,26,6.72,14.84,16.58),(2,'Kagiso Rabada','Delhi Capitals',12,12,47.0,368,25,7.80,11.28,14.72),(3,'Deepak Chahar','Chennai Super Kings',17,17,64.3,482,22,7.50,17.59,21.91),(4,'Shreyas Gopal','Rajasthan Royals',14,14,48.0,347,20,7.20,14.40,17.35),(5,'Mohammad Shami','Kings XI Punjab',14,14,54.0,469,19,8.70,17.05,24.68),(6,'Khaleel Ahmed','Sunrisers Hyderabad',9,9,34.5,287,19,8.22,11.00,15.11),(7,'Jasprit Bumrah','Mumbai Indians',16,16,61.4,409,19,6.66,19.47,21.53),(8,'Yuzvendra Chahal','Royal Challengers Bangalore',14,14,49.2,386,18,7.80,16.44,21.44),(9,'Rashid Khan','Sunrisers Hyderabad',15,15,60.0,377,17,6.30,21.17,22.18),(10,'Lasith Malinga','Mumbai Indians',12,12,44.5,438,16,9.78,16.81,27.38),(11,'Harbhajan Singh','Chennai Super Kings',11,11,44.0,312,16,7.08,16.50,19.50),(12,'Ravichandran Ashwin','Kings XI Punjab',14,14,55.0,400,15,7.26,22.00,26.67),(13,'Ravindra Jadeja','Chennai Super Kings',16,16,54.0,343,15,6.36,21.60,22.87),(14,'Hardik Pandya','Mumbai Indians',16,16,42.3,390,14,9.18,18.21,27.86),(15,'Chris Morris','Delhi Capitals',9,9,33.0,306,13,9.30,15.23,23.54),(16,'Rahul Chahar','Mumbai Indians',13,13,47.0,308,13,6.54,21.69,23.69),(17,'Ishant Sharma','Delhi Capitals',13,13,46.0,349,13,7.56,21.23,26.85),(18,'Bhuvneshwar Kumar','Sunrisers Hyderabad',15,15,59.0,461,13,7.80,27.23,35.46),(19,'Krunal Pandya','Mumbai Indians',16,16,46.0,335,12,7.26,23.00,27.92),(20,'Sandeep Sharma','Sunrisers Hyderabad',11,11,42.4,352,12,8.28,21.33,29.33),(21,'Dwayne Bravo','Chennai Super Kings',12,12,41.1,330,11,8.04,22.45,30.00),(22,'Amit Mishra','Delhi Capitals',11,11,40.0,270,11,6.78,21.81,24.55),(23,'Andre Russell','Kolkata Knight Riders',14,12,30.1,287,11,9.54,16.45,26.09),(24,'Navdeep Saini','Royal Challengers Bangalore',13,13,48.0,397,11,8.28,26.18,36.09),(25,'Jofra Archer','Rajasthan Royals',11,11,43.0,291,11,6.78,23.45,26.45),(26,'Sam Curran','Kings XI Punjab',9,9,33.0,323,10,9.78,19.80,32.30),(27,'Axar Patel','Delhi Capitals',14,14,51.0,364,10,7.14,30.60,36.40),(28,'Piyush Chawla','Kolkata Knight Riders',13,13,44.3,399,10,8.94,26.70,39.90),(29,'Sunil Narine','Kolkata Knight Riders',12,12,44.2,347,10,7.80,26.60,34.70),(30,'Jaydev Unadkat','Rajasthan Royals',11,11,37.2,398,10,10.68,22.40,39.80),(31,'Keemo Paul','Delhi Capitals',8,8,27.1,237,9,8.70,18.11,26.33),(32,'Shardul Thakur','Chennai Super Kings',10,9,30.0,281,8,9.36,22.50,35.13),(33,'Mohammad Nabi','Sunrisers Hyderabad',8,8,29.1,194,8,6.66,21.87,24.25),(34,'Umesh Yadav','Royal Challengers Bangalore',11,11,37.5,371,8,9.78,28.37,46.38),(35,'Sandeep Lamichhane','Delhi Capitals',6,6,23.0,210,8,9.12,17.25,26.25),(36,'Mohammed Siraj','Royal Challengers Bangalore',9,9,28.1,269,7,9.54,24.14,38.43),(37,'Harry Gurney','Kolkata Knight Riders',8,8,27.0,238,7,8.82,23.14,34.00),(38,'Hardus Viljoen','Kings XI Punjab',6,6,23.0,222,7,9.66,19.71,31.71),(39,'Siddarth Kaul','Sunrisers Hyderabad',7,7,27.0,242,6,8.94,27.00,40.33),(40,'Moeen Ali','Royal Challengers Bangalore',11,9,25.0,169,6,6.78,25.00,28.17),(41,'Alzarri Joseph','Mumbai Indians',3,3,8.4,87,6,10.02,8.66,14.50),(42,'Dhawal Kulkarni','Rajasthan Royals',10,10,35.0,335,6,9.60,35.00,55.83),(43,'Ben Stokes','Rajasthan Royals',9,6,16.5,189,6,11.22,16.83,31.50),(44,'Jason Behrendorff','Mumbai Indians',5,5,19.0,165,5,8.70,22.80,33.00),(45,'Trent Boult','Delhi Capitals',5,5,19.0,163,5,8.58,22.80,32.60),(46,'Oshane Thomas','Rajasthan Royals',4,4,10.0,79,5,7.92,12.00,15.80),(47,'Murugan Ashwin','Kings XI Punjab',10,10,34.0,255,5,7.50,40.80,51.00),(48,'Washington Sundar','Royal Challengers Bangalore',3,3,9.0,74,4,8.22,13.50,18.50),(49,'Dale Steyn','Royal Challengers Bangalore',2,2,8.0,69,4,8.64,12.00,17.25),(50,'Ish Sodhi','Rajasthan Royals',2,2,7.1,67,4,9.36,10.75,16.75),(51,'Prasidh Krishna','Kolkata Knight Riders',11,11,40.2,377,4,9.36,60.50,94.25),(52,'Kuldeep Yadav','Kolkata Knight Riders',9,9,33.0,286,4,8.64,49.50,71.50),(53,'Mitchell Santner','Chennai Super Kings',4,4,14.0,94,4,6.72,21.00,23.50),(54,'Varun Aaron','Rajasthan Royals',5,5,12.0,116,4,9.66,18.00,29.00),(55,'Mujeeb Ur Rahman','Kings XI Punjab',5,5,19.0,191,3,10.08,38.00,63.67),(56,'Arshdeep Singh','Kings XI Punjab',3,3,10.0,109,3,10.92,20.00,36.33),(57,'Nitish Rana','Kolkata Knight Riders',14,6,8.0,72,3,9.00,16.00,24.00),(58,'Ankit Rajpoot','Kings XI Punjab',4,4,16.0,152,3,9.48,32.00,50.67),(59,'Pawan Negi','Royal Challengers Bangalore',7,4,11.1,102,3,9.12,22.33,34.00),(60,'Andrew Tye','Kings XI Punjab',6,6,22.0,233,3,10.62,44.00,77.67),(61,'Mitchell McClenaghan','Mumbai Indians',5,5,18.0,142,3,7.86,36.00,47.33),(62,'Shakib Al Hasan','Sunrisers Hyderabad',3,3,10.5,95,2,8.76,32.50,47.50),(63,'Shahbaz Nadeem','Sunrisers Hyderabad',3,3,9.0,90,2,10.02,27.00,45.00),(64,'Scott Kuggeleijn','Chennai Super Kings',2,2,8.0,71,2,8.88,24.00,35.50),(65,'Sandeep Warrier','Kolkata Knight Riders',3,3,12.0,85,2,7.08,36.00,42.50),(66,'Marcus Stoinis','Royal Challengers Bangalore',10,6,16.4,145,2,8.70,50.00,72.50),(67,'Riyan Parag','Rajasthan Royals',7,7,14.0,121,2,8.64,42.00,60.50),(68,'Harshal Patel','Delhi Capitals',2,2,8.0,77,2,9.60,24.00,38.50),(69,'Rahul Tewatia','Delhi Capitals',5,3,6.2,42,2,6.66,19.00,21.00),(70,'Jagadeesha Suchith','Delhi Capitals',1,1,4.0,28,2,7.02,12.00,14.00),(71,'Lockie Ferguson','Kolkata Knight Riders',5,5,17.0,183,2,10.74,51.00,91.50),(72,'Abhishek Sharma','Sunrisers Hyderabad',3,2,2.0,21,1,10.50,12.00,21.00),(73,'Deepak Hooda','Sunrisers Hyderabad',11,2,2.0,21,1,10.50,12.00,21.00),(74,'Vijay Shankar','Sunrisers Hyderabad',15,5,8.0,70,1,8.76,48.00,70.00),(75,'Varun Chakaravarthy','Kings XI Punjab',1,1,3.0,35,1,11.64,18.00,35.00),(76,'Mayank Markande','Mumbai Indians',3,3,6.0,59,1,9.84,36.00,59.00),(77,'Kulwant Khejroliya','Royal Challengers Bangalore',2,2,5.0,47,1,9.42,30.00,47.00),(78,'Krishnappa Gowtham','Rajasthan Royals',7,7,20.0,166,1,8.28,120.00,166.00),(79,'Tim Southee','Royal Challengers Bangalore',3,3,9.0,118,1,13.14,54.00,118.00),(80,'Karn Sharma','Chennai Super Kings',1,1,2.5,33,1,11.64,17.00,33.00),(81,'Stuart Binny','Rajasthan Royals',8,5,7.0,44,1,6.30,42.00,44.00),(82,'Anukul Roy','Mumbai Indians',1,1,2.0,11,1,5.52,12.00,11.00),(83,'Mohit Sharma','Chennai Super Kings',1,1,3.0,27,1,9.00,18.00,27.00),(84,'Sherfane Rutherford','Delhi Capitals',7,6,6.5,59,1,8.64,41.00,59.00),(85,'Ben Cutting','Mumbai Indians',3,1,2.0,27,1,13.50,12.00,27.00),(86,'Jayant Yadav','Mumbai Indians',2,2,7.0,50,1,7.14,42.00,50.00),(87,'Prithvi Raj Yarra','Kolkata Knight Riders',2,2,5.0,57,1,11.40,30.00,57.00);
/*!40000 ALTER TABLE `bowling2019` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-07-17 20:26:48
