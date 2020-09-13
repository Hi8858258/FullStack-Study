# JS

## Js文件的引入

html有两种方式可以使用js代码，在head或者body中使用script标签：

1. 不同的是script标签里没有src属性的时候，可以直接写在标签里携代码

   ```javascript
   <head>
       <script type = "text/javascript">
           xxx
       </script>
   </head>
   ```

2. 也可以使用src属性引用外部的js文件

   ```javascript
   <head>
       <script type = "text/javascript" src = "js/asd.js ">
       </script>
   </head>
   ```

## 一.数据类型转换

在js中主要有两种数据大类：

1. 基本数据类型：Number, String, Boolean, undefined, null

2. 引用数据类型：object, Array, Function

   可以通过typeof 去检验变量存的数据的类型

   ```js
   var a = 1;
   alert(typeof a)
   //当变量没有被赋值时，typeof 变量会显示undefined
   //null是空对象
   ```

   

- Boolean() 将其他数据类型，转换成布尔值

- Number() 将其他数据类型，转换成数字

- 变量.toString() 会把变量转成字符串

  - 只能纯数字的字符串可以使用

    Number（null ） 为 0 

    Number(undefined ) 为NaN

- parseInt()  只会转换第一个字母前的数字
  - 作用：
    - 取整
    - 转换进制

- parseFloat() 取浮点数

- num.toFixed(2)；浮点数取两位小数，但是会转换为字符串



## 二. 运算符

- 赋值运算符：=

- 比较运算符：>,<,>=,<=,==,!=,===(恒等),!==（恒不等）

  为什么会有==,和===呢，因为js在使用==时候，会将==两边的数据类型自动转换成一样的比如"10" == 10 为true，而===不会转换，所以两边的数据需要类型相等，值相等

- 逻辑运算

  - 与 &&
  - 或 ||
  - 非 ！

- 三目运算符

  格式: 表达式1? 表达式2：表达式3

  表达式1为true,则执行表达式2，否则执行3
  
  ```js
  1>2? '真的':'假的'
  >>>>假的
  ```

## 三. 流程控制语句

- if语句

  ```javascript
  单分支
  if(判断条件){
     执行语句
     }
  
  双分支
  if(){
     
  }else{
      
  }
  
  多分支
  if(){
     
  }else if{
      
  }else{
      
  }
  ```

- switch

  ```javascript
  switch(表达式){
         case 常量1:
         		语句;
         		breaK;
         case 常量2:
         		语句;
         		break;
         default:
         	当上述所有case都不执行的时候，
         break;
  }
  switch的表达式与case常量相等，就执行语句。如
  var weather = "sunny";
  switch(weather){
      case 'sunny':
          console.log('是晴天')
          break;
      case 'xiayu':
          console.log('下雨了')
          break;
      default:
          console.log('多云');
          break
  }
  //如果每个case中没有break就会case穿透，执行下一个case
  ```

## 四. 循环

### 4.1 for循环

for循环主要用于初始和终止条件都已知

```js
for(初始化条件;结束条件；条件递增变化){
    要执行的代码
}
//例子
var i;
var sum = 0;
for(i = 1;1 <= 1000;i++){
    console.log(i);
    sum = sum + i
}
```

break 和continue的区别：break是直接终止循环体，而continue是跳过continue后面的代码，直接进入下一次循环

### 4.2 while循环

```
初始化条件
while(判断循环结束条件){
     //run this code
    递增条件
}

var i = 1;
var sum = 0;
while(i<=100){
    sum += i;
    i += 2;
}


```

### 4.3 do while先执行，再判断

计算1到100之间数的合

```js
var sum = 0
var i = 1;
do{
    sum += i;
    i++;
}while(i<100);
```





## 五. 函数

### 5.1 arguments

每个函数内部都有一个arguments,系统内置的，用来存储实际传入的参数

属性：

