# Linux

## 一.分区

一个硬盘最多只能有4个分区（主分区＋扩展分区）

扩展分区最多只有1个，而且不能写入数据，只能包含逻辑分区。

逻辑分区可以正常格式化，写入数据。

格式化又称逻辑格式化，为了在硬盘中写入文件系统，它是根据用户选定的文件系统（如FAT16,FAT32,NTFS,EXT2,EXT3,EXT4等）

格式化就是按照文件系统的规则把硬盘分成等大小的数据块，比如EXT4就是把分区分成一个个等大小（4K）的数据块block

格式化主要有两个作用，1是上面讲的将硬盘分成等大小的数据块，2是建立i节点号

当我们要找文件的时候，就会找这个文件的i节点号，从而通过i节点号来得到文件放在哪几个数据块中，然后把数据块中的数据拼凑起来

### 1.1 硬件设备名

linux中一切皆可当作是文件，所以一些硬件就有硬件设备文件名

| 硬件              | 设备文件名             |
| ----------------- | :--------------------- |
| IDE硬盘           | /dev/hd[a-d]           |
| SCSI/SATA/USB硬盘 | /dev/sd[a-p]           |
| 光驱              | /dev/cdrom或者/dev/sr0 |
| 软盘              | /dev/fd[0-1]           |
| 打印机（25针）    | /dev/lp[0-2]           |
| 打印机（USB）     | /dev/usb/lp[0-15]      |
| 鼠标              | /dev/mouse             |
|                   |                        |

比如/dev/hda1   代表IDE第一块硬盘中的第1个分区，所以硬盘有设备文件名，分区也就有文件名。两者连在一起。不过现在IDE和SCSI不怎么用了，现在大多用sda硬盘接口，传输速度块很多

### 1.2 挂载（盘符）

- 必须分区的
  - /     根分区
  - swap分区，内存的2倍，但不能超过2GB
- 推荐分区
  - /boot（启动分区，200M就够）

### 1.3 网络安装相关

![image-20200808081902728](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200808081902728.png)

- 桥接模式：代表直接用真实机的网卡配置，虚拟机和真实机在同一个网段。可以和局域往网的其他机器通信，占用一个真实网段的ip地址

![image-20200808082512394](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200808082512394.png)

- NAT模式（VMNET8）：通过VMWare虚拟网卡，只能跟真实机通信，局域网内的其他机器无法通信，不占用真实ip。并且如果真实机可以访问互联网的化，虚拟机也可以访问
- 仅主机模式（VMNET1）：类似NAT，但是只能访问真实机，不能访问互联网

linux查询网络配置: 输入ifconfig

![image-20200808083008049](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200808083008049.png)

显示出来的eth0就代表网卡，如果有多网卡就会有eth1

如何给linux机器设置网卡配：ifconfig eth0 192.168.163.130 这个ip地址必须要跟VMNET8里面的ip在同一个网段。

当使用桥接的时候，linux的ip地址就会调整到跟真实机的ip地址同一个网段。在命令行中使用ifconfig 来改变ip地址只是暂时更改，如果想要永久更改需要去配置文件里面去改配置

## 二.Linux各目录作用

命令对于linux来讲就是一个可执行的二进制文件，所以bin就代表的就是二进制文件

- /bin/
  - 存放系统命令的目录，普通和超级用户都可以执行。这个目录下的命令在单用户（类似windows的安全模式）模式下也可以执行
- /sbin/
  - 只有root用户可以执行的命令
- /usr/bin/
  - 类似/bin/   但不能在单用户模式下执行
- /usr/sbin/
  - 类似/sbin/ 但不能在单用户模式下执行
- /boot/
  - 系统启动目录，保存系统启动相关的文件，如内核文件和启动引导程序（grub）文件等。不要在里面写东西，而且要备份
- /dev/
  - 设备文件目录，用来保存所有硬件设备文件的。
- /etc/
  - 配置文件保存位置，系统内所有采用默认安装方式（rpm安装）的服务的配置文件全部都保存在这个目录当中，如用户账户和密码，服务的启动脚本，常用服务的配置文件等
