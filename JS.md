#  JS

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

### 5.4 回调函数

回调函数就是没有被调用，但是依然执行的函数，回调函数有3个特点

1. 你定义的
2. 没有调用
3. 最终执行了

常见的回调函数有setTimeout里面的函数，和dom里面的事件函数，ajax请求，生命周期

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
     - 元素自身有fixed定位，offsetParent就默认是null
     - 元素自身没有fixed定位，offsetParent就会去找上层的定位元素
     - body元素的offsetParent是null
   - offsetLeft;offsetTop
     - offsetTop等于当前元素的上边框到offsetParent元素上边框的距离,offsetLeft同理
     - 当前元素的offsetParent元素是上面一个元素的话，offsetTop就等于margin-top的值
     - 如果父元素不是定位，那就继续找
   - offsetHeight，offsetWidth;
     - 只读属性，不能通过box.offsetHeight = 500px来修改它们的值
     - offsetWidth/height是把盒子的width+padding+border 之和，数值类型
     - 和box.style.width只能获取行内样式的值，并且是字符串形式比如100px

2. client 家族(客户端,主要用于获取当前页面的大小)

   - 只读属性
   - 给元素设置display:none 客户端client属性都为0
   - 尽量避免方位client属性，会消耗很多资源
- clientWidth
     - width + padding
   - clientHeight
     - height + padding
   - clientLeft
   - clientTop
   
3. scroll 家族

   - scrollheight

     - 不可写 
     - 表示元素的总高度，包含由于溢出而无法在网页上显示的

   - scrollwidth

     - 不可写
     - 表示总宽度

   - 无滚动条时，scrollheight就等于内容高+padding

   - 有滚动条（overflow:scroll时），就要包含所有隐藏的内容了

   - scrollTop

     - 可读写的属性，可以通过该元素.scrollTop来实现不停向下滚动的动画

     - 元素被卷起的高度，就是滚动条往下拉的时候。被隐藏到上方的内容高，可以使用

       ```js
       node.onscroll = function(){
           //使用整个来监听scroll动作
       }
       ```

     - 当滚动条滚动到内容底部时：

       - scrollHeight = clientHeight + scrollTop

   - scrollLeft

     - 可读写
     - 同scrollTop

## 十四. 事件流

事件流描述的是从页面中接收事件的顺序。

如果点击了某个按钮上，那么点击事件不仅仅发生在按钮上，也点击了整个页面。

事件顺序分别由IE和网景提出了两个完全相反的顺序

1. 事件冒泡：事件自底向上传播，先有具体点击的元素接收，然后逐级向上传播，div->body（document.body对象)>html(documentElemnt对象)>文档（document对象）>windon对象

   ```js
   <div id = 'box'></div>
   
   var box = document.getEl('box')
   box.onclick
   ```

2. 事件捕获

   与事件冒泡完全相反

3. 事件处理程序

   1. HTML事件处理程序

      - 直接在html里写事件代码

        ```js
        <div onclick = "test()"></div>
        
        <script>
            function test(){
            ....
        }
        </script>
        ```

        

      - 不建议使用，html和js无分离，后期不易维护

   2. DOM0级事件处理程序

      - 常见的一种方法，所有浏览器都兼容 

      - 在js代码中先获取元素节点，然后给这个节点对象赋予事件

        ```js
        var box = document.get....
        box.onclick = function(){
            ...
        }
        //删除事件处理程序
        box.onclikc = null
        ```

      - 这个只能在冒泡阶段才能用

      - 缺点：不能给同一个节点绑定相同的事件处理程序，否则会有覆盖现象

   3. DOM2级事件处理程序

      - IE8浏览器不支持这个方法

      - addEventListner(事件名，处理程序函数，布尔值)。布尔值为false处于冒泡阶段，true就在捕获阶段

      - removeEventListner()

        ```js
        var box = document.get....
        box.addEventListner('click',function(){
            this.innerHTML +=1;
        },false)
        ```

   4. IE事件处理程序