- arguments.length   获得参数个数
- arguments[索引]     获得指定缩影的参数

当传入的参数不知道有几个的时候，就可以使用argument来直接掉这些参数，比如数字求和

```javascript
function sum(){
    var total = 0;
    for (var i = 0; i < arguments.length; i++){
        total += arguments[i]
    }
    return total
}
```

### 5.2 作用域

如果在函数外部申明了变量（全局变量），可以直接在函数里面使用。（变量在函数前后位置没有关系）

```javascript
var a = 0;
function test(){
    //和python不一样的地方就是，哪怕没有形参，函数也可以直接到全局里面找到这个变量a
    a += 1
};

var a = 0;
console.log(a);
test(a)
console.log(a);
test(a)
console.log(a)

>>>0;
>>>1;
>>>2

这是时候变量a其实有单独的一块内存，函数是单独的一块内存，每次调用函数的时候都是去内存里面取a变量，然后改变内存中a的值。函数每次调用结束，函数的内存空间就会被释放
```

但是如果函数里面有形参，那么形参就会在函数的内存空间里拥有一个形参的内存，而这个形参就是对实参的一个复制。

```javascript
var a = 0;
function test(aa){
    aa += 1
};

var a = 0;
console.log(a);
test(a)  //每次调用函数，a变量的值都不会改变
console.log(a);
test(a)
console.log(a)

>>>0;
>>>0;
>>>0;
```

在函数中的变量是属于函数的内存空间中的，叫局部变量。有效范围，只是当前函数的大括号，这些参数只会在函数创建的时候被创建，函数结束调用结束就随着函数一起被销毁。这是js的垃圾回收机制

```javascript
function test(){
    var a = 0;
    a += 1
    alert(a)
};


test()     >>>>1
console.log(a);   >>>undefined
```

#### 5.2.1 全局污染

比如一个html文件引入两个外部js文件，这两个js文件都有相同名的函数，那么再html调用这个函数的时候，就只会调用第二个引入的文件中的函数

```html
<script src = "first.js"></script>
<script src="second.js"></script>
<script>
    console.log(hello())
</script>
```

```js
//first.js
var name = 'li';
function hello(){
    return ('hello' + name);
}

//second.js
var name = 'ke';
function hello(){
    return ('hello' + name);
}
```

解决这种全局污染的方式是将两个函数放到作用域里去。然后将函数挂载到window对象上

```html
<script src = "first.js"></script>
<script src="second.js"></script>
<script>
    //window可以省略不写，直接使用first（），second()
    console.log(window.first())
    console.log(window.second())
</script>
```

```js
//使用(function（）{})()这样的自执行匿名函数，把作用域包裹
//把想要的函数放到一个函数作用域里去
//first.js
(function(){
    var name = 'li';
    function hello(){
    return ('hello' + name);
}
    window.first = hello;
})();


//second.js
(function(){
    var name = 'ke';
    function hello(){
    return ('hello' + name);
}
    window.second = hello;
})();
```

### 5.3 函数表达式

```js
function sum(a,b){
    return a+b
}
console.log(sum(2,3))


//下面是函数表达式，合上面的结果一样
var ss = function(a,b){
    return a+b
}
console.log(ss(2,3))

```

## 六. 对象

```js
var person = {
    //和函数不一样的地方就是没有括号
    name:"mj",
    age:18,
    sex:"女",
    ff:function(){
        alert('吃饭')
    }
}
console.log(person.name)
person.ff()
```

### 6.1 内置对象数组

数组的申明方式：

1. 通过new创建数组（构造函数创建，少用）

   ```javascript
   var arr = new Array(100,true,'hello');
   ```

2. 可以省略new运算符（构造函数创建，少用）

   ```javascript
   var arr = Array(100,true,'hello');
   ```

3. 可以用中括号直接创建（常用的方式）

   ```javascript
   var arr = [100,true,'hello']
   ```

