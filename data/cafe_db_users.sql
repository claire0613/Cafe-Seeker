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
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `user_id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `pwd_hash` varchar(255) NOT NULL,
  `avatar` varchar(255) DEFAULT 'https://d2ltlh9sj9r3jz.cloudfront.net/cafe-seeker/images/user.png',
  `verify` tinyint(1) DEFAULT '0',
  `identity` int DEFAULT NULL,
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `email` (`email`),
  KEY `email_name_index` (`email`,`username`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'root','root@gmail.com','pbkdf2:sha256:260000$iKyOuoiGQPQGwKgV$78162e4080531f674cf35ec5617e11c28b3d010910b4640379e1a97e5e1b6b66','https://d2ltlh9sj9r3jz.cloudfront.net/cafe-seeker/images/user.png',0,NULL),(2,'cowork','cowork@gmail.com','pbkdf2:sha256:260000$KhiqnS3FYJaNiSqn$e2e89921cb476cdbe321e06b0d4a53922dfff9d6f1edbecdc055ab152609518b','https://d2ltlh9sj9r3jz.cloudfront.net/cafe-seeker/images/user.png',0,NULL),(3,'nomad','nomad@gmail.com','pbkdf2:sha256:260000$eUqJsEBQOcp4x6dd$cf328010ec7451b21c49749ddd33d6f44ae3788a2ffe3bf5120fc89f350c61d2','https://d2ltlh9sj9r3jz.cloudfront.net/cafe-seeker/images/user.png',0,NULL),(4,'test1','test1@gmail.com','pbkdf2:sha256:260000$jWv47IRzhaG8XH9q$2ae82060a03f42140cd45b579646b0889ec771da19af71a6b80e3942febc2471','https://d2ltlh9sj9r3jz.cloudfront.net/cafe-seeker/images/user.png',0,NULL),(5,'test2','test2@gmail.com','pbkdf2:sha256:260000$LBaT5x91XSNtyvIR$9487204ca2717d307964c063648e161cb369418b7e2e0c335edb85f5cd5a6906','https://d2ltlh9sj9r3jz.cloudfront.net/cafe-seeker/images/user.png',0,NULL),(6,'test3','test3@gmail.com','pbkdf2:sha256:260000$nlqhpWpQf9xW6ANe$bc8cc30c04e59128256cb3d491e539bc4e10b9ea0dca95e969a17a262e81315e','https://d2ltlh9sj9r3jz.cloudfront.net/cafe-seeker/images/user.png',0,NULL),(7,'test4','test4@gmail.com','pbkdf2:sha256:260000$scL4HGjMc9yiP69O$7dafa056a686dc2d7c89ff656911beec82834badd1e4800fa045429705e85453','https://d2ltlh9sj9r3jz.cloudfront.net/cafe-seeker/images/user.png',0,NULL);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-06-06 12:34:49