## 十五. 深入理解函数

1. 函数声明语句

   ```js
   function fn(形参){
       ...
   }
   ```

2. 函数表达式,将匿名函数赋给一个变量

   ```js
   var hello = function(x,y){
       return ...
   }
   ```

3.  Function构造函数

   ```js
   new Function(形参，构造体)
   如下
   var fn = function('x','y','return x + y');
   ==
   function fn(x,y){
       return x + y
   }
   ```

4. 函数调用模式

   this在普通函数中调用指向的是window,在构造函数中使用指向当前函数，当作对象的方法指向对象

   - 函数调用模式

     ```js
     function add(x,y){
         return x + y;
     }
     
     var sum = add(3,4)
     ```

   - 方法调用模式

     ```js
     var obj = {
         fn:function(){}
     }
     
     obj.fn()
     ```

   - 构造函数调用模式

     ```js
     function fn(){}
     var obj = new fn();
     ```

   - 间接调用模式

     ```js
     function sum(x,y){
         return x + y;
     }
     console.log(sum.call(obj,1,2 ))
     ```

5. 函数参数

   函数自带的arguments不是一个真正的数组，只能说类似。当需要传的实参比形参多的时候，就可以用arguments来

6. 函数属性

   - length属性

   ```js
   function add(x,y){
       console.log(arguments.length);//实参的个数   4
       console.log(add.length);//形参的个数  2
   }
   add(2,3,4,5)
   ```

   - name属性

     当前函数的名字

   - prototype属性

     每一个函数都有一个prototype属性,这是一个原型链（对象）。意思就是 函数对象.prototype是函数对象的父对象，所以函数.prototype拥有的方法和属性，函数也会拥有

7. 函数方法

   - apply(),call()。这两个方法都不是继承来的，函数本身有的。可以改变函数内部this的指向对象，另一个意思是让函数变成指定对象的方法

     ```js
     window.color = 'red';
     var obj = {color:'blue'};
     function sayColor(){
         console.log(this.color);
     }
     sayColor(); //red .因为普通函数的this指向window
     sayColor.call(this); //red，this指向window
     sayColor.call(window);//red,this指向window
     sayColor.call(obj); //blue,this指向obj
     ```
     
   - call和apply的区别

     - call（{}，1，2，3）。call第一个参数是对象，后面是一个个数字
     - apply({},[])。apply第一个参数也是对象，但后面可以跟数组

   - 在非严格模式下，给call/apply传入一个null或者undefined会被指向window这个全局对象

   - 在严格模式下，传什么就指向什么。比如传null就会指向null对象

   - call和apply方法的应用

     - 找出数组的最大元素配合
       
       - Math.max(数字1，数字2，数字3)
       - Math.max.apply(null.[2,3,4,5])求数组的最大元素
       
     - 将类数组对象转换成真正的数组

       - 类数组就相当于函数中的arguments对象
         - 使用Array.prototype.slice.apply(arguments)可以把arguments变成真实的数组

     - 数组追加

       ```js
       var arr = []
       Array.prototype.push.apply(arr,[1,2,3,4])//将[1，2，3，4]push到arr中
       Array.prototype.push.apply(arr,[8,9,0])//[1,2,3,4,8,9,0]
       ```

     - 利用call和apply做继承

       ```js
       function Animail(name,age){
           //这是一个类
           this.name = name;//类属性
           this.age = age;//类属性
           this.sayAge = function(){
               console.log(this.age)
           }
       }
       
       function Cat(name,age){
        //这是一个子类  
           Animal.call(this,name,age)//把this指向了cat实例
       }
       
       //实例化Cat
       var c = new Cat('小花',20);
       c.sayAge();
       ```

     - 使用log代理console.log()

   - bind方法

     - es5新增

     - 主要作用：将函数绑定到某个对象中，并且有返回值（一个函数）

       ```js
       function fn(y){
           return this.x + y;
       }
       var obj = {
           x:1
       }
       var gn = fn.bind(obj)
       gn(3)
       //上面的过程就是，先把fn绑定给obj对象，这个时候fn中的this会改变指向obj。然后bind会返回一个函数其实是fn给gn。所以调用gn(3)的时候，其实是在调用obj对象里的fn
       ```

     - 这是常见的函数式编程技术-函数柯里化 

       ```js
       function getConfig(colors,size,otherOperations){
           console.log(colors,size,otherOperations)
       }
       var defaultConfig = getConfig.bind(null,'heise',1000);
       
       defaultConfig('123');>> heise,1000,123
       defaultConfig('456');>> heise,1000,456
       //相当于是给函数赋予了默认方法，框架里使用的较多
       ```

