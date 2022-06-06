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
-- Table structure for table `station_ref`
--

DROP TABLE IF EXISTS `station_ref`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `station_ref` (
  `station_id` int NOT NULL AUTO_INCREMENT,
  `station` varchar(255) NOT NULL,
  `station_tw` varchar(255) NOT NULL,
  PRIMARY KEY (`station_id`),
  UNIQUE KEY `station` (`station`)
) ENGINE=InnoDB AUTO_INCREMENT=114 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `station_ref`
--

LOCK TABLES `station_ref` WRITE;
/*!40000 ALTER TABLE `station_ref` DISABLE KEYS */;
INSERT INTO `station_ref` VALUES (1,'28 St','28 St'),(2,'2nd Ave','2nd Ave'),(3,'5 Avenue Bryant Park','5 Avenue Bryant Park'),(4,'5 Avenue-53 St','5 Avenue-53 St'),(5,'7 Avenue','7 Avenue'),(6,'Apgujeongrodeo','狎鷗亭羅德奧站'),(7,'Banqiao','板橋'),(8,'Bedford Av','Bedford Av'),(9,'Beimen','北門'),(10,'Bercy','Bercy'),(11,'Causeway Bay','Causeway Bay'),(12,'Central Park Station','中央公園'),(13,'Central','Central'),(14,'Chiang Kai-Shek Memorial Hall','中正紀念堂'),(15,'City Council','City Council'),(16,'Daan, Zhongxiao Fuxing','大安, 忠孝復興'),(17,'Daan','大安'),(18,'Daikanyama','代官山'),(19,'Dazhi','大直'),(20,'Dhoby Ghaut','Dhoby Ghaut'),(21,'Dongdaemun History & Culture Park','東大門與歷史文化公園站'),(22,'Dongmen','東門'),(23,'Dunhua','敦化'),(24,'Ebisu','惠比壽'),(25,'Far Eastern Hospital','亞東醫院'),(26,'Fuzhong','府中'),(27,'Gangnam','江南'),(28,'Ginza','銀座'),(29,'Gongdeok','孔德站'),(30,'Gongguan','公館'),(31,'Gotanda','五反田'),(32,'Guting','古亭'),(33,'Gwanghwamun','光化門站'),(34,'Hanzomon','半藏門'),(35,'Hapjeong','合井'),(36,'Harajuku','原宿'),(37,'Hongik University','弘益大學（弘大站）'),(38,'Houshanpi','後山埤'),(39,'Ikebukuro','池袋'),(40,'Jamsil','蠶室站'),(41,'Jiannan Rd','劍南路站'),(42,'Keelung','基隆'),(43,'Korakuen','後樂園'),(44,'Kunyang','昆陽'),(45,'Lai Chi Kok','荔枝角'),(46,'Linguang','麟光'),(47,'Liuzhangli','六張犁'),(48,'Mangwon','望遠站'),(49,'Marcy Av','Marcy Av'),(50,'Maubert - Mutualité','Maubert - Mutualité'),(51,'Meguro','目黑'),(52,'Minquan West Road','民權西'),(53,'Nagatacho, Akasaka-Mitsuke','永田町，赤坂見附'),(54,'Nagatacho','永田町'),(55,'Nangang Expo','南港展覽館'),(56,'Nangang Software Park','南港軟體園區'),(57,'Nangang','南港'),(58,'Nanjing Fuxing','南京復興'),(59,'Nanjing Sanmin','南京三民'),(60,'Nassau Avenue','Nassau Avenue'),(61,'Neihu','內湖'),(62,'Nogizaka, Roppongi','乃木坂，六本木'),(63,'North Point','North Point'),(64,'Prince Edward','Prince Edward'),(65,'Roppongi','六本木'),(66,'Sai Ying Pun','西營盤'),(67,'Samseong','三成站'),(68,'Sangsu','上水站'),(69,'Seoulleung','宣陵站'),(70,'Shandao Temple','善導寺'),(71,'Shanwai Bus Station','鳳雛公園'),(72,'Sheung Wan','上環站'),(73,'Shibuya, Harajuku','涉谷站，原宿'),(74,'Shibuya','涉谷站'),(75,'Shilin','士林'),(76,'Shin-Okubo, Seibu-Shinjuku, Higashi-Shinjuku','新久保, 西武新宿, 東新宿'),(77,'Shinjuku-sanchome','新宿三丁目'),(78,'Shinjuku','新宿'),(79,'Shuanglian','雙連'),(80,'Sizihwan','西子灣'),(81,'Songjiang Nanjing','松江南京'),(82,'Songshan','松山'),(83,'Suidobashi','水道橋'),(84,'Sun Yat-Sen Memorial Hall','國父紀念館'),(85,'Taipei 101/World Trade Center','Taipei 101/世貿中心'),(86,'Taipei Arena','台北小巨蛋'),(87,'Taipei City Hall','台北市政府'),(88,'Taipei Main','台北火車站'),(89,'Taipei Zoo','動物園'),(90,'Taipower Building','台電大樓'),(91,'Takadanobaba','高田馬場站'),(92,'Tamsui','淡水'),(93,'Technology Building','科技大樓'),(94,'Tokyo','東京'),(95,'Toucheng','頭城'),(96,'Ttukseom','纛島站'),(97,'Wai\'ao','外澳'),(98,'Wende','文德'),(99,'Xiangshan','象山'),(100,'Xihu','西湖'),(101,'Ximen','西門'),(102,'Xinyi Anhe','信義安和'),(103,'Yau Ma Tei','油麻地站'),(104,'Yongchun','永春'),(105,'York St','York St'),(106,'Yoyogi-koen','Yoyogi-koen'),(107,'Yuanshan','圓山'),(108,'Zhongshan Junior High School','中山國中'),(109,'Zhongshan','中山'),(110,'Zhongxiao Dunhua','忠孝敦化'),(111,'Zhongxiao Fuxing','忠孝復興'),(112,'Zhongxiao Xinsheng','忠孝新生'),(113,'Powell Street','Powell Street');
/*!40000 ALTER TABLE `station_ref` ENABLE KEYS */;
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
