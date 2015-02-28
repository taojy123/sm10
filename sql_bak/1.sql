-- phpMyAdmin SQL Dump
-- version 3.3.8.1
-- http://www.phpmyadmin.net
--
-- 主机: w.rdc.sae.sina.com.cn:3307
-- 生成日期: 2014 年 02 月 09 日 17:45
-- 服务器版本: 5.5.23
-- PHP 版本: 5.3.3

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- 数据库: `app_sm10`
--

-- --------------------------------------------------------

--
-- 表的结构 `auth_group`
--

CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

--
-- 转存表中的数据 `auth_group`
--


-- --------------------------------------------------------

--
-- 表的结构 `auth_group_permissions`
--

CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_425ae3c4` (`group_id`),
  KEY `auth_group_permissions_1e014c8f` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

--
-- 转存表中的数据 `auth_group_permissions`
--


-- --------------------------------------------------------

--
-- 表的结构 `auth_permission`
--

CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_1bb8f392` (`content_type_id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=34 ;

--
-- 转存表中的数据 `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add permission', 1, 'add_permission'),
(2, 'Can change permission', 1, 'change_permission'),
(3, 'Can delete permission', 1, 'delete_permission'),
(4, 'Can add group', 2, 'add_group'),
(5, 'Can change group', 2, 'change_group'),
(6, 'Can delete group', 2, 'delete_group'),
(7, 'Can add user', 3, 'add_user'),
(8, 'Can change user', 3, 'change_user'),
(9, 'Can delete user', 3, 'delete_user'),
(10, 'Can add content type', 4, 'add_contenttype'),
(11, 'Can change content type', 4, 'change_contenttype'),
(12, 'Can delete content type', 4, 'delete_contenttype'),
(13, 'Can add session', 5, 'add_session'),
(14, 'Can change session', 5, 'change_session'),
(15, 'Can delete session', 5, 'delete_session'),
(16, 'Can add site', 6, 'add_site'),
(17, 'Can change site', 6, 'change_site'),
(18, 'Can delete site', 6, 'delete_site'),
(19, 'Can add type', 7, 'add_type'),
(20, 'Can change type', 7, 'change_type'),
(21, 'Can delete type', 7, 'delete_type'),
(22, 'Can add product', 8, 'add_product'),
(23, 'Can change product', 8, 'change_product'),
(24, 'Can delete product', 8, 'delete_product'),
(25, 'Can add order', 9, 'add_order'),
(26, 'Can change order', 9, 'change_order'),
(27, 'Can delete order', 9, 'delete_order'),
(28, 'Can add bom', 10, 'add_bom'),
(29, 'Can change bom', 10, 'change_bom'),
(30, 'Can delete bom', 10, 'delete_bom'),
(31, 'Can add comment', 11, 'add_comment'),
(32, 'Can change comment', 11, 'change_comment'),
(33, 'Can delete comment', 11, 'delete_comment');

-- --------------------------------------------------------

--
-- 表的结构 `auth_user`
--

CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(75) NOT NULL,
  `password` varchar(128) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `last_login` datetime NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=2 ;

--
-- 转存表中的数据 `auth_user`
--

INSERT INTO `auth_user` (`id`, `username`, `first_name`, `last_name`, `email`, `password`, `is_staff`, `is_active`, `is_superuser`, `last_login`, `date_joined`) VALUES
(1, 'admin', '', '', 'admin@admin.com', 'pbkdf2_sha256$10000$i4MjYkEc5T5y$30vPQGVovgGMVonvKUUSaYay/3VirMF6FCTnzxqLo58=', 1, 1, 1, '2014-02-08 10:03:38', '2014-02-08 10:03:38');

-- --------------------------------------------------------

--
-- 表的结构 `auth_user_groups`
--

CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_403f60f` (`user_id`),
  KEY `auth_user_groups_425ae3c4` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

--
-- 转存表中的数据 `auth_user_groups`
--


-- --------------------------------------------------------

--
-- 表的结构 `auth_user_user_permissions`
--

CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_403f60f` (`user_id`),
  KEY `auth_user_user_permissions_1e014c8f` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

--
-- 转存表中的数据 `auth_user_user_permissions`
--


-- --------------------------------------------------------

--
-- 表的结构 `django_content_type`
--

CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app_label` (`app_label`,`model`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=12 ;

--
-- 转存表中的数据 `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `name`, `app_label`, `model`) VALUES
(1, 'permission', 'auth', 'permission'),
(2, 'group', 'auth', 'group'),
(3, 'user', 'auth', 'user'),
(4, 'content type', 'contenttypes', 'contenttype'),
(5, 'session', 'sessions', 'session'),
(6, 'site', 'sites', 'site'),
(7, 'type', 'supermarketten', 'type'),
(8, 'product', 'supermarketten', 'product'),
(9, 'order', 'supermarketten', 'order'),
(10, 'bom', 'supermarketten', 'bom'),
(11, 'comment', 'supermarketten', 'comment');