## 十六.作用域

1. 作用域的内部原理

   - 全局作用域
   - 函数作用域，可以相互嵌套
   - 作用域内部原理的5个阶段：编译（解释），执行，查询，嵌套，异常

2. 编译（解释阶段）

   编译也有两个阶段：

   - 分词

     ```js
     var a = 2;
     //词法单元：var,a, =,2,;
     //js会把词法单元放到一个对象里
     {
         "var":"keyword"//关键词
         "a":"indentifier"//标识符
         "=":"assignment"，//分配
         "2":"interger",//整数
         ";":"eos" //end of statement结束语句
     }
     ```

   - 解析

     ```js
     //分词结束后，就会对对象进行解析。解析时成抽象语法树AST。var a = 2;语句是根，等号是中间的子树，等号左边的var,a,是左子树，等号右边2，；是右子树
     ```

   - 代码生成

     ```js
     //将AST转换成可执行的代码的过程，转换成一组机器指令
     ```

3. 执行阶段

   - 引擎运行代码时首先查找当前的作用域，看a变量是否在当前的作用域，如果在，引擎会直接使用变量；如果否，引擎会继续查找；
   - 如果找到了变量，就会将2赋值给当前变量，否则就会抛出异常

4. 查询

   - LHS，RHS实际看视频

5. 嵌套（作用域变量的查找机制）

   ```js
   function foo(a){
       console.log(a + b);//函数作用域里没有b这个变量，引擎就会到外层作用域里去找这个变量，找不到就会异常
   }
   var b = 2;//变量声明提升
   foo(4);
   ```

6. 异常（了解）

