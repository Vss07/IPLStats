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
-- Table structure for table `aucunsold2021`
--

DROP TABLE IF EXISTS `aucunsold2021`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `aucunsold2021` (
  `PLAYER` varchar(30) DEFAULT NULL,
  `TYPE` varchar(15) DEFAULT NULL,
  `PRICE` varchar(15) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `aucunsold2021`
--

LOCK TABLES `aucunsold2021` WRITE;
/*!40000 ALTER TABLE `aucunsold2021` DISABLE KEYS */;
INSERT INTO `aucunsold2021` VALUES ('Jason Roy','Batsman','Rs 2,00,00,000'),('Liam Plunkett','Bowler','Rs 2,00,00,000'),('Morne Morkel','Bowler','Rs 1,50,00,000'),('Alex Hales','Batsman','Rs 1,50,00,000'),('Alex Carey','Wicket Keeper','Rs 1,50,00,000'),('Adil Rashid','Bowler','Rs 1,50,00,000'),('Shaun Marsh','Batsman','Rs 1,50,00,000'),('David Willey','All-Rounder','Rs 1,50,00,000'),('Lewis Gregory','All-Rounder','Rs 1,50,00,000'),('Aaron Finch','Batsman','Rs 1,00,00,000'),('Evin Lewis','Batsman','Rs 1,00,00,000'),('Hanuma Vihari','Batsman','Rs 1,00,00,000'),('Sheldon Cottrell','Bowler','Rs 1,00,00,000'),('Mushfiqur Rahim','Wicket Keeper','Rs 1,00,00,000'),('Marnus Labuschagne','All-Rounder','Rs 1,00,00,000'),('Jason Behrendorff','Bowler','Rs 1,00,00,000'),('Billy Stanlake','Bowler','Rs 1,00,00,000'),('Matthew Wade','Wicket Keeper','Rs 1,00,00,000'),('Sherfane Rutherford','All-Rounder','Rs 75,00,000'),('Hilton Cartwright','All-Rounder','Rs 75,00,000'),('James Faulkner','All-Rounder','Rs 75,00,000'),('Mohammad Mahmudullah','All-Rounder','Rs 75,00,000'),('Corey Anderson','Batsman','Rs 75,00,000'),('Darren Bravo','Batsman','Rs 75,00,000'),('Tim Southee','Bowler','Rs 75,00,000'),('Keemo Paul','All-Rounder','Rs 75,00,000'),('Fidel Edwards','Bowler','Rs 75,00,000'),('Carlos Brathwaite','All-Rounder','Rs 50,00,000'),('Rishi Dhawan','All-Rounder','Rs 50,00,000'),('Andile Phehlukwayo','All-Rounder','Rs 50,00,000'),('Dasun Shanaka','All-Rounder','Rs 50,00,000'),('Isuru Udana','All-Rounder','Rs 50,00,000'),('Jacob Duffy','Bowler','Rs 50,00,000'),('Daryn Dupavillon','Bowler','Rs 50,00,000'),('Shannon Gabriel','Bowler','Rs 50,00,000'),('Joel Paris','Bowler','Rs 50,00,000'),('Blair Tickner','Bowler','Rs 50,00,000'),('Ravi Bopara','All-Rounder','Rs 50,00,000'),('George Linde','All-Rounder','Rs 50,00,000'),('Kyle Mayers','All-Rounder','Rs 50,00,000'),('Daryl Mitchell','All-Rounder','Rs 50,00,000'),('Colin Munro','All-Rounder','Rs 50,00,000'),('Dwaine Pretorius','All-Rounder','Rs 50,00,000'),('Romario Shepherd','All-Rounder','Rs 50,00,000'),('Stuart Binny','All-Rounder','Rs 50,00,000'),('Akeal Hosein','All-Rounder','Rs 50,00,000'),('David Wiese','All-Rounder','Rs 50,00,000'),('Jack Wildermuth','All-Rounder','Rs 50,00,000'),('Glenn Phillips','Wicket Keeper','Rs 50,00,000'),('Qais Ahmad','Bowler','Rs 50,00,000'),('Rahul Sharma','Bowler','Rs 50,00,000'),('Ish Sodhi','Bowler','Rs 50,00,000'),('Jacques Snyman','All-Rounder','Rs 50,00,000'),('Kusal Janith Perera','Wicket Keeper','Rs 50,00,000'),('Dushmantha Chameera','Bowler','Rs 50,00,000'),('Parveez Rasool','All-Rounder','Rs 50,00,000'),('Devon Conway','Batsman','Rs 50,00,000'),('Martin Guptill','Batsman','Rs 50,00,000'),('Rovman Powell','Batsman','Rs 50,00,000'),('Rassie Van der Dussen','Batsman','Rs 50,00,000'),('Gurkeerat Singh Mann','All-Rounder','Rs 50,00,000'),('Varun Aaron','Bowler','Rs 50,00,000'),('Mitchell McClenaghan','Bowler','Rs 50,00,000'),('Naveen Ul Haq','Bowler','Rs 50,00,000'),('Mohit Sharma','Bowler','Rs 50,00,000'),('Oshane Thomas','Bowler','Rs 50,00,000'),('Colin De Grandhomme','All-Rounder','Rs 50,00,000'),('Thisara Perera','All-Rounder','Rs 50,00,000'),('Mohammad Shaifuddin','All-Rounder','Rs 50,00,000'),('Ben Duckett','Wicket Keeper','Rs 50,00,000'),('Rahmanullah Gurbaz','Wicket Keeper','Rs 50,00,000'),('Ben McDermott','Wicket Keeper','Rs 50,00,000'),('Sean Abbott','Bowler','Rs 50,00,000'),('Matt Henry','Bowler','Rs 50,00,000'),('Chemar Holder','Bowler','Rs 50,00,000'),('Alzarri Joseph','Bowler','Rs 50,00,000'),('Obed McCoy','Bowler','Rs 50,00,000'),('Wanindu Hasaranga','All-Rounder','Rs 50,00,000'),('Karim Janat','All-Rounder','Rs 50,00,000'),('Scott Kuggeleijn','All-Rounder','Rs 50,00,000'),('Wayne Parnell','All-Rounder','Rs 50,00,000'),('Beuran Hendricks','Bowler','Rs 50,00,000'),('Abhimanyu Mithun','Bowler','Rs 50,00,000'),('Reece Topley','Bowler','Rs 50,00,000'),('Hardus Viljoen','Bowler','Rs 50,00,000'),('Neil Wagner','Bowler','Rs 50,00,000'),('Mark Steketee','Bowler','Rs 40,00,000'),('Sandeep Lamichhane','Bowler','Rs 40,00,000'),('Ali Khan','Bowler','Rs 40,00,000'),('Brendan Doggett','Bowler','Rs 40,00,000'),('Fazalhaq Farooqi','Bowler','Rs 40,00,000'),('Ankit Singh Rajpoot','Bowler','Rs 30,00,000'),('Ben Dwarshuis','Bowler','Rs 30,00,000'),('Chris Green','All-Rounder','Rs 30,00,000'),('Jayden Seales','Bowler','Rs 20,00,000'),('Tanveer Ul haq','Bowler','Rs 20,00,000'),('Subodh Bhati','All-Rounder','Rs 20,00,000'),('Aamir Gani','All-Rounder','Rs 20,00,000'),('Karanveer Kaushal','All-Rounder','Rs 20,00,000'),('Anustup Majumdar','All-Rounder','Rs 20,00,000'),('Dikshanshu Negi','All-Rounder','Rs 20,00,000'),('Kshitiz Sharma','All-Rounder','Rs 20,00,000'),('Shubham Singh Rohilla','All-Rounder','Rs 20,00,000'),('Shashank Singh','All-Rounder','Rs 20,00,000'),('Milind Tandon','All-Rounder','Rs 20,00,000'),('Sandeep Bavanaka','All-Rounder','Rs 20,00,000'),('Chaitanya Bishnoi','All-Rounder','Rs 20,00,000'),('Arun Chaprana','All-Rounder','Rs 20,00,000'),('Ajay Dev Goud','All-Rounder','Rs 20,00,000'),('Umran Malik','All-Rounder','Rs 20,00,000'),('Tanay Thyagarajan','All-Rounder','Rs 20,00,000'),('N.Tilak Varma','All-Rounder','Rs 20,00,000'),('Arshdeep Brar','All-Rounder','Rs 20,00,000'),('Digvijay Deshmukh','All-Rounder','Rs 20,00,000'),('Aakarshit Gomel','All-Rounder','Rs 20,00,000'),('Arjit Gupta','All-Rounder','Rs 20,00,000'),('Shubhang Hegde','All-Rounder','Rs 20,00,000'),('Azim Kazi','All-Rounder','Rs 20,00,000'),('Rahul Singh','All-Rounder','Rs 20,00,000'),('Rahul Ajay Tripathy','All-Rounder','Rs 20,00,000'),('Harsh Tyagi','All-Rounder','Rs 20,00,000'),('Nachiket Bhute','All-Rounder','Rs 20,00,000'),('Josh Clarkson','All-Rounder','Rs 20,00,000'),('Gerald Coetzee','All-Rounder','Rs 20,00,000'),('Tim David','All-Rounder','Rs 20,00,000'),('Deeparaj Gaonkar','All-Rounder','Rs 20,00,000'),('Aaron Hardie','All-Rounder','Rs 20,00,000'),('Nathan McAndrew','All-Rounder','Rs 20,00,000'),('M Mohammed','All-Rounder','Rs 20,00,000'),('Rahul Gahlaut','Batsman','Rs 20,00,000'),('Govinda Poddar','All-Rounder','Rs 20,00,000'),('Pratyush Singh','All-Rounder','Rs 20,00,000'),('Himanshu Rana','Batsman','Rs 20,00,000'),('Himmat Singh','Batsman','Rs 20,00,000'),('Vishnu Solanki','Batsman','Rs 20,00,000'),('Sadiq Hassan Kirmani','Wicket Keeper','Rs 20,00,000'),('Ayush Badoni','All-Rounder','Rs 20,00,000'),('Cheepurupalli Stephen','Bowler','Rs 20,00,000'),('Nidheesh M D Dinesan','Bowler','Rs 20,00,000'),('Atit Sheth','All-Rounder','Rs 20,00,000'),('Vivek Singh','All-Rounder','Rs 20,00,000'),('Avi Barot','Wicket Keeper','Rs 20,00,000'),('Armaan Jaffer','Batsman','Rs 20,00,000'),('Kedar Devdhar','Wicket Keeper','Rs 20,00,000'),('Tejas Singh Baroka','Bowler','Rs 20,00,000'),('Apoorv Vijay Wankhade','Batsman','Rs 20,00,000'),('Tushar Deshpande','Bowler','Rs 20,00,000'),('Prathamesh Ganesh Dake','Bowler','Rs 20,00,000'),('Jay Gokul Bista','All-Rounder','Rs 20,00,000'),('T Ravi Teja','All-Rounder','Rs 20,00,000'),('Kuldeep Sen','Bowler','Rs 20,00,000'),('Anirudha Ashok Joshi','All-Rounder','Rs 20,00,000'),('Mujtaba Yousuf','Bowler','Rs 20,00,000'),('Pradeep Sahu','Bowler','Rs 20,00,000'),('Prayas Ray Barman','All-Rounder','Rs 20,00,000'),('Siddhesh Dinesh Lad','Batsman','Rs 20,00,000'),('Karanveer Singh','Bowler','Rs 20,00,000'),('Midhun Sudhesan','Bowler','Rs 20,00,000'),('Nikhil Shankar Naik','Wicket Keeper','Rs 20,00,000'),('Prithvi Raj Yarra','Bowler','Rs 20,00,000'),('Noor Ahmad','Bowler','Rs 20,00,000'),('Xavier Bartlett','Bowler','Rs 20,00,000'),('Rohit Damodaran','All-Rounder','Rs 20,00,000'),('Jiyas K','Bowler','Rs 20,00,000'),('Mayank Dagar','All-Rounder','Rs 20,00,000'),('Ashok Menaria','All-Rounder','Rs 20,00,000'),('Finn Allen','Batsman','Rs 20,00,000'),('Harpreet Bhatia','Batsman','Rs 20,00,000'),('Shivam Chauhan','Batsman','Rs 20,00,000'),('Naushad Shaikh','Batsman','Rs 20,00,000'),('Pratham Singh','Batsman','Rs 20,00,000'),('Atharva Ankolekar','All-Rounder','Rs 20,00,000'),('Rojith Ganesh','All-Rounder','Rs 20,00,000'),('Sumit Kumar','All-Rounder','Rs 20,00,000'),('Akshdeep Nath','All-Rounder','Rs 20,00,000'),('Pradeep Sangwan','All-Rounder','Rs 20,00,000'),('Karan Sharma','All-Rounder','Rs 20,00,000'),('R. Sonu Yadav','All-Rounder','Rs 20,00,000'),('Dhruv Jurel','Wicket Keeper','Rs 20,00,000'),('Arun Karthick','Wicket Keeper','Rs 20,00,000'),('Smit Patel','Wicket Keeper','Rs 20,00,000'),('K.L Shrijith','Wicket Keeper','Rs 20,00,000'),('Wesley Agar','Bowler','Rs 20,00,000'),('Akash Deep','Bowler','Rs 20,00,000'),('Kulwant Khejroliya','Bowler','Rs 20,00,000'),('Arzan Nagwaswalla','Bowler','Rs 20,00,000'),('G Periyasamy','Bowler','Rs 20,00,000'),('Karthik Meiyappan','Bowler','Rs 20,00,000'),('Prince Balwant Rai Singh','Bowler','Rs 20,00,000'),('Sagar Udeshi','Bowler','Rs 20,00,000'),('Kushaal Wadhwani','Bowler','Rs 20,00,000'),('Akshay Wakhare','Bowler','Rs 20,00,000'),('Rajesh Bishnoi','Batsman','Rs 20,00,000'),('Abhimanyu Easwaran','Batsman','Rs 20,00,000'),('Rohan Kadam','Batsman','Rs 20,00,000'),('Amandeep Khare','Batsman','Rs 20,00,000'),('Mohammed Taha','Batsman','Rs 20,00,000'),('Tajinder Dhillon','All-Rounder','Rs 20,00,000'),('Pankaj Jaswal','All-Rounder','Rs 20,00,000'),('Khrievitso Kense','All-Rounder','Rs 20,00,000'),('Prerak Mankad','All-Rounder','Rs 20,00,000'),('Shams Mulani','All-Rounder','Rs 20,00,000'),('Ansh Patel','All-Rounder','Rs 20,00,000'),('Parth Sahani','All-Rounder','Rs 20,00,000'),('Ankit Sharma','All-Rounder','Rs 20,00,000'),('Dhruv Shorey','All-Rounder','Rs 20,00,000'),('Josh Inglis','Wicket Keeper','Rs 20,00,000'),('Aryan Juyal','Wicket Keeper','Rs 20,00,000'),('Rohit Sharma','Wicket Keeper','Rs 20,00,000'),('Sandeep Kumar Tomar','Wicket Keeper','Rs 20,00,000'),('Aniket Choudhary','Bowler','Rs 20,00,000'),('Mukesh Choudhary','Bowler','Rs 20,00,000'),('Nathan Ellis','Bowler','Rs 20,00,000'),('Sayan Ghosh','Bowler','Rs 20,00,000'),('Ronit More','Bowler','Rs 20,00,000'),('Simarjeet Singh','Bowler','Rs 20,00,000'),('Zeeshan Ansari','Bowler','Rs 20,00,000'),('Nayan Doshi','Bowler','Rs 20,00,000'),('Jon Russ Jaggesar','Bowler','Rs 20,00,000'),('Kevin Koththigoda','Bowler','Rs 20,00,000'),('Tanveer Sangha','Bowler','Rs 20,00,000'),('Maheesh Theekshan','Bowler','Rs 20,00,000'),('Vijayakanth Viyaskanth','Bowler','Rs 20,00,000'),('Max Bryant','Batsman','Rs 20,00,000'),('Saahil Jain','Batsman','Rs 20,00,000'),('Subhranshu Senapati','Batsman','Rs 20,00,000'),('Ravi Thakur','Batsman','Rs 20,00,000'),('Jake Weatherald','Batsman','Rs 20,00,000'),('Shubham Agrawal','All-Rounder','Rs 20,00,000'),('Rajjakuddin Ahmed','All-Rounder','Rs 20,00,000'),('Baba Aparajith','All-Rounder','Rs 20,00,000'),('George Garton','All-Rounder','Rs 20,00,000'),('Kartik Kakade','All-Rounder','Rs 20,00,000'),('Shoaib Khan','All-Rounder','Rs 20,00,000'),('Dhruv Patel','All-Rounder','Rs 20,00,000'),('Latest Kumar Patel','All-Rounder','Rs 20,00,000'),('Varun Choudhary','Bowler','Rs 20,00,000'),('Baltej Dhanda','Bowler','Rs 20,00,000'),('Saurabh Dubey','Bowler','Rs 20,00,000'),('Matt Kelly','Bowler','Rs 20,00,000'),('Chama Milind','Bowler','Rs 20,00,000');
/*!40000 ALTER TABLE `aucunsold2021` ENABLE KEYS */;
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