- /home/
  - 普通用户的家目录。建立每个用户时，每个用户都需要有一个登入位置（命令行后面直接显示），所有普通用户就是在/home下建立一个和用户同名的目录，如用户user1就会建立一个/home/user1。而管理员用户是在/root一级目录（和/home同级）
- /lib/
  - 系统调用的函数保存位置
- /lost+found/
  - 当系统意外崩溃，产生的一些碎片就放在这里。系统启动时，fsck工具会检查这里，并修复损毁的文件系统。这个目录会在每个分区中出现，例如/lost+found/就是根分区的备份恢复目录，/boot/lost+found/就是boot目录分区的备份文件
- /media/
  - 挂载目录，系统建议用来挂载媒体设别的，如光盘
- /mnt/
  - 挂载目录，挂载u盘，移动硬盘和其他操作系统的分区
- /misc/
  - 挂载目录。系统建议用来挂载NFS服务的共享目录。系统虽然准备了三个默认挂载目录media,mnt,misc，但是到底在哪个目录挂载什么设备是由管理员决定的。加入只有一个/mnt目录，就需要在/mnt目录下再建立/mnt/cdrom挂载光盘，/mnt/usb挂载U盘
- /opt/
  - 第三方安装的软件保存位置，这个位置就是放置和安装其他软件的位置，源码包软件都可以安装到这个目录。不过现在都放在/usr/local/目录中
- /proc/
  - 虚拟文件系统，该目录中的数据并不保存在硬盘中，而是内存里。主要保存系统的内核，进程，外部设备状态，和网络状态灯。如/proc/cpuinfo/保存的就是CPU信息，/proc/devices/保存的是设备驱动的列表,/proc/filesystems/保存的是文件系统列表，/proc/net/保存网络协议信息
- /sys/
  - 虚拟文件系统，类似proc目录。主要保存内核的信息
- /root/
  - 超级用户家目录，在根目录下
- /srv/
  - 服务数据目录，一些系统服务启动后，可以在这个目录中保存所需要的数据
- /tmp/
  - 临时目录，系统存放临时文件的目录，该目录下所有用户都可以访问和写入，不建议存放重要数据，最好每次开机都要清空这个目录
- /usr/
  - UNIX SOFTWARE RESOURCE系统软件资源目录，不是存放用户数据的。系统中安装的软件大多保存在这里
- /var/
  - 动态数据保存目录。主要保存缓存，日志，以及软件运行产生的文件

## 三.linux常用命令

### 3.1 文件处理命令

命令格式： 命令 [-选项] [参数(命令操作对象)]

​			如：ls -la /etc

说        明：1）个别命令不用遵循此格式

​					2）当有多个选项时候，可以写一起

​					3）简写选项，与完整选项。如 -a等于--all，简化的只要一个-，完整的要两个--

#### 3.1.1 命令格式与命令处理命令ls

原意：list

需要权限：所有用户

描述：显示目录中的文件

语法：ls [-ald] [文件目录]

​			-a,显示所有文件，包括隐藏文件

​			-l,详细信息显示

​			-d,查看目录属性

文件一般会有三个组别：1.所有组（默认是文件创建者），2.用户组（在这个组里的人可以使用文件），3.其他组

![image-20200808123418052](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200808123418052.png)

1代表文件使用的次数

root代表所有组

root代表用户组

4096代表文件大小bit

后面是修改时间，linux中没有创建时间

-rw-r--r--是权限说明：

- -是文件类型（-二进制文件， d目录， l软连接文件，这三种是常见的）

- rw- r-- r--

  u     g   o    (u代表所有者，g是所属组，o是其他人)

  r读   w写   x执行

使用ls -ld显示当前母的信息

使用ls -i 可以显示文件的id号

#### 3.1.2 目录处理命令mkdir

原意：make directories

执行权限：所有用户

语法：mkdir -p [目录名]

​	-p代表是递归创建。如果一个目录本身不存在，但是需要在这个目录下创建一个子目录，就需要用p, 不然会报错不能创建

例如：

​	mkdir -p /tmp/Japon/boduo

​	mkdir -p /tmp/Japan/longze /tmp/Japan/cangjing 创建多个目录

其他命令：

pwd:显示目前的路径

