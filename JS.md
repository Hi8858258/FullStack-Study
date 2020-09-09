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

- parseInt() 
  - 作用：
    - 取整
    - 转换进制

- parseFloat() 取浮点数



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

它的部分方法

Math.random() 返回0-1之间的随机数

Math.max(num1,num2)

Math.min(num1,num2)

Math.abs(num)

Math.ceil(19.3) 向上取整

Math.floor(11.8) 向下取整

Math.pow(x,y)

Math.sqrt(num)

### 9.6 Date时间对象

```javascript
var d = new Date();
```

日期对象的方法：

d.toDateString();

d.toTimeString()

比较重要的是：

d.getDay() 返回0-6。 0 代表星期天

d.getHours()

d.getMinutes();

d.getSeconds();

#### 9.6.1 Date方法

Date.parse(日期对象) 转成毫秒数，相对1970年的

```javascript
var d = Date();
Date.parse(d)
```

### 9.7 定时器 setInterval

setInterval(函数，时间（1000ms）) ,每个1000ms执行一次函数

## 十.BOM 浏览器对象模型

### 10.1 窗口对象window

像alert（）其实是window的一个方法，完整的用法师window.alert()

show（）方法和alert一样

其实所有的属性，变量，函数前面都可以跟window

```javascript
var num =10;
alert(window.num)
```

![image-20200718135055742](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200718135055742.png)

### 10.2 confirm（）

带确定和取消的弹出框,返回值是true/false  

```javascript
var res = confirm("内容")
```

### 10.3 prompt()

带输入框的弹出框

​	第一个参数：面板上显示的内容

​	第二个内容：输入框里面默认的内容（可以不穿）

```javascript
var res = prompt("请输入内容"，1000)
```

### 10.4 open()

打开一个新的页面

参数：open（url,"xxx","xxx"）

第一个参数是，打开新页面跳转的url

第二个参数，打开新窗口的名字

第三个参数，可以设置窗口的宽高

### 10.5 history()

掌管的当前窗口（不是浏览器）的历史记录

属性：

​	history.length

方法：

​	history.back()

​	history.forward()

​	history.go()

### 10.6 location()

属性：

​	location.protocol 返回的是url的协议类型，有file,http,https

​	location.hostname 返回主机域名

​	location.port 返回端口

​	location.pathname 路径

​	location.search 返回查询字符串，就是问号后面的

​	

## 十一.DOM



