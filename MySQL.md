# MySQL

## 一.概述

### 数据库种类

数据库管理系统（DBMS）

1.RDBMS 关系型数据库

- Oracle
- MySQL
- Microsoft SQL server

2.NoSQL 非关系型数据库

- MangoDB
- ES
- Redis

3.云数据库

RDS，PolarDB，TDSQL

4.NewSQL

TiDB

## 二.MySQL体系结构及基础管理

MySQL 客户端/服务器工作模型（C/S）

本地socket连接方式去连接数据库，不依赖IP和端口号：

也可以通过TCP/IP地址端口号远程登入(使用本机)

​		mysql  -h 10.0.0.1 -p3306 -uroot -p123

服务器端：也被称为mysql实例(包括mysqld守护进程+工作线程+与分配的内存结构)

mysqld:一直在后台守护运行，mysqld在启动时会一次性申请大量内存（预分配内存，属于mysqld独占的内存，其他程序不能使用）。mysql支持高并发，所以它在内存中会开辟一堆线程（图中的圆圈）

![image-20200610173336198](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200610173336198.png)

### 2.1 mysqld程序结构

![img](https://img2018.cnblogs.com/blog/1485191/201910/1485191-20191008202330054-125227915.png)



组成: Service + 引擎层

Service 层又分为：连接层（connection pool）+ SQL层 

### 2.2 mysqld语句执行过程

1. 客户端首先要连接到mysqld 

#### 连接层操作

2. mysql连接层：主要提供 1.各种连接协议：socket，TCP/IP。2. 收到客户端的请求后，需要验证用户。3. 提供专用的连接线程负责接收客户端发来的sql语句。

#### SQL层操作

3. 连接线程会把sql语句发送给sql层，sql层会做以下工作：
   1. 语法检查
   2. 语义（DDL，DCL，DML,DTL）
   3. 对用户的权限检查
   4. 解析器：预处理（会给出执行语句有哪些方式，比如说a.走索引还是b.全表扫描），得出执行计划
   5. 优化器：会帮助我们选择他认为最优的方案（基于代价COST模型），选择哪个执行计划
   6. 执行器：按照优化器的选择，执行sql语句得出执行结果：我们需要的数据在哪个段，哪个区，哪个页
   7. 查询缓存（query_cache，默认不开启。原理是将语句的哈希值和结果存入缓存中，下一次执行同一条语句的时候就可以直接从缓存中取结果了，大部分没卵用8.0以后已经取消了），用redis替代缓存方案
   8. 日志记录（binlog二进制日志：记录修改类操作，glog：将所有语句记录，默认不开启）

#### 存储引擎层操作

​	相当于Linux文件系统，和磁盘交互的模块，将数据从磁盘中取出来，然后通过server层，传给连接层。最后数据拿到数据

### 2.3MySQL逻辑结构

​	逻辑结构又是抽象结构：

库结构（相当于文件系统的目录）：库名 + 库属性

表结构（相当于文件系统的文件）：表名 + 表属性 + 表内容 + 列

### 2.4MySQL物理结构

磁盘扇区：连续的一段磁盘空间顺序IO（512字节）

OS通过磁盘驱动程序可以读取扇区。应用程序使用磁盘的时候，需要先通过文件系统（文件系统主要用来将连续的8个扇区组成block(4KB)，格式化操作，就是把磁盘变成一堆连续的block），然后再通过操作系统OS Kernal 驱动来错做磁盘。

而Mysql则是通过存储引擎层取获取连续的block，将block做成配页（page:16KB，连续的4个block）

简单来说就是：1个页 （16KB）= 4个连续的block（4KB） = 8个扇区（512B），这样就把一切都变成物理连续

段：一个段就是一个表（分区表除外），表中含有很多区（不一定连续）

区（textent ）：等于64个连续的16KB的page （区默认1M）

页：等于4个连续的block （每个block是8 个扇区），页是 最小的IO单元16KB

## 三. Mysql基础管理

### 3.1用户管理

用户的作用：登入数据库，管理Mysql对象（逻辑结构）

### 3.2 用户定义

MySQL用户名： 用户名@‘白名单’    （白名单就是地址列表）

用户表现方式：

like@'localhost'： like可以通过本地登入数据库

like@'10.0.0.10':    like可以通过10.0.0.10远程登入

like@'10.0.0.%':     like通过 10.0.0.xx/24 网段登入

like@'10.0.0.5%':                   10.0.0.50-59

like@'10.0.0.0/255.255.254.0'

like@'%':所有人都可以连接数据库

### 3.3 用户管理

查：select user,host from mysql.user

增：create user like@'localhost' identified by 'password';

改：修改密码： alter user like@'localhost' identified by '新密码'; 

删：drop user like@'localhost';

注意：8.0以前可以通过grant命令建立用户+授权，8.0后必须要先创建用户再授权

### 3.4 权限管理

#### 3.4.1 作用

作用：赋予用户对数据库管理能力的权限，权限是用户的属性

#### 3.4.2 权限的表现方式

可以通过 show privileges；去查看有多少中权限

#### 3.4.3 授权、回收权限操作

语法：

##### 	8.0以前   授权和创建用户可以放在一块

​	grant 权限 on 对象 to 用户@‘地址’ identifield by '密码'；

##### 	8.0+以后，必须分开

​	create user 用户@‘地址’ identifield by '密码';

​	grant 权限1,权限2，权限3 on 对象（数据库.表） to 用户@地址 identified by ‘密码‘；

#### 3.4.4 权限解释

权限                                  使用者

ALL         ——————> 管理员

权限1，2，3————>  用户

grant option————> 赋予用户赋予权限的权限

grant option例子：

创建管理员用户：

grant all on \*.\* to like@'10.0.0.%' identified by '密码'   with grant option;

on后面的对象：

\*.\*     --------------->     所有数据库                 （管理员）

库.\*    —————>    库下所有的表          （用的最多的，普通用户）

库.表  —————>     指定表 

查询用户授权情况：

show grants for ’用户‘@’地址‘； 注意用户名也要带引号

#### 3.4.5 授权表

针对不同的对象，用户所拥有的权限记录在不同的表当中。在mysql启动时，会把这些表加载到内存中

user                          :\*.\*

db                            :app.\*

tables_priv              :app.t1

columns_priv         :列

#### 3.4.6回收权限

mysql只能通过回收权限的方式修改权限

语法：revoke 权限 on 对象 from ’用户‘@’地址‘

#### 3.4.7 超级管理员密码忘了怎么办

跳过连接层，验证用户的功能

方法：1.关闭数据库

--skip-grant-tables; 跳过授权表

--skip-networking; 跳过TCP/IP连接

1.进入维护模式，修改密码



### 3.5 连接管理

![image-20200611051620519](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200611051620519.png)

#### 3.5.1 Mysql自带的客户端程序

存放在mysql/bin下，通过TCP/IP或者socket的方式访问mysqld。

1）mysql

常用参数列表

 -u用户名，

-p密码，

-s 本地socket文件位置, 

-h 数据库ip地址, 

-p端口号, 

-e免交互，不登入数据库直接在对话窗口返回结果。例如：mysql -uroot -p123 -e "select * from mysql.user"

<导入sql脚本  例如：mysql -uroot -p </脚本路径

本地socket连接：

​	前提：数据库必须事先实现授权like@'localhost'

TCP/IP远程连接

​	前提：必须提前创建远程用户

#### 3.5.2 远程客户端

类似workbrench这些

#### 3.5.3 程序连接

类似语言通过安装驱动程序连接如python 通过 pymysql 连接

#### 3.5.4 初始化配置

注意：在数据库启动之前修改配置

修改配置的方式：

- 源码安装：编译过程中设置初始化参数（不常用）
- 配置文件：数据库启动之前，设定配置文件参数（windows 下my.ini，linux下是my.cnf）
- 启动脚本命令行

#### 3.5.5 启动和关闭

mysqld：

mysqld_safe：可以定制默认的一些功能

## 四. SQL基础

#### 4.1 SQL介绍

定义：结构化的查询语言，关系型数据库中通用的一类语言

SQL标准：SQL 89 92 99 03 

#### 4.2 SQL常用类型

##### 4.2.1 mysql客户端

​	 进入到mysql会话后，使用help会显示

##### 4.2.2 mysql服务端

​	help contents显示服务端的SQL分类，里面会包含DDL

​	然后键入 help 某个分类 会显示细分的。比如 help Data Defination

我们常用的SQL类型就是

- DDL: 数据定义语言

- DCL: 数据控制语言

- DML: 数据操作语言

- DQL: 数据查询语言

#### 4.3 SQL名词

##### 4.3.1 sql_mode SQL模式

（mysql> select @@sql_mode;查看所有的规范）

作用：规范SQL语言书写方式，里面包括除数不能为0、日期不能为0规范

主要的一个规范是： only_full_group_by

##### 4.3.2 字符集（charset）校对规则(collection)

字符集：将文字，数字等转码成二进制的集合   show charset;

一般都是用utf8，utf8mb4（建议使用）。两者的区别支持的编码比utf8更多，比如emoji字符mb4中支持，utf8中不支持。emoji字符占4个字节，utf最大存储长度是3个字节，mb4最多是4个字节，所以utf8存不下。

在创建数据库的时候可以设定数据库使用的字符集：

create database basename charset utf8mb4;

查看建库的语句：(可以看他默认的设置，如字符集设置)

show createdatabase basename;

注意：建库的时候一定要指定字符集，因为不同版本的默认字符集不同（5.7默认latin），所以不同环境下生成的库就不一样了。

校对规则collation（排序规则）：

作用：影响到排序的操作，简单来说就是大小写是否铭感

比如：

a b A aB Ba

大小写敏感，ASCII 顺序

A Ba a aB b

大小写不敏感就是另一种排序规则了

##### 4.3.3 数据类型

|                            | 存储长度 | 二进制范围        | 十进制范围              |
| -------------------------- | -------- | ----------------- | ----------------------- |
| tinyint                    | 1B=8bit  | 00000000-11111111 | 0-255,-128-127          |
| int                        | 4B=32bit |                   | 0~2^32-1,-2^31 ~ 2^31-1 |
| bigint                     | 8B       |                   | 0~2^64-1,-2^63~ 2^63-1  |
| char(长度)            定长 |          |                   |                         |
| varchar（长度） 变长       |          |                   |                         |
| enum（‘北京‘,'上海'）      |          |                   |                         |

1. varchar类型，在存储数据时，先判断字符长度再合理分配存储空间，char类型，直接分配空间。所以在性能上char要比varchar会快一点

2. varchar类型，除了存储字符串外，还会额外使用1-2个字节存储字符长度

3. char类型最多设定255字符，varchar65535字符

   

2.枚举类型enum('bj','sh')

​	说明：枚举类型也属于字符串类型，不能存数字。他会给每个字符串加一个下标索引，以后用的时候只要存下标索引就行了，可以节省很多的空间（将字符变成数字）

3. 时间类型

| 类型      | 格式                        | 示例                       |
| --------- | --------------------------- | -------------------------- |
| DATE      | YYYY-MM-DD                  | 2006-08-04                 |
| TIME      | hh:mm:ss[.uuuuu]            | 12:59:02.123456            |
| DATETIME  | YYYY-MM-DD hh:mm:ss[.uuuuu] | 2006-08-04 12:59:02.123456 |
| TIMESTAMP | YYYY-MM-DD hh:mm:ss[.uuuuu] | 2006-08-04 12:59:02.123456 |
| YEAR      | YYYY                        | 2006                       |

DATETIME 从1000-01-01 00：00：00.000000~9999-12-31 23：59：59.9999999

TIMESTAMP  1970-01-01 00：00：00.000000 ~ 2038-01-19 03：14：07.999999

Datetime占8个字节长度，timestamp占4个字节长度

timestamp会受时区影响

4. 二进制类型，图片等
5. json格式

##### 4.3.4 约束

- PK	           主键约束             作用：唯一+非空  一张表只有一个主键
- not null      非空约束             作用：必须非空，建议每个列都设置为非空
- unique        唯一约束            作用：必须不重复
- unsigned    非负数                针对数字列

##### 4.3.5 其他属性

- default        默认值
- comment    注释

#### 4.4 SQL应用

##### 4.4.1 client

可以通过help命令来查看命令列表

常用的命令：

- \c      结束命令的运行
- \G     以竖向显示数据
- \q      退出SQL  （CRTL + D）
- source   导入SQL脚本，类似与<        source /脚本路径

##### 4.4.2 Server

linux中一切皆命令，一切皆文件

MySQL中一切皆SQL，一切皆表

###### 4.4.2.1 DDL 数据定义语言

 1. 库定义： 库名     库属性

    创建库定义：create database 库名 charset 字符集;

    ​     规范：

                1. 库名字：小写，与业务有关，不要数字开头，长度不能太长，保留字符不能使用
                   2. 必须指定字符集

    查询库定义：show databases; 查看所有库       show create database 库名

    修改库定义：alter database 库民 charset utf8; 一般从小字符集改成大字符集。改不了库名

    删除库：drop database 库名；

 2. 表定义： 

    1.创建表定义

    ​	建表规范：

    ​		1.表名：小写字母，不能数字开头，和业务有关，不能太长，不能和保留字段冲突

    ​        2.必须设置引擎和字符集

    ​        3.数据类型：合适，简短，足够

    ​        4.必须有主键

    ​        5.每列尽量设置notnull

    ​        6.每个列要有注释

    2.查询表定义

    ​	show tables; 看数据库下所有的表名

    ​	desc 表名;查看表结构

    ​	show create table 表名

    3.修改表定义

    	1. 添加一个列： alter table 表名 add column 列名 char(11) not null unique key comment '想添加的信息';
     	2. 修改列数据类型：alter table 表明 **modify** 列名 新类型 not null unique key comment '手机号'
     	3. 删除手机号列： alter table 表名 drop 列名；

    4.删除表定义

    ​	drop table 表名

DDL操作对生产的影响：比如修改表

​	在Mysql中，DDL语句在对表进行操作时，是要锁“元数据表”的，此时所有类的修改命令无法正常运行，夯住。因为元数据表里存的是表属性，创建表，删除表，修改表都会锁住元数据表。所以对于大表，业务繁忙的表进行线上DDL操作必须要谨慎，对大表的修改会比较慢，锁住的时间也会比较久。尽量避开业务繁忙期。

​	实在需要进行onlineDDL的，建议使用pt-osc工具，减少锁表的影响

###### 4.4.2.2 DCL

主要就是grant和revoke

DDL，DCL实在对元数据进行操作，DML是对表数据进行操作

###### 4.4.2.3 DML

- insert

insert into 表名（列名）values (数据行1) ,（数据行2）,……            列名也可以省略，可以调整顺序，但是要跟数据一一对应

- update

  更新指定数据行的值，一般都会有where条件

  update 表名 set 列名= ‘新数据’  where id = 6;不加where会把所有列名的值都改成新数据

- delete

  一般也要配合where条件

  delete from 表名 where id= 9 ；

  扩展：

  伪删除，指并不是想真的删除这条数据，以免将来需要回退。原理就是让这条数据查不到，方式就是修改表结构，增加一个状态列表

  alter table 表名 add column state tinyint not null default 1;

  原来是delete操作，现在将state改为0就行了

  alter table 表名 set state = 0 where id = 1;

  删除命令的区别：

  delete from student, drop table student. truncate table student 区别？

  delete语句是逐行进行删除，逻辑性的操作。如果数据行很多，操作很慢。只是在存储层面打标记，磁盘空间不会立即释放，自增的值也不会释放。HWM高水位线不会降低：自增值不会较少

  drop table 表名：将表结构（元数据）和数据行物理层删除，属于DDL 

  truncate table 表名：清空表段中所有数据页。磁盘空间立即释放，HWM高水位线会降低

- select

功能:获取表中的数据行

select单独使用（Mysql独有）：

1. ​	select配合内置函数使用（其他数据库需要在后面加上from dual才能调用函数）

   select now();					查看时间

   select database();           当前使用的库

   select concat('hello world!');      命令拼接用。实例如下

   ​			select concat(user,"@",host) from mysql.user;

   select user();                    查看当前登入的用户                

   所有的函数，可以通过help contents 中的help function里看

2. ​    计算（很少使用）

3. ​    查询参数(MYsql 独有)

   select @@port；            查询端口号

   select @@datadir；       查看路径

   select  @@socket；

   show variables;              显示所有的参数      

   show variables like "%trx%"      模糊查询   

select标准用法（兼容所有数据库的用法）

1. 默认单表执行顺序：select,from,where,group by,having,order by,limit


​		from        表1，表2

​		where      判断条件1    判断条件2

​		group by   条件列1      条件列2

​		having      过滤条件1    过滤条件2           和判断条件类似

​		order by      条件列1    条件列2

​		limit            限制

2.  select 配合from 字句的使用：

​		语法： select 列 from 表；

​      select 配合 where 字句使用:

 where 要配合判断符号： =，>,<,>=,<=,!=

where 配合like进行模糊查询，查询国家代号以CH开头的城市信息

​		select * from world.city where countrycode like 'CH%';

​		注意：1模糊查询不要出现%在开头的情况，因为mysql会不走索引

​					2like只能用于字符串

​	where配合逻辑符号AND OR

​		例子：查询中国人口大于100W的城市

​			select * from city where countrycode = 'CHN' and population>50000000;

​					查询中国或美国的城市信息；

​			select * from city where countrycod= 'CHN' or countrycode = 'USA';

​					查询中国和美国人口大于500W的城市；

​			select * from city where countrycode in ('CHN','USA') and population >=5000000;这里先获得了中国美国城市的并集，然后再将整个并集与人口大于500000W的城市做交集。

​	3. where 配合between and使用

​		例子：查询城市人口信息在100W到200W之间的城市。

​		select * from city where population betweent 1000000 and 200000;

​         select + from + where + group by:

​	           group by 分组必然是配合聚合函数（max（）,min(),avg(),count(),sum(),group_concat()）使用

​	操作顺序，先把要查询的列都取出来，然后再根据group by的条件1进行排序操作，然后进行去重，把条件1里重复的放在一起（这里就需要用到聚合函数）

​		例子：统计city中，每个国家城市数

​		select countrycode, count(id) from city group by conutrycode

​		例子：统计中国每个省份的城市个数

​		select countrycode, disctrict, count(id) from city where countrycode = 'CHN' group by district;

​		例子：统计每个国家的总人口

​		select countrycode,sum(population) from city group by countrycode;

​		例子：统计中国，每个省的总人口

​		select district sum(population) from city where countrycode = 'CHN' group by district;

​		例子：统计中国，每个省的总人口，城市个数，城市名列表

 		select district,sum(population),count(id) from city where countrycode ='CHN' group by district;

​		在查询中添加name会报错：sql_mode = only_full_group。意思是在select list 中的列，要么在group by中，要么在聚合函数中出现，不然就会导致mysql显示 一行多应多行的问题 。

​		delete，drop, truncate 如果不小心删除了，可以恢复码？

​		通过备份+日志，恢复数据。也可以通过延时从库进行回复

​		delete可以通过日志就可以回复，因为它是逐行删除，会在日志中都记录

having语句

​		作用：与where配合，进行后过滤

​		例子：统计中国，每个省的总人口，只显示总人口数大于500W的(并按总人口从大到小排序输出)

​		select district, sum(population) from city where countrycode = 'CHN' group by district having sum(population) > 5000000（order by sum(population) DESC); 默认排序是从小大大，加DESC是从大到小