7. 词法作用域

   ```js
   function foo(a){
       var b = a * 2;
       function bar(c){
           console.log(a,b,c) //2,4,12
       }
       bar( b*3 )
   }
   
   foo(2);
   
   //一共有3层作用域：
   //第一层是全局作用域，含有foo这个词
   //第二层是foo函数里面的，有b，a,bar这三个词
   //第三层就是bar函数里面的，有c这个词
   ```

   - 遮蔽效应

     - 作用域查找从运行时所处的最内部作用域开始，逐级向上进行，直到遇到第一个匹配的标识符为止

     - 在多层的嵌套作用域可以定义同名的标识符，这叫做遮蔽

       ```js
       var a = 0;
       function test(){
           var a = 1; 
           console.log(a); 
       }
       //test()执行函数test的时候，作用域查找就是从test函数开始，当在函数中找到a变量的时候，就不会再往上查找
       ```

   - 变量的声明提升

     ```js
     a = 2;
     var a;
     console.log(a);//可以执行，不会报错但显示undefined，其实就等于下面这个情况
     var a;//变量被提升到最上面
     console.log(a);//显示undifined
     a = 2;
     //这是预解释现象
     ```

   - 函数的声明提升

     ```js
     foo();
     function foo(){
         console.log(1);
     }//这段代码可以执行，显示1
     
     foo()
     var foo = function(){
         console.log(1)
     }//函数表达式不能提升，会显示foo不是一个function
     ```

   - 声明的注意事项

     - 变量声明和函数声明，变量的声明会先于函数声明，函数的声明会覆盖未定义（未赋值）的同名变量

       ```js
       var a;
       function a (){}
       console.log(a) >>> //会显示函数
           
       var a = 10;
       function a (){}
       console.log(a) >>>>//会显示10,因a变量定义了
       ```

   - 作用域链

     下面的作用域链就是 bar->fn->全局，标识符解析就是沿着作用域链一级一级地搜索标识符的过程，而作用域链就是保证对变量和函数的有序访问

     ```js
     var a = 1;
     var b = 2;
     function fn(x){
         var a = 10;
         function bar(x){
             var a =100;
             b = x + a; //b是自由变量
             return b
         }
         bar(20);
         console.log(b);
         bar(200);
         console.log(b);
     }
     fn(0)
     ```

   - 自由变量：在当前作用域中存在，但未在当前作用域中声明的变量（在上级或全局作用域存在）。如上面bar函数中的b变量

   - 执行环境和执行流

     - 执行环境也叫执行上下文
     
     - 每个执行环境都有一个与之关联的变量对象，环境中定义的函数和变量都保存在这个对象中
     
       ```js
       //比如上面的fn(0)执行环境就是一个变量对象，包含了这个函数的所有变量：
       {
           x:0;
           a:undefined;
           bar:function;
           arguments:[0];
           this:window;
       }
       ```
     
   - 执行环境栈

     ```js
     //比如上面的fn(0),首先是全局执行环境入栈，随着fn函数的调用，会顺着执行流，将fn函数的执行环境入栈，然后再把bar函数的执行环境入栈，当函数执行完毕，就再依次出栈，最后将执行环境交还给全局环境
     ```

   总结：

   - 在js中，除了全局作用域，每个函数都有自己的作用域
   - 作用域在函数定义的时候就已经确定了，与函数调用无关
   - 通过作用域，可以查找作用域范围内的变量和函数有哪些，却不知道变量的值是什么，所以作用域是静态的
   - 对于函数来说，执行环境是函数调用时候确定的，执行环境中包含作用域内的所有变量和函数。在同一个作用于下，不同的调用会产生不同的执行环境，比如上面的bar(20),bar(200)。所以执行环境是动态的

## 十七. 闭包

### 17.1 理解闭包

定义：一般来说函数外部是不能访问到函数内部的变量的，如下

```js
function fn1(){
    var b = 234
    console.log('内部')
}
console.log(b)//这个会报错
```

但通过闭包，可以实现从外部访问内部的变量，原理就是在函数内部嵌套一个函数

```js
function fn1(){
    var b = 123;
    function fn2(){
        console.log(b)
    }
    return fn2
}
var result = fn1();
result()
```

闭包最大的特点是可以记住它诞生的执行环境，所以fn2可以得到fn1中的内部变量

### 17.2 闭包的用途   

1. 计数器

   ```js
   function a(){
       var start = 0;
       function b(){
           return start++;
       }
       return b;
   }
   var inc = a();
   console.log(inc()) >>> 1
   console.log(inc()) >>> 2
   //当调用inc的时候，实际是在调用函数b，每次调用函数b执行环境其实都是在a函数中，所以a函数中的start会随着inc的调用而不断改变
   //当不需要使用闭包的时候，要记得释放当前的变量防止内存泄漏
   inc = null;
   ```

2. 封装对象的私有属性和方法

   ```js
   function Person(name){
       //私有属性
       var age;
       //私有方法
       function setAge(n){
           age = n;
       }
       function getAge(){
           return age;
       }
       return {
           name:name,
           setAge:setAge,
           getAge:getAge
       }
   }
   
   var p1 = Person('mjj') //返回一个对象，对象里面有name属性，setAge和getAge方法
   p1.setAge(18),
   console.lo(p1.getAge())//
   p1 = null;//一定要释放
   ```

3. 闭包注意点 

   - 使用闭包使得函数中的变量始终在内存中，内存消耗很大，所以不能滥用闭包，否则会造成页面的性能问题
   -  闭包需要的三个条件
     - 函数嵌套
     
     - 访问所在的作用域
     
     - 所在作用域外被调用
     
       

4. 立即执行函数（IIFF）

