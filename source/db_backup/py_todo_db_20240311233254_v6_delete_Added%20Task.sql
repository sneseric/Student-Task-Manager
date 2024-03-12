-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: localhost    Database: py_todo_db
-- ------------------------------------------------------
-- Server version	8.0.31

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `completion_time`
--

DROP TABLE IF EXISTS `completion_time`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `completion_time` (
  `date` date DEFAULT NULL,
  `avg_completion_time` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `completion_time`
--

LOCK TABLES `completion_time` WRITE;
/*!40000 ALTER TABLE `completion_time` DISABLE KEYS */;
INSERT INTO `completion_time` VALUES ('2024-02-01',6),('2024-02-02',5),('2024-02-03',5),('2024-02-04',6),('2024-02-05',4),('2024-02-06',2),('2024-02-07',3),('2024-02-08',3),('2024-02-09',3),('2024-02-10',3),('2024-02-11',2),('2024-02-12',1),('2024-02-13',1),('2024-02-14',0.33),('2024-02-19',0.33),('2024-02-20',0.29),('2024-02-21',0.29),('2024-02-28',0.4),('2024-03-06',1.73),('2024-03-11',3.13);
/*!40000 ALTER TABLE `completion_time` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `notification_status`
--

DROP TABLE IF EXISTS `notification_status`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `notification_status` (
  `on` int DEFAULT NULL,
  `off` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `notification_status`
--

LOCK TABLES `notification_status` WRITE;
/*!40000 ALTER TABLE `notification_status` DISABLE KEYS */;
INSERT INTO `notification_status` VALUES (1,0);
/*!40000 ALTER TABLE `notification_status` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `py_todo_items`
--

DROP TABLE IF EXISTS `py_todo_items`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `py_todo_items` (
  `id` int NOT NULL AUTO_INCREMENT,
  `task` varchar(255) DEFAULT NULL,
  `due_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `py_todo_items`
--

LOCK TABLES `py_todo_items` WRITE;
/*!40000 ALTER TABLE `py_todo_items` DISABLE KEYS */;
INSERT INTO `py_todo_items` VALUES (8,'task 8','2024-02-14'),(9,'task 9','2024-02-13'),(28,'new311','2024-03-12'),(33,'a','2024-03-13');
/*!40000 ALTER TABLE `py_todo_items` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = cp850 */ ;
/*!50003 SET character_set_results = cp850 */ ;
/*!50003 SET collation_connection  = cp850_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `before_insert_py_todo_items` AFTER INSERT ON `py_todo_items` FOR EACH ROW BEGIN
    SET @today_date = CURDATE();
    INSERT INTO task_statistics (task, date_added)
    VALUES (NEW.task, @today_date);
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `task_statistics`
--

DROP TABLE IF EXISTS `task_statistics`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `task_statistics` (
  `id` int NOT NULL AUTO_INCREMENT,
  `task` varchar(255) DEFAULT NULL,
  `date_added` date DEFAULT NULL,
  `date_completed` date DEFAULT NULL,
  `completion_time` varchar(255) GENERATED ALWAYS AS (concat((to_days(`date_completed`) - to_days(`date_added`)),_cp850' days')) VIRTUAL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `task_statistics`
--

LOCK TABLES `task_statistics` WRITE;
/*!40000 ALTER TABLE `task_statistics` DISABLE KEYS */;
INSERT INTO `task_statistics` (`id`, `task`, `date_added`, `date_completed`) VALUES (1,'task 1','2024-02-12','2024-02-13'),(2,'task 2','2024-02-12','2024-02-13'),(3,'task 3','2024-02-12','2024-02-12'),(4,'task 4','2024-02-13','2024-02-13'),(5,'task 5','2024-02-13','2024-02-13'),(6,'task 6','2024-02-13','2024-02-13'),(7,'task 7','2024-02-13','2024-02-28'),(8,'task 8','2024-02-13',NULL),(9,'task 9','2024-02-13',NULL),(10,'task 10','2024-02-19','2024-02-19'),(11,'new 1','2024-02-19','2024-02-21'),(12,'new 2','2024-02-21','2024-03-11'),(13,'new 3','2024-02-21','2024-03-06'),(14,'new 3','2024-02-21','2024-03-06'),(15,'new 3','2024-03-06','2024-03-06'),(16,'new 4','2024-03-06','2024-03-11'),(17,'Test Task','2024-03-06','2024-03-11'),(18,'Test Task for Deletion','2024-03-06','2024-03-06'),(19,'Test Task','2024-03-06','2024-03-11'),(20,'Test Task for Deletion','2024-03-06','2024-03-06'),(21,'Test Task','2024-03-06','2024-03-11'),(22,'Test Task for Deletion','2024-03-06','2024-03-06'),(23,'new 3.11.24','2024-03-11','2024-03-11'),(24,'new 3.11.24-2','2024-03-11','2024-03-11'),(25,'new311','2024-03-11','2024-03-11'),(26,'new311','2024-03-11','2024-03-11'),(27,'new311','2024-03-11','2024-03-11'),(28,'new311','2024-03-11',NULL),(29,'new312','2024-03-11','2024-03-11'),(30,'new312','2024-03-11','2024-03-11'),(31,'new task 311','2024-03-11','2024-03-11'),(32,'g','2024-03-11','2024-03-11'),(33,'a','2024-03-11',NULL),(34,'Added Task','2024-03-11','2024-03-11');
/*!40000 ALTER TABLE `task_statistics` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = cp850 */ ;
/*!50003 SET character_set_results = cp850 */ ;
/*!50003 SET collation_connection  = cp850_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `after_update_task_statistics` AFTER UPDATE ON `task_statistics` FOR EACH ROW BEGIN
    IF OLD.date_added <> NEW.date_added THEN
        UPDATE py_todo_items
        SET date_added = NEW.date_added
        WHERE task = NEW.task;
    END IF;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-03-11 23:32:54