limit 应用

作用：用于结果分页显示，一般是配合排序来做的

例子：统计中国，每个省的总人口，只显示总人口数大于500W的，并按总人口从大到小排序输出，只显示前5名

select district, sum(population) from city where countrycode = 'CHN' group by district having sum(population) > 5000000 order by sum(population) DESC limit 5;

显示6-10名的： limit 5,5 = limit 5 offset 5        意思是跳过前5名，再显示5名



多表连接查询

作用：我们的查询需求，来自于多张表，单张表无法满足

多表连接查询类型：

- 笛卡尔乘积(最简单的，没有意义)

  ​	select * from teacher,course;（select * from teacher join course;）

![image-20200613093442561](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200613093442561.png)

​			两张表直接相乘

- 内连接(应用最广泛)

  ​	A join B on A.xx = B.yy

  ​	在笛卡尔乘积的基础上，将关联的数据放在一起

  ​	select city.name, country.name, city.population from city join country on city.countrycode= country.code where city.population <100;

  ![image-20200615170956237](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200615170956237.png)

- 外连接(强制驱动表)

​	left join(取左表所有数据+右表满足条件的数据)

​	select city.name, country.name, city.population 

​	from city left join country 

​	on city.countrycode= country.code and city.population <100;

![image-20200615171116899](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200615171116899.png)