rmdir [目录名]:删除空目录

cp复制目录或文件：cp -rp [原文件或目录] [目标目录]

​			-r复制目录 没有-r只能复制文件

​			-p保留文件原属性，比如保留文件的修改时间，不然直接复制时					间也会变

mv（剪切或更名）:

​			mv [原文件名或目录] [目标目录]

rm：   rm -rf [文件目录或文件]

​					-r 删除目录 一般rf一起使用，避免删一次就问一次

​					-f 强制执行 不会再询问

#### 3.1.3 文件处理命令

- touch 创建文件
  - touch [文件名]     linux里面文件后缀没有严格要求
- cat 显示文件内容
  - cat -n [文件名]    -n会把文件里的行号也显示出来
  - tac [文件名]    cat倒着显示
  - more [文件名]  cat如果看很大的文件，就只能看到最后一页了，所以用more。more之后可以使用f，来一页页翻页。但是more不能往上翻页
  - less [文件名]   和more类似，但是可以向上翻页。并且可以搜索（进入文件后使用斜杠/）
  - head [-n 20] [文件名]    -n指定行数。查看文件开头20行内容
  - tail [-n 20] [文件名]    查看文件末尾20行内容

#### 3.1.4 链接命令

ln -s [原文件] [目标文件] 软链接，类似window的快捷方式。

功能描述：生成链接文件，-s代表软连接，没有-s就是硬链接

特点：所有的软连接文件，所有人的权限都全开了，但真正的权限还是要看源文件

硬链接：所有的文件信息跟源文件都一样（大小，修改时间）,硬链接文件会跟随源文件同步更新。

当源文件被删除后，软连接文件就不能打开了，硬链接文件依然可以打开。硬链接文件的i节点号跟源文件的i节点号是一样的，这也是为什么它们会同步更新，但是硬链接不能跨分区，但是软连接可以。硬链接不能对目录使用，而软连接可以

### 3.2 权限管理命令

#### 3.2.1 权限管理命令 chmod

文件只有文件所有者或者root可以更改

chmod [{ugoa}{+-=}{rwx}] [文件或目录]    a表示所有用户

```shell
chmod u+x 文件名    给文件的所有者增加执行权限
chmod g=rwx        给用户组权限改为rwx
```

chmod [mode=421] [文件或目录]    ,意思就是把权限改为r---w---x

​               -R 递归修改

​	          权限的数字表示： r---4,w----2,x----1

​			  例子：   rwxrw-r--      764

```shell
chmod 640 文件    把文件权限改成rw-r-----
```

#### 3.2.2 其他权限管理命令

- chown [新所有者] [文件或目录]   更改文件所有者,changeowner.只有管理员能改，文件所有者也不能改

  ```shell
  chown like love.py 将love.py的所有者改成like
  ```

- chgrp [新用户组] [文件或目录]

- umask -S   显示创建目录时候的默认权限，文件的话会少一个x可执行权限，这是linux默认的新创建文件不能拥有可执行权限

- 直接使用 umask 会显示0022即默认目录的默认权限  ，第一个0代表特殊权限，022   --- -w- -w-   会跟777做一个逻辑与运算，将w排除。所以看到0022实际上就是755 rwxr-xr-x。如果使用umask 077 就会把目录权限改成rwx------

#### 3.2.3 文件搜索命令(尽量不要是使用，因为会使用大量的工具)

- find [搜索范围] [匹配条件]   搜索范围可以是根目录即全盘扫描，或者某个目录

  - 根据名字查找

  ```shell
  find /etc -name init 在etc目录下找到名字为init的文件，精准搜索
  find /etc -name *init* 模糊搜索
  find /etc -name init* 以init开发
  find /etc -name init???   找到init开头并且带3个字符的文件，如initabc
  find /etc -iname init？？？  不区分大小写来查找，如INITABC，initAbc
  ```

  - 根据文件大小搜索

  ```shell
  find / -size +204800 在根目录下查找大于100MB的文件，还可以用-小于，=等于。这个单位是block 512字节
  ```

  - 根据所有者来查找

  ```shell
  find /home -user shenchao 查找所有者为shenchao的文件
  ```

  - 根据访问时间

  ```shell
  find /etc -amin -5
  ```

  - 根据文件属性

  ```shell
  find /etc -cmin -5   在etc下查找5分钟内修改的文件和目录
  ```

  - 根据文件内容

  ```shell
  find /etc -mmin          文件内容modify
  ```

  - -a 并且，前后条件都要满足

  ```shell
  find /etc -size +163840 -a -size -204800 找到大于163840并且小于204800的文件
  ```

  - -O 或，只要满足一个就行

  - -type 根据文件类型查找 f文件，d目录，i软连接文件

  - -inum根据i节点查找

  - -exec/-ok找到文件后，执行后续操作

    ```shell
    find /etc -name -initab -exec ls -l {} \
    ```

