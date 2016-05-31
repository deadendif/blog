-- MySQL dump 10.13  Distrib 5.5.49, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: deadend
-- ------------------------------------------------------
-- Server version	5.5.49-0ubuntu0.14.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `about_email`
--

DROP TABLE IF EXISTS `about_email`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `about_email` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `topic` varchar(128) NOT NULL,
  `name` varchar(32) NOT NULL,
  `address` varchar(254) NOT NULL,
  `content` longtext NOT NULL,
  `ip` varchar(64) DEFAULT NULL,
  `ua` varchar(1024) DEFAULT NULL,
  `send_time` datetime NOT NULL,
  `success` tinyint(1) NOT NULL,
  `is_spam` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `about_email`
--

LOCK TABLES `about_email` WRITE;
/*!40000 ALTER TABLE `about_email` DISABLE KEYS */;
/*!40000 ALTER TABLE `about_email` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group__permission_id_1f49ccbbdc69d2fc_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_group__permission_id_1f49ccbbdc69d2fc_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permission_group_id_689710a9a73b7457_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  CONSTRAINT `auth__content_type_id_508cf46651277a81_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=46 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add tag',7,'add_tag'),(20,'Can change tag',7,'change_tag'),(21,'Can delete tag',7,'delete_tag'),(22,'Can add tagged item',8,'add_taggeditem'),(23,'Can change tagged item',8,'change_taggeditem'),(24,'Can delete tagged item',8,'delete_taggeditem'),(25,'Can add user',9,'add_author'),(26,'Can change user',9,'change_author'),(27,'Can delete user',9,'delete_author'),(28,'Can add category',10,'add_category'),(29,'Can change category',10,'change_category'),(30,'Can delete category',10,'delete_category'),(31,'Can add entry',11,'add_entry'),(32,'Can change entry',11,'change_entry'),(33,'Can delete entry',11,'delete_entry'),(34,'Can add image',12,'add_image'),(35,'Can change image',12,'change_image'),(36,'Can delete image',12,'delete_image'),(37,'Can add site',13,'add_site'),(38,'Can change site',13,'change_site'),(39,'Can delete site',13,'delete_site'),(40,'Can add entry counter',14,'add_entrycounter'),(41,'Can change entry counter',14,'change_entrycounter'),(42,'Can delete entry counter',14,'delete_entrycounter'),(43,'Can add email',15,'add_email'),(44,'Can change email',15,'change_email'),(45,'Can delete email',15,'delete_email');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) DEFAULT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$20000$jGfpEfcDWEGO$xOC306JiIrPc/59qB22Z9bgZMWKUqj8bVhdsdg6zdqo=','2016-05-31 20:24:46',1,'daybyday','','','deadend.endif@gmail.com',1,1,'2016-05-31 20:24:43'),(2,'1qaz@WSX',NULL,0,'deadend','','','deadend.endif@gmail.com',0,1,'2016-05-31 20:35:00');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_33ac548dcf5f8e37_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_33ac548dcf5f8e37_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_4b5ed4ffdb8fd9b0_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_u_permission_id_384b62483d7071f0_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_user_u_permission_id_384b62483d7071f0_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissi_user_id_7f0938558328534a_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `blog_author`
--

DROP TABLE IF EXISTS `blog_author`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `blog_author` (
  `user_ptr_id` int(11) NOT NULL,
  PRIMARY KEY (`user_ptr_id`),
  CONSTRAINT `blog_author_user_ptr_id_c1b751042a6ae71_fk_auth_user_id` FOREIGN KEY (`user_ptr_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blog_author`
--

LOCK TABLES `blog_author` WRITE;
/*!40000 ALTER TABLE `blog_author` DISABLE KEYS */;
INSERT INTO `blog_author` VALUES (2);
/*!40000 ALTER TABLE `blog_author` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `blog_category`
--

DROP TABLE IF EXISTS `blog_category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `blog_category` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `slug` varchar(255) NOT NULL,
  `description` longtext NOT NULL,
  `lft` int(10) unsigned NOT NULL,
  `rght` int(10) unsigned NOT NULL,
  `tree_id` int(10) unsigned NOT NULL,
  `level` int(10) unsigned NOT NULL,
  `parent_id` int(11) DEFAULT NULL,
  `weight` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `slug` (`slug`),
  KEY `blog_category_caf7cc51` (`lft`),
  KEY `blog_category_3cfbd988` (`rght`),
  KEY `blog_category_656442a0` (`tree_id`),
  KEY `blog_category_c9e9a848` (`level`),
  KEY `blog_category_6be37982` (`parent_id`),
  CONSTRAINT `blog_category_parent_id_9319425f5a9536a_fk_blog_category_id` FOREIGN KEY (`parent_id`) REFERENCES `blog_category` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blog_category`
--

LOCK TABLES `blog_category` WRITE;
/*!40000 ALTER TABLE `blog_category` DISABLE KEYS */;
INSERT INTO `blog_category` VALUES (1,'Linux','linux','Knowledge about linux.',1,2,1,0,NULL,2),(2,'编程语言','programming-language','Knowledge about programming language.',1,2,4,0,NULL,1),(3,'大数据','big-data','Knowledge about big data.',1,2,3,0,NULL,3),(4,'其他','others','Other Knowledege.',1,2,2,0,NULL,4);
/*!40000 ALTER TABLE `blog_category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `blog_entry`
--

DROP TABLE IF EXISTS `blog_entry`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `blog_entry` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `slug` varchar(255) NOT NULL,
  `status` int(11) NOT NULL,
  `create_time` datetime NOT NULL,
  `start_publish` datetime DEFAULT NULL,
  `end_publish` datetime DEFAULT NULL,
  `last_update` datetime NOT NULL,
  `excerpt` longtext NOT NULL,
  `content` longtext NOT NULL,
  `featured` tinyint(1) NOT NULL,
  `tags` varchar(255) NOT NULL,
  `login_required` tinyint(1) NOT NULL,
  `password` varchar(64) NOT NULL,
  `detail_template` varchar(255) NOT NULL,
  `author_id` int(11) DEFAULT NULL,
  `category_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `blog_entry_author_id_6548b6ad62a06256_fk_blog_author_user_ptr_id` (`author_id`),
  KEY `blog_entry_category_id_55ddfd490ea94d47_fk_blog_category_id` (`category_id`),
  KEY `blog_entry_2dbcba41` (`slug`),
  KEY `blog_entry_9acb4454` (`status`),
  KEY `blog_entry_b16a6265` (`create_time`),
  KEY `blog_entry_da306df2` (`start_publish`),
  KEY `blog_entry_6c2cab93` (`end_publish`),
  CONSTRAINT `blog_entry_author_id_6548b6ad62a06256_fk_blog_author_user_ptr_id` FOREIGN KEY (`author_id`) REFERENCES `blog_author` (`user_ptr_id`),
  CONSTRAINT `blog_entry_category_id_55ddfd490ea94d47_fk_blog_category_id` FOREIGN KEY (`category_id`) REFERENCES `blog_category` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blog_entry`
--

LOCK TABLES `blog_entry` WRITE;
/*!40000 ALTER TABLE `blog_entry` DISABLE KEYS */;
INSERT INTO `blog_entry` VALUES (1,'Markdown入门','markdown-tutorial',3,'2016-05-31 20:36:00',NULL,NULL,'2016-05-31 20:58:04','markdown的基本语法，涉及了标题、引用、列表、代码块、内嵌代码、水平分割线、文本样式、图片、转义等方面。','### 简介\r\n+ 标记语言，简介明了，易于学习\r\n+ 兼容Html，但Html标签内的Markdown语法无效\r\n\r\n### 语法\r\n\r\n#### 1. 标题\r\n+ h1 : # h1 \r\n+ h2 : ## h2\r\n+ h3 : ### h3\r\n+ h4 : #### h4\r\n+ h5 : ##### h5\r\n+ h6 : ###### h6\r\n\r\n#### 2. 引用\r\n**注意：Markdown不支持首行缩进，比较low的方法可以在行首插入 `&emsp;`**   \r\n**格式**： > 引用内容  \r\n\\> &amp;emsp;&amp;emsp;时维九月，序属三秋。潦水尽而寒潭清，烟光凝而暮山紫。俨骖騑于上路，访风景于崇阿。临帝子之长洲，得仙人之旧馆。层峦耸翠，上出重霄；飞阁流丹，下临无地。鹤汀凫渚，穷岛屿之萦回；桂殿兰宫，即冈峦之体势。  \r\n\\> &amp;emsp;&amp;emsp;披绣闼，俯雕甍，山原旷其盈视，川泽纡其骇瞩。闾阎扑地，钟鸣鼎食之家；舸舰迷津，青雀黄龙之舳。云销雨霁，彩彻区明。落霞与孤鹜齐飞，秋水共长天一色。渔舟唱晚，响穷彭蠡之滨，雁阵惊寒，声断衡阳之浦。\r\n\r\n**显示结果：**  \r\n> &emsp;&emsp;时维九月，序属三秋。潦水尽而寒潭清，烟光凝而暮山紫。俨骖騑于上路，访风景于崇阿。临帝子之长洲，得仙人之旧馆。层峦耸翠，上出重霄；飞阁流丹，下临无地。鹤汀凫渚，穷岛屿之萦回；桂殿兰宫，即冈峦之体势。  \r\n> &emsp;&emsp;披绣闼，俯雕甍，山原旷其盈视，川泽纡其骇瞩。闾阎扑地，钟鸣鼎食之家；舸舰迷津，青雀黄龙之舳。云销雨霁，彩彻区明。落霞与孤鹜齐飞，秋水共长天一色。渔舟唱晚，响穷彭蠡之滨，雁阵惊寒，声断衡阳之浦。\r\n\r\n#### 3. 列表\r\n+ 无序列表\r\n    使用加号、减号、星号均可  \r\n    \\+ ul1  \r\n    \\+ ul2  \r\n    \\+ ul3  \r\n\r\n+ 有序列表\r\n    使用数字+英文句号，数字可以随便写，最终输出总是1,2,3...  \r\n    1\\. ol1  \r\n    2\\. ol2  \r\n    3\\. ol3  \r\n\r\n#### 4. 代码块\r\n* **格式**\r\n    * 代码整体缩进四个空格或一个tab键\r\n    * 代码块前后分别添加3个反引号(```)  \r\n\r\n**显示结果：**  \r\n\r\n    def hello(namelist):\r\n        hellolist = {}\r\n        for name in namelist:\r\n            hellolist[name] = \"hello, %s\" % name\r\n        return hellolist\r\n\r\n\r\n#### 5. 内嵌代码\r\n**格式**：\\`内嵌代码\\`，即用反义号（\\`）内嵌代码包起来  \r\n如：这是\\`hello\\`函数  \r\n**显示结果：**  \r\n这是`hello`函数\r\n\r\n#### 6. 水平分隔线\r\n**格式**：同一行中使用三个及以上的星号、下划线、减号  \r\n\\*\\*\\*\\*\\*\\*\\*\\*\\*\\*\\*  \r\n\\- \\- \\- \\- \\- \\- \\- \\-  \r\n**注意：使用连续的减号做水平分割线时要保证上一行为空行，因为连续的减号对应h2标签的样式**  \r\n**显示结果：**  \r\n************\r\n\r\n#### 7. 文本样式\r\n+ **链接**  \r\n    **格式**：\\[name\\]\\(url\\) 或 \\[name\\]\\(url  title)，如 Here is \\[my blog\\]\\(http://www.deadend.me \"my blog\"\\).   \r\n    **显示结果**：Here is [my blog](http://www.deadend.me \"my blog\")\r\n+ **加粗**  \r\n    **格式**：\\*\\*内容\\*\\* （星号与加粗字体间不能有空格），如 \\*\\*blog\\*\\*  \r\n    **显示结果**：**blog**  \r\n+ **斜体**  \r\n    **格式**：\\*内容\\* （星号与斜体内容间不能有空格），如 \\*blog\\*  \r\n    **显示结果**：*blog*\r\n+ **段落**  \r\n    **格式**：段落之间空一行  \r\n\r\n####  8. 图片\r\n格式：!\\[Alt text\\]\\(url \"可选标题名称\"\\)  \r\n如：\\!\\[程序猿\\]\\(https://fighting.deadend.me/media/images/2016/05/31/9216d0f6-48c8-4c03-b846-33822c72837d.png \"programmer\"\\)  \r\n\r\n![程序猿](https://fighting.deadend.me/media/images/2016/05/31/9216d0f6-48c8-4c03-b846-33822c72837d.png \"programmer\")\r\n\r\n#### 9. 转义\r\n下列符号前添加反斜杠（\\）可进行转义  \r\n\r\n+ \\   反斜线\r\n+ `   反引号\r\n+ \\*   星号\r\n+ _   下划线\r\n+ {}  花括号\r\n+ []  方括号\r\n+ ()  括弧\r\n+ \\#   井号\r\n+ \\+   加号\r\n+ \\-   减号\r\n+ .   英文句点\r\n+ !   惊叹号\r\n\r\n**注意：若要输出`&`符号，可在文件中输入&amp;amp;**   ',0,'markdown',0,'','default',2,2);
/*!40000 ALTER TABLE `blog_entry` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `blog_entrycounter`
--

DROP TABLE IF EXISTS `blog_entrycounter`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `blog_entrycounter` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `page_view_num` int(11) NOT NULL,
  `useful_num` int(11) NOT NULL,
  `useless_num` int(11) NOT NULL,
  `entry_id` int(11),
  PRIMARY KEY (`id`),
  UNIQUE KEY `entry_id` (`entry_id`),
  CONSTRAINT `blog_entrycounter_entry_id_12ff41df06f35623_fk_blog_entry_id` FOREIGN KEY (`entry_id`) REFERENCES `blog_entry` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blog_entrycounter`
--

LOCK TABLES `blog_entrycounter` WRITE;
/*!40000 ALTER TABLE `blog_entrycounter` DISABLE KEYS */;
INSERT INTO `blog_entrycounter` VALUES (1,0,0,0,1);
/*!40000 ALTER TABLE `blog_entrycounter` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `blog_image`
--

DROP TABLE IF EXISTS `blog_image`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `blog_image` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `caption` longtext,
  `image` varchar(100) NOT NULL,
  `entry_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `blog_image_entry_id_13064d00251a7517_fk_blog_entry_id` (`entry_id`),
  CONSTRAINT `blog_image_entry_id_13064d00251a7517_fk_blog_entry_id` FOREIGN KEY (`entry_id`) REFERENCES `blog_entry` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blog_image`
--

LOCK TABLES `blog_image` WRITE;
/*!40000 ALTER TABLE `blog_image` DISABLE KEYS */;
INSERT INTO `blog_image` VALUES (1,'Markdown图片示例','images/2016/05/31/9216d0f6-48c8-4c03-b846-33822c72837d.png',1);
/*!40000 ALTER TABLE `blog_image` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `blog_site`
--

DROP TABLE IF EXISTS `blog_site`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `blog_site` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `url` varchar(255) NOT NULL,
  `added_time` datetime NOT NULL,
  `is_visible` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blog_site`
--

LOCK TABLES `blog_site` WRITE;
/*!40000 ALTER TABLE `blog_site` DISABLE KEYS */;
INSERT INTO `blog_site` VALUES (1,'armsword的涅槃之地','http://armsword.com/','2016-05-31 20:43:00',1);
/*!40000 ALTER TABLE `blog_site` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `djang_content_type_id_697914295151027a_fk_django_content_type_id` (`content_type_id`),
  KEY `django_admin_log_user_id_52fdd58701c5f563_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_user_id_52fdd58701c5f563_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `djang_content_type_id_697914295151027a_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2016-05-31 20:25:07','1','Linux: linux',1,'',10,1),(2,'2016-05-31 20:25:19','2','编程语言: programming-language',1,'',10,1),(3,'2016-05-31 20:26:04','3','大数据: big-data',1,'',10,1),(4,'2016-05-31 20:26:19','4','其他: others',1,'',10,1),(5,'2016-05-31 20:27:33','2','编程语言: programming-language',2,'已修改 description 。',10,1),(6,'2016-05-31 20:27:52','2','编程语言: programming-language',2,'已修改 weight 。',10,1),(7,'2016-05-31 20:27:56','1','Linux: linux',2,'已修改 weight 。',10,1),(8,'2016-05-31 20:28:00','3','大数据: big-data',2,'已修改 weight 。',10,1),(9,'2016-05-31 20:28:04','4','其他: others',2,'已修改 weight 。',10,1),(10,'2016-05-31 20:36:26','2','deadend',1,'',9,1),(11,'2016-05-31 20:37:41','1','Markdown入门: published',1,'',11,1),(12,'2016-05-31 20:43:08','1','armsword的涅槃之地',1,'',13,1),(13,'2016-05-31 20:47:06','1','Markdown入门: Markdown图片示例',1,'',12,1),(14,'2016-05-31 20:49:17','1','Markdown入门: published',2,'已修改 content 。',11,1),(15,'2016-05-31 20:49:33','1','Markdown入门: published',2,'已修改 content 。',11,1),(16,'2016-05-31 20:50:00','1','Markdown入门: published',2,'已修改 content 。',11,1),(17,'2016-05-31 20:50:26','1','Markdown入门: published',2,'已修改 content 。',11,1),(18,'2016-05-31 20:53:35','1','Markdown入门: published',2,'已修改 content 。',11,1),(19,'2016-05-31 20:58:04','1','Markdown入门: published',2,'已修改 content 。',11,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_45f3b1d93ec8c61c_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (15,'about','email'),(1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(9,'blog','author'),(10,'blog','category'),(11,'blog','entry'),(14,'blog','entrycounter'),(12,'blog','image'),(13,'blog','site'),(5,'contenttypes','contenttype'),(6,'sessions','session'),(7,'tagging','tag'),(8,'tagging','taggeditem');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'about','0001_initial','2016-05-31 20:24:02'),(2,'about','0002_auto_20160520_1519','2016-05-31 20:24:02'),(3,'about','0003_auto_20160520_2116','2016-05-31 20:24:02'),(4,'about','0004_auto_20160520_2117','2016-05-31 20:24:02'),(5,'about','0005_auto_20160520_2118','2016-05-31 20:24:02'),(6,'contenttypes','0001_initial','2016-05-31 20:24:02'),(7,'auth','0001_initial','2016-05-31 20:24:03'),(8,'admin','0001_initial','2016-05-31 20:24:03'),(9,'contenttypes','0002_remove_content_type_name','2016-05-31 20:24:03'),(10,'auth','0002_alter_permission_name_max_length','2016-05-31 20:24:03'),(11,'auth','0003_alter_user_email_max_length','2016-05-31 20:24:03'),(12,'auth','0004_alter_user_username_opts','2016-05-31 20:24:03'),(13,'auth','0005_alter_user_last_login_null','2016-05-31 20:24:03'),(14,'auth','0006_require_contenttypes_0002','2016-05-31 20:24:03'),(15,'blog','0001_initial','2016-05-31 20:24:04'),(16,'blog','0002_site','2016-05-31 20:24:04'),(17,'blog','0003_auto_20160508_1011','2016-05-31 20:24:04'),(18,'blog','0004_auto_20160512_2333','2016-05-31 20:24:04'),(19,'blog','0005_auto_20160513_0016','2016-05-31 20:24:04'),(20,'blog','0006_auto_20160513_0034','2016-05-31 20:24:04'),(21,'blog','0007_entrycounter_entry','2016-05-31 20:24:04'),(22,'blog','0008_email','2016-05-31 20:24:04'),(23,'blog','0009_auto_20160518_1509','2016-05-31 20:24:04'),(24,'blog','0010_auto_20160518_1510','2016-05-31 20:24:04'),(25,'blog','0011_delete_email','2016-05-31 20:24:04'),(26,'blog','0012_category_weight','2016-05-31 20:24:05'),(27,'sessions','0001_initial','2016-05-31 20:24:05'),(28,'tagging','0001_initial','2016-05-31 20:24:05');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('qpaui3223t52gxti4dnxq9k7yw7so4cj','YjVhYzVkMmQxZWIyNjZmOGM4NTZmNzI2MzRhODg4ZDVmMTcyZjdmZjp7Il9hdXRoX3VzZXJfaGFzaCI6IjI3ODQ3YzRhZDI1OTMxMDllNmNjNTM2ZWU0Yzk2ODgyZTNmYTljNGIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2016-06-14 20:24:46');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tagging_tag`
--

DROP TABLE IF EXISTS `tagging_tag`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tagging_tag` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tagging_tag`
--

LOCK TABLES `tagging_tag` WRITE;
/*!40000 ALTER TABLE `tagging_tag` DISABLE KEYS */;
INSERT INTO `tagging_tag` VALUES (1,'markdown');
/*!40000 ALTER TABLE `tagging_tag` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tagging_taggeditem`
--

DROP TABLE IF EXISTS `tagging_taggeditem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tagging_taggeditem` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `object_id` int(10) unsigned NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `tag_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `tagging_taggeditem_tag_id_2ccbe9f5fed37043_uniq` (`tag_id`,`content_type_id`,`object_id`),
  KEY `taggi_content_type_id_716a325781ea128d_fk_django_content_type_id` (`content_type_id`),
  KEY `tagging_taggeditem_af31437c` (`object_id`),
  CONSTRAINT `tagging_taggeditem_tag_id_7c6426178988e7e_fk_tagging_tag_id` FOREIGN KEY (`tag_id`) REFERENCES `tagging_tag` (`id`),
  CONSTRAINT `taggi_content_type_id_716a325781ea128d_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tagging_taggeditem`
--

LOCK TABLES `tagging_taggeditem` WRITE;
/*!40000 ALTER TABLE `tagging_taggeditem` DISABLE KEYS */;
INSERT INTO `tagging_taggeditem` VALUES (1,1,11,1);
/*!40000 ALTER TABLE `tagging_taggeditem` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-05-31 21:21:37
