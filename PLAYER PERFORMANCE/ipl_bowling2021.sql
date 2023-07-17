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
-- Table structure for table `bowling2021`
--

DROP TABLE IF EXISTS `bowling2021`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bowling2021` (
  `POS` int DEFAULT NULL,
  `Player` varchar(30) DEFAULT NULL,
  `Team` varchar(30) DEFAULT NULL,
  `Matches` int DEFAULT NULL,
  `Innings` int DEFAULT NULL,
  `Overs` decimal(3,1) DEFAULT NULL,
  `Runs` int DEFAULT NULL,
  `Wickets` int DEFAULT NULL,
  `Econ` decimal(4,2) DEFAULT NULL,
  `SR` decimal(5,2) DEFAULT NULL,
  `Average` decimal(5,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bowling2021`
--

LOCK TABLES `bowling2021` WRITE;
/*!40000 ALTER TABLE `bowling2021` DISABLE KEYS */;
INSERT INTO `bowling2021` VALUES (1,'Harshal Patel','Royal Challengers Bangalore',15,15,56.2,459,32,8.16,10.56,14.34),(2,'Avesh Khan','Delhi Capitals',16,16,61.0,450,24,7.38,15.25,18.75),(3,'Jasprit Bumrah','Mumbai Indians',14,14,55.0,410,21,7.44,15.71,19.52),(4,'Shardul Thakur','Chennai Super Kings',16,16,59.5,527,21,8.82,17.09,25.10),(5,'Mohammad Shami','Punjab Kings',14,14,52.4,395,19,7.50,16.63,20.79),(6,'Rashid Khan','Sunrisers Hyderabad',14,14,56.0,375,18,6.72,18.66,20.83),(7,'Arshdeep Singh','Punjab Kings',12,12,41.2,342,18,8.28,13.77,19.00),(8,'Varun Chakaravarthy','Kolkata Knight Riders',17,17,68.0,448,18,6.60,22.66,24.89),(9,'Yuzvendra Chahal','Royal Challengers Bangalore',15,15,53.0,374,18,7.08,17.66,20.78),(10,'Jason Holder','Sunrisers Hyderabad',8,8,31.5,247,16,7.74,11.93,15.44),(11,'Sunil Narine','Kolkata Knight Riders',14,14,56.0,361,16,6.42,21.00,22.56),(12,'Chris Morris','Rajasthan Royals',11,11,41.0,376,15,9.18,16.40,25.07),(13,'Axar Patel','Delhi Capitals',12,12,46.0,306,15,6.66,18.40,20.40),(14,'Kagiso Rabada','Delhi Capitals',15,15,56.0,456,15,8.16,22.40,30.40),(15,'Chetan Sakariya','Rajasthan Royals',14,14,52.0,426,14,8.22,22.28,30.43),(16,'Deepak Chahar','Chennai Super Kings',15,15,54.0,451,14,8.34,23.14,32.21),(17,'Dwayne Bravo','Chennai Super Kings',11,11,33.4,263,14,7.80,14.42,18.79),(18,'Mustafizur Rahman','Rajasthan Royals',14,14,51.5,436,14,8.40,22.21,31.14),(19,'Ravindra Jadeja','Chennai Super Kings',16,16,49.0,346,13,7.08,22.61,26.62),(20,'Lockie Ferguson','Kolkata Knight Riders',8,8,30.0,224,13,7.44,13.84,17.23),(21,'Trent Boult','Mumbai Indians',14,14,51.2,406,13,7.92,23.69,31.23),(22,'Rahul Chahar','Mumbai Indians',11,11,43.0,318,13,7.38,19.84,24.46),(23,'Ravi Bishnoi','Punjab Kings',9,9,35.0,222,12,6.36,17.50,18.50),(24,'Anrich Nortje','Delhi Capitals',8,8,30.2,187,12,6.18,15.16,15.58),(25,'Prasidh Krishna','Kolkata Knight Riders',10,10,38.3,351,12,9.12,19.25,29.25),(26,'Shivam Mavi','Kolkata Knight Riders',9,9,32.1,233,11,7.26,17.54,21.18),(27,'Josh Hazlewood','Chennai Super Kings',9,9,35.0,293,11,8.40,19.09,26.64),(28,'Mohammed Siraj','Royal Challengers Bangalore',15,15,52.0,353,11,6.78,28.36,32.09),(29,'Andre Russell','Kolkata Knight Riders',10,8,19.0,188,11,9.90,10.36,17.09),(30,'Pat Cummins','Kolkata Knight Riders',7,7,26.5,237,9,8.82,17.88,26.33),(31,'Sam Curran','Chennai Super Kings',9,9,33.0,328,9,9.96,22.00,36.44),(32,'Kyle Jamieson','Royal Challengers Bangalore',9,9,28.0,269,9,9.60,18.66,29.89),(33,'Rahul Tewatia','Rajasthan Royals',14,13,37.0,340,8,9.18,27.75,42.50),(34,'Siddarth Kaul','Sunrisers Hyderabad',8,8,30.0,247,7,8.22,25.71,35.29),(35,'Nathan Coulter-Nile','Mumbai Indians',5,5,20.0,127,7,6.36,17.14,18.14),(36,'Ravichandran Ashwin','Delhi Capitals',13,13,44.4,331,7,7.44,38.28,47.29),(37,'Shahbaz Ahmed','Royal Challengers Bangalore',11,6,14.0,92,7,6.60,12.00,13.14),(38,'Amit Mishra','Delhi Capitals',4,4,14.0,109,6,7.80,14.00,18.17),(39,'Bhuvneshwar Kumar','Sunrisers Hyderabad',11,11,42.0,335,6,7.98,42.00,55.83),(40,'Moeen Ali','Chennai Super Kings',15,10,25.2,161,6,6.36,25.33,26.83),(41,'Lungi Ngidi','Chennai Super Kings',3,3,12.0,125,5,10.44,14.40,25.00),(42,'Chris Woakes','Delhi Capitals',3,3,11.0,82,5,7.44,13.20,16.40),(43,'Krunal Pandya','Mumbai Indians',13,12,33.1,265,5,7.98,39.80,53.00),(44,'Jimmy Neesham','Mumbai Indians',3,3,9.0,66,5,7.32,10.80,13.20),(45,'Harpreet Brar','Punjab Kings',7,7,23.0,139,5,6.06,27.60,27.80),(46,'Kieron Pollard','Mumbai Indians',14,9,13.1,95,5,7.20,15.80,19.00),(47,'Khaleel Ahmed','Sunrisers Hyderabad',7,7,27.0,219,5,8.10,32.40,43.80),(48,'Abhishek Sharma','Sunrisers Hyderabad',8,6,10.0,64,4,6.42,15.00,16.00),(49,'Lalit Yadav','Delhi Capitals',7,5,14.0,101,4,7.20,21.00,25.25),(50,'Jaydev Unadkat','Rajasthan Royals',6,6,22.0,168,4,7.62,33.00,42.00),(51,'Tom Curran','Delhi Capitals',3,3,11.2,104,4,9.18,17.00,26.00),(52,'Chris Jordan','Punjab Kings',4,4,12.0,96,4,7.98,18.00,24.00),(53,'Kartik Tyagi','Rajasthan Royals',4,4,14.0,124,4,8.88,21.00,31.00),(54,'Moises Henriques','Punjab Kings',5,5,10.0,45,4,4.50,15.00,11.25),(55,'Dan Christian','Royal Challengers Bangalore',9,9,16.4,155,4,9.30,25.00,38.75),(56,'Riley Meredith','Punjab Kings',5,5,17.0,169,4,9.96,25.50,42.25),(57,'Shakib Al Hasan','Kolkata Knight Riders',8,8,26.0,187,4,7.20,39.00,46.75),(58,'Washington Sundar','Royal Challengers Bangalore',6,6,16.0,118,3,7.38,32.00,39.33),(59,'Venkatesh Iyer','Kolkata Knight Riders',10,4,8.3,69,3,8.10,17.00,23.00),(60,'Sandeep Sharma','Sunrisers Hyderabad',7,7,23.3,203,3,8.64,47.00,67.67),(61,'Adam Milne','Mumbai Indians',4,4,14.0,131,3,9.36,28.00,43.67),(62,'Tim Southee','Kolkata Knight Riders',3,3,12.0,95,3,7.92,24.00,31.67),(63,'Vijay Shankar','Sunrisers Hyderabad',7,5,11.0,100,3,9.12,22.00,33.33),(64,'Jhye Richardson','Punjab Kings',3,3,11.0,117,3,10.62,22.00,39.00),(65,'Glenn Maxwell','Royal Challengers Bangalore',15,6,16.0,135,3,8.46,32.00,45.00),(66,'George Garton','Royal Challengers Bangalore',5,5,15.0,135,3,9.00,30.00,45.00),(67,'T Natarajan','Sunrisers Hyderabad',2,2,8.0,69,2,8.64,24.00,34.50),(68,'Jayant Yadav','Mumbai Indians',5,5,17.0,130,2,7.62,51.00,65.00),(69,'Imran Tahir','Chennai Super Kings',1,1,4.0,16,2,4.02,12.00,8.00),(70,'Umran Malik','Sunrisers Hyderabad',3,3,12.0,96,2,7.98,36.00,48.00),(71,'Marco Jansen','Mumbai Indians',2,2,6.0,45,2,7.50,18.00,22.50),(72,'Marcus Stoinis','Delhi Capitals',10,8,11.1,117,2,10.50,33.50,58.50),(73,'Mohammad Nabi','Sunrisers Hyderabad',3,3,8.0,86,2,10.74,24.00,43.00),(74,'Mujeeb Ur Rahman','Sunrisers Hyderabad',1,1,4.0,29,2,7.26,12.00,14.50),(75,'Deepak Hooda','Punjab Kings',12,7,16.0,136,2,8.52,48.00,68.00),(76,'Fabian Allen','Punjab Kings',4,3,11.0,90,1,8.16,66.00,90.00),(77,'Glenn Phillips','Rajasthan Royals',3,2,2.0,20,1,10.02,12.00,20.00),(78,'Piyush Chawla','Mumbai Indians',1,1,4.0,38,1,9.48,24.00,38.00),(79,'Ishan Porel','Punjab Kings',1,1,4.0,39,1,9.78,24.00,39.00),(80,'Daniel Sams','Royal Challengers Bangalore',2,2,6.0,39,1,6.48,36.00,39.00),(81,'Ishant Sharma','Delhi Capitals',3,3,12.0,97,1,8.10,72.00,97.00),(82,'Kane Richardson','Royal Challengers Bangalore',1,1,3.0,29,1,9.66,18.00,29.00),(83,'KM Asif','Chennai Super Kings',1,1,2.1,18,1,8.28,13.00,18.00),(84,'Shahbaz Nadeem','Sunrisers Hyderabad',1,1,4.0,36,1,9.00,24.00,36.00),(85,'Lukman Meriwala','Delhi Capitals',1,1,3.0,32,1,10.68,18.00,32.00),(86,'Mahipal Lomror','Rajasthan Royals',4,4,7.0,47,1,6.72,42.00,47.00),(87,'Riyan Parag','Rajasthan Royals',11,6,6.1,73,1,11.82,37.00,73.00),(88,'Murugan Ashwin','Punjab Kings',3,3,11.0,97,1,8.82,66.00,97.00),(89,'Nathan Ellis','Punjab Kings',3,3,12.0,98,1,8.16,72.00,98.00);
/*!40000 ALTER TABLE `bowling2021` ENABLE KEYS */;
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