注意，1，2两种方法当只有1个参数（比如10）时候，创建的是长度为10的数组，并不是创建了拥有10这个元素的数组

#### 6.1.1 for....in

```html
var a = [10,20,30,40]
for(var i in a){
	document.write(a[i] + '</br>')
}
```

#### 6.1.2 for....of

```javascript
var a = [10,20,30,40]
for(var i of a){
    document.write(i + '</br>')
}
```

#### 6.1.3 数组的方法

- 数组实现栈结构的方法：
  - arr.push(参数1，参数2)    依次插入到数组中，返回值是数组插入元素后的新长度
  - arr.pop() 没有参数，从尾部开始pop元素，返回值是pop出来的元素
- 数组实现队列结构的方法：
  - arr.shift() 从数组首部开始取元素，返回值是还余留下的元素
  - arr.unshift(参数1，参数2)  从数组头部插入元素，返回值是新数组的长度

-  concat拼接 

arr.concat(数组/数据) 拷贝原数组生成新数组（原数组不会改变），返回新的数组

```javascript
var arr1 = [10,20]
var arr2 = [30,49]
var newArr = arr1.concat(arr2,'hello')

alert(newArr) >>> [10,20,30,49,'hello']
```

- #### slice切片 （类似python中的数组切片）


arr.slice(start,end) 生成新数组，原数组不改变 

- #### splice


arr.splice(start,length,数据1，数据2，……)

start: 开始的位置

length：要截取的元素个数

第三个参数开始，就是要新插入的元素

用这个方法，可以实现数组的增加，删除，修改（先删除，再增加）

```js
//删除
var names = ['li','e','js','fd','adf'] 
names.splice(1,1)删除‘e’
//修改
names.splice(1,1，‘eee’)删除‘e’
```

- #### join


arr.join(拼接符) 将数组中的元素，用传入的字符，拼接成一个字符串

- #### reverse


arr.reverse()

- #### sort


arr.sort(函数) 不传参默认从小到大（按照第一位数字的大小）

下面是按照数值从小到大排序

```javascript
var arr = [1,10,20,15,25,5]
arr.sort(function(value1,value2){
    return value1-value2
})
//当排序函数里面返回的是正值，就说明value1.value2的位置是升序的，不用交换，如果是负值，就会交换
```

js的数组变量和python里面一样，都是对实际数组内存的引用，所以下面的情况

- ```javascript
  var arr1 = [10,20]
  var arr2 = arr1
  arr2.push(30)
  alert(arr1)  >>>[10,20,30]
  ```


- 位置方法 indexOf（），lastIndexOf()

  - 如果查不到结果，返回-1

  ```js
  var names = ['li','e','js','fd','li','adf']
  alert(names.indexOf('li'));    0 第一个元素
  alert(names.indexOf('li'));    4 最后一个元素
  ```

  

- #### ES5新增的数组方法：

  1. indexOf()

     arr.indexOf(item,start)     从start下标开始查找第一次出现item的下标,不传start的话默认为0，如果找不到这个元素的话，返回-1

  2. forEach()  

     arr.forEach(item,index,arr)    //item就是当前的元素，index是当前元素的下标}

  3. map 映射函数

```javascript
var arr = [10,20,30,40]
var newArr = arr.map(function(item,index,arr){
    return item*1.3
})
```

​		4. filter过滤

```javascript
var arr = [10,20,30,40]
var newArr = arr.filter(function(item,index,arr){
    //过滤条件
    return item>20
})
```

5. some 返回值是true/false，数组中是否有符合条件的元素，找到就结束不会一直找下去

```javascript
var arr = [10,20,30,40]
var newArr = arr.some(function(item,index,arr){
    return item>20
})
```

6. every  找全数组中的所有元素

7. reduce 归并

