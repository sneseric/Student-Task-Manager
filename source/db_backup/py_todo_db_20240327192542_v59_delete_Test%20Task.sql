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
INSERT INTO `completion_time` VALUES ('2024-02-01',6),('2024-02-02',5),('2024-02-03',5),('2024-02-04',6),('2024-02-05',4),('2024-02-06',2),('2024-02-07',3),('2024-02-08',3),('2024-02-09',3),('2024-02-10',3),('2024-02-11',2),('2024-02-12',1),('2024-02-13',1),('2024-02-14',0.33),('2024-02-19',0.33),('2024-02-20',0.29),('2024-02-21',0.29),('2024-02-28',0.4),('2024-03-06',1.73),('2024-03-11',3.13),('2024-03-12',2.87),('2024-03-27',2.87);
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
) ENGINE=InnoDB AUTO_INCREMENT=139 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `py_todo_items`
--

LOCK TABLES `py_todo_items` WRITE;
/*!40000 ALTER TABLE `py_todo_items` DISABLE KEYS */;
INSERT INTO `py_todo_items` VALUES (117,'\'; DROP TABLE py_todo_items; DELETE FROM py_todo_items WHERE task_id > 0;; ALTER TABLE py_todo_items ADD COLUMN SQL_INJECTION_TEST VARCHAR(255); INSERT INTO py_todo_items; DROP DATABASE py_todo_db; --','2023-12-31'),(118,'Test Task','2023-12-31'),(120,'\'; DROP TABLE py_todo_items; DELETE FROM py_todo_items WHERE task_id > 0;; ALTER TABLE py_todo_items ADD COLUMN SQL_INJECTION_TEST VARCHAR(255); INSERT INTO py_todo_items; DROP DATABASE py_todo_db; --','2023-12-31'),(121,'Test Task','2023-12-31'),(123,'\'; DROP TABLE py_todo_items; DELETE FROM py_todo_items WHERE task_id > 0; ALTER TABLE py_todo_items ADD COLUMN SQL_INJECTION_TEST VARCHAR(255); INSERT INTO py_todo_items; DROP DATABASE py_todo_db; --','2023-12-31'),(124,'Test Task','2023-12-31'),(126,'\'; DROP TABLE py_todo_items; DELETE FROM py_todo_items WHERE task_id > 0; ALTER TABLE py_todo_items ADD COLUMN SQL_INJECTION_TEST VARCHAR(255); DROP DATABASE py_todo_db; --','2023-12-31'),(127,'Test Task','2023-12-31'),(129,'\'; DROP TABLE py_todo_items; DELETE FROM py_todo_items WHERE task_id > 0; ALTER TABLE py_todo_items ADD COLUMN SQL_INJECTION_TEST; DROP DATABASE py_todo_db; --','2023-12-31'),(130,'Test Task','2023-12-31'),(132,'\'; DROP TABLE py_todo_items; DELETE FROM py_todo_items WHERE task_id > 0; ALTER TABLE py_todo_items ADD COLUMN SQL_INJECTION_TEST VARCHAR(255); DROP DATABASE py_todo_db; --','2023-12-31'),(133,'Test Task','2023-12-31'),(135,'\'; DROP TABLE py_todo_items; DELETE FROM py_todo_items WHERE task_id > 0; ALTER TABLE py_todo_items ADD COLUMN SQL_INJECTION_TEST; DROP DATABASE py_todo_db; --','2023-12-31'),(136,'Test Task','2023-12-31'),(138,'\'; DROP TABLE py_todo_items; DELETE FROM py_todo_items WHERE task_id > 0; ALTER TABLE py_todo_items ADD COLUMN SQL_INJECTION_TEST; DROP DATABASE py_todo_db; --','2023-12-31');
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
) ENGINE=InnoDB AUTO_INCREMENT=139 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `task_statistics`
--