定义函数之后，立即调用该函数，这种函数叫做立即执行函数

- 如果function出现在行首，一律解释成声明语句，解决这种问题的一个方式就是用括号，括号js会当成表达式

  ```js
  (function (){})();
  //这就是IIF，用括号把函数包围起来了
  (function(){}());//这也可以
  ```

- IIFF应用，可以当作闭包使用，封装私有的属性

  - 计数器

    ```js
    //需求：每次调用add,都返回加1的数字
    var add = (function(){
        var count = 0;
        return function (){
            return count++;
        }
    })();
    ```

- 对循环和闭包的错误理解

  ```js
  function foo(){
      var arr = [];
      for(var i = 0; i < 0; i++){
          //由于for循环中的i（foo函数作用域下）和return的i不再一个作用域中，所以每次返回的i都是循环完成后的
          arr[i] = function(){
              return i;
          }
      }
      return arr;
  }
  var bar = foo();
  console.log(bar[0]());>>10
  console.log(bar[5]());>>10
  
  //解决的方案是在arr[i]函数外面嵌套一个函数，形成闭包
  function foo(){
      var arr = [];
      for(var i = 0; i < 0; i++){
          arr[i] = (function(n){
              //n接收到了实参
              return function(){
                  return n
              }
          })(i);//这个是给自执行函数传的实参
      }
      return arr;
  }
  ```

5. 闭包的10种表现形式

   1. 返回值 (最常见的一种形式)

      ```js
      var fn = function(){
          var name = 'mjj'
          return function(){
              return name;
          }
      }
      var fnc = fn()
      ```

   2. 函数赋值(将内部的函数，赋值给外部的变量)

      ```js
      var fn2;
      var fn = function(){
          var name = 'mjj'
          var a = function(){
              return name;
          }
          fn2 = a;
      }
      fn();//先执行fn，fn会执行fn2=a，fn2就被赋值成了a函数
      cosole.log(fn2())//这样fn2()就可以使用内部的函数了
      ```

   3. 函数参数

      ```js
      var fn2 = function(f){
          console.log(f()) 
      }
      
      function fn(){
          var name = 'mjj';
          var a = function(){
              return name;
          }
          fn2(a);
      }
      
      fn();//1.外部调用fn，就会去执行fn2(a),a函数就会被传递到fn2里面去，这样就相当于是把一个a函数的参数传到另一个函数里面去了
      ```

   4. IIFF

      ```js
      //和上面的类似，只是利用自执行函数省略了调用函数的代码
      var fn3 = function(f){
          console.log(f())
      }
      
      (function(){
          var name = 'mjj';
          var a = function(){
              return name;
          }
          fn3(a);
      })()
      ```

   5. 循环赋值

      ```js
      function foo(){
          var arr = [];
          for(var i = 0; i<10;i++){
              (function(i){
                  arr[i] = function(){
                      return i;
                  }
              })(i);
          }
      }
      ```

   6. getter和setter函数来将要保存的函数放在内部

      ```js
      var getValue,setValue;
      (function(){
          var num = 0;
          getValue = function(){
              return num;
          }
          setValue = function(n){
              if(typeof n ==='numbser'){
              	num = n
              }
          }
      })();
      console.log(getValue());
      setValue(10)
      ```

   7. 迭代器

      ```js
      //计数器   
      var add = function(){
          var num = 0;
          return function(){
              return num++;
          }
      }();
      console.log(add())
      
      //迭代器实现
      //['mss','like','ss']
      var setUp = function(arr){
          var i = 0;
          return function(){
             	return arr[i++];
          }
      }
      var next = setUp(['mss','like','ss'])
      
      console.log(next());>>>mss
      console.log(next());>>>like
      ```

   8. 区分是不是首次调用

      ```js
      var firstload = (function(){
          var n = 0
          return function(){
              if(n === 0){
                  n++;
                  return true
              }else{
                  return false
              }
          }
      })();
      
      firstload();>>>true
      firstload();>>>false
      ```

   9. 缓存机制

      - 未加入缓存

      ```js
      function mult(){
          var sum =0;
          for(var i = 0;i< argument.length;i++){
              sum = sum + arguments[i];
          }
          return sum;
      }
      
      console.log(mult(1,2,3));>>>//显示6
      console.log(mult(1,2,3));>>>//显示6
      //因为没有加入缓存，所以两次调用都会去执行函数
      ```

      - 加入缓存

      ```js
      //看视频
      ```

   10. img对象图片上报