​	right join(取右表所有数据+左表满足条件的数据)

​	select city.name, country.name, city.population 

​	from city right join country 

​	on city.countrycode= country.code and city.population <100;

​	![image-20200615171359966](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200615171359966.png)

多表连接查询例子：

1. 查询wuhan这个城市，国家名，城市名，城市人口数，国土面积

   select  city.name, country.name, city.population, country.surfaceArea from city left join country on country.code = city.countrycode where city.name ="wuhan";

2. 统计zhang4学习了几门课

   select student.sname, count(sc.cno) from student left join sc on student.sno = sc.sno where student.sname = 'zhang4'

   group by student.sno;;

3. 查询zhang4学习的课程名称有哪些

   ![image-20200615182313376](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200615182313376.png)

   select student.sname, sc.cno, course.cname
   from student join sc on student.sno = sc.sno
   join course on sc.cno = course.cno
   where student.sname='zhang4';

   如果想把同一个人的课程放在一行显示，就需要group_concat

   select student.sname, group_concat(course.cname)
   from student join sc on student.sno = sc.sno
   join course on sc.cno = course.cno
   where student.sname='zhang4';

4. 查询oldguo老师教的学生名

   查询的列：teacher.tname, student.sname

   关联的条件： 

   ​	techer	    teacher.tno

   ​	course	   teacher.tno =  course.tno

   ​		sc		    course.cno =  sc.cno

   ​	student	   sc.sno = student.sno

   

   select concat(teacher.tname,"_",teacher.tno),

   group_concat(student.sname)
   from teacher join course 
   on teacher.tno = course.tno
   join sc on course.cno = sc.cno
   join student on sc.sno = student.sno
   where teacher.tname = 'oldguo'
   group by teacher.tno,teacher.tname;

   