LOCK TABLES `task_statistics` WRITE;
/*!40000 ALTER TABLE `task_statistics` DISABLE KEYS */;
INSERT INTO `task_statistics` (`id`, `task`, `date_added`, `date_completed`) VALUES (1,'task 1','2024-02-12','2024-02-13'),(2,'task 2','2024-02-12','2024-02-13'),(3,'task 3','2024-02-12','2024-02-12'),(4,'task 4','2024-02-13','2024-02-13'),(5,'task 5','2024-02-13','2024-02-13'),(6,'task 6','2024-02-13','2024-02-13'),(7,'task 7','2024-02-13','2024-02-28'),(8,'task 8','2024-02-13','2024-03-27'),(9,'task 9','2024-02-13','2024-03-27'),(10,'task 10','2024-02-19','2024-02-19'),(11,'new 1','2024-02-19','2024-02-21'),(12,'new 2','2024-02-21','2024-03-11'),(13,'new 3','2024-02-21','2024-03-06'),(14,'new 3','2024-02-21','2024-03-06'),(15,'new 3','2024-03-06','2024-03-06'),(16,'new 4','2024-03-06','2024-03-11'),(17,'Test Task','2024-03-06','2024-03-27'),(18,'Test Task for Deletion','2024-03-06','2024-03-27'),(19,'Test Task','2024-03-06','2024-03-27'),(20,'Test Task for Deletion','2024-03-06','2024-03-27'),(21,'Test Task','2024-03-06','2024-03-27'),(22,'Test Task for Deletion','2024-03-06','2024-03-27'),(23,'new 3.11.24','2024-03-11','2024-03-11'),(24,'new 3.11.24-2','2024-03-11','2024-03-11'),(25,'new311','2024-03-11','2024-03-27'),(26,'new311','2024-03-11','2024-03-27'),(27,'new311','2024-03-11','2024-03-27'),(28,'new311','2024-03-11','2024-03-27'),(29,'new312','2024-03-11','2024-03-11'),(30,'new312','2024-03-11','2024-03-11'),(31,'new task 311','2024-03-11','2024-03-11'),(32,'g','2024-03-11','2024-03-11'),(33,'a','2024-03-11','2024-03-27'),(34,'Added Task','2024-03-11','2024-03-11'),(35,'new 3-12','2024-03-12','2024-03-27'),(36,'Test Task','2024-03-27','2024-03-27'),(37,'Test Task for Deletion','2024-03-27','2024-03-27'),(38,'\'; DROP TABLE py_todo_items; --','2024-03-27','2024-03-27'),(39,'Test Task','2024-03-27','2024-03-27'),(40,'Test Task for Deletion','2024-03-27','2024-03-27'),(41,'\'; DROP TABLE py_todo_items;','2024-03-27','2024-03-27'),(42,'Test Task','2024-03-27','2024-03-27'),(43,'Test Task for Deletion','2024-03-27','2024-03-27'),(44,'\'; DROP TABLE py_todo_items; --','2024-03-27','2024-03-27'),(45,'Test Task','2024-03-27','2024-03-27'),(46,'Test Task for Deletion','2024-03-27','2024-03-27'),(47,'Test Task','2024-03-27','2024-03-27'),(48,'Test Task for Deletion','2024-03-27','2024-03-27'),(49,'\'; DROP TABLE py_todo_items; --','2024-03-27','2024-03-27'),(50,'Test Task','2024-03-27','2024-03-27'),(51,'Test Task for Deletion','2024-03-27','2024-03-27'),(52,'\'; DROP TABLE py_todo_items; --','2024-03-27','2024-03-27'),(53,'Test Task','2024-03-27','2024-03-27'),(54,'Test Task for Deletion','2024-03-27','2024-03-27'),(55,'\'; DROP TABLE py_todo_items; DELETE FROM py_todo_items; INSERT INTO py_todo_items; DROP DATABASE py_todo_db; --','2024-03-27','2024-03-27'),(56,'Test Task','2024-03-27','2024-03-27'),(57,'Test Task for Deletion','2024-03-27','2024-03-27'),(58,'Test Task','2024-03-27','2024-03-27'),(59,'Test Task for Deletion','2024-03-27','2024-03-27'),(60,'\'; DROP TABLE py_todo_items; DELETE FROM py_todo_items; INSERT INTO py_todo_items; DROP DATABASE py_todo_db; --','2024-03-27','2024-03-27'),(61,'Test Task','2024-03-27','2024-03-27'),(62,'Test Task','2024-03-27','2024-03-27'),(63,'Test Task for Deletion','2024-03-27','2024-03-27'),(64,'\'; DROP TABLE py_todo_items; DELETE FROM py_todo_items; INSERT INTO py_todo_items; DROP DATABASE py_todo_db; --','2024-03-27','2024-03-27'),(65,'Test Task','2024-03-27','2024-03-27'),(66,'Test Task for Deletion','2024-03-27','2024-03-27'),(67,'\'; DROP TABLE py_todo_items; DELETE FROM py_todo_items; INSERT INTO py_todo_items; DROP DATABASE py_todo_db; --','2024-03-27','2024-03-27'),(68,'Test Task','2024-03-27','2024-03-27'),(69,'Test Task for Deletion','2024-03-27','2024-03-27'),(70,'\'; DROP TABLE py_todo_items; DELETE FROM py_todo_items; INSERT INTO py_todo_items; DROP DATABASE py_todo_db; --','2024-03-27','2024-03-27'),(71,'test 1','2024-03-27','2024-03-27'),(72,'Test Task','2024-03-27','2024-03-27'),(73,'Test Task for Deletion','2024-03-27','2024-03-27'),(74,'\'; DROP TABLE py_todo_items; DELETE FROM py_todo_items; INSERT INTO py_todo_items; DROP DATABASE py_todo_db; --','2024-03-27','2024-03-27'),(75,'Test Task','2024-03-27','2024-03-27'),(76,'Test Task for Deletion','2024-03-27','2024-03-27'),(77,'Test Task','2024-03-27','2024-03-27'),(78,'Test Task for Deletion','2024-03-27','2024-03-27'),(79,'\'; DROP TABLE py_todo_items; DELETE FROM py_todo_items; INSERT INTO py_todo_items; DROP DATABASE py_todo_db; --','2024-03-27','2024-03-27'),(80,'Test Task','2024-03-27','2024-03-27'),(81,'Test Task for Deletion','2024-03-27','2024-03-27'),(82,'\'; DROP TABLE py_todo_items; DELETE FROM py_todo_items; INSERT INTO py_todo_items; DROP DATABASE py_todo_db; --','2024-03-27','2024-03-27'),(83,'test 3.27.24','2024-03-27','2024-03-27'),(84,'Test Task','2024-03-27','2024-03-27'),(85,'Test Task for Deletion','2024-03-27','2024-03-27'),(86,'\'; DROP TABLE py_todo_items; DELETE FROM py_todo_items; INSERT INTO py_todo_items; DROP DATABASE py_todo_db; --','2024-03-27','2024-03-27'),(87,'manual test 3.27.24','2024-03-27','2024-03-27'),(88,'Test Task','2024-03-27','2024-03-27'),(89,'Test Task for Deletion','2024-03-27','2024-03-27'),(90,'\'; DROP TABLE py_todo_items; DELETE FROM py_todo_items WHERE task_id > 0; INSERT INTO py_todo_items (task_name, due_date) VALUES (\'Complete homework\', \'2024-04-05\'); DROP DATABASE py_todo_db; --','2024-03-27','2024-03-27'),(91,'manaul test 3.27.24','2024-03-27','2024-03-27'),(92,'Test Task','2024-03-27','2024-03-27'),(93,'Test Task for Deletion','2024-03-27','2024-03-27'),(94,'\'; DROP TABLE py_todo_items; DELETE FROM py_todo_items WHERE task_id > 0; INSERT INTO py_todo_items (task_name, due_date) VALUES (\'Complete homework\', \'2024-04-05\'); DROP DATABASE py_todo_db; --','2024-03-27','2024-03-27'),(95,'Test Task','2024-03-27','2024-03-27'),(96,'Test Task for Deletion','2024-03-27','2024-03-27'),(97,'\'; DROP TABLE py_todo_items; DELETE FROM py_todo_items WHERE task_id > 0; ALTER TABLE py_todo_items ADD COLUMN SQL_INJECTION_TEST VARCHAR(255); DROP DATABASE py_todo_db; --','2024-03-27','2024-03-27'),(98,'Test Task','2024-03-27','2024-03-27'),(99,'Test Task for Deletion','2024-03-27','2024-03-27'),(100,'\'; DROP TABLE py_todo_items; DELETE FROM py_todo_items; INSERT INTO py_todo_items; DROP DATABASE py_todo_db; --','2024-03-27','2024-03-27'),(101,'Test Task','2024-03-27','2024-03-27'),(102,'Test Task for Deletion','2024-03-27','2024-03-27'),(103,'\'; DROP TABLE py_todo_items; DELETE FROM py_todo_items; ALTER TABLE py_todo_items ADD COLUMN SQL_INJECTION_TEST VARCHAR(255); INSERT INTO py_todo_items; DROP DATABASE py_todo_db; --','2024-03-27','2024-03-27'),(104,'Test Task','2024-03-27','2024-03-27'),(105,'Test Task for Deletion','2024-03-27','2024-03-27'),(106,'\'; DROP TABLE py_todo_items; DELETE FROM py_todo_items; ALTER TABLE py_todo_items ADD COLUMN SQL_INJECTION_TEST VARCHAR(255); INSERT INTO py_todo_items; DROP DATABASE py_todo_db; --','2024-03-27','2024-03-27'),(107,'manual test 3.27.24','2024-03-27','2024-03-27'),(108,'Test Task','2024-03-27','2024-03-27'),(109,'Test Task for Deletion','2024-03-27','2024-03-27'),(110,'\'; DROP TABLE py_todo_items; DELETE FROM py_todo_items; ALTER TABLE py_todo_items ADD COLUMN SQL_INJECTION_TEST VARCHAR(255); INSERT INTO py_todo_items; DROP DATABASE py_todo_db; --','2024-03-27','2024-03-27'),(111,'manual test 3.27.24','2024-03-27','2024-03-27'),(112,'Test Task','2024-03-27','2024-03-27'),(113,'Test Task for Deletion','2024-03-27','2024-03-27'),(114,'\'; DROP TABLE py_todo_items; DELETE FROM py_todo_items WHERE task_id > 0;; ALTER TABLE py_todo_items ADD COLUMN SQL_INJECTION_TEST VARCHAR(255); INSERT INTO py_todo_items; DROP DATABASE py_todo_db; --','2024-03-27','2024-03-27'),(115,'Test Task','2024-03-27','2024-03-27'),(116,'Test Task for Deletion','2024-03-27','2024-03-27'),(117,'\'; DROP TABLE py_todo_items; DELETE FROM py_todo_items WHERE task_id > 0;; ALTER TABLE py_todo_items ADD COLUMN SQL_INJECTION_TEST VARCHAR(255); INSERT INTO py_todo_items; DROP DATABASE py_todo_db; --','2024-03-27','2024-03-27'),(118,'Test Task','2024-03-27','2024-03-27'),(119,'Test Task for Deletion','2024-03-27','2024-03-27'),(120,'\'; DROP TABLE py_todo_items; DELETE FROM py_todo_items WHERE task_id > 0;; ALTER TABLE py_todo_items ADD COLUMN SQL_INJECTION_TEST VARCHAR(255); INSERT INTO py_todo_items; DROP DATABASE py_todo_db; --','2024-03-27','2024-03-27'),(121,'Test Task','2024-03-27','2024-03-27'),(122,'Test Task for Deletion','2024-03-27','2024-03-27'),(123,'\'; DROP TABLE py_todo_items; DELETE FROM py_todo_items WHERE task_id > 0; ALTER TABLE py_todo_items ADD COLUMN SQL_INJECTION_TEST VARCHAR(255); INSERT INTO py_todo_items; DROP DATABASE py_todo_db; --','2024-03-27',NULL),(124,'Test Task','2024-03-27','2024-03-27'),(125,'Test Task for Deletion','2024-03-27','2024-03-27'),(126,'\'; DROP TABLE py_todo_items; DELETE FROM py_todo_items WHERE task_id > 0; ALTER TABLE py_todo_items ADD COLUMN SQL_INJECTION_TEST VARCHAR(255); DROP DATABASE py_todo_db; --','2024-03-27',NULL),(127,'Test Task','2024-03-27','2024-03-27'),(128,'Test Task for Deletion','2024-03-27','2024-03-27'),(129,'\'; DROP TABLE py_todo_items; DELETE FROM py_todo_items WHERE task_id > 0; ALTER TABLE py_todo_items ADD COLUMN SQL_INJECTION_TEST; DROP DATABASE py_todo_db; --','2024-03-27',NULL),(130,'Test Task','2024-03-27','2024-03-27'),(131,'Test Task for Deletion','2024-03-27','2024-03-27'),(132,'\'; DROP TABLE py_todo_items; DELETE FROM py_todo_items WHERE task_id > 0; ALTER TABLE py_todo_items ADD COLUMN SQL_INJECTION_TEST VARCHAR(255); DROP DATABASE py_todo_db; --','2024-03-27',NULL),(133,'Test Task','2024-03-27','2024-03-27'),(134,'Test Task for Deletion','2024-03-27','2024-03-27'),(135,'\'; DROP TABLE py_todo_items; DELETE FROM py_todo_items WHERE task_id > 0; ALTER TABLE py_todo_items ADD COLUMN SQL_INJECTION_TEST; DROP DATABASE py_todo_db; --','2024-03-27',NULL),(136,'Test Task','2024-03-27','2024-03-27'),(137,'Test Task for Deletion','2024-03-27','2024-03-27'),(138,'\'; DROP TABLE py_todo_items; DELETE FROM py_todo_items WHERE task_id > 0; ALTER TABLE py_todo_items ADD COLUMN SQL_INJECTION_TEST; DROP DATABASE py_todo_db; --','2024-03-27',NULL);
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

-- Dump completed on 2024-03-27 19:25:42
