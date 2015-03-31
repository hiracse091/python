-- phpMyAdmin SQL Dump
-- version 4.0.4
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Mar 31, 2015 at 07:34 AM
-- Server version: 5.5.32
-- PHP Version: 5.4.16

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `kherokhata`
--
CREATE DATABASE IF NOT EXISTS `kherokhata` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `kherokhata`;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_0e939a4f` (`group_id`),
  KEY `auth_group_permissions_8373b171` (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_417f1b1c` (`content_type_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=64 ;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can add permission', 2, 'add_permission'),
(5, 'Can change permission', 2, 'change_permission'),
(6, 'Can delete permission', 2, 'delete_permission'),
(7, 'Can add group', 3, 'add_group'),
(8, 'Can change group', 3, 'change_group'),
(9, 'Can delete group', 3, 'delete_group'),
(10, 'Can add user', 4, 'add_user'),
(11, 'Can change user', 4, 'change_user'),
(12, 'Can delete user', 4, 'delete_user'),
(13, 'Can add content type', 5, 'add_contenttype'),
(14, 'Can change content type', 5, 'change_contenttype'),
(15, 'Can delete content type', 5, 'delete_contenttype'),
(16, 'Can add session', 6, 'add_session'),
(17, 'Can change session', 6, 'change_session'),
(18, 'Can delete session', 6, 'delete_session'),
(19, 'Can add user type', 7, 'add_usertype'),
(20, 'Can change user type', 7, 'change_usertype'),
(21, 'Can delete user type', 7, 'delete_usertype'),
(22, 'Can add user profile', 8, 'add_userprofile'),
(23, 'Can change user profile', 8, 'change_userprofile'),
(24, 'Can delete user profile', 8, 'delete_userprofile'),
(25, 'Can add project', 9, 'add_project'),
(26, 'Can change project', 9, 'change_project'),
(27, 'Can delete project', 9, 'delete_project'),
(28, 'Can add work area', 10, 'add_workarea'),
(29, 'Can change work area', 10, 'change_workarea'),
(30, 'Can delete work area', 10, 'delete_workarea'),
(31, 'Can add project document', 11, 'add_projectdocument'),
(32, 'Can change project document', 11, 'change_projectdocument'),
(33, 'Can delete project document', 11, 'delete_projectdocument'),
(34, 'Can add project user', 12, 'add_projectuser'),
(35, 'Can change project user', 12, 'change_projectuser'),
(36, 'Can delete project user', 12, 'delete_projectuser'),
(37, 'Can add project work area', 13, 'add_projectworkarea'),
(38, 'Can change project work area', 13, 'change_projectworkarea'),
(39, 'Can delete project work area', 13, 'delete_projectworkarea'),
(40, 'Can add module', 14, 'add_module'),
(41, 'Can change module', 14, 'change_module'),
(42, 'Can delete module', 14, 'delete_module'),
(43, 'Can add module user', 15, 'add_moduleuser'),
(44, 'Can change module user', 15, 'change_moduleuser'),
(45, 'Can delete module user', 15, 'delete_moduleuser'),
(46, 'Can add urgency', 16, 'add_urgency'),
(47, 'Can change urgency', 16, 'change_urgency'),
(48, 'Can delete urgency', 16, 'delete_urgency'),
(49, 'Can add task', 17, 'add_task'),
(50, 'Can change task', 17, 'change_task'),
(51, 'Can delete task', 17, 'delete_task'),
(52, 'Can add task user', 18, 'add_taskuser'),
(53, 'Can change task user', 18, 'change_taskuser'),
(54, 'Can delete task user', 18, 'delete_taskuser'),
(55, 'Can add task checklist', 19, 'add_taskchecklist'),
(56, 'Can change task checklist', 19, 'change_taskchecklist'),
(57, 'Can delete task checklist', 19, 'delete_taskchecklist'),
(58, 'Can add checklist item', 20, 'add_checklistitem'),
(59, 'Can change checklist item', 20, 'change_checklistitem'),
(60, 'Can delete checklist item', 20, 'delete_checklistitem'),
(61, 'Can add task time', 21, 'add_tasktime'),
(62, 'Can change task time', 21, 'change_tasktime'),
(63, 'Can delete task time', 21, 'delete_tasktime');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(75) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$12000$SKdXfc3qtiXU$XYLE4+gImLepy051JBqvg2H/NWsoshr4rzaahb8kg5E=', '2015-01-22 06:41:25', 1, 'admin', '', '', 'admin@dcastalia.com', 1, 1, '2015-01-22 06:06:25'),
(2, 'pbkdf2_sha256$12000$OpGRSgmVVR5d$neuQJAEBonseTt0MUKbAKYDYhdntLSRKq02tE34gmv8=', '2015-01-22 06:33:38', 0, 'Naher', '', '', '', 0, 1, '2015-01-22 06:19:27'),
(3, 'pbkdf2_sha256$12000$JuuM3UvzwdRt$H5LsAzDveZNXD71ZfZ3VpNjM71sJhD7PNsiCRe8oX+0=', '2015-01-22 06:22:29', 0, 'pavel', '', '', '', 0, 1, '2015-01-22 06:19:57');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_e8701ad4` (`user_id`),
  KEY `auth_user_groups_0e939a4f` (`group_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_e8701ad4` (`user_id`),
  KEY `auth_user_user_permissions_8373b171` (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_417f1b1c` (`content_type_id`),
  KEY `django_admin_log_e8701ad4` (`user_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=11 ;

--
-- Dumping data for table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2015-01-22 06:13:00', '1', 'UserType object', 1, '', 7, 1),
(2, '2015-01-22 06:16:42', '2', 'project manager', 1, '', 7, 1),
(3, '2015-01-22 06:17:10', '3', 'project member', 1, '', 7, 1),
(4, '2015-01-22 06:17:51', '1', 'admin', 1, '', 8, 1),
(5, '2015-01-22 06:19:27', '2', 'Naher', 1, '', 4, 1),
(6, '2015-01-22 06:19:36', '2', 'Naher', 2, 'No fields changed.', 4, 1),
(7, '2015-01-22 06:19:58', '3', 'pavel', 1, '', 4, 1),
(8, '2015-01-22 06:20:15', '3', 'pavel', 2, 'No fields changed.', 4, 1),
(9, '2015-01-22 06:21:02', '2', 'Naher', 1, '', 8, 1),
(10, '2015-01-22 06:21:47', '3', 'pavel', 1, '', 8, 1);

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_32e52f82_uniq` (`app_label`,`model`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=22 ;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `name`, `app_label`, `model`) VALUES
(1, 'log entry', 'admin', 'logentry'),
(2, 'permission', 'auth', 'permission'),
(3, 'group', 'auth', 'group'),
(4, 'user', 'auth', 'user'),
(5, 'content type', 'contenttypes', 'contenttype'),
(6, 'session', 'sessions', 'session'),
(7, 'user type', 'kk_user', 'usertype'),
(8, 'user profile', 'kk_user', 'userprofile'),
(9, 'project', 'kk_project', 'project'),
(10, 'work area', 'kk_project', 'workarea'),
(11, 'project document', 'kk_project', 'projectdocument'),
(12, 'project user', 'kk_project', 'projectuser'),
(13, 'project work area', 'kk_project', 'projectworkarea'),
(14, 'module', 'kk_module', 'module'),
(15, 'module user', 'kk_module', 'moduleuser'),
(16, 'urgency', 'kk_task', 'urgency'),
(17, 'task', 'kk_task', 'task'),
(18, 'task user', 'kk_task', 'taskuser'),
(19, 'task checklist', 'kk_task', 'taskchecklist'),
(20, 'checklist item', 'kk_task', 'checklistitem'),
(21, 'task time', 'kk_task', 'tasktime');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=14 ;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2015-01-22 06:05:26'),
(2, 'auth', '0001_initial', '2015-01-22 06:05:32'),
(3, 'admin', '0001_initial', '2015-01-22 06:05:33'),
(4, 'kk_project', '0001_initial', '2015-01-22 06:05:36'),
(5, 'kk_module', '0001_initial', '2015-01-22 06:05:38'),
(6, 'kk_project', '0002_auto_20150122_1204', '2015-01-22 06:05:38'),
(7, 'kk_task', '0001_initial', '2015-01-22 06:05:41'),
(8, 'kk_task', '0002_auto_20141230_1605', '2015-01-22 06:05:42'),
(9, 'kk_task', '0003_auto_20150114_1159', '2015-01-22 06:05:43'),
(10, 'kk_task', '0004_remove_task_task_estimatedtime', '2015-01-22 06:05:44'),
(11, 'kk_task', '0005_auto_20150122_1204', '2015-01-22 06:05:45'),
(12, 'kk_user', '0001_initial', '2015-01-22 06:05:46'),
(13, 'sessions', '0001_initial', '2015-01-22 06:05:47');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('k16gyavu38rlhvamh3jqsulb4c71sh9e', 'MmY2YjE3YjMzMjQ4ZDY3MmVhMjcxZGU4Y2E2NzM0ODIzNjU3OWZhMzp7Il9hdXRoX3VzZXJfaGFzaCI6ImQ0ZDc3YWNhNDZkOWU4MjcxNTExNGYxMzU1YWM5NGQ3ZjgwNDI4MzciLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjF9', '2015-02-05 06:41:25'),
('nzvtw3wsr9x980f8s3u03ci846p6pvre', 'NzlkZjk2ZTJmZDc1MjYzOTU2YWNlMDZlZWIwM2IzYzg3ODNlNGRkMjp7fQ==', '2015-02-05 06:52:19');

-- --------------------------------------------------------

--
-- Table structure for table `kk_module_module`
--

CREATE TABLE IF NOT EXISTS `kk_module_module` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `module_name` varchar(100) NOT NULL,
  `module_due_date` date NOT NULL,
  `module_estimatedtime` int(11) NOT NULL,
  `module_description` longtext NOT NULL,
  `timestamp` datetime NOT NULL,
  `project_workarea_id_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `kk_module_module_a340b7d7` (`project_workarea_id_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `kk_module_module`
--

INSERT INTO `kk_module_module` (`id`, `module_name`, `module_due_date`, `module_estimatedtime`, `module_description`, `timestamp`, `project_workarea_id_id`) VALUES
(1, 'm1', '2015-01-31', 50, 'gdfgdfgd', '2015-01-22 06:39:35', 1);

-- --------------------------------------------------------

--
-- Table structure for table `kk_module_moduleuser`
--

CREATE TABLE IF NOT EXISTS `kk_module_moduleuser` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `timestamp` datetime NOT NULL,
  `module_id_id` int(11) NOT NULL,
  `module_user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `kk_module_moduleuser_ddb6ae0c` (`module_id_id`),
  KEY `kk_module_moduleuser_6ad4b731` (`module_user_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `kk_module_moduleuser`
--

INSERT INTO `kk_module_moduleuser` (`id`, `timestamp`, `module_id_id`, `module_user_id`) VALUES
(1, '2015-01-22 06:40:18', 1, 3);

-- --------------------------------------------------------

--
-- Table structure for table `kk_project_project`
--

CREATE TABLE IF NOT EXISTS `kk_project_project` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `project_name` varchar(100) NOT NULL,
  `project_due_date` date NOT NULL,
  `project_estimatedtime` int(11) NOT NULL,
  `project_descriptoin` longtext NOT NULL,
  `timestamp` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `kk_project_project`
--

INSERT INTO `kk_project_project` (`id`, `project_name`, `project_due_date`, `project_estimatedtime`, `project_descriptoin`, `timestamp`) VALUES
(1, 'p1', '2015-01-31', 200, 'hcvbcnhc', '2015-01-22 06:30:00');

-- --------------------------------------------------------

--
-- Table structure for table `kk_project_projectdocument`
--

CREATE TABLE IF NOT EXISTS `kk_project_projectdocument` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `document_name` varchar(100) NOT NULL,
  `document_description` longtext NOT NULL,
  `document_location` varchar(256) NOT NULL,
  `document_type` varchar(100) NOT NULL,
  `timestamp` datetime NOT NULL,
  `project_id_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `kk_project_projectdocument_bfec2ef8` (`project_id_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `kk_project_projectuser`
--

CREATE TABLE IF NOT EXISTS `kk_project_projectuser` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `timestamp` datetime NOT NULL,
  `project_id_id` int(11) NOT NULL,
  `project_user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `kk_project_projectuser_bfec2ef8` (`project_id_id`),
  KEY `kk_project_projectuser_27c7effd` (`project_user_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `kk_project_projectuser`
--

INSERT INTO `kk_project_projectuser` (`id`, `timestamp`, `project_id_id`, `project_user_id`) VALUES
(1, '2015-01-22 06:33:01', 1, 2),
(2, '2015-01-22 06:33:09', 1, 3);

-- --------------------------------------------------------

--
-- Table structure for table `kk_project_projectworkarea`
--

CREATE TABLE IF NOT EXISTS `kk_project_projectworkarea` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `timestamp` datetime NOT NULL,
  `area_id_id` int(11) NOT NULL,
  `project_id_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `kk_project_projectworkarea_bfd7c587` (`area_id_id`),
  KEY `kk_project_projectworkarea_bfec2ef8` (`project_id_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `kk_project_projectworkarea`
--

INSERT INTO `kk_project_projectworkarea` (`id`, `timestamp`, `area_id_id`, `project_id_id`) VALUES
(1, '2015-01-22 06:31:34', 1, 1),
(2, '2015-01-22 06:31:44', 2, 1);

-- --------------------------------------------------------

--
-- Table structure for table `kk_project_workarea`
--

CREATE TABLE IF NOT EXISTS `kk_project_workarea` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `area` varchar(100) NOT NULL,
  `timestamp` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `kk_project_workarea`
--

INSERT INTO `kk_project_workarea` (`id`, `area`, `timestamp`) VALUES
(1, 'core dev', '2015-01-22 06:30:58'),
(2, 'r&d', '2015-01-22 06:31:12');

-- --------------------------------------------------------

--
-- Table structure for table `kk_task_checklistitem`
--

CREATE TABLE IF NOT EXISTS `kk_task_checklistitem` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `checklist_item` varchar(256) NOT NULL,
  `timestamp` datetime NOT NULL,
  `checklist_id_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `kk_task_checklistitem_ec3dfab9` (`checklist_id_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `kk_task_task`
--

CREATE TABLE IF NOT EXISTS `kk_task_task` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `task_name` varchar(100) NOT NULL,
  `task_due_date` date NOT NULL,
  `task_description` longtext NOT NULL,
  `task_type` varchar(100) NOT NULL,
  `timestamp` datetime NOT NULL,
  `module_id_id` int(11) NOT NULL,
  `task_urgency_level_id` int(11) NOT NULL,
  `task_status` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `kk_task_task_ddb6ae0c` (`module_id_id`),
  KEY `kk_task_task_0a3b8364` (`task_urgency_level_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `kk_task_task`
--

INSERT INTO `kk_task_task` (`id`, `task_name`, `task_due_date`, `task_description`, `task_type`, `timestamp`, `module_id_id`, `task_urgency_level_id`, `task_status`) VALUES
(1, 'T1', '2015-01-31', 'dkfbjdgbjfd gjkdsf h', '1', '2015-01-22 06:43:09', 1, 1, '2');

-- --------------------------------------------------------

--
-- Table structure for table `kk_task_taskchecklist`
--

CREATE TABLE IF NOT EXISTS `kk_task_taskchecklist` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `task_checklist_name` varchar(100) NOT NULL,
  `timestamp` datetime NOT NULL,
  `task_id_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `kk_task_taskchecklist_423c378e` (`task_id_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `kk_task_tasktime`
--

CREATE TABLE IF NOT EXISTS `kk_task_tasktime` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `starttime` datetime NOT NULL,
  `endtime` datetime NOT NULL,
  `task_status` varchar(100) NOT NULL,
  `task_id_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `kk_task_tasktime_423c378e` (`task_id_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `kk_task_taskuser`
--

CREATE TABLE IF NOT EXISTS `kk_task_taskuser` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `timestamp` datetime NOT NULL,
  `task_id_id` int(11) NOT NULL,
  `task_user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `kk_task_taskuser_423c378e` (`task_id_id`),
  KEY `kk_task_taskuser_0736eaa1` (`task_user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `kk_task_urgency`
--

CREATE TABLE IF NOT EXISTS `kk_task_urgency` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `urgency_level` varchar(100) NOT NULL,
  `timestamp` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `kk_task_urgency`
--

INSERT INTO `kk_task_urgency` (`id`, `urgency_level`, `timestamp`) VALUES
(1, 'high', '2015-01-22 06:41:48'),
(2, 'low', '2015-01-22 06:41:57'),
(3, 'medium', '2015-01-22 06:42:07');

-- --------------------------------------------------------

--
-- Table structure for table `kk_user_userprofile`
--

CREATE TABLE IF NOT EXISTS `kk_user_userprofile` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `emp_id` varchar(100) NOT NULL,
  `email` varchar(254) NOT NULL,
  `user_id` int(11) NOT NULL,
  `user_type_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `kk_user_userprofile_e8701ad4` (`user_id`),
  KEY `kk_user_userprofile_4da4d835` (`user_type_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `kk_user_userprofile`
--

INSERT INTO `kk_user_userprofile` (`id`, `emp_id`, `email`, `user_id`, `user_type_id`) VALUES
(1, '12', 'admin@admin.com', 1, 1),
(2, '13', 'naher@gmail.com', 2, 2),
(3, '14', 'pavel@pavel.com', 3, 3);

-- --------------------------------------------------------

--
-- Table structure for table `kk_user_usertype`
--

CREATE TABLE IF NOT EXISTS `kk_user_usertype` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `type` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `kk_user_usertype`
--

INSERT INTO `kk_user_usertype` (`id`, `type`) VALUES
(1, 'admin'),
(2, 'project manager'),
(3, 'project member');

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissions_group_id_202dde2f_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_group_permissi_permission_id_2c93d8cd_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permissi_content_type_id_6a6b5316_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_1bb1899d_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_54d14c3_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permissions_user_id_9fab7c0_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `auth_user_user_perm_permission_id_421b06e4_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_user_id_3ea55178_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `django_admin__content_type_id_10250963_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `kk_module_module`
--
ALTER TABLE `kk_module_module`
  ADD CONSTRAINT `a9d3323a683750ac961bbdadcf687f8c` FOREIGN KEY (`project_workarea_id_id`) REFERENCES `kk_project_projectworkarea` (`id`);

--
-- Constraints for table `kk_module_moduleuser`
--
ALTER TABLE `kk_module_moduleuser`
  ADD CONSTRAINT `kk_module_moduleuser_module_user_id_5187b84_fk_auth_user_id` FOREIGN KEY (`module_user_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `kk_module_moduleuse_module_id_id_6d51878b_fk_kk_module_module_id` FOREIGN KEY (`module_id_id`) REFERENCES `kk_module_module` (`id`);

--
-- Constraints for table `kk_project_projectdocument`
--
ALTER TABLE `kk_project_projectdocument`
  ADD CONSTRAINT `kk_project_proje_project_id_id_65cd17b2_fk_kk_project_project_id` FOREIGN KEY (`project_id_id`) REFERENCES `kk_project_project` (`id`);

--
-- Constraints for table `kk_project_projectuser`
--
ALTER TABLE `kk_project_projectuser`
  ADD CONSTRAINT `kk_project_projectuser_project_user_id_4aff83ba_fk_auth_user_id` FOREIGN KEY (`project_user_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `kk_project_proje_project_id_id_28fd90cd_fk_kk_project_project_id` FOREIGN KEY (`project_id_id`) REFERENCES `kk_project_project` (`id`);

--
-- Constraints for table `kk_project_projectworkarea`
--
ALTER TABLE `kk_project_projectworkarea`
  ADD CONSTRAINT `kk_project_projectwo_area_id_id_ba86a4_fk_kk_project_workarea_id` FOREIGN KEY (`area_id_id`) REFERENCES `kk_project_workarea` (`id`),
  ADD CONSTRAINT `kk_project_proje_project_id_id_165d8c61_fk_kk_project_project_id` FOREIGN KEY (`project_id_id`) REFERENCES `kk_project_project` (`id`);

--
-- Constraints for table `kk_task_checklistitem`
--
ALTER TABLE `kk_task_checklistitem`
  ADD CONSTRAINT `kk_task_che_checklist_id_id_559712e8_fk_kk_task_taskchecklist_id` FOREIGN KEY (`checklist_id_id`) REFERENCES `kk_task_taskchecklist` (`id`);

--
-- Constraints for table `kk_task_task`
--
ALTER TABLE `kk_task_task`
  ADD CONSTRAINT `kk_task_task_module_id_id_839aade_fk_kk_module_module_id` FOREIGN KEY (`module_id_id`) REFERENCES `kk_module_module` (`id`),
  ADD CONSTRAINT `kk_task_tas_task_urgency_level_id_466040d7_fk_kk_task_urgency_id` FOREIGN KEY (`task_urgency_level_id`) REFERENCES `kk_task_urgency` (`id`);

--
-- Constraints for table `kk_task_taskchecklist`
--
ALTER TABLE `kk_task_taskchecklist`
  ADD CONSTRAINT `kk_task_taskchecklist_task_id_id_7cc7cfc2_fk_kk_task_task_id` FOREIGN KEY (`task_id_id`) REFERENCES `kk_task_task` (`id`);

--
-- Constraints for table `kk_task_tasktime`
--
ALTER TABLE `kk_task_tasktime`
  ADD CONSTRAINT `kk_task_tasktime_task_id_id_7e9c95dd_fk_kk_task_task_id` FOREIGN KEY (`task_id_id`) REFERENCES `kk_task_task` (`id`);

--
-- Constraints for table `kk_task_taskuser`
--
ALTER TABLE `kk_task_taskuser`
  ADD CONSTRAINT `kk_task_taskuser_task_id_id_461d0638_fk_kk_task_task_id` FOREIGN KEY (`task_id_id`) REFERENCES `kk_task_task` (`id`),
  ADD CONSTRAINT `kk_task_taskuser_task_user_id_4e585cdd_fk_auth_user_id` FOREIGN KEY (`task_user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `kk_user_userprofile`
--
ALTER TABLE `kk_user_userprofile`
  ADD CONSTRAINT `kk_user_userprofile_user_id_2b6c9abe_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `kk_user_userprofile_user_type_id_50523d61_fk_kk_user_usertype_id` FOREIGN KEY (`user_type_id`) REFERENCES `kk_user_usertype` (`id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
