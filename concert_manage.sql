-- phpMyAdmin SQL Dump
-- version 4.4.15.10
-- https://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: 2021-01-22 00:39:21
-- 服务器版本： 5.6.49-log
-- PHP Version: 7.0.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `concert_manage`
--

-- --------------------------------------------------------

--
-- 表的结构 `concert`
--

CREATE TABLE IF NOT EXISTS `concert` (
  `id` int(11) NOT NULL,
  `name` varchar(100) CHARACTER SET utf8mb4 NOT NULL,
  `remain_seat` int(11) NOT NULL,
  `total_seat` int(11) NOT NULL,
  `time` varchar(100) CHARACTER SET utf8mb4 NOT NULL,
  `site` varchar(100) CHARACTER SET utf8mb4 NOT NULL,
  `singer_id` int(11) DEFAULT NULL
) ENGINE=InnoDB AUTO_INCREMENT=48 DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `concert`
--

INSERT INTO `concert` (`id`, `name`, `remain_seat`, `total_seat`, `time`, `site`, `singer_id`) VALUES
(46, '上海巡回演唱会', 38, 40, '2021年7月8日', '上海徐汇区', 2),
(47, '北京演唱会', 0, 0, '2021年12月21日', '北京市大兴区体育场', 1);

-- --------------------------------------------------------

--
-- 表的结构 `fan`
--