- 其他搜索命令：locate，它不想find那样是全盘扫面，而是建立了一个文件资料库，搜索的时候到文件资料库里去搜索

  - locate [文件名]
    - 可以使用updatedb将资料库先更新，然后再locate。但是放在tmp目录下的不能更新到资料库里 
    - -i 可以不区分大小写搜索

- which 搜索命令所在的目录，还能显示命令的别名

  - which ls

- whereis 和which类似，不同的是它不光显示路径，还显示该命令的帮助手册

  - whereis ls

- grep 在文件中搜寻字符串匹配的行并输出 。 -i 不区分大小写， -v 排除指定字串

  - grep -iv [指定字符串] [文件]
  - grep mysql /root/install.log
  - grep -v ^# /etc/inittab   把以#号开头的行去掉

### 3.3 帮助命令

- man 获得帮助信息
  - man [命令或配置文件]，不用写绝对路径
  - man ls 显示ls的帮助信息
    - 在linux中可以通过whereis来查看命令或者配置文件帮助信息，一般man1代表的是命令帮助，man5代表配置的帮助。比如passwd就有两个帮助信息
    - ![image-20200809140449731](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200809140449731.png)
    - man 5 passwd， 通过指定man5来查看配置信息的帮助
- what is [命令] 可以通过这个命令来查看命令的解释
- apropos [配置文件] 查看配置文件的简短信息
- [命令] --help 获得命令的选项信息
- help [命令] 查看shell内置的命令帮助信息，比如cd命令就是shell内置的。用which cd找不到它的文件路径，只能使用whereis cd 来查看它的帮助信息位置。
  - 用man来查看shell内置命令，会显示shell的所有内置命令，不会单独显示某个命令的帮助信息

### 3.4 用户管理命令

- useradd [用户名] ，添加新用户
- passed [用户名]，给用户添加密码
- who，查看登入用户的信息

![image-20200809142350580](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200809142350580.png)

​			第一部分是用户，第二部分是登入地点（tty代表本地登入，pts远程终端），第三部分是登入时间

- w，更详细的显示用户的信息
- uptime,查看服务器的运行状态

### 3.5 压缩解压命令

- gzip [文件] 压缩文件，格式为.gz，gzip只能压缩文件，不能压缩目录，而且压缩完会只剩下压缩包，源文件就没了
- gunzip [压缩文件] 解压缩 或者gzip -d也可以解压缩
- tar [-zcf] [压缩后文件名] [目录] ，打包目录
  - -c 打包
  - -v 显示详细信息
  - -f 指定文件名
  - -z 打包同时压缩，可以直接生成
  - -x 是解包
  - 压缩后的格式 .tar.gz
    - tar -cf 生成.tar文件   -xf是解包
    - 使用tar -zc f 会直接生成.tar.gz文件    -zxf 是解包
- zip [-r] [压缩后文件名] [源文件或目录] 可用来压缩目录或文件。这个压缩后源文件依然存在
  - -r 压缩目录
- unzip [文件] 解压缩
- bzip2 [-k] [文件] gzip的升级版本，-k表示压缩后还会保留原文件，bzip2压缩比很高
  - bzip2 -k boduo
  - tar -cjf 生成.tar.bz2压缩包
- bunzip2 [-k] [bz2文件] 解压缩，-k会保留压缩包
  - tar -xjf 是解压.tar.bz2压缩包

### 3.6 网络命令