```javascript
var arr = [10,20,30,40]
var newArr = arr.reduce(function(pre,next,index,arr){
    //过滤条件
    return pre + next
    //pre 第一次是下标为0的元素，接下来就是pre+next的值
    //next第一次是下标为1的元素，接下来就是依次往后取
})
```

### 6.2 Global 对象

是一种不由对象调用，但可以使用的方法，不能console.log(global)；浏览器中有一个window对象，其实就相当于global对象

uri:统一资源标识。在js中我们可以看到一些链接中的空格会被编码成%20，如果想要节码，可以使用如下方式

```js
URI = 'http://www.df.com/ keke'
var encodeURI = encodeURI(URI)
var deco = decodeURI(encodeURI)
//还有一种时encodeURIComponent(URI)可以把所有符号都编码
```

## 六.变量声明提升

在当前作用域下，变量的申明会提前，但是赋值不会，所以在变量前面使用alert(变量)，会显示undefined，而不是报错

```javascript
alert(a);  >>>undefined
var a = 10; 
alert(a)   >>>10
就相当于
var a;
alert(a)
a = 10
alert(a)
```

除了变量申明会提前，函数也会提前

省略var的话，这个变量会强制变成全局变量，不建议这么用

```javascript
function(){
    alert(a)    >>>undefined
    var a = 10;
    alert(a)    >>>>10
}
如果省略了var
function(){
    alert(a)    >>>10
    a = 10;
    alert(a)    >>>>10
}
```

## 七.严格模式

在每个函数的开始使用"use strict"会开启严格模式

## 八. 字符串

### 8.1字符串声明

- 通过new运算符

  ```javascript
  var start1 = new String(100)
  ```

- 省略new

  ```javascript
  var start1 = String(100)
  ```

- 常量赋值

  ```javascript
  var start1 = "100"
  ```

### 8.2 字符串方法

比较重要的

- str.length

- str.charAt(下标) 获取字符   也可以使用str[下标来获取]

- str.charCodeAt() 返回对应字 符的ASCII码

- str.indexOf(substr,start) 在字符串从start开始查找substr字符串，并返回所在下标，start默认为0。如果返回-1说明没找到

- str.lastIndexOf（substr） 返回substr最后一次出现的位置

- str.search(substr) 返回substr第一次出现位置

- str.replace(oldstr,newstr)   将str里面的oldstr替换成newstr， 只能替换第一个oldstr。如过要替换所有的oldstr，就要使用正则表达式

  ```javascript
  var str = "how are aRe are you"
  var newStr = str.replace(/are/g,"old are")     //斜括号里的就是正则表达式字符，后面的g代表的就是全局，还能使用i代表大小写不敏感，还有gi
  alert(newStr);
  alert(str)
  ```

- str.split(分隔符，length) 返回lenght长度的参数，

String对象本身的方法：

​	String.fromCharCode(码值1，码值2),返回对应ASCII码对应的字符

没那么重要的

- str.big() 用大号字体显示字符串
- str.blink() 显示闪动字符串
- str.fixed() 以打字机文本显示字符串
- str.strike() 使用删除线
- str.fontcolor() 指定颜色
- str.fontsize() 指定字符大小
- str.link() 将字符串显示为连接
- str.sub() 将字符串显示为下标
- str.sup() 将字符串显示为上标
- str.trim()清除字符串前后空格

## 九. 对象

在js中没有类这个概念，只有对象，但是到了ES6就有类的概念了

### 9.1 声明一个对象

1. 通过new运算符

   ```javascript
   var obj1 = new Object()
   ```

2. 省略new

   ```javascript
   var obj2 = Object()
   ```

3. 常量赋值{}

   ```javascript
   var obj3 = {}
   ```

   给对象添加属性：

   1. obj3.username = "sdf"    相当于obj3['username'] = "sdf"

### 9.2 对象方法

```javascript
obj3.show = function(){
    代码块
}
```

### 9.3 常用的对象申明

```javascript
var obj4 = {
    username:"sdf",
    show:function(){
        
    }
}
```