CREATE TABLE IF NOT EXISTS `fan` (
  `id` int(11) NOT NULL,
  `cardid` varchar(100) CHARACTER SET utf8mb4 NOT NULL COMMENT '身份证号',
  `name` varchar(100) CHARACTER SET utf8mb4 NOT NULL,
  `gender` enum('0','1') NOT NULL COMMENT '0女1男',
  `is_select` enum('0','1') NOT NULL COMMENT '0可选1不可选',
  `account` int(11) NOT NULL COMMENT '账户余额看够不够买票',
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `fan`
--

INSERT INTO `fan` (`id`, `cardid`, `name`, `gender`, `is_select`, `account`, `user_id`) VALUES
(9, '54160128', 'alexzzl', '1', '1', 620, 39),
(10, '54160127', 'wang', '0', '1', 100, 43);

-- --------------------------------------------------------

--
-- 表的结构 `fan_ticket`
--

CREATE TABLE IF NOT EXISTS `fan_ticket` (
  `id` int(11) NOT NULL,
  `fan_id` int(11) NOT NULL,
  `ticket_id` int(11) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `fan_ticket`
--

INSERT INTO `fan_ticket` (`id`, `fan_id`, `ticket_id`) VALUES
(17, 9, 21),
(18, 10, 21);

-- --------------------------------------------------------

--
-- 表的结构 `node`
--

CREATE TABLE IF NOT EXISTS `node` (
  `id` int(11) NOT NULL,
  `function_name` varchar(100) CHARACTER SET utf8mb4 NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `node`
--

INSERT INTO `node` (`id`, `function_name`) VALUES
(1, '演唱会管理'),
(4, '演唱会购票情况查询'),
(3, '用户管理'),
(2, '购票管理');

-- --------------------------------------------------------

--
-- 表的结构 `role`
--

CREATE TABLE IF NOT EXISTS `role` (
  `id` int(11) NOT NULL,
  `rolename` varchar(100) CHARACTER SET utf8mb4 NOT NULL,
  `level` enum('1','2','3') NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `role`
--

INSERT INTO `role` (`id`, `rolename`, `level`) VALUES
(1, '后台管理者', '3'),
(2, '歌手', '2'),
(3, '购票人', '1');

-- --------------------------------------------------------

--
-- 表的结构 `role_node`
--

CREATE TABLE IF NOT EXISTS `role_node` (
  `id` int(11) NOT NULL,
  `role_id` int(11) NOT NULL,
  `node_id` int(11) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `role_node`
--

INSERT INTO `role_node` (`id`, `role_id`, `node_id`) VALUES
(7, 1, 1),
(8, 1, 2),
(9, 1, 3),
(10, 1, 4),
(11, 2, 4);

-- --------------------------------------------------------

--
-- 表的结构 `singer`
--

CREATE TABLE IF NOT EXISTS `singer` (
  `id` int(11) NOT NULL,
  `name` varchar(100) CHARACTER SET utf8mb4 NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `singer`
--

INSERT INTO `singer` (`id`, `name`, `user_id`) VALUES
(1, 'jayz', 41),
(2, 'eason', 42);

-- --------------------------------------------------------

--
-- 表的结构 `ticket`
--

CREATE TABLE IF NOT EXISTS `ticket` (
  `id` int(11) NOT NULL,
  `name` varchar(100) CHARACTER SET utf8mb4 NOT NULL,
  `price` int(11) NOT NULL,
  `type` enum('0','1','2') NOT NULL COMMENT '0vip 1内场 2看台',
  `remain` int(11) NOT NULL,
  `total` int(11) NOT NULL,
  `concert_id` int(11) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `ticket`
--

INSERT INTO `ticket` (`id`, `name`, `price`, `type`, `remain`, `total`, `concert_id`) VALUES
(21, '看台', 200, '2', 18, 20, 46),
(22, '内场', 300, '1', 10, 10, 46),
(23, 'VIP', 400, '0', 10, 10, 46);

-- --------------------------------------------------------

--
-- 表的结构 `user`
--

CREATE TABLE IF NOT EXISTS `user` (
  `id` int(11) NOT NULL,
  `username` varchar(100) CHARACTER SET utf8mb4 NOT NULL,
  `password` varchar(100) CHARACTER SET utf8mb4 NOT NULL,
  `role_id` int(11) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=58 DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `user`
--

INSERT INTO `user` (`id`, `username`, `password`, `role_id`) VALUES
(39, 'zzl', '123456', 3),
(40, 'www', '654321', 1),
(41, 'jayzhou', '123456', 2),
(42, 'easonchen', '123456', 2),
(43, 'wxy', '123456', 3),
(44, 'wdw', '4654646', 3),
(45, 'wdwdw', '123', 3),
(46, 'test1', '123456', 3),
(47, 'test2', '123456', 3),
(48, 'test3', '123456', 3),
(50, 'wjl', '123456', 1),
(55, 'test10', '123456', 3);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `concert`
--
ALTER TABLE `concert`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`),
  ADD UNIQUE KEY `singer_id` (`singer_id`),
  ADD UNIQUE KEY `singer_id_2` (`singer_id`);

--
-- Indexes for table `fan`
--
ALTER TABLE `fan`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_id` (`user_id`),
  ADD UNIQUE KEY `cardid` (`cardid`);

--
-- Indexes for table `fan_ticket`
--
ALTER TABLE `fan_ticket`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fan_id` (`fan_id`),
  ADD KEY `ticket_id` (`ticket_id`);

--
-- Indexes for table `node`
--
ALTER TABLE `node`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `function_name` (`function_name`);

--
-- Indexes for table `role`
--
ALTER TABLE `role`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `rolename` (`rolename`);

--
-- Indexes for table `role_node`
--
ALTER TABLE `role_node`
  ADD PRIMARY KEY (`id`),
  ADD KEY `role_id` (`role_id`),
  ADD KEY `node_id` (`node_id`);

--
-- Indexes for table `singer`
--
ALTER TABLE `singer`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `ticket`
--
ALTER TABLE `ticket`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`),
  ADD KEY `building_id` (`concert_id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`),
  ADD KEY `role_id` (`role_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `concert`
--
ALTER TABLE `concert`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=48;
--
-- AUTO_INCREMENT for table `fan`
--
ALTER TABLE `fan`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=11;
--
-- AUTO_INCREMENT for table `fan_ticket`
--
ALTER TABLE `fan_ticket`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=19;
--
-- AUTO_INCREMENT for table `node`
--
ALTER TABLE `node`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=7;
--
-- AUTO_INCREMENT for table `role`
--
ALTER TABLE `role`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT for table `role_node`
--
ALTER TABLE `role_node`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=12;
--
-- AUTO_INCREMENT for table `singer`
--
ALTER TABLE `singer`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT for table `ticket`
--
ALTER TABLE `ticket`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=24;
--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=58;
--
-- 限制导出的表
--

--
-- 限制表 `concert`
--
ALTER TABLE `concert`
  ADD CONSTRAINT `concert_ibfk_1` FOREIGN KEY (`singer_id`) REFERENCES `singer` (`id`);

--
-- 限制表 `fan`
--
ALTER TABLE `fan`
  ADD CONSTRAINT `stu_user` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`);

--
-- 限制表 `fan_ticket`
--
ALTER TABLE `fan_ticket`
  ADD CONSTRAINT `fan_ticket_ibfk_1` FOREIGN KEY (`fan_id`) REFERENCES `fan` (`id`),
  ADD CONSTRAINT `fan_ticket_ibfk_2` FOREIGN KEY (`ticket_id`) REFERENCES `ticket` (`id`);

--
-- 限制表 `role_node`
--
ALTER TABLE `role_node`
  ADD CONSTRAINT `role_node_ibfk_1` FOREIGN KEY (`role_id`) REFERENCES `role` (`id`),
  ADD CONSTRAINT `role_node_ibfk_2` FOREIGN KEY (`node_id`) REFERENCES `node` (`id`);

--
-- 限制表 `singer`
--
ALTER TABLE `singer`
  ADD CONSTRAINT `singer_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`);

--
-- 限制表 `ticket`
--
ALTER TABLE `ticket`
  ADD CONSTRAINT `ticket_ibfk_1` FOREIGN KEY (`concert_id`) REFERENCES `concert` (`id`);

--
-- 限制表 `user`
--
ALTER TABLE `user`
  ADD CONSTRAINT `user_ibfk_1` FOREIGN KEY (`role_id`) REFERENCES `role` (`id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