- write [用户]   给用户发送信息，前提是所有用户都登入在一台服务器
  - 以Ctrl+D保存结束，并发送
- wall [message] 给所有在线用户广播信息
- ping [-c] [ip地址]
  - -c是指定发送次数    ping -c 3 [ip地址]
- ifconfig [网卡名] [配置的ip地址]，
- mail [用户民]， 发送电子邮件
  - 单单使用mail，会查看当前用户有多少封邮件
- last ，  查看机器上所有的登入信息
- lastlog，查看所有用户的信息
- traceroute [url]，显示数据包到url的所有节点
- netstat [选项]，显示网络相关信息
  - -t：tcp协议
  - -u: udp协议
  - -l: 监听
  - -r：路由
  - -n：显示ip地址和端口号
    - netstat -tlun       查看本机监听的端口
    - netstat -an         查看本机所有的网络链接
    - netstat -rn          查看本机路由表
- setup，会打开网络配置界面，这个是redhat系列linux独有的，其他版本的没有。这个命令配置的ip是永久生效的
- mount -t iso9660 [设备文件名] [挂载盘符] 
  - 设备文件名都是/dev/sr0
  - 挂载盘符要先创建，/mnt/cdrom/
  - -t iso9660可以省略
- umount [设备文件名]，将挂载取消

### 3.7 关机重启命令

- shutdown [选项] 时间
  - -c:取消前一个关机命令
  - -h:关机
    - shutdown -h 20:30  晚上8.30关机，还可以跟now现在
  - -r:重启
- 其他关机命令(不常用)
  - halt
  - poweroff
  - init 0
- 其他重启命令（不常用）
  - reboot
  - init 6
    - 系统运行级别 ：0关机，1单用户（核心程序启动），2不完全多用户，3完全多用户，4未分配，5图形界面，6重启
    - cat /etc/inittab可以查看所有的运行级别，如果。
    - ![image-20200809162833998](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200809162833998.png)
    - 左下角id代表的是目前的运行级别5，图形启动，0就启动不了，3文字界面启动，6就一直在重启。所以0，6不允许被设为默认
- runlevel ，查询目前的运行级别
- logout，退出登入

## 四. Vim

Vim 没有菜单，只有命令

vim有三种模式：

- 命令模式：刚进入一个文件的时候，就是命令模式

  - a:在光标后面插入

  - A：在光标所在行尾插入

  - i：在光标所在字符前插入

  - I：在光标所在行行首插入

  - o：在光标下插入新行

  - O：在光标上插入新行

  - x：删除光标所在字符

  - nx：删除光标所在处后n个字符

  - dd：删除光标所在行，ndd删除n行

  - dG：删除光标所在行到文件末尾内如

  - D：删除光标所在处到行尾内容

  - :n1,n2d：删除指定范围的行

  - yy：复制当前行

  - nyy：复制当前行以下n行

  - dd：剪切当前行

  - ndd：剪切当前行以下n行

  - p、P：粘贴在当前光标所在行下或行上

  - r：取代光标所在字符

  - R：从光标所在处开始替换字符，嗯ESC结束

  - u：取消上一步操作

  - /string：查找string

    

- 插入模式：使用aio都可以进入插入模式

- 使用shift+：进入编辑模式

  - set number ：加上行号
  - set nonumber：取消行号
  - gg：到第一行
  - G：到最后一行
  - nG：到第n行
  - ：n：到第n行
  - $：移至行尾
  - 0：移至行首

## 五. 软件包分类

- 源码包
  - 脚本安装包（类似windows中的安装程序），这种包就是把源码包封装了一个界面，非常少见
  - .tar.gz这些包就是源码包
  - 优点：
    - 开源，可以修改源代码
    - 可以自由选择需要的功能
    - 编译安装，所以更加适合自己的系统，更加稳定，效率也更高
    - 卸载方便（直接把源码包安装的目录卸载）
  - 缺点：
    - 安装步骤较多，尤其较大的软件集合（如LAMP环境搭建），容易出现拼写错误
    - 编译时间较长，比二进制要长
    - 由于是编译安装，一旦报错新手很难解决