### 9.4 delete

可以使用  delete object.属性/方法去删除对象中的属性和方法

### 9.5 Math对象

Math属性：可以通过浏览器直接看到

​	Math.E 自然对数e

部分方法

​	Math.random() 返回0-1之间的随机数

​	Math.max(num1,num2)

​			Math.max.apply(null,arr)

​	Math.min(num1,num2)

​	Math.abs(num)

​	Math.ceil(19.3) 向上取整

​	Math.floor(11.8) 向下取整

​	Math.round(num) 标准的四舍五入

​	Math.pow(x,y)

​	Math.sqrt(num)

几个小demo

```js
<script>
        //获取一个范围内的随机数
        function random(min,max){
            return Math.floor(Math.random()*(max-min) + min)
        }
        console.log(random(1,100))


        //获取随机rgb颜色
        function randomColor(){
            var r = random(0,256);
            var g = random(0,256);
            var b = random(0,256);
            return result = `rgb(${r},${g},${b})`    //使用``模板字符串，可以使用${}来使用表达式，很强大
        }
        document.body.style.backgroundColor = randomColor()
        console.log(randomColor())
</script>
```



### 9.6 Date时间对象

```javascript
var d = new Date();  //不带参数直接获得当前事件
var dd = new Date(1995,11,25,14,30,0) 年，月，日，时，分，秒
```

日期对象的格式化方法：

1. d.toDateString(); 获取了星期几 月 日 年
2. d.toTimeString() 获取时分秒
3. d.toLocaleDateString(); 年/月/日
4. now.toLocaleTimeString()；时间

比较重要的是：

1. d.getDay() 返回0-6。 0 代表星期天
2. d.getDate() 获取日期
3. d.getMonth() 获取月分
4. d.getFullYear() 获取年份
5. d.getHours()
6. d.getMinutes();
7. d.getSeconds();

#### 9.6.1 Date方法

Date.parse(日期对象) 转成毫秒数，相对1970年的

```javascript
var d = Date();
Date.parse(d)
```

### 9.7 定时器 setInterval

setInterval(函数，时间（1000ms）) ,每个1000ms执行一次函数

## 十.BOM 浏览器对象模型

主要包含以下几个对象

### 10.1 窗口对象window（）

- 像alert（）其实是window的一个方法，完整的用法window.alert()


-  show（）方法alert（）一 样


其实所有的属性，变量，函数前面都可以跟window。相当于所有的变量和对象其实都是挂载到window对象上的

```javascript
var num =10;
alert(window.num)
```

![image-20200718135055742](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200718135055742.png)

- confirm（）

带确定和取消的弹出框,返回值是true/false  

```javascript
var res = confirm("内容")
```

- prompt()

带输入框的弹出框

​	第一个参数：面板上显示的内容

​	第二个内容：输入框里面默认的内容（可以不穿）

```javascript
var res = prompt("请输入内容"，1000)
//可以把res传给需要用到的地方
```

- setTimeout()    延时方法，只会执行一次

  ```js
  window.setTimeout(function(){
      console.log('like')
  },2000)
  //过两秒后执行function方法
  ```

- setInterval(funcion，2000) 周期循环执行的方法，能配合clearInterval(定时器方法名)

  ```js
  var num = 0;
  var timer = null;
  timer = setInterval(function(){
      num ++;
      if(nunm>5){
          //当num大于5时候，定时器方法就会清除
          clearInterval(timer);
      }
  },1000)
  ```

