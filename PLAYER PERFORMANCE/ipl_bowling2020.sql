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
-- Table structure for table `bowling2020`
--

DROP TABLE IF EXISTS `bowling2020`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bowling2020` (
  `POS` int DEFAULT NULL,
  `Player` varchar(30) DEFAULT NULL,
  `Team` varchar(30) DEFAULT NULL,
  `Matches` int DEFAULT NULL,
  `Innings` int DEFAULT NULL,
  `Overs` decimal(4,1) DEFAULT NULL,
  `Runs` int DEFAULT NULL,
  `Wickets` int DEFAULT NULL,
  `Econ` decimal(5,2) DEFAULT NULL,
  `SR` decimal(5,2) DEFAULT NULL,
  `Average` decimal(5,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bowling2020`
--

LOCK TABLES `bowling2020` WRITE;
/*!40000 ALTER TABLE `bowling2020` DISABLE KEYS */;
INSERT INTO `bowling2020` VALUES (1,'Kagiso Rabada','Delhi Capitals',17,17,65.4,548,30,8.35,13.13,18.27),(2,'Jasprit Bumrah','Mumbai Indians',15,15,60.0,404,27,6.73,13.33,14.96),(3,'Trent Boult','Mumbai Indians',15,15,57.2,457,25,7.97,13.76,18.28),(4,'Anrich Nortje','Delhi Capitals',16,16,61.0,512,22,8.39,16.63,23.27),(5,'Yuzvendra Chahal','Royal Challengers Bangalore',15,15,57.1,405,21,7.08,16.33,19.29),(6,'Mohammad Shami','Kings XI Punjab',14,14,53.4,460,20,8.57,16.10,23.00),(7,'Jofra Archer','Rajasthan Royals',14,14,55.4,365,20,6.56,16.70,18.25),(8,'Rashid Khan','Sunrisers Hyderabad',16,16,64.0,344,20,5.38,19.20,17.20),(9,'Varun Chakaravarthy','Kolkata Knight Riders',13,13,52.0,356,17,6.85,18.35,20.94),(10,'T Natarajan','Sunrisers Hyderabad',16,16,62.5,504,16,8.02,23.56,31.50),(11,'Rahul Chahar','Mumbai Indians',15,15,53.0,433,15,8.17,21.20,28.87),(12,'Jason Holder','Sunrisers Hyderabad',7,7,28.0,233,14,8.32,12.00,16.64),(13,'Sandeep Sharma','Sunrisers Hyderabad',13,13,52.0,374,14,7.19,22.28,26.71),(14,'Marcus Stoinis','Delhi Capitals',17,13,29.4,283,13,9.54,13.69,21.77),(15,'Ravichandran Ashwin','Delhi Capitals',15,15,51.0,391,13,7.67,23.53,30.08),(16,'Sam Curran','Chennai Super Kings',14,13,42.0,344,13,8.19,19.38,26.46),(17,'Pat Cummins','Kolkata Knight Riders',14,14,52.0,409,12,7.87,26.00,34.08),(18,'Ravi Bishnoi','Kings XI Punjab',14,14,51.0,376,12,7.37,25.50,31.33),(19,'Deepak Chahar','Chennai Super Kings',14,14,52.0,396,12,7.62,26.00,33.00),(20,'Mohammed Siraj','Royal Challengers Bangalore',9,9,27.1,236,11,8.69,14.81,21.45),(21,'James Pattinson','Mumbai Indians',10,10,34.5,320,11,9.19,19.36,29.09),(22,'Chris Morris','Royal Challengers Bangalore',9,9,31.4,210,11,6.63,17.27,19.09),(23,'Shreyas Gopal','Rajasthan Royals',14,14,50.0,427,10,8.54,30.00,42.70),(24,'Murugan Ashwin','Kings XI Punjab',9,9,31.3,235,10,7.46,18.90,23.50),(25,'Shardul Thakur','Chennai Super Kings',9,9,32.2,275,10,8.51,19.40,27.50),(26,'Rahul Tewatia','Rajasthan Royals',14,14,46.0,326,10,7.09,27.60,32.60),(27,'Lungi Ngidi','Chennai Super Kings',4,4,16.0,167,9,10.44,10.66,18.56),(28,'Kartik Tyagi','Rajasthan Royals',10,10,38.1,367,9,9.62,25.44,40.78),(29,'Arshdeep Singh','Kings XI Punjab',8,8,24.5,218,9,8.78,16.55,24.22),(30,'Axar Patel','Delhi Capitals',15,15,51.0,327,9,6.41,34.00,36.33),(31,'Shivam Mavi','Kolkata Knight Riders',8,8,26.0,212,9,8.15,17.33,23.56),(32,'Chris Jordan','Kings XI Punjab',9,9,31.3,304,9,9.65,21.00,33.78),(33,'Khaleel Ahmed','Sunrisers Hyderabad',7,7,25.4,242,8,9.43,19.25,30.25),(34,'Isuru Udana','Royal Challengers Bangalore',10,10,29.0,282,8,9.72,21.75,35.25),(35,'Washington Sundar','Royal Challengers Bangalore',15,15,50.0,298,8,5.96,37.50,37.25),(36,'Piyush Chawla','Chennai Super Kings',7,7,21.0,191,6,9.10,21.00,31.83),(37,'Navdeep Saini','Royal Challengers Bangalore',13,13,45.4,379,6,8.30,45.66,63.17),(38,'Sheldon Cottrell','Kings XI Punjab',6,6,20.0,176,6,8.80,20.00,29.33),(39,'Lockie Ferguson','Kolkata Knight Riders',5,5,19.5,148,6,7.46,19.83,24.67),(40,'Ravindra Jadeja','Chennai Super Kings',14,13,36.2,318,6,8.75,36.33,53.00),(41,'Krunal Pandya','Mumbai Indians',16,16,50.1,380,6,7.57,50.16,63.33),(42,'Dwayne Bravo','Chennai Super Kings',6,6,21.0,180,6,8.57,21.00,30.00),(43,'Andre Russell','Kolkata Knight Riders',10,7,18.0,175,6,9.72,18.00,29.17),(44,'Shahbaz Nadeem','Sunrisers Hyderabad',7,7,22.0,178,5,8.09,26.40,35.60),(45,'Nathan Coulter-Nile','Mumbai Indians',7,7,26.0,206,5,7.92,31.20,41.20),(46,'Karn Sharma','Chennai Super Kings',5,5,19.0,165,5,8.68,22.80,33.00),(47,'Kamlesh Nagarkoti','Kolkata Knight Riders',10,9,26.0,231,5,8.88,31.20,46.20),(48,'Sunil Narine','Kolkata Knight Riders',10,10,38.0,302,5,7.95,45.60,60.40),(49,'Vijay Shankar','Sunrisers Hyderabad',7,5,13.1,82,4,6.23,19.75,20.50),(50,'Shivam Dube','Royal Challengers Bangalore',11,5,9.0,73,4,8.11,13.50,18.25),(51,'Kieron Pollard','Mumbai Indians',16,11,21.0,190,4,9.05,31.50,47.50),(52,'Prasidh Krishna','Kolkata Knight Riders',6,6,17.3,164,4,9.37,26.25,41.00),(53,'Jaydev Unadkat','Rajasthan Royals',7,7,23.0,228,4,9.91,34.50,57.00),(54,'Bhuvneshwar Kumar','Sunrisers Hyderabad',4,4,14.1,99,3,6.99,28.33,33.00),(55,'Glenn Maxwell','Kings XI Punjab',13,7,21.0,169,3,8.05,42.00,56.33),(56,'Harshal Patel','Delhi Capitals',5,5,15.0,134,3,8.93,30.00,44.67),(57,'Tom Curran','Rajasthan Royals',5,5,18.1,208,3,11.45,36.33,69.33),(58,'Tushar Deshpande','Delhi Capitals',5,5,17.0,192,3,11.29,34.00,64.00),(59,'Amit Mishra','Delhi Capitals',3,3,10.0,72,3,7.20,20.00,24.00),(60,'Ankit Rajpoot','Rajasthan Royals',6,6,17.0,199,2,11.71,51.00,99.50),(61,'Siddarth Kaul','Sunrisers Hyderabad',1,1,4.0,64,2,16.00,12.00,32.00),(62,'Ben Stokes','Rajasthan Royals',8,6,15.0,154,2,10.27,45.00,77.00),(63,'Adam Zampa','Royal Challengers Bangalore',3,3,11.0,92,2,8.36,33.00,46.00),(64,'Abhishek Sharma','Sunrisers Hyderabad',8,6,10.0,91,2,9.10,30.00,45.50),(65,'Shahbaz Ahmed','Royal Challengers Bangalore',2,2,6.0,44,2,7.33,18.00,22.00),(66,'Jimmy Neesham','Kings XI Punjab',5,5,15.0,148,2,9.87,45.00,74.00),(67,'Mitchell Santner','Chennai Super Kings',2,2,7.0,53,2,7.57,21.00,26.50),(68,'Dale Steyn','Royal Challengers Bangalore',3,3,11.4,133,1,11.40,70.00,133.00),(69,'Basil Thampi','Sunrisers Hyderabad',1,1,4.0,46,1,11.50,24.00,46.00),(70,'Imran Tahir','Chennai Super Kings',3,3,11.0,76,1,6.91,66.00,76.00),(71,'Jayant Yadav','Mumbai Indians',2,2,7.0,43,1,6.14,42.00,43.00),(72,'Andrew Tye','Rajasthan Royals',1,1,4.0,50,1,12.50,24.00,50.00),(73,'Josh Hazlewood','Chennai Super Kings',3,3,10.0,64,1,6.40,60.00,64.00),(74,'Mohit Sharma','Delhi Capitals',1,1,4.0,45,1,11.25,24.00,45.00),(75,'Krishnappa Gowtham','Kings XI Punjab',2,2,8.0,84,1,10.50,48.00,84.00),(76,'Moeen Ali','Royal Challengers Bangalore',3,3,5.0,42,1,8.40,30.00,42.00),(77,'Kuldeep Yadav','Kolkata Knight Riders',5,4,12.0,92,1,7.67,72.00,92.00),(78,'Abdul Samad','Sunrisers Hyderabad',12,3,7.0,96,1,13.71,42.00,96.00);
/*!40000 ALTER TABLE `bowling2020` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-07-17 20:26:49