- 二进制包（以rpm结尾的包、系统默认包），目前最常用的经过编译的安装包
  - 二进制包就是源码包经过编译的变成二进制的包，不能看到源代码。
  - 优点：
    - 包管理系统简单，只通过几个命令就可以实现包的安装、升级、查询和卸载
    - 安装速度要快得多
  - 缺点
    - 经过编译，看不到源代码
    - 功能选择不如源码包灵活
    - 依赖性

### 5.1 rpm包

#### 5.1.1命名规则

httpd-2.2.15-15.e16.centos.1.i686.rpm

- httpd              软件包名
- 2.2.15             软件版本
- 15                   软件发布的次数
- e16.centos    适合的linux平台
- i686                适合的硬件平台
- rpm                扩展名

#### 5.1.2 rpm-命令管理

树形依赖： a->b->c ，意思是a依赖b，b依赖c。安装的时候先c，再b，后a。卸载的时候先a再b后c

环形依赖：a->b->c->a

模块依赖：模块依赖查询网站：www.rpmfind.net  可以查看rpm模块

#### 5.1.3 rpm-yum在线管理

yum直接通过文件服务器来安装，不要担心依赖问题，就跟python的包一样，会安装需要的依赖包

#### 5.1.4 rpm 命令管理

如果操作的是没有安装的软件包时（安装，或者升级），需要用包全名

如果操作的是已经安装的软件包时，使用包名，是搜索/var/lib/rpm/中的数据库

- #### rpm安装（很折磨人，建议使用yum）

安装时要先cd到rpm包所在目录

rpm -ivh 包全名    安装

- 选项
  - -i	安装
  - -v    显示详细信息
  - -h    显示进度
  - --nodeps     不检测依赖性

rpm -Uvh 包全名，升级

rpm -e 包名，卸载

rpm -q 包名，查询改包名有没有安装（不用在包所在目录）

- 选项
  - -q 查询
  - -a 所有
  - rpm -qa， 查询所有的rpm包
  - rpm -qi 包名，     查询以安装的包软件信息
  - rpm -qip 包全名，   查询未安装的包软件信息
  - rpm -ql 包名，    查询包中的文件安装位置
  - rpm -qlp 包全名， 查询到这个包打算要安装的位置
  - rpm -qf 文件名，   查询系统文件属于哪个软件包

#### 5.1.6 rpm包校验

- rpm -V [已安装包名]，主要时为了校验我们的文件有没有被修改果
  - -V校验指定RPM包中的文件
  - 如果文件没有修改，就不会显示任何信息
  - 经过修改的文件会显示以下信息：
    - S 文件大小是否改变
    - M 文件的类型或文件的权限
    - 5 文件MD5校验和是否改变（我们可以理解成文件内容有咩有改）
    - D 设备的中，从代码是否改变
    - U 文件的属主（所有者）是否改变
    - G 文件的属组是否改变
    - T 文件的修改时间是否改变
  - 还会显示文件类型
    - c 配置文件
    - d 普通文档
    - g ‘鬼’文件
    - I 授权文件
    - r 描述文件

#### 5.1.7 rpm包中提取文件（主要是为了修复损坏的配置文件）

- rpm2cpio 包全名  | cpio-idv ./bin/ls



###  5.2 yum在线管理

yum不一定要在线上，有关盘也可以进行yum 

想要使用yum的网上管理，必须要能上网才行

#### 5.2.1 网络yum源

一般yum会默认有一个国外的源，但速度比较满，所以需要配置成国内的，一般不用我们去修改什么东西

vi /etc/yum.repos.d/CentOS-Base.repo

CentOS-Base.repo 就是默认的yum源，文件里面的配置说明：

- [base] 容器说明，一定要放在[]中
- name 容器说明，可以自己随便写
- mirrorlist 镜像站点，这个可以注释掉
- baseurl yum源服务器的地址，默认是centos官方的源服务器，是可以使用的
- enabled 此容器是否有效，如果不写或写成enable=1都是生效，0不生效
- gpgcheck 如果是1是rpm数字证书生效
- gpgkey 数字证书的公钥文件保存位置，不用修改

#### 5.2.2 yum命令

- yum list                                     查询源服务器上软件包
- yum search 包名                     查询包 
- yum -y install 包名
  - -y 代表装依赖的时候自动选择yes，不然每装一个都会让你选择
