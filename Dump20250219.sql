-- MySQL dump 10.13  Distrib 8.0.41, for Win64 (x86_64)
--
-- Host: localhost    Database: game_db
-- ------------------------------------------------------
-- Server version	8.0.41

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
-- Table structure for table `game_results`
--

DROP TABLE IF EXISTS game_results;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE game_results (
  id int NOT NULL AUTO_INCREMENT,
  player_choice varchar(50) DEFAULT NULL,
  computer_choice varchar(50) DEFAULT NULL,
  result varchar(50) DEFAULT NULL,
  `timestamp` timestamp(6) NULL DEFAULT NULL,
  PRIMARY KEY (id)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `game_results`
--

LOCK TABLES game_results WRITE;
/*!40000 ALTER TABLE game_results DISABLE KEYS */;
INSERT INTO game_results VALUES (1,'Paper','Paper','It\'s a Draw!',NULL),(2,'Rock','Scissors','You Win!',NULL),(3,'Scissors','Scissors','It\'s a Draw!',NULL),(4,'Rock','Rock','It\'s a Draw!',NULL),(5,'Paper','Paper','It\'s a Draw!',NULL),(6,'Paper','Paper','It\'s a Draw!',NULL),(7,'Paper','Scissors','You Lose!',NULL),(8,'Scissors','Scissors','It\'s a Draw!',NULL),(9,'Scissors','Scissors','It\'s a Draw!',NULL),(10,'Scissors','Scissors','It\'s a Draw!',NULL),(11,'Scissors','Scissors','It\'s a Draw!',NULL),(12,'Rock','Rock','It\'s a Draw!',NULL),(13,'Paper','Rock','You Win!',NULL),(14,'Scissors','Scissors','It\'s a Draw!',NULL),(15,'Rock','Paper','You Lose!',NULL),(16,'Paper','Paper','It\'s a Draw!',NULL),(17,'Scissors','Paper','You Win!',NULL);
/*!40000 ALTER TABLE game_results ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-02-19 17:38:32
