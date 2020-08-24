# Mysql常用命令

### 一. 公用命令

show processlist;    查看连接线程

show privileges;      查看权限表

show * from mysql.user\G    查看所有用户的命令权限情况

\G将行显示变为竖显示

查看字符集： show charset;

### 二. 表操作命令

desc tablename;    查看表的列信息,一般每次查询时都可以通过整个语句查看表含有哪些列

### 三 用户管理

查：select user,host from mysql.user

增：create user like@'localhost' identified by 'password';

改：修改密码： alter user like@'localhost' identified by '新密码'; 

删：drop user like@'localhost';   

授权：grant 权限1,权限2，权限3 on 对象（数据库.表） to 用户@地址 identified by ‘密码‘；

### 四 DDL语句

#### 4.1 表

建表语句：

```mysql
create table 库名.表名 (
id int not null primary key auto_increment comment'学号',
sname varchar(64) var,
age tinyint,    
gender tinyint,
addr enum('北京'，'上海'),
cometime datetime,
telnum bigint,
)engine = innodb charset=utf8mb4;
```