- yum -y update 包名                      升级包
- yum -y remove 包名                     卸载
  - 卸载尽量不要用，因为它会自动把依赖包也删除掉，而依赖包可能被其他包也使用
- yum grouplist                                显示软件组
- yum groupinstall 软件组名
- yum groupremove

#### 5.2.3 关盘yum源搭建

步骤：

1. 挂载光盘   mount /dev/cdrom /mnt/cdrom/
2. 让网络yum失效
3. 修改光盘yum源文件

### 5.3 源码包管理

#### 5.3.1 源码包和rpm包的区别：安装位置不同

rpm包不用指定位置，源码包需要指定位置

rpm包默认安装位置

| 路径            | 目录                       |
| --------------- | -------------------------- |
| /etc/           | 配置文件安装目录           |
| /usr/bin/       | 可执行的命令安装目录       |
| /usr/lib/       | 程序所使用的函数库保存位置 |
| /usr/share/doc/ | 基本的软件使用手册保存位置 |
| /usr/share/man/ | 帮助文件保存位置           |

源码包一般是指定位置中    /usr/local/软件名/

#### 5.3.2 安装位置不同带来的影响

rpm包安装的服务可以使用系统服务管理命令（service）来管理，例如rpm包安装的apache的启动方法是：

- /etc/rc.d/init.d/httpd start（执行文件根本启动方式）
- service [服务名] start (简化的启动方式)
  - 只有在红帽系列可以用
  - service httpd start
  - service 只会去rpm的安装目录去找，所以源码包不能用service来启动

而源码包只能用绝对路径的启动方式：

- /usr/local/apache2/bin/apachectl start

#### 5.3.3 源码包安装过程

1. 安装c语言编译器
2. 下载源码包
   - http://mirror.bit.edu.cn/apache/httpd/
   - 源代码保存位置 /usr/local/src
   - 软件安装位置:/usr/local/
3. 解压源码包
4. 进入源码包
5. 按照源码包里面的INSTALL文件安装
   - ./configure 软件配置与检查
   - 完成./configure后会生成makefile文件用于编译
6. make      编译过程，将源码编译成二进制码
   - make clean 清空编译文件
7. make install              编译安装
8. 卸载源码包      不需要命令，直接删除安装目录

### 5.3.4 脚本安装包

实际上脚本安装不是独立的软件包，是认为把安装过程写成了自动安装的脚本，只要执行脚本，定义简单的参数，就可以完成安装，类似windows下软件的安装方式

## 六. 用户和用户组管理

对服务器安全性要求高的服务器，需要建立合理的用户权限等级制度和服务器操作规范，linux是通过用户配置文件来管理

### 6.1 用户配置文件

#### 6.1.1 用户信息文件/etc/passwd

每一行代表一个用户，可以通过man 5 passwd来查看配置文件的帮助信息

- 第一字段：用户名称
- 第二字段：密码标志，显示的都是x
- 第三字段：UID（用户ID）
  - 0：超级用户
  - 1-499：系统用户
  - 500-65535：普通用户（如果想把一个普通用户改成超级用户，只要改uid为0就行）
- 第四字段：GID（用户初始组ID）
  - 初始组：每添加一个用户，就会拥有一个初始组。比如创建user1用户，就会生成一个user1初始组。每个用户的初始组只能有一个，一般不要去改
  - 附加组：指用户可以加入多个其他的用户组，并拥有这些权限，附加组可以有多个
- 第五字段：用户说明
  - 相当于备注，有可能没有
- 第六字段：家目录
  - 普通用户：/home/用户名/
  - 超级用户：/root/
- 第七字段：登入后的shell
  - shell就是linux的命令解释器，比如我们输入ls会显示目录列表，就是因为shell窗口得到ls命令后会去解释。其实和windows点击开始菜单弹出窗口时类似的
  - 在/etc/passwd当中，除了标准shell（/bin/bash之外），还可以/sbin/nologin（伪用户，就是无法登入）。普通用户和超级用户都是标准shell



#### 6.1.2 影子文件/etc/shadow

密码存放在这个文件里