## 十八. this

1. this的绑定规则 - 默认绑定

   任何函数在没有指定前其实都是挂载在window对象下的，所以这也是为什么在对象下的this指向对象，而函数的this指向window

   - this默认指向window

     - 全局环境下的this指向了window

     -  函数独立调用(函数挂载在window对象下)，函数内部的this也指向了window

     - 被嵌套的函数独立调用时，this也指向window

       ```js
       var a = 0
       var obj = {
           a:2,
           foo:function(){
               function test(){
                   console.log(this.a)
               }
               test()
           }
       }
       obj.foo();>>>0
       
       //函数作为对象的方法时，this就会指向当前的对象
       var a = 0
       var obj = {
           a:2,
           foo:function(){
               var that = this
               function test(){
                   console.log(that.a)
               }
               test()
           }
       }
       obj.foo();>>>2
       
       ```

     - IIFE函数中的this也指向window

     - 闭包默认this指向window  

2. this隐式绑定



## 十九.js面向对象

1. 对象是什么

   - 对象是单个实物的抽象

2. 构造函数

   定义：js不是基于类的，而是基于构造函数constructor和原型链prototype

   ```js
   function Dog(name,age){
       //这就是一个构造函数，为了和普通函数区别，函数名的第一个通常大写
       //函数体内的this代表了索要生成的实例对象
       this.name = name;
       this.age = age
   }
   //必须使用new关键字来实例化对象
   var dog1 = new Dog('阿黄',10);
   //如果不写new，就相当于是使用普通函数，但是可以使用instanceof来纠正new关键字忽略的情况，如下
   
   function Dog(name){
       if(!(this instanceof Dog)){
           //如果实例化的时候没用new，this就会指向window
           return new Dog(name)
       }else{
           this.name = name
       }
   }
   var d1 = Dog('kk')
   ```

   1. new 命令内部原理

      ```js
      //1.创建一个空对象，作为将要返回的对象实例
      //2.将这个空的对象原型对象，指向了构造函数的prototype属性对象
      //3.将这个实例对象的值赋值给函数内部的this关键词
      //4.执行构造函数体内的代码
      function Persion(name){
          this.name = name
          this.sayName = function(){
              console.log(this.name)
          }
      }
      var p1 = new Person();
      
      console.log(p1.__proto__ === Person.prototype);>>>true
      ```

   2. constructor

      每个对象在创建时都会自动拥有一个构造函数属性constructor，这个constructor是通过继承关系继承来的，它指向了构造函数

   3. 使用构造函数的利与弊

      - 好处就是每个对象都可以拥有自己的属性和方法

      - 坏处就是，不同对象的相同方法都会被创建，消耗内存，可以使用原型对象避免

3. 原型对象

   - 原型对象

   一个构造函数的prototype     Foo.prototype。其实所有函数都有一个prototype属性，它默认指向一个objec

   - 实例对象

   f1/f2就是实例两个拥有不同内存地址的对象，

   - 构造函数

   ```js
   //用来初始化新创建对象的函数，Foo是构造函数，它有一个属性prototype（原型属性），指向实例的__proto__属性
   
   function Foo(){};
   Foo.prototype.name = 'mjj'//mjj就是通过原型对象来赋予方法的，可以理解成python的类属性，类方法
   
   var f1 = new Foo();
   var f2 = new Foo();
   ```

4. 创建对象的5种模式

   1. 对象字面量
   2. 工厂模式
   3. 构造函数模式
   4. 原型模式
   5. 组合模式

5. 实现继承的5种方式



