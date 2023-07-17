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
-- Table structure for table `mvp2020`
--

DROP TABLE IF EXISTS `mvp2020`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mvp2020` (
  `Position` int DEFAULT NULL,
  `Player` varchar(30) DEFAULT NULL,
  `Team` varchar(30) DEFAULT NULL,
  `Matches` int DEFAULT NULL,
  `Wickets` int DEFAULT NULL,
  `DotBalls` int DEFAULT NULL,
  `4s` int DEFAULT NULL,
  `6s` int DEFAULT NULL,
  `Catches` int DEFAULT NULL,
  `Stumpings` int DEFAULT NULL,
  `RunOuts` int DEFAULT NULL,
  `Points` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mvp2020`
--

LOCK TABLES `mvp2020` WRITE;
/*!40000 ALTER TABLE `mvp2020` DISABLE KEYS */;
INSERT INTO `mvp2020` VALUES (1,'Jofra Archer','Rajasthan Royals',14,20,175,5,10,5,0,2,307),(2,'Kagiso Rabada','Delhi Capitals',17,30,156,4,2,8,0,0,298),(3,'Jasprit Bumrah','Mumbai Indians',15,27,175,0,0,0,0,1,270.5),(4,'Rashid Khan','Sunrisers Hyderabad',16,20,168,3,2,3,0,1,261),(5,'Trent Boult','Mumbai Indians',15,25,157,0,0,4,0,0,254.5),(6,'Lokesh Rahul','Kings XI Punjab',14,0,0,58,23,10,0,1,251.5),(7,'Anrich Nortje','Delhi Capitals',16,22,160,0,0,4,0,0,247),(8,'Quinton de Kock','Mumbai Indians',16,0,0,46,22,18,4,0,247),(9,'Rahul Tewatia','Rajasthan Royals',14,10,95,13,17,9,0,0,244.5),(10,'Pat Cummins','Kolkata Knight Riders',14,12,140,9,8,3,0,2,242),(11,'Marcus Stoinis','Delhi Capitals',17,13,50,31,16,3,0,0,236.5),(12,'Sam Curran','Chennai Super Kings',14,13,91,12,12,7,0,0,226),(13,'Shikhar Dhawan','Delhi Capitals',17,0,0,67,12,5,0,0,222),(14,'Mohammed Shami','Kings XI Punjab',14,20,140,0,0,2,0,1,216),(15,'Suryakumar Yadav','Mumbai Indians',16,0,0,61,11,8,0,2,213),(16,'David Warner','Sunrisers Hyderabad',16,0,0,52,14,12,0,1,210),(17,'T Natarajan','Sunrisers Hyderabad',16,16,136,0,0,3,0,0,199.5),(18,'Ishan Kishan','Mumbai Indians',14,0,0,36,30,1,0,0,197.5),(19,'Yuzvendra Chahal','Royal Challengers Bangalore',15,21,118,0,0,1,0,0,194),(20,'AB de Villiers','Royal Challengers Bangalore',15,0,0,33,23,10,1,0,190.5),(21,'Axar Patel','Delhi Capitals',15,9,100,6,8,6,0,1,190.5),(22,'Ravindra Jadeja','Chennai Super Kings',14,6,56,22,11,5,0,1,184),(23,'Faf du Plessis','Chennai Super Kings',13,0,0,42,14,12,0,0,184),(24,'Kieron Pollard','Mumbai Indians',16,4,33,15,22,8,0,1,182.5),(25,'Varun Chakravarthy','Kolkata Knight Riders',13,17,111,0,0,3,0,0,178),(26,'Mayank Agarwal','Kings XI Punjab',11,0,0,44,15,6,0,0,177.5),(27,'Devdutt Padikkal','Royal Challengers Bangalore',15,0,0,51,8,8,0,1,176.5),(28,'Washington Sundar','Royal Challengers Bangalore',15,8,114,10,2,0,0,0,174),(29,'Ravi Bishnoi','Kings XI Punjab',14,12,122,1,0,2,0,1,172.5),(30,'Eoin Morgan','Kolkata Knight Riders',14,0,0,32,24,3,0,0,171.5),(31,'Sanju Samson','Rajasthan Royals',14,0,0,21,26,9,2,0,171),(32,'Shreyas Iyer','Delhi Capitals',17,0,0,40,16,6,0,0,171),(33,'Krunal Pandya','Mumbai Indians',16,6,100,9,5,4,0,0,171),(34,'Sandeep Sharma','Sunrisers Hyderabad',13,14,119,1,0,0,0,0,170.5),(35,'Manish Pandey','Sunrisers Hyderabad',16,0,0,35,18,7,0,1,169),(36,'Deepak Chahar','Chennai Super Kings',14,12,118,0,0,3,0,0,167.5),(37,'Rahul Chahar','Mumbai Indians',15,15,104,0,0,4,0,0,166.5),(38,'Nicholas Pooran','Kings XI Punjab',14,0,0,23,25,7,0,3,165.5),(39,'Ravichandran Ashwin','Delhi Capitals',15,13,101,3,1,2,0,1,163.5),(40,'Chris Morris','Royal Challengers Bangalore',9,11,91,2,3,7,0,1,163.5),(41,'Ben Stokes','Rajasthan Royals',8,2,24,36,7,6,0,0,160.5),(42,'Shubman Gill','Kolkata Knight Riders',14,0,0,44,9,7,0,0,159),(43,'Nitish Rana','Kolkata Knight Riders',14,0,0,43,12,2,0,0,154.5),(44,'Navdeep Saini','Royal Challengers Bangalore',13,6,116,3,0,2,0,0,149.5),(45,'Rohit Sharma','Mumbai Indians',12,0,0,27,19,6,0,0,149),(46,'Jonny Bairstow','Sunrisers Hyderabad',11,0,0,31,13,7,1,1,144),(47,'Sunil Narine','Kolkata Knight Riders',10,5,67,10,8,2,0,1,143.5),(48,'Rishabh Pant','Delhi Capitals',14,0,0,31,9,13,0,1,142.5),(49,'Jos Buttler','Rajasthan Royals',13,0,0,27,16,6,0,0,138.5),(50,'Hardik Pandya','Mumbai Indians',14,0,0,14,25,6,0,0,137.5),(51,'Shreyas Gopal','Rajasthan Royals',14,10,86,3,0,2,0,0,133.5),(52,'Shane Watson','Chennai Super Kings',11,0,0,33,13,2,0,0,133),(53,'Jason Holder','Sunrisers Hyderabad',7,14,58,5,3,0,0,1,131),(54,'Mohammed Siraj','Royal Challengers Bangalore',9,11,77,2,0,4,0,0,130.5),(55,'James Pattinson','Mumbai Indians',10,11,78,2,0,2,0,0,126.5),(56,'Ambati Rayudu','Chennai Super Kings',12,0,0,30,12,3,0,1,125.5),(57,'Chris Gayle','Kings XI Punjab',7,0,0,15,23,1,0,0,120.5),(58,'Kartik Tyagi','Rajasthan Royals',10,9,83,0,0,2,0,0,119.5),(59,'Andre Russell','Kolkata Knight Riders',10,6,39,9,9,2,0,0,119),(60,'Steven Smith','Rajasthan Royals',14,0,0,32,9,2,0,0,116.5),(61,'Kane Williamson','Sunrisers Hyderabad',12,0,0,26,10,6,0,0,115),(62,'Murugan Ashwin','Kings XI Punjab',9,10,70,0,0,4,0,0,115),(63,'Chris Jordan','Kings XI Punjab',9,9,62,2,0,5,0,0,111),(64,'Shardul Thakur','Chennai Super Kings',9,10,68,0,0,2,0,0,108),(65,'Shivam Mavi','Kolkata Knight Riders',8,9,63,1,0,4,0,0,107),(66,'Prithvi Shaw','Delhi Capitals',13,0,0,27,8,4,0,0,105.5),(67,'Aaron Finch','Royal Challengers Bangalore',12,0,0,28,8,3,0,0,105.5),(68,'MS Dhoni','Chennai Super Kings',14,0,0,16,7,15,1,0,104.5),(69,'Virat Kohli','Royal Challengers Bangalore',15,0,0,23,11,3,0,0,103.5),(70,'Nathan Coulter-Nile','Mumbai Indians',7,5,69,4,0,2,0,0,101.5),(71,'Rahul Tripathi','Kolkata Knight Riders',11,0,0,21,10,3,0,0,95),(72,'Arshdeep Singh','Kings XI Punjab',8,9,56,0,0,2,0,0,92.5),(73,'Khaleel Ahmed','Sunrisers Hyderabad',7,8,62,0,0,1,0,0,92.5),(74,'Isuru Udana','Royal Challengers Bangalore',10,8,49,1,1,3,0,1,91.5),(75,'Shimron Hetmyer','Delhi Capitals',12,0,0,11,12,7,0,0,87),(76,'Dinesh Karthik','Kolkata Knight Riders',14,0,0,20,4,9,0,0,86.5),(77,'Wriddhiman Saha','Sunrisers Hyderabad',4,0,0,24,5,2,1,0,85),(78,'Lockie Ferguson','Kolkata Knight Riders',5,6,48,4,1,0,0,0,82.5),(79,'Sheldon Cottrell','Kings XI Punjab',6,6,59,0,0,0,0,0,80),(80,'Glenn Maxwell','Kings XI Punjab',13,3,37,9,0,4,0,0,80),(81,'Robin Uthappa','Rajasthan Royals',12,0,0,19,7,3,0,0,79.5),(82,'Vijay Shankar','Sunrisers Hyderabad',7,4,31,10,1,1,0,2,78),(83,'Shivam Dube','Royal Challengers Bangalore',11,4,14,5,9,2,0,0,77),(84,'Kamlesh Nagarkoti','Kolkata Knight Riders',10,5,46,1,0,4,0,0,76),(85,'Ruturaj Gaikwad','Chennai Super Kings',6,0,0,16,6,4,0,1,72),(86,'Lungi Ngidi','Chennai Super Kings',4,9,35,0,0,0,0,0,66.5),(87,'Abdul Samad','Sunrisers Hyderabad',12,1,9,8,6,5,0,0,66),(88,'Tom Curran','Rajasthan Royals',5,3,25,5,3,1,0,0,61),(89,'Dwayne Bravo','Chennai Super Kings',6,6,35,0,0,1,0,1,59.5),(90,'Piyush Chawla','Chennai Super Kings',7,6,37,0,0,0,0,0,58),(91,'Priyam Garg','Sunrisers Hyderabad',14,0,0,9,4,6,0,2,53.5),(92,'Shahbaz Nadeem','Sunrisers Hyderabad',7,5,31,1,0,1,0,0,53.5),(93,'Prasidh Krishna','Kolkata Knight Riders',6,4,35,0,0,1,0,0,51.5),(94,'Jaydev Unadkat','Rajasthan Royals',7,4,35,0,0,1,0,0,51.5),(95,'Tushar Deshpande','Delhi Capitals',5,3,29,2,1,1,0,0,50.5),(96,'Bhuvneshwar Kumar','Sunrisers Hyderabad',4,3,40,0,0,0,0,0,50.5),(97,'Ajinkya Rahane','Delhi Capitals',9,0,0,12,2,4,0,1,48),(98,'Abhishek Sharma','Sunrisers Hyderabad',8,2,11,6,3,1,0,0,46),(99,'Karn Sharma','Chennai Super Kings',5,5,27,0,0,0,0,0,44.5),(100,'Ankit Rajpoot','Rajasthan Royals',6,2,34,0,1,0,0,0,44.5),(101,'Mandeep Singh','Kings XI Punjab',7,0,0,10,4,1,0,1,42.5),(102,'Harshal Patel','Delhi Capitals',5,3,23,2,0,1,0,0,41),(103,'Deepak Hooda','Kings XI Punjab',7,0,2,5,5,3,0,0,39.5),(104,'James Neesham','Kings XI Punjab',5,2,26,0,1,1,0,0,39),(105,'Josh Hazlewood','Chennai Super Kings',3,1,31,0,0,0,0,0,34.5),(106,'Gurkeerat Singh Mann','Royal Challengers Bangalore',8,0,0,8,0,5,0,1,33.5),(107,'Saurabh Tiwary','Mumbai Indians',7,0,0,8,3,1,0,0,33),(108,'Riyan Parag','Rajasthan Royals',12,0,3,6,3,1,0,0,31),(109,'Amit Mishra','Delhi Capitals',3,3,17,0,0,1,0,0,30),(110,'Daniel Sams','Delhi Capitals',3,0,22,0,0,3,0,0,29.5),(111,'Adam Zampa','Royal Challengers Bangalore',3,2,20,0,0,1,0,0,29.5),(112,'Krishnappa Gowtham','Kings XI Punjab',2,1,11,3,2,0,0,0,29),(113,'Imran Tahir','Chennai Super Kings',3,1,19,2,0,0,0,0,27.5),(114,'Dale Steyn','Royal Challengers Bangalore',3,1,24,0,0,0,0,0,27.5),(115,'Joshua Philippe','Royal Challengers Bangalore',5,0,0,9,1,0,0,0,26),(116,'Kuldeep Yadav','Kolkata Knight Riders',5,1,19,1,0,0,0,0,25),(117,'Mitchell Santner','Chennai Super Kings',2,2,12,0,0,1,0,0,21.5),(118,'Varun Aaron','Rajasthan Royals',3,0,21,0,0,0,0,0,21),(119,'Kedar Jadhav','Chennai Super Kings',8,0,0,7,0,1,0,0,20),(120,'Shahbaz Ahamad','Royal Challengers Bangalore',2,2,9,0,0,1,0,0,18.5),(121,'Sarfaraz Khan','Kings XI Punjab',5,0,0,5,0,2,0,0,17.5),(122,'Moeen Ali','Royal Challengers Bangalore',3,1,8,1,0,1,0,0,16.5),(123,'Jayant Yadav','Mumbai Indians',2,1,13,0,0,0,0,0,16.5),(124,'Umesh Yadav','Royal Challengers Bangalore',2,0,14,0,0,0,0,2,16),(125,'Yashasvi Jaiswal','Rajasthan Royals',3,0,0,2,2,1,0,1,15.5),(126,'Mahipal Lomror','Rajasthan Royals',3,0,0,2,3,0,0,0,15.5),(127,'Praveen Dubey','Delhi Capitals',3,0,12,0,0,1,0,1,15.5),(128,'Siddarth Kaul','Sunrisers Hyderabad',1,2,6,0,0,0,0,0,13),(129,'Mujeeb Ur Rahman','Kings XI Punjab',2,0,12,0,0,0,0,0,12),(130,'Andrew Tye','Rajasthan Royals',1,1,5,0,1,0,0,0,12),(131,'Mohit Sharma','Delhi Capitals',1,1,7,0,0,0,0,0,10.5),(132,'Narayan Jagadeesan','Chennai Super Kings',5,0,0,4,0,0,0,0,10),(133,'Mohammad Nabi','Sunrisers Hyderabad',1,0,5,2,0,0,0,0,10),(134,'Murali Vijay','Chennai Super Kings',3,0,0,4,0,0,0,0,10),(135,'Alex Carey','Delhi Capitals',3,0,0,0,1,2,0,0,8.5),(136,'Basil Thampi','Sunrisers Hyderabad',1,1,5,0,0,0,0,0,8.5),(137,'Sandeep Warrier','Kolkata Knight Riders',1,0,8,0,0,0,0,0,8),(138,'Prabhsimran Singh','Kings XI Punjab',2,0,0,2,0,1,0,0,7.5),(139,'Karun Nair','Kings XI Punjab',4,0,0,2,0,1,0,0,7.5),(140,'Avesh Khan','Delhi Capitals',1,0,7,0,0,0,0,0,7),(141,'Harpreet Brar','Kings XI Punjab',1,0,6,0,0,0,0,0,6),(142,'Chris Green','Kolkata Knight Riders',1,0,6,0,0,0,0,0,6),(143,'Tom Banton','Kolkata Knight Riders',2,0,0,1,1,0,0,0,6),(144,'Dhawal Kulkarni','Mumbai Indians',1,0,6,0,0,0,0,0,6),(145,'Rinku Singh','Kolkata Knight Riders',1,0,0,1,0,1,0,0,5),(146,'Monu Kumar','Chennai Super Kings',1,0,4,0,0,0,0,0,4),(147,'Ishant Sharma','Delhi Capitals',1,0,4,0,0,0,0,0,4),(148,'Shreevats Goswami','Sunrisers Hyderabad',2,0,0,0,0,1,0,0,2.5),(149,'Nikhil Naik','Kolkata Knight Riders',1,0,0,0,0,1,0,0,2.5),(150,'Mitchell Marsh','Sunrisers Hyderabad',1,0,1,0,0,0,0,0,1);
/*!40000 ALTER TABLE `mvp2020` ENABLE KEYS */;
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