- location()

  - 属性：

  ​	location.protocol 返回的是url的协议类型，有file,http,https

  ​	location.hostname 返回主机域名

  ​	location.href 返回完整的url，而且是经过编码的

  ```js
  //可以使用这个对窗口的网页进行跳转
  location.href = 'www.like.com'
  location.replace = 'www.like.com' //replace跳转后不能使用后退按钮，不会产生历史记录
  location.reload() //重载整个网页
  ```

  ​	location.port 返回端口

  ​	location.pathname 路径

  ​	location.search 返回查询字符串，就是问号后面的

  ```js
  //获取查询字符串
  var qs = location.search.length>0? qs = location.search.substring(1); //取得去掉？的查询字符串
  var items = qs.length? qs.split('&'):[]; //当qs存在时候，就取分割不同的查询词
  console.log(items); //这就是取得的每一项查询
  ```

- navigator对象里有一个plugins属性，可以查看浏览器安装的插件

-  history() 掌管当前窗口（不是浏览器）的历史记录

  属性：

  ​	history.length

  方法：

  ​	history.back()

  ​	history.forward()

  ​	history.go()

  ```js
  history.go(0)//刷新当前页面
  history.go(1) //前进一次，也可以前进2次
  history.go(-1) //后退一次，也能后退2次
  ```

- open()

  打开一个新的页面

  参数：open（url,"xxx","xxx"）

  第一个参数是，打开新页面跳转的url

  第二个参数，打开新窗口的名字

  第三个参数，可以设置窗口的宽高

## 十一.DOM

文档对象模型，dom把整个html文档看作一颗树。html标签是树根，head，body是第二层节点。

DOM中主要由三种节点：

1. 元素节点：就是html标签
2. 文本节点：比如p标签中的文本内容就是文本节点
3. 属性节点：标签的属性

### 11.1 获取节点

1. 获取元素节点

   ```js
   var eleNode = document.getElementById('id名') //通过id名来获取单个对象
   var oLis = document.getElementsByTagName('li') //通过标签名来获取一个对象集合，记住不是数组，不能用push方法
   var oitems =  document.getElementsByClassName('类名'); //通过类名获取以对象集合
   
   ```

2. 获取节点对象的属性

   节点对象.getAttribute(‘属性名’)

   ```js
   <p title = '这里的'>dsfafda</p>
   
   var node = document.getElementByTagName('p')[0]
   var title = node.getAttribute('title') >>>>这里的
   ```

3. 设置节点对象的属性

   ```js
   #box{
   	color:red
   }
   node.setAttribute('id','box') //给P标签设置id属性，这样P就会获得css的color样式
   ```

### 11.2 节点属性

1. 节点的名称

   - 元素节点的nodeName与标签名相同
   - 属性节点的nodeName与属性的名称相同
   - 文本节点的nodeName永远是#text
   - 文档节点的nodeName永远是#document

   ```js
   <p title = '这里的' id = ‘tt’>dsfafda</p>
   
   //1.获取元素节点
   var node = document.getElementByID('tt')  //node就是元素节点对象
   node.nodeName  >>>> p
   node.nodeValur >>>>null
   node.nodeTyoe >>>>>1
   //2.获取属性节点
   var att = node.attributes  //获取到的是P元素的属性节点集合
   att[0].nodeName = title
   att[0].nodeValue = '这里的'
   att[0]。nodeType = 2
   //3.获取文本节点
   var text = node.childNodes[0]    //文本节点和注释节点都是元素节点的子节点。所以获取到的是节点对象集
   ```

2. 节点的值

3. 节点的类型

   元素节点：1。属性节点：2。文本节点：3。注释节点：8

### 11.3 常用的节点属性

- node.childNodes   获取到元素节点的所有子节点

```js
<div id = 'tt'>
    <p>asdf</p> //也属于div元素的子节点，可以通过node.childNodes来获取
 	<p>dffd</p> //同上
</div>


var node = document.getElementById('tt')
node.childNodes 
//会返回5个子节点，分别是：text,p,text,p,text。三个text文本节点是换行符
```

- node.firstChild    获取到元素节点的第一个子节点

- node.lastChild     获取到元素节点的最后一个子节点

- node.parentNode   获取元素节点的父节点