5. 查询oldguo老师教的课程平均分

   ​	关联条件： teacher.tno

   ​	course:      teacher.tno = couse.tno

   ​	sc         :     course.cno = sc.cno

   

   select teacher.tname, avg(sc.score)
   from teacher join course on
   teacher.tno = course.tno
   join sc on
   course.cno = sc.cno
   where teacher.tname = 'oldguo';

   ​	

6. 每位老师所教课程的平均分，并按平均分排序

   

   select teacher.tname, avg(sc.score) as average
   from teacher join course on
   teacher.tno = course.tno
   join sc on
   course.cno = sc.cno
   group by teacher.tno order by average;

   

7. 查询oldguo所教不及格学生的姓名

   select teacher.tname, student.sname
   from teacher join course
   on teacher.tno = course.tno
   join sc
   on course.cno = sc.cno 
   join student
   on sc.sno= student.sno
   where teacher.tname='oldguo' and sc.score <=60;

8. 查询所有老师所教学生不及格的信息

   select teacher.tname, student.sname
   from teacher join course
   on teacher.tno = course.tno
   join sc
   on course.cno = sc.cno 
   join student
   on sc.sno= student.sno
   where sc.score <=60;

9. 查询平均成绩大于60分的同学的学号和平均成绩

   select student.sno, student.sname, avg(sc.score) as average
   from student join sc
   on student.sno = sc.sno
   group by student.sno having average>60;

10. 查询所有同学的学号、姓名、选课数、总成绩

    select student.sno, student.sname, count(course.cno), sum(sc.score)
    from student join sc
    on student.sno = sc.sno
    join course
    on sc.cno = course.cno
    group by student.sno;

11. 查询各科成绩最高和最低的分：以如下形式显示：课程ID，最高分，最低分。

    select course.cname, max(sc.score), min(sc.score)
    from course join sc
    on course.cno = sc.cno
    group by course.cno;

12. 统计各位老师所教课程的及格率

    

13. 查询没门课程被选秀的学生数

14. 查询出只选了一门课程的全部学生的学号和姓名

15. 查询选修课程门数超过1门的学生信息

16. 统计每门课程：优秀（85），良好（70-85），一般（60-70），不及格（小于60）的学生列表

17. 查询平均成绩大于85的所有学生的学号、姓名、和平均成绩



case when then end:

select case when sc.score>90 then sc.score end from sc;



外连接底层原理：next loop，以left join左边的表（作为驱动表）做for遍历循环，匹配两表中符合条件的数据并拼接。

驱动表是什么？

在多表连接当中，承当for循环中外层循环的角色，此时MySQL会拿着驱动表的每个满足条件的关联列的值，依次去找内循环中的关联值。

建议，将数据行数少的表设置为驱动表，可以降低外循环（next loop）的次数，并且where条件会执行，然后拼接

对于内连接来说，我们没法控制驱动表是谁，完全由优化器决定，如果要人为干预，就需要将内连接写成外连接的方式。



- 别名

  列别名： 一般我们在列后面添加as给列起别名，但是注意列别名不能在where条件里使用，因为where条件是在select之前执行的。别名可以在group后使用（having, order by）

  表别名可以在全部语句使用

- distinct 应用 去重

​	select distinct(countrycode) from world.city;

- union和union all(联合查询)

例子:查询中国和美国的城市信息

1. select * from world.city where countrycode = 'CHN' or countrycode = 'USA';

2. select * from world.city where countrycode in ('CHN' , 'USA');

3. select * from world.city where countrycode = 'CHN'

   union all

   select * from world.city where countrycode = 'USA';

union和union all区别

union： 聚合两个结果集，会自动进行结果集去重复

