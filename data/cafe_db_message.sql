-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: localhost    Database: cafe_db
-- ------------------------------------------------------
-- Server version	8.0.28

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
-- Table structure for table `message`
--

DROP TABLE IF EXISTS `message`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `message` (
  `msg_id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `cafe_id` int NOT NULL,
  `user_name` varchar(255) NOT NULL,
  `msg_content` text NOT NULL,
  `floor` int NOT NULL,
  `like_count` int NOT NULL DEFAULT '0',
  `create_time` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`msg_id`),
  KEY `user_id` (`user_id`),
  KEY `cafe_id` (`cafe_id`),
  CONSTRAINT `message_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`) ON DELETE CASCADE,
  CONSTRAINT `message_ibfk_2` FOREIGN KEY (`cafe_id`) REFERENCES `cafes` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `message`
--

LOCK TABLES `message` WRITE;
/*!40000 ALTER TABLE `message` DISABLE KEYS */;
INSERT INTO `message` VALUES (2,4,8,'test1','這間店東西不錯喔~~',1,0,'2022-06-12 00:58:54'),(3,9,217,'test6','這間店推推~尤其是蛋糕特別不錯!',1,1,'2022-06-13 02:33:47'),(4,4,1,'test1','咖啡餐點都蠻不錯的咖啡館~\n好喜歡喝得到香蕉的香蕉拿鐵',1,2,'2022-06-13 04:04:21'),(9,4,7,'test1','自家烘焙手沖義式咖啡香氣逼人',1,1,'2022-06-13 04:22:23'),(10,4,8,'test1','這間店除了咖啡、茶、手工蛋糕、輕食，還有日本生活器皿與自然風格雜貨喔',2,3,'2022-06-13 04:33:42'),(11,4,243,'test1','是一間結合美髮沙龍、咖啡廳、酒吧的好地方',1,2,'2022-06-13 04:37:22'),(12,4,293,'test1','品嚐專業咖啡與文學書籍的好地方',1,0,'2022-06-13 04:45:39'),(15,1,1,'claire','氣氛好，飲品種類很多~甜點也好吃有特色xD',2,0,'2022-06-16 21:59:56'),(17,1,6,'claire','食物用心 新鮮又好吃，CP值高',1,0,'2022-06-16 22:11:42'),(19,1,1801,'claire','咖啡蛋糕都不錯 ~還有貓咪可以看xD',1,1,'2022-06-17 01:46:40'),(20,1,2,'claire','覺得不錯喝~下次還想再來!',1,0,'2022-06-17 01:51:47'),(21,10,2,'test1','手沖咖啡很好喝，主食大部分都是辣的(韓式泡菜那種辣)，拌飯和兩款薄餅都好吃。',2,0,'2022-06-17 01:54:02'),(22,10,217,'Jerry','放鬆的好地方',2,0,'2022-06-17 03:16:24'),(23,10,312,'Jerry','咖啡就是順口❤️餐點新鮮美味又吃得飽',1,0,'2022-06-17 04:47:37');
/*!40000 ALTER TABLE `message` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-06-17  6:12:49