- node.nextSibing     获取兄弟节点

  ```js
  var n = document.get....
  function get_nextSibling(n){
      var x = n.nextSibling;
      while (x && x.nodeType !=1){
          //节点的兄弟节点可能是文本节点，也可能是注释节点
          x = x.nextSibling
      }
      return x;
  }
  ```

  

- node.previousSibling 获取上一个兄弟节点

### 11.4 元素节点对象的增删改查

- createElement()
- 插入节点
  - appendChild()
  - insertBefore(newNode,node)
- 删除节点 removeChild(子节点名)
- 替换节点 replaceChild(新节点对象（需要先创建），需要被替换的节点对象（需要被赋给一个变量）)
- 创建文本节点 createTextNode() 

```js
<div id = 'tt'>
    <p>sdf</p>
</div>

var oDiv = document.getElementById('tt')  //获取父节点
var newNode = document.createElement('p') //创建一个p标签节点
oDiv.appendChild(newNode);//将新建的p节点插入给父节点

var textNode = document.createTextNode('like')
newNode.appendChild(textNode)   //将文本节点赋给新建的P节点
newNode.innerHTML = 'like' //可以直接对p节点创建一个文本
newNode.innnerHTML = '<a href="#">sfsdf</a>' //innerHTML也可以渲染标签
//还有一种innerText不能渲染标签
```

### 11.5 元素节点操作样式 

通过node.style可以获得节点的样式对象

```js
<style>
    .highlight{
        color:'black';
        font-size:16px
    }
</style>

<p id = 'tt'>adsf</p>

var node = document.getElementById('tt')
//第一种操作样式的方法
node.style.backgroudcolor = 'black'
//第二种操作的方法是通过类属性来操作样式（用的比较多）
node.setAttribute('class':'highlight')
```

### 11.6 事件

常用事件

| 事件        | 说明               |
| ----------- | ------------------ |
| onclick     | 鼠标点击           |
| onmouseover | 鼠标经过           |
| onmouseout  | 鼠标移开           |
| onchange    | 文本框内容改变事件 |
| onselect    | 文本框内容选中事件 |
| onfocus     | 光标聚焦           |
| onblur      | 光标失焦           |
| onload      | 网页加载事件       |

- 鼠标点击事件

当发生事件的时候，就会触发后续的函数，给元素绑定事件由两种方式：

```js
var node = ....
//1.第一种方式(第一种方式用得比较多)
<script>
node.onclick = function(){
    alert('事件被触发')
}
</script>
//2.第二种方式，直接在标签中赋予一个属性
<p id = 'tt' onclick="add()"></p>
<script>
    function add(){
    	alert(222)
    }
</script>
```

- 鼠标悬停事件

```js
<div id="box"></div>

//悬停
var box = document.getElementById('box')
box.onmouseover = function(){
    this.style.backgroundColor= 'green';
}
//移开
box.onmouseout = function(){
    this.style.back----
}

```

- 表单控件事件

- onload事件

  ```jd
  //如果我们的script脚本是写在head里面的，那么就需要设置等html标签都加载号了再执行脚本，不然会抓取不到节点
  window.onload = function(){
  	//等待文档元素加载完成之后才会执行这里面的代码 
  }
  ```

## 十二. js 特效

1. 图片轮播切换

2. 显示和隐藏图片

3. 焦点图片切换

4. 关闭小广告

5. 图标切换

6. 百度换肤

7. tab选项

8. 发表评论

9. 九宫格布局

10. 定时器鲜花表白

11. 始终案例

12. 瀑布流

13. 轮播图

14. 无缝轮播图

15. 旋转木马

16. 放大镜效果


## 十三. js动画

1. offset 家族
   - 定位父级 offsetParent 就是元素上层的第一个定位的父元素
   - offsetLeft;offsetTop
   - offsetHeight;offsetWeight
   - 元素自身有fixed定位，offsetParent就默认是null