union all：不会去重复

###### 4.4.2.4 DQL



#### 4.5 元数据获取

##### 4.5.1show语句的应用：

- show database; 
- show tables;
- show tables from world;
- show processlist;
- show charset;
- show collation;
- show engines;
- show privileges;
- show grants for;
- show create database;
- show create table;
- show index from 表明;
- show engine innodb status; 查询innodb引擎状态
- show status; 查看数据库状态信息
- show status like '%%'; 模糊查询数据库状态
- show variables; 查看所有数据库参数
- show variables like '%%';
- show binary logs; 查询所有二进制文件信息
- show binlog events in   查询二进制日志事件
- show master status 查询二进制日志的位置点信息
- show slave status 查询从库信息
- show relaylog events in 查看中继日志事件

可以使用help show查看所有的show命令

##### 4.5.2 逻辑表的组成

逻辑表与以下数据相关

1. 数据字典：表中列的定义信息（myisam以frm文件，innodb(8.0以前，frm和ibdata1都会存)）
2. 数据行记录（innodb以ibd文件结尾，myisam以MYD结尾）
3. 索引（myisam以MYI文件里，innodb直接存在idb文件中）
4. 数据库状态：存在mysql，PS，SYS，I_S，P_S等库里
5. 权限:存在mysql库，user,db，table，coulum
6. 日志：专门的日志文件

##### 4.5.3 information_schema:视图

用来帮助我们查询数据字典，权限，数据库状态的信息

介绍：每次数据库启动，会自动在内存中生成I_S，生成查询Mysql部分元数据信息图

视图是什么： select 语句的执行方法，不保存数据本身。相当于把语句起了一个别名，方便我们查询，主要用于我们经常会查询的表，I_S里面保存的就是视图

```mysql
create view v_select as select * from world.city;
select * from v_select;
```

###### 4.5.3.1 I_S.tables视图(也可以理解成虚拟表)

作用：保存了所有表的数据字典信息。

desc tables;

常用的几个字段：

- TABLE_SCHEMA     表所在的库
- TABLE_NAME          表名
- ENGINE                    表引擎
- TABLE_ROWS           表的数据行（不是特别实时）
- AVG_ROW_LENGTH     平均行长度
- DATA_LENGTH            表使用的存储空间大小（不是特别实时）
- INDEX_LENGTH          表的索引所占空间大小
- DATA_FREE                  表中是否有碎片

I_S.tables 应用案例

- 数据库资产统计(可以直观显示数据库的使用情况)

  1. 统计每个库下所有表的个数，表名

     ```mysql
     select table_schema,count(table_name),group_concat(table_name) from information_schema.tables group by table_schema; 
     ```

  2. 统计每个库的占用空间总大小（所有表的空间之和）

     一张表大小 = AVG_ROW_LENGTH*TABLE_ROWS+INDEX_LENGTH

     ```mysql
     select table_schema, sum(avg_row_length*table_rows+index_length)
     from information_schema.tables
     group by table_schema;
     ```

     一张表大小 = DATA_LENGTH

     ```mysql
     select table_schema,sum(DATA_LENGTH)
     from information_schema.tables
     group by table_schema;
     ```

  3. 查询数据库（系统库除外，我们自己创建的业务库），所有非innodb表

     ```mysql
     select table_schema,table_name from information_schema.tables where engine !='InnoDB' and table_schema not in('sys','performance_schema','information_schema','mysql');
     ```

  4. 把非innodb的表转换为innodb的表(使用拼接语句)

     ```mysql
     select concat ("alter table ",table_schema,".",table_name," engine=innodb;")
     from information_schema.tables 
     where engine != 'innodb'
     and table_schema not in ('sys','performance_schema','information_schema','mysql')
     into outfile 'D:/Desktop/sqldata/ss.sql';
     ```

     如果报错1290，则需要修改保存数据的路径

## 五. 基础优化- 索引及执行计划

### 5.1 Mysql 索引类型

- Btree索引
- Rtree索引
- HAH索引
- Fulltext全文索引
- GIS地理位置索引

### 5.2 B+ Tree结构

查找算法介绍：遍历---->二叉树- -->平衡二叉树--->Balance Tree

B树种类

- Btree 
- B+tree
- B*tree（ innodb使用的）

页节点先生成>>>然后到支节点>>>>最后生成根节点

叶子节点每个16kb正好对应mysql页的容量大小

支节点存的是下层节点的主键范围

Btree查找算法 ![image-20200616192634480](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200616192634480.png)

假设要找28，就会先进入根节点，找到在25-33之间，然后找25的节点，依次往下找。

B+树是在叶子节点上增加了双向指针，每个叶子节点除了自身的数据外还存有相邻两个叶子节点的数据范围

B*树不仅在叶子节点上加，还在支节点上加了双向指针

### 5.3 B+tree索引构建过程

#### 5.3.1 聚簇索引Btree结构（Innodb独有）

区（extent）= 簇 =64个pages = 1M

构建前提：

1. 建表时，指定了主键。MySQL innodb会将主键自动生成聚簇索引，比如ID not null primary key
2. 没有指定主键，自动选择唯一键（unique）的列，作为聚簇索引
3. 以上都没有，就生成隐藏的聚簇索引

作用：

​	有了聚簇索引后，以后插入的数据行，在同一个区内，都会按照ID值的顺序，有序在磁盘存储数据。

​	所以也把innodb表，称为聚簇索引组织存储数据表

​	以例子来说明：  select * from t1 where id = 21

![image-20200617060543574](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200617060543574.png)

有聚簇索引的情况： 先到根节点遍历找到主键id为21所在的支节点，然后从支节点出发找到叶子节点，拿到内存中。一共会发生3次IO

没有索引的情况，会将所有叶子页放到内存中，对叶子节点进行遍历，如果表的数据非常大，性能会非常差。

最小的表也至少包含2个page， 一个是叶子节点，一个是根节点。

如果拿非聚簇索引id列作条件，就会直接将整表数据全部加载到内存，非常低效，所以就出现了辅助索引

#### 5.3.2 辅助索引Btree结构

辅助索引的细分：

1. 单列索引     select * from t1 where name ='s' 如上图

2. 联合索引     select * from t1 where name ='s' and gender='m'

3. 前缀索引    

   

**单列索引**：使用普通列作为条件构建的索引（select * from t1 where name ='s'）

作用：优化**非聚簇索引列**作为条件查询。需要人为创建（alter table t1 add index idx(name)）

构建过程：将主键列和辅助索引列拿出来按照name进行排序，并生成相应的叶子节点页，然后把以name列的范围，生成支节点

![image-20200617064510436](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200617064510436.png)