-- --------------------------------------------------------

--
-- 表的结构 `django_session`
--

CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_3da3d3d8` (`expire_date`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `django_session`
--


-- --------------------------------------------------------

--
-- 表的结构 `django_site`
--

CREATE TABLE IF NOT EXISTS `django_site` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `domain` varchar(100) NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=2 ;

--
-- 转存表中的数据 `django_site`
--

INSERT INTO `django_site` (`id`, `domain`, `name`) VALUES
(1, 'example.com', 'example.com');

-- --------------------------------------------------------

--
-- 表的结构 `supermarketten_bom`
--

CREATE TABLE IF NOT EXISTS `supermarketten_bom` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `order_id` int(11) NOT NULL,
  `product_id` int(11) NOT NULL,
  `quantity` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `supermarketten_bom_7cc8fcf5` (`order_id`),
  KEY `supermarketten_bom_44bdf3ee` (`product_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

--
-- 转存表中的数据 `supermarketten_bom`
--


-- --------------------------------------------------------

--
-- 表的结构 `supermarketten_comment`
--

CREATE TABLE IF NOT EXISTS `supermarketten_comment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `product_id` int(11) NOT NULL,
  `content` varchar(1024) DEFAULT NULL,
  `user` varchar(255) DEFAULT NULL,
  `time` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `supermarketten_comment_44bdf3ee` (`product_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

--
-- 转存表中的数据 `supermarketten_comment`
--


-- --------------------------------------------------------

--
-- 表的结构 `supermarketten_order`
--