- 字段1：用户名

- 字段2：加密密码
  - 加密算法升级为SHA512散列加密算法
  - 如果密码时'!!'或'*'代表没有密码，不能登入
- 字段3：密码最后一次修改日期
  - 使用1970年1月1日作为标准时间，每过一天加1
- 字段4：两次修改密码的时间间隔
- 字段5：密码有效期，默认是99999天，可以修改成特定天数
- 字段6：密码到期前的警告天数
- 字段7：密码到期后的宽限天数：0代表马上失效，-1代表永不失效
- 字段8：账号失效时间
- 字段9：保留

#### 6.1.3 组信息文件/etc/group 和组密码文件/etc/gshadow

/etc/group

- 字段1：组名
- 字段2：组密码（一般不会使用）
- 字段3：GID, group id
- 字段4：组中附加用户

### 6.2 用户管理相关文件

#### 6.2.1 用户家目录

普通用户：/home/用户名/，目录信息里的所有者和所属组都是此用户，权限是700

超级用户：/root/，所有者和所属组都是root用户，权限是550

命令行如果以$符就是普通用户，如果是#就是超级用户

#### 6.2.2 用户邮箱

/var/spool/mail/用户名/

这个是linux内置的用于本机不同用户之间传递信息的邮箱

#### 6.2.3 用户模板

在/etc/skel/ 目录下包含一些模板，当创建一个新用户就会，这个新用户就会拥有这些模板信息

### 6.3 用户管理命令

1. useradd [选项] 用户名

   - -u UID：手动指定用户的UID
   - -d 家目录：手动指定用户的家目录
   - -c 用户说明： 手动指定用户的说明
   - -g 组名： 手动指定用户的初始组
   - -G 组名： 指定用户的附加组
   - -s shell：手动指定用户的登入shell,默认是/bin/bash

   ```shell
   useradd -u 666 -G root,bin -c ‘test user’ -d /liming -s /bin/bash like
   #添加了一个uid 666,到root和bin用户组的liming 用户，家目录在/liming，并且有说明是一个test用户
   ```

2. 用户默认值文件 /etc/default/useradd

   - GROUP =100
   - HOME = /home
   - INACTIVE = -1          密码过去宽限天数
   - EXPIRE =                   密码失效时间
   - SHELL = /bin/bash
   - SKEL = /etc/skel        模板目录
   - CREATE_MAIL_SPOOL = yes            是否建立邮箱

3. passwd [选项] 用户名         #修改密码

   以下选项都不常用

   - -S 查询用户密码的密码状态。仅root用户可用
   - -l 暂时锁定用户。仅root用户可用
   - -u 解锁用户。 仅root用户可用
   - --stdin 可以通过管道符输出的数据作用用户的密码

#### 6.3.1 usermode 修改用户信息

usermod [选项] 用户名

- -u UID: 修改用户的UID号
- -c 用户说明：修改用户说明
- -G 组名
- -L：临时锁定用户
- -U：解锁用户锁定

#### 6.3.2 chage 修改用户密码状态

chage [选项] 用户名

- -l：列出用户的详细密码状态
- -d 日期： 修改密码最后一次更改日期
- -m 天数：两次密码修改间隔（4字段）
- -M 天数：密码有效期
- -W 天数：密码过期前警告天数
- -I 天数：密码过后宽限天数
- -E 日期：账号失效时间

#### 6.3.3 userdel 删除用户命令

userdel [-r] 用户名     -r删除用户同时删除家目录

#### 6.3.4 su 用户切换命令 

su [选项] 用户名

- -: 代表连同用户的环境变量一起切换，绝对不要省略

- -c 命令：仅执行一次命令，而不切换用户身份 

  - ```shell
    su - root -c 'useradd user3' 不切换身份使用root创建一个用户
    ```

###  6.4 用户组管理命令

groupadd [选项] 组名

- -g GID:   指定组ID

groupmod [选项] 组名

- -g GID：      修改组ID

- -n 新组名： 修改组名

  - ```shell
    groupmod -n testgrp group1
    #把组名group1修改为testgrp
    ```

groupdel 组名

## 七.ACL 权限 

专门解决身份不够的问题