找到s 对应的主键id值后，再通过聚簇索引找到具体的数据行（这步操作叫做回表查询） 。一般都会有回表，除非我们只查询聚簇索引和辅助索引所在的数据，比如id和name。那么可以直接拿出来，如果要查整行数据，就必须回表

减少回表的方式：

1. 查询尽可能使用ID主键查询
2. 设计合理的联合索引并完全覆盖查询条件
3. 精确的擦汗寻条件
4. 优化器算法

**联合索引**：select * from t1 where name ='s' and gender='m'，

以name列为主排序，gender为辅。

建索引语句： alter table t1 add idx(name,gender)

叶子节点会将主键，name，gender3列拿出来生成，支节点只会拿name出来（带叶子节点的指针）生成支节点。

注意：

1. 最左原则，比如有一个联合索引 idx（a,b,c），查询条件中必须包含最左列a（位置没有关系），不然就不会走联合索引，因为索引支节点就是以a列的数据来建立的
2. 建立联合索引的时候，一定要选择重复值少的列作为最左列

**前缀索引：** 一个数据的值特别长，就会影响索引树高度，导致索引应用时，需要读取更多的索引数据页。所以可以选择大字段的前面部分字符作为索引列生成条件。

Mysql中建议索引树高度3-4层

#### 5.3.3 索引树高度影响因素

1. 索引字段较长： 前缀索引
2. 数据行过多： 分布式架构、分区表、归档表（pt-archive工具）
3. 数据类型：不合适的数据类型也会影响

#### 5.3.4 索引的管理命令

1. 什么时候创建索引？

   按照业务语句的需求创建合适的索引，并不是将所有列都建立索引，（因为每次更新数据，都需要导致索引的变动，可能会阻塞其他的操作）索引不是越多越好。

   将索引建立在经常做where、group by、order by、 join on的条件列上。

   为什么不能乱建索引？

   1. 如果冗余索引过多，表的数据变化的时候，很有可能会导致索引频繁更新。这样会阻塞很多正常业务的请求，维护索引树的成本也会极高
   2. 索引过多，会导致优化器选择出现偏差。

2. 管理命令

   1. 查询表的索引情况

      mysql>desc 表名；

      key: PRI聚簇索引    MUL辅助索引     UNI唯一索引

      mysql>show index from 表名

   2. 建索引： 

      分析业务语句:发现name列经常被作为条件查询

      单表/联合索引：alter table **city** add index idx_na(**name**);

      前缀索引：alter table **city** add index idx_d(name**(5)**); 前5个字符

   3. 删索引

      alter table **city** drop index **idx_na**;

更新数据时，对索引的影响。

insert，update，delete一行数据，聚簇索引会立即更新，辅助索引不是实时更新（会先把辅助索引的更新放到changebuffer中，等使用查询后，更新才会合并落到磁盘上）

#### 5.3.5 执行计划

1. 什么是执行计划？其实就是执行语句的方案，主要有两种方式，1）是全表扫描。2）是索引
2. 执行计划分析，分析的是优化器按照内置的cost计算模型，最终选择后的执行计划。

一.查看执行计划：

​	explain select * from ……;

![image-20200617191437003](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200617191437003.png)

​	显示结果分析：

- table:此次查询涉及到的表
- type：查询类型（全表扫，索引扫）
- possible_keys: 所有可能的索引方案
- key： 最后选择的索引
- key_len： 索引覆盖长度
- rows：此次查询需要扫描的行数
- Extra：额外信息

​	显示详细介绍：

- table

  - 此次查询涉及到的表（用来分析哪张表比较慢）

    ```mysql
    explain select country.name, city.name from city join country on city.countrycode = country.code;
    ```

    ![image-20200617193251008](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200617193251008.png)

    从接过来看country没有走索引，可以优化

- type 查询类型

  - all： 不走索引全表扫描的情况

    select * from city;

    select * from city where 1=1

    select * from city where countrycode like '%ch%'

    select * from city where country not in ('CH')    

  - 索引扫描(性能依次升高)：

    - index：全索引扫描，获取整颗索引数

      ```mysql
      desc select countrycode from world.city
      ```

      查询所有countrycode的值，而且这个列上正好有索引

    - range： 在索引列上进行范围查询 ><>=<= like in or between and

      ```mysql
      desc select * from city where id<10;
      ```

      ```mysql
      desc select * from city where countrycode in ('CHN','USA');
      ```

      ![image-20200617195125310](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200617195125310.png)

      in 可以改写为union all

      ```mysql
      desc select * from city where countrycode = 'CHN'
      union all
      desc select * from city where countrycode = 'USA'
      ```

      ![image-20200617195305024](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200617195305024.png)

    - ref:  辅助索引的等值查询

      ```mysql
      desc select * from city where countrycode='CHN'
      ```

    - eq_ref: 多表连接中，非驱动表连接条件是主键或唯一键

      ```mysql
      desc select country.name, city.name
      from city join country
      on city.countrycode = country.code
      where city.countrycode = 'CHN';   
      ```

      ![image-20200617213010295](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200617213010295.png)

      country.code就是非驱动表country的主键

    - const(system)主键索引等值查询

      ```mysql
      desc select * from city where id =10
      ```

- possible_key, key

  possilbe_key可能会走的索引，所有和此次查询有关的索引

  key：此次查询所选择的索引

- key_len:  联合索引的覆盖长度

  对于联合索引，index(a,b,c)，我们希望我们将来的查询语句对于联合索引应用的越充分越好。key_len可以帮助检查联合索引走了几部分

  

  key_len计算：

  假设某条查询可以完全覆盖三列联合索引，例如：

  select * from t1 where a = and b= and c=;

  key_len = a 长度+ b长度 +c长度

  长度指的是什么？列的最大储值字节长度

  长度受到：数据类型，字符集影响

  数字列长度：

  ​							not null           长度             没有not null的长度

  ​		tinyint         1个字节             1                             1+1

  ​		int                4个字节             4                             4+1

  ​		bigint           8个字节             8                             8+1

  字符列长度：    

  ​				utf8         1个字符最多占3个字节

  ​                                                       not null               没有not null

  ​				char(10)                           3\*10                            3\*10+1

  ​				varchar(10)                     3\*10+2                        3*10+2+1

- extra

  using filesort: 表时此次查询使用到了文件排序，说明在查询中产生了排序操作：order by group by distinct。需要查一下是否有索引，并且根据查询条件（如果是多字句条件就需要建联合索引）来修改索引。比如
  
  ```mysq
  select * from city where countrycode = 'CHN' order by popuplation;
  ```
  
  这句话里有两个条件列，countrycode 和population，就需要在这两个条件上建立联合索引