CREATE TABLE IF NOT EXISTS `supermarketten_order` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sn` varchar(255) DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `phone` varchar(255) DEFAULT NULL,
  `status` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

--
-- 转存表中的数据 `supermarketten_order`
--


-- --------------------------------------------------------

--
-- 表的结构 `supermarketten_product`
--

CREATE TABLE IF NOT EXISTS `supermarketten_product` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sn` varchar(255) DEFAULT NULL,
  `type_id` int(11) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `info` varchar(1024) DEFAULT NULL,
  `details` varchar(10000) DEFAULT NULL,
  `price` double NOT NULL,
  `pic` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `supermarketten_product_777d41c8` (`type_id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=13 ;

--
-- 转存表中的数据 `supermarketten_product`
--

INSERT INTO `supermarketten_product` (`id`, `sn`, `type_id`, `name`, `info`, `details`, `price`, `pic`) VALUES
(1, '', 1, '立顿组合装', '立顿办公室组合装（红茶50包+绿茶50包）100包200g', '名　　称：办公茶包组合（红茶&绿茶）\r\n红茶配料：红茶\r\n绿茶配料：绿茶\r\n规　　格：净含量200g（2g*100包）（绿茶50包，红茶50包）\r\n包　　装：一盒内含100包独立包装\r\n保 质 期：24个月贮存方法：于阴凉干燥，不受阳光直射处\r\n适宜人群：皆宜\r\n产品标准号：Q/TNBE 1003S\r\n食品生产许可证号：QS3401 1401 0134\r\n产品介绍：\r\n黄牌红茶：选用世界各地优质红茶拼配而成，综合了各地红茶的优良品质。选用高品质的进口包装材料，经先进包装工艺制成。独特的双室茶包，让茶味更快渗出。色泽红亮清醇，口感纯正，饮用卫生方便。提供丰富的天然氨基酸和其它有益成份，有益身体健康。\r\n绿茶：精挑细选原片茶叶，切碎后以先进工艺加工而成，确保上佳品质。色泽鲜亮，茶香宜人，口味鲜爽甘醇。', 32.9, 'http://sm10-product.stor.sinaapp.com/b0718f2d-fcf2-407a-a6a4-71f1e4ea700a.jpg'),
(2, '', 1, '黄飞红', '黄飞红 麻辣花生76g*10包', '规格参数\r\n品种：花生米口味：五香国家：中国大陆进口/国产：国产包装方式：袋装花生种类：辣椒花生', 39, 'http://sm10-product.stor.sinaapp.com/6ad1d55a399dc6e7YY.jpg'),
(3, '', 1, '碧根果', '每食每嗑 碧根果 年货好吃的休闲零食坚果炒货美国特产山核桃长寿果', '规格参数\r\n口味：奶油包装：袋装国家：中国大陆进口/国产：国产食品保质期：240天', 36.9, 'http://sm10-product.stor.sinaapp.com/CgQCtlLLeSqAB-tfAANYyyyi6xo21700.jpg'),
(4, '', 1, '夏威夷果', '百草味 夏威夷果200gx3袋 坚果零食 奶油味', '规格参数\r\n零食口味：奶油国家：中国大陆进口/国产：国产包装方式：袋装是否带壳：是食品保质期：300', 39.8, 'http://sm10-product.stor.sinaapp.com/CgQCtVL0bByAEV3uAANAtloUkPg87800.jpg'),
(5, '', 1, '香卤驴肉', '冠云 中华老字号 山西特产 香卤驴肉家庭装', '规格参数\r\n包装方式：整包进口/国产：国产', 145, 'http://sm10-product.stor.sinaapp.com/CgQCrVIOQ-iAL629AARv8iPskNU42900.jpg'),
(6, '', 1, '乐事', '乐事 美国经典原味45g/袋 X 3', '规格参数\r\n包装：袋装国家：中国大陆进口/国产：国产口味：原味种类：薯片是否油炸：非油炸食品', 9.9, 'http://sm10-product.stor.sinaapp.com/CgQCrVIn33uAQMBYAAMvpkMcbU885601.jpg'),
(7, '', 1, '卡乐薯', '康师傅 卡乐薯马铃薯条 番茄味 40g/杯', '规格参数\r\n包装：罐装国家：中国大陆进口/国产：国产口味：番茄味种类：薯片是否油炸：非油炸食品', 6.5, 'http://sm10-product.stor.sinaapp.com/CgQDr1LYx5aASFBiAALdZko_c7Y57701.jpg'),
(8, '', 2, '双立人', 'Zwilling 双立人 Enjoy系列 刀具 5件套', '规格参数\r\n\r\n材质 不锈钢\r\n包装清单\r\n由于厂商产品批次不同，具体包装清单可能各有不同，请以实物为准 ！', 648, 'http://sm10-product.stor.sinaapp.com/CgQCslFvz3eATDFqAAGjwUo93Eo87100.jpg'),
(9, '', 2, '洗衣刷', '亿威特 家用硬刷丝 精巧洗衣刷 YS-0308', '服务承诺\r\n网站所售产品均为厂商正品，如有任何问题可与我们客服人员联系，我们会在第一时间跟您沟通处理。我们将争取以最低的价格、最优的服务来满足您最大的需求。 开箱验货：签收时在付款后与配送人员当面核对：商品及配件、应付金额、商品数量及发货清单、发票（如有）、赠品（如有）等；如存在包装破损、商品错误、商品短缺、商品 存在质量问题等影响签收的因素，请您可以拒收全部或部分商品，相关的赠品，配件或捆绑商品应一起当场拒收；为了保护您的权益，建议您尽量不要委托他人代为签收；如由他 人代为签收商品而没有在配送人员在场的情况下验货，则视为您所订购商品的包装无任何问题。', 11, 'http://sm10-product.stor.sinaapp.com/d0b0102fe9992b53c77fecedee40a191.jpg'),
(10, '', 3, '联想笔记本', 'Lenovo 联想 G510AT-IFI 15.6英寸 笔记本电脑 黑色-I5-4200M/4G/500G/HD8570M', '主体\r\n商品品牌 Lenovo 联想  型号 G510\r\n预装系统 Linpus Lite\r\n外壳颜色 黑色\r\n处理器\r\nCPU类型 智能英特尔® 酷睿Haswell双核处理器\r\nCPU型号 i5-4200M\r\nCPU核心数 双核\r\nCPU速度 2.5GHz，睿频至3.0 GHz\r\n三级缓存 3MB\r\n内存\r\n内存容量 4GB\r\n内存类型 DDR3\r\n硬盘\r\n硬盘类型 机械硬盘\r\n硬盘容量 500GB', 3699, 'http://sm10-product.stor.sinaapp.com/CgQDrVJ7HpOAdG_EAAHteR1TRUs03701.jpg'),
(11, '', 4, '水彩笔', 'Disney/迪士尼 米奇72/90件美劳派礼盒/文具套装水彩笔大礼盒儿童美术用品画', '商品品牌：美国迪士尼/Disney\r\n\r\n商品型号：DM6901-X\r\n\r\n商品规格：包体约长：31cm， 高：20cm， 厚：3.5cm\r\n\r\n商品颜色：蓝色米奇/粉色米妮/灰色米奇/大红米妮\r\n\r\n商品材质：塑胶\r\n\r\n商品重量：约0.7千克\r\n\r\n商品包装：迪士尼原版统一透明包装袋+迪士尼红色镭射激光防伪标记+合格证/说明书\r\n\r\n商品等级：一等品/美国迪士尼授权、原装正品/镭射激光、双重防伪\r\n\r\n商品特点：本品套装为米妮米奇图案，内置直尺、12色彩色铅笔、12色水彩笔、1块调色板、5张画形板、12色粉饼，1把毛刷、1支沾头铅笔、1个迷你削、1块橡皮、12色蜡笔（长）、12色蜡笔（短）、1支细管胶水，整套学习用品齐全，造型简单大方 安全实用，是小朋友绘画学习的好帮手.自用，送礼高档优惠。\r\n\r\n品牌保证：本店所有产品保证100%正品。此款带合格证、激光防伪商标，接受专柜验货和315认证，假一赔十！请购买本店商品的朋友们100%放心。七天无理由退货，如有质量问题,包退包换直到满意为止！\r\n\r\n生 产 商：广东中山联众文具有限公司', 58, 'http://sm10-product.stor.sinaapp.com/CgQCtFKeiJeATJ_FAANZXCo0lUk34000.jpg'),
(12, '', 6, '大红包', '欧芬 富贵大红包', '【名称】：富贵大红包\r\n【尺寸】：17*9 cm\r\n【材质】：厚纸\r\n【工艺】：烫金 压纹\r\n【温馨提示】：请以实物为准', 5, 'http://sm10-product.stor.sinaapp.com/CgQDrVKv5zOAEs6fAAa8qEHEwq852301.jpg');

-- --------------------------------------------------------

--
-- 表的结构 `supermarketten_type`
--

CREATE TABLE IF NOT EXISTS `supermarketten_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `info` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=7 ;

--
-- 转存表中的数据 `supermarketten_type`
--

INSERT INTO `supermarketten_type` (`id`, `name`, `info`) VALUES
(1, '食品', '食品饮料、酒水、生鲜\r\n休闲零食、饮料饮品\r\n厨房调料、白酒、啤酒、黄酒'),
(2, '家居', '床上用品、家纺日用品、收纳洗晒、运动保健、装饰/日用、家具家装、厨具锅具、餐具水具、宠物园艺、清洁剂、纸制品、清洁用具、一次性用品'),
(3, '数码', '电脑、平板、办公设备、周边配件、外设产品、存储产品\r\n'),
(4, '文具', '书包、笔袋及笔盒、文具礼盒、油画棒、水彩笔、画具及画材、学生彩泥、几何用具\r\n'),
(6, '礼品', '文化礼品、贺卡、相册');