#### 5.3.6 索引应用规范

说明：为了使索引的使用效率更高，在创建索引时，必须考虑在哪些字段上创建索引和创建什么类型的索引。

原则：

1. 建表时一定要有主键，一般是非空唯一数字列

2. 尽量选择唯一性索引（联合索引中的最左原则）

3. 尽量使用前缀索引

4. 限制索引的数目，（1索引需要更多存储空间。2修改表结构时会影响性能）

   percona-toolkit工具，可以分析索引是否重复（比如单列索引会跟联合索引重复）

5. 尽量少在经常更新（update）值的列上建索引

6. 在经常做where条件的列上，order by, group by, join on, disctinct 建立索引

#### 5.3.7 不走索引的情况

1. 没有查询条件（select * from table），或者查询条件列没有建立索引

2. 查询结果是原表中的而大部分数据，占到15-30%，优化器会觉得没有必要走索引，这跟数据库的预读能力有关（预读指读取数据页的时候，会连带读取附近的页）

   怎么改写？判断有没有更好的方式，没有就考虑不要使用mysql，将数据放到redis中

3. 索引本身失效，统计数据不真实

   索引和表有自我维护的能力，如果表的内容频繁变化，统计信息不准确，过旧。就可能会导致索引失效。

   可以使用以下语句查看表索引的修改统计信息情况（这张表在mysql库下，它不是实时更新的）

   ```mysql
   select * from innodb_table_stats;
   ```

   比如：一条select语句平时很快，突然变慢了。就可能

   解决方法：删除索引并重建

4. 在查询条件中使用了函数，或者算数 如 select * from test where id-1=9;

5. 隐式转换：条件语句中的数据类型发生了隐式转换，如下

   telnum是char类型，但是使用数字做条件的时候就不会走telnum列上索引，因为在内部发生了函数计算

![image-20200618061327351](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200618061327351.png)

![image-20200618061355163](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200618061355163.png)

6. <>,not in 不走索引（辅助索引）。主键索引会走range索引

   or 或 in 尽量可以改成union，使用不同的条件进行压力测试

7. like "%_" 百分号在前面的模糊查询不走索引

   如果业务中有大量的模糊查询，建议使用mangodb或elasticsearch专门做服务的数据库

#### 5.3.8 优化器针对索引的算法

怎么看算法看起状态：select @@optimizer_switch;

修改算法开关：1.从配置文件修改

​							2. set global optimizer_switch='算法名=on/off'

1. Mysql索引的自优化-AHI（自适应哈希索引）

   用于生成经常被查询的数据页，把这些页的哈希值存在内存中
   
   MySQL的innodb引擎，能够创建的只有B树
   
2. ICP

index(a,b,c)

select * from t1 where a =  and b = and c = 就会完全走联合索引

```mysql
select * from t1 where a = and c =
```

如果没有ICP，这条语句的执行逻辑是根据a条件从磁盘上取出数据，然后将c条件应用在取出来的数据页上再查一遍。有了ICP，则会在引擎层使用c条件先过滤一次，再去磁盘取数据

下图是不走ICP的

![image-20200619054832099](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200619054832099.png)

有ICP的

![image-20200619054939901](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200619054939901.png)

3. MRR:multi  range read

   如果要使用mrr，需要将mrr_cost_based关闭，不然基本上不会用这个算法

   使用过程：

   ![image-20200619062318104](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200619062318104.png)

   没有MRR的情况是，每次匹配到辅助索引的条件就回表一次，如下

   ![image-20200619063404397](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200619063404397.png)

![image-20200619063234093](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200619063234093.png)

有了MMR，拿到辅助索引页数据后，先基于主键值排序，然后回标再走聚簇索引，这样有可能会减少回表次数，比如id1，和id2是在同一个聚簇索引页上：

![image-20200619063430998](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200619063430998.png)

![image-20200619063319426](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200619063319426.png)

4. SNLJ     在多表查询的时候，所有表的查询条件上都没有索引的情况下使用

   ![image-20200619070354754](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200619070354754.png)

   执行逻辑：

   ​	每次找到t1表中的匹配数据行，就会去t2表中找匹配的数据，然后将找到的数据发给客户

   ![image-20200619064930366](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200619064930366.png)

基于这种情况，就会尽量选择小的表作为t1驱动表，也可以通过left join 强制驱动表

5. BNLJ（目前所有的join多表操作都是使用这种方式）下图是加入了BKA的

   ![image-20200619070245015](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200619070245015.png)

   执行逻辑：把t1表中的所有匹配数据都加入到join buffer中，然后去t2表中查找匹配的数据

   主要优化了，CPU消耗，减少了IO次数

   但是还是有缺陷：**如上上图所**示，如果不排序的话就会对同一个数据页多次IO（上图是排过序BKA算法）

6. BKA 算法（前提是非驱动表的条件是有辅助索引的），在BNL的基础上加入MRR算法，对join buffer中t1表数据进行排序（基于t2表的辅助索引顺序）

   如果非驱动表的条件列是主键或者唯一列的话，就不需要走BKA了，因为数据行是唯一的，不用进行第二次匹配

## 六. MySQL 存储引擎体系结构

InnoDB核心特性

![image-20200620103332276](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200620103332276.png)

```php
1、事务（Transaction）
2、MVCC（Multi-Version Concurrency Control多版本并发控制）
3、行级锁(Row-level Lock)
4、ACSR（Auto Crash Safey Recovery）自动的故障安全恢复
5、支持热备份(Hot Backup)
6、Replication: Group Commit , GTID (Global Transaction ID) ,多线程(Multi-Threads-SQL ) 
```

### 6.1 宏观结构

下面是5.7的结构，不同版本ibdata1的数据不一样

![image-20200620100406602](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200620100406602.png)

![image-20200620100439558](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200620100439558.png)

- .frm: 数据字典信息（列的定义和属性）

- .ibd（独立表空间）：数据行和索引

- ibdata1（共享表空间）：数据字典信息，undo（回滚日志）, double write, change buffer(在做insert等修改操作时，会将辅助索引更新临时存到change buffer中，之后再进行merge，挂到磁盘)

  - 5.5版本： ibdata1中还会存储临时表数据 + 用户数据（数据行+索引）

  - 5.6版本：ibdata1还会存储零时表数据，用户数据被拿出来了

  - 8.0版本：ibdata1取消存储数据字典信息

    趋势好像是在慢慢将ibdata1瘦身，把关键数据独立出来，解耦

- ib_logfile 0 ~ib_logfile 1:Innodb事务重做日志（Redoblog）

- ibtml:临时表空间文件，用在排序、分组、多表连接、子查询、逻辑备份等时候。

- ib_buffer_pool:正常关闭数据库的时候，存储缓冲区的热数据

所以：仅仅拷贝ibd和frm文件到新的数据库，是无法正常使用的

### 6.2 InnoDB微观结构

#### 6.2.1 磁盘

1. 表空间

   什么是表空间？为了解决存储空间扩展的问题，相当于在MySQL和文件系统之间加了一个表空间，

   MySQL表空间类型（5.5版本以后引入）：

   共享表空间：

   ​	5.5版本后引入了共享表空间（ibdata1），用来存储系统数据，日志，undo，临时表，用户数据和索引。这样导致了有的盘IO非常集中，有的盘又很空闲

   独立表空间：

   ​	为了解决5.5表空间的问题，5.6版本默认独立表空间。一个表对应一个ibd文件

   通用（普通）表空间：跟oracle一致的表空间管理模式

   通用表空间：

   undo表空间：用来存储undo回滚日志

   临时表空间：存世临时表（5.7独立出来）

2. 表空间管理

   用户数据默认的存储方式，独立表空间模式。独立表空间和共享表空间是可以切换的。

   - 查看默认表空间模式：select @@innodb_file_per_table; 1代表独立表空间。0代表共享表空间

   - 如何切换： set global innodb_file_per_table=0;重新登入会话

     修改完成之后，只影响新创建的一些表

   - 如何扩展共享表空间大小和个数？

     通常在初始化数据库时，在配置文件中就设定好。

     也可以在运行的数据库上扩展多个ibdata文件

     

3. 表存储到表空间，表空间有物理结构连续的段，段有多个区，区包含多个页

### 6.3 事务日志

#### 6.3.1 redo log(重做日志)：

​	文件日志：ib_logfile 0~1

​	查看配置信息：show variables like "%innodb_log%";

![image-20200620104354691](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200620104354691.png)

​	控制参数：

​		innodb_log_file_size   设置文件大小

​		innodb_log_files_in_group    设置文件个数

​		innodb_log_group_home_dir  设置存储位置

​	功能：

​		用来存储，mysql在做修改类操作（insert,updata等）操作时的数据页变化及版本号LSN，属于物理日志。

​		默认两个文件存储redo，循环覆盖使用。（第一个文件用完用第二个，第二个用来再循环回第一个，直接覆盖）

#### 6.2.1 undo log(回滚日志)：

1. 默认文件位置： ibdata（5.7默认），有一部分在ibtmp1

2. 控制参数 （最关键的）：show variables like "%segments%";回滚段个数。

3. 功能：

   用来存储回滚日志的

   提供多版本的读写

   提供回滚功能

### 6.2 内存

#### 6.2.1 数据内存区域

1. 共享内存区

   buffer_pool 缓冲区池

   select @@innodb_buffer_pool_size;查看大小

   功能：缓冲数据页和索引页

2. 会话内存区

   （1.1）会话内存区域（每个会话独有的内存区域）

   ​		join_buffer_size

   ​		key_buffer_size

   ​		read_buffer_size

   ​		read_rnd_buffer_size

   ​		sort_buffer_size

​	

#### 6.2.2 日志

​	innodb_log_buffer_size

​	功能：负责redo日志的缓冲

## 七. innoDB核心特性详解

### 7.1 事务ACID特性

A: atomicity      原子性

​	在一个事务工作单元中，所有标准事务语句（DML），要么全成功，要么全回滚

C: consistency    一致性

​	事务发生前，中，后都应该保证数据是始终一致的状态，MySQL的各项功能设计，都是要保证一致性

I:   isolation      隔离性

​	MySQL可以支持多事务并发工作的系统

​	A事务工作时候，不能受到其他事务的影响

D：durability    持久性

​	当事务提交成功，此次事务操作的所有数据，都要永久保存下去（已经完成落盘），不会因为宕机而失效

### 7.2 事务生命周期管理

#### 7.2.1 标准的事务控制语句

​	begin/start transaction

​	commit

​	rollback

#### 7.2.2 标准的事务语句（DML语句，在begin和commit/rollback中）

​	insert

​	update

​	delete

​	select

  	selecet @@autocommit;(默认情况下这个参数等于1，意思是不需要使用begin直接使用dml语句也会自动提交。自动提交不适合交易类应用)

​	例子：

​	begin;

​	DML1;

​	DML2;

​	rollback/commit;

事务的设置方法：如果事务不提交或者不回滚。会当值事务所使用的数据锁住，无法被其他人访问

1. 临时生效：set global autocommit =0;
2. 永久生效：写道配置文件中，重启数据库

#### 7.2.3 隐式事务控制语句

设置了autocommit =1 

DDL,DCL等非DML 标准事务语句时，会触发隐式提交 ，意思就是你在开启一个事务，并且写了DML语句后，直接写DDL语句，会把上面的事务提交完成

### 7.3 ACID如何保证

#### 7.3.1名词介绍

1. redo log 重做日志

   ib_logfile0~N      48M, 轮询使用，记录的是数据页的变化。

   redo log buffer: redo内存区域。redo的生成和使用都在内存里发生，然后写入到日志里面

2. 磁盘数据页

   ibd：存储数据行和索引（磁盘上）

   buffer pool:缓冲区池，数据和索引的缓冲

3. LSN： 日志序列号

   磁盘数据页，redo文件，buffer pool，redo buffer

   MySQL每次数据库启动，都会比较磁盘数据页和redo log的LSN，必须要求两者LSN一致数据库才能正常启动

4. WAL：write ahead log 日志优先写的方式实现持久化

   日志写完之后，数据才会写到磁盘。因为写日志会更加高效

5. 脏页：内存脏页，内存中发生了修改，没写入磁盘之前，我们把内存页称为脏页

6. CKPT:Checkpoint ,检查点，就是将脏页刷写到磁盘的动作被称为CKPT

7. TXID：事务号，InnoDB会为每一个事务生成一个事务号，伴随着整个事务生命周期

8. UNDO：存在ibdata1里，存储了事务工作过程中的回滚信息

#### 7.3.2 事务工作流程

- redo log

  1. 重做日志，是事务日志的一种
  2. 在ACID中，实现的是D持久化的而作用。对于AC也有相应的作用
  3. redo日志存在 iblogfile0~1
  4. redo buffer: 数据页的变化信息+数据页当时的LSN号
  5. LSN：日志序列号 磁盘数据页、内存数据页、redo buffer、redolog

  redo的刷新策列:当commit时，会把当前事务的redo buffer刷新到磁盘，还会顺便将一部分redo buffer中没提交的事务日志页刷新到磁盘

- 

​	