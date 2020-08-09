#   HTML

有问题查MDN web官方文档

## 一.标签知识点

### 1.1相对路径

- . /当前目录
- ../上一层目录

### 1.2 图片格式

- png: 静态图片，支持透明     
- jpg:静态图片，不支持透明
- gif：动态图片，静态图片，支持透明

img元素如果只设置了width(或height)，浏览器会根据图片宽高比自动计算出height（width）

alt属性，当图片加载失效，显示的文本

px就是像素点

### 1.3 a标签属性

- 基本使用

  ```html
  <a href="www.baidu.com">百度以下</a>
  ```

- target属性

  _self(默认值)：在原来的窗口打开网页

  _blank：新建一个窗口打开网页

  ```html
  <a href="www.baidu.com" target="_blank">百度以下</a>
  ```

  _parent(和iframe一起使用才有效果)

  _top（和iframe一起使用才有效果)

  iframe是用来嵌套网页的，但是现在用得非常少

- base和a标签结合使用

  在head里面先设定一个base元素，在body中的a元素就可以直接将自己的值拼接到base里面去。简单来说就是base元素抽取了a标签中的一些元素

  ```html
  <head>
      <base href = "www.baidu.com" target="_blank">
  </head>
  
  <body>
      <a href="">百度以下</a>
      <a href="/1234">百度以下</a>
  </body>
  ```

- 锚点连接（点击a标签可以跳转到页面中的其他地方）,其实利用的就是id属性

  ```html
  <a href="#text1">跳转到text1</a>
  <div id="text1"></div>
  ```

- 伪链接（不是为了打开新的url，而是为了做别的事情，比如执行js代码）

  ```html
  <a href="javascript:alter()">弹窗一下</a>
  ```

## 二.列表元素

### 2.1 有序列表-ol、li

​	order list有序列表，前面会默认显示序号，直接子元素只能是li(list item)

```html
<ol>
    <li>奥迪</li>
    <li>宝马</li>
    <li>雅阁</li>
</ol>
```

### 2.2 无序列表-ul、li

​	unordered list，直接子元素只能是li

```html
<ul>
    <li>奥迪</li>
    <li>宝马</li>
    <li>雅阁</li>
</ul>
```

### 2.3 定义列表-dl、dt、dd

​	definition list，直接子元素只能是dt(definition term一般是用来做标题的)、dd（definition description 每一项的具体描述）

​	一般是一个dt后面跟着多个dd

​	dt,dd常见的组合：

​		事物的名称，事物的描述

​		问题、答案

​		类别名、归属于种类的各种事务

```html
<dl>
    <dt>西瓜汁</dt>
    <dd>红色的饮料</dd>
    
    <dt>咖啡</dt>
    <dd>黑色的饮料</dd>
    
    <dt>牛奶</dt>
    <dd>白色的饮料</dd>
</dl>
```

![image-20200708062625697](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200708062625697.png)

典型的使用

![image-20200708062723484](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200708062723484.png)

### 2.4 列表的属性

这些属性可以继承，给ol,ul元素设置，默认会用到li元素

ul和ol的区别就在与list-style-type这个属性

- list-style-type:设置前面的标记样式

  属性值：decimal(阿拉伯数字)，lower-roman(小罗马数字)，disc(实心圆)，circle(空心圆)，square（实心方块），none（什么也没有）

- list-style-image：设置某张图片为li元素前面的标记，会覆盖list-style-type的设置

- list-style-position：设置列表样式（序号，实心点）算不算在内容里面

  属性值:inside，outside

- list-style:上面三个属性的集合

  ```html
  list-style:outside url('路径')
  ```

## 三.表格元素

table:表格

tr: 表格中的行

td（table definition）：行中的单元格

thead:表格第一行

tbody:表格主体

caption:表格的标题

thead里面一般用th来代替td

tfoot：表格尾部

### 3.1 table常用的属性

![image-20200708064120683](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200708064120683.png)

表格边框默认单元格有自己的边框，如果想要相邻的边框实现合并，实现细线表格，在table属性里面设置border-collapse:collapse

### 3.2 th,td的常用属性

![image-20200708064303134](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200708064303134.png)

### 3.3 单元格合并

只能向右、向下合并

对td标签使用colspan="2" 向右合并

使用rowspan=“2‘ 向下合并

### 3.4 boder-spacing

设置在table上面，可以设置两个值，分别代表水平，和垂直方向

## 四. 表单元素

### 4.1 常用元素

- form 表单，一般情况下其他元素都是它的后代元素

- input（可以设置maxlength属性）

  属性值：

  type = text(明文）/password（暗文）/radio（单选）/checkbox{复选}/button（按钮）/reset/submit/file

  value = "要显示的内容"

  maxlength = 120

  placeholder=”向显示的内容“，占位文字

  readonly:只读属性，不能输入（不用给值）

  disabled:禁用标签（没有值）

  checked默认被选中（没有值）、

  autofocus：页面刷新自动获得焦点（没有值）

  name: 在提交表单的时候作为key出现在url中    &name = value

- textarea 多行文本

- selet, option

- button

- label 表单元素的标题

- fieldset 表单元素组

- legend fieldset的标题

实例：

![image-20200708203645057](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200708203645057.png)

使用fieldset，和legend就可以实现带标题的外边框

```html
<body>
    <fieldset>
        <legend>必填信息</legend>
        <div><span>手机：<input type="text"></span></div>
        <div><span>密码：<input type="text"></span></div>
        <div><span>验证码：<input type="text"></span><button>获取验证码</button></div>
    </fieldset>
</body>
```

```html
<body>
    <form action="">
    <fieldset>
        <legend>选填信息</legend>
        <div>
            <span>照片：</span>
            <input type="file">
        </div>
        <div>
            <span>性别：</span>
            <!-- 单选框互斥选择要设定相同的name属性 -->
            男<input type="radio" value="男" name="sex">
            女<input type="radio" value="女" name="sex">
        </div>
        <div>
            <span>爱好：</span>
            <!-- 复选框也要使用name，这样才能配合提交 -->
            嫦娥<input type="checkbox" name="hobbies">
            王昭君<input type="checkbox" name="hobbies">
            貂蝉<input type="checkbox" name="hobbies">
            大桥<input type="checkbox" name="hobbies">
        </div>
        <div>
            <span>学历：</span>
            select 里使用mutable属性可以让它变成多选
            <select name="" id="">
                <!-- value才是真正提交到服务器的数据 -->
                在option里增加selected属性，让它变成select标签的默认值	
                <option value="0">小学</option>
                <option value="1">初中</option>
                <option value="2">高中</option>
            </select>
        </div>
        <div>
            <span>简历：</span>
            <!-- cols代表每行的字符个数，rows代表可以显示的行数 -->
            <textarea cols="20" rows="5"></textarea>
        </div>
    </fieldset>
    <!-- 重置input的类型必须是reset类型，可以不用写value -->
    <!-- 如果要重置生效，所有的元素必须是在form表单里 -->
    <input type="reset">
    </form>
</body>
```

### 4.2 布尔属性

可以没有属性值，属性名就代表这个属性

disabled,checked,readonly,multiple,autofocus,selected

如果要给bool类型设置，属性值就是它本身

### 4.3 按钮

按钮的实现可以使用：

1. input(type设为button，设为reset就是重置按钮)

2. button

   button也有type属性，也可以设为reset，默认是submit

按钮的属性重要的是submit,要在表单里面设置action属性。

表单里单个input标签提交表单的时候里面必须要设置name属性

表单里多个数据提交，只要有一个input设置submit属性就可以提交

```html
<form action="https://www.baidu.com">
    <input type="text" name="username">
    input里面填写like
    提交的url变成 https://www.baidu.com/?username=like
</form>
```

### 4.4 input和label的关系

点击label标签，input获得聚焦。label要设置for属性

```html
<div>
    <label for="phone">手机</label>
    <input type="text" id="phone">
</div>
```

### 4.5 input边框

默认情况下，输入框获得聚焦后，边框会改变样式,可以设置outline：none来取消它的默认设置，也通过动态伪类来更改它聚焦的样式

```html
<style>
    input{
        outline:none
    }
    input:focus{
        border-color:blue
    }
</style>
```

### 4.6 textarea

常用属性：

- cols:行数
- rows：列数
- resize：none;禁用缩放功能。resize:horizontal/vertical水平垂直缩放

### 4.7 select和option

select属性:

- mutible,多选
- size=‘2’    显示的个数是2

option属性：

- selected，默认选中

### 4.8 表单提交

1. 传统的表单提交

   1. 将所有的input包裹到一个form中

   2. form设置action

   3. 有一个input/button标签属性是submit

      弊端：

         1.会进行页面的跳转，服务器必须提前渲染并提交一个页面给前端

      2. 不利于表单数据的验证

      好处：服务端渲染有利于seo优化

2. 前后端分离，通过js获取表单内容，然后浏览器先进行验证，再通过ajax将数据传给后端。

想要提交，input里面必须要有name属性，作为查询的key。一般输入框里的内容作为值。但有的比如radio没有输入框，那就需要设置value值

### 4.9 get/post请求

get请求（默认方式）：

​	表单默认的提交方式，会将要查询的东西通过?拼接到url后面，多个参数用&连接。但是url有长度限制，如果在textarea里面写了很多东西，那么get方法就提交不过去，需要用到post。因为post会将请求的参数放到请求体里面去，这样就可以随便写多少东西了

post请求：

### 4.10 target属性

form也可以设置target属性，默认是在当前页面跳转，设置为_blank就会打开新的页面

### 4.11 accept-charset(一般不用)

默认值是unknow，和文档的编码一致

### 4.12 enctype（encode type）

规定了在向服务器发送表单数据之前如何对数据进行编码

一般有三种值：

- application/x-www-form-urlencoded     默认的编码方式
- multipart/form-data          有一个input的type类型是file，上传文件时必须是这个值，method必须是post
- text/plain   普通文本传输

## 五. 布局

如果想要给将div元素在网页中居中显示，就设置一个抽离的类

```html
.wrap{
	width:1000px;
	margin:0 auto;
}
```

然后其他元素使用这个类就行了

```html
<html>
    <div class="header wrap"></div>
</html>
```



# CSS 使用

## 一. 基本使用

三种引用方式：

- 内联样式

- 文档样式

  在head标签里面通过选择器写style link

  ```html
  <head>
      <link rel="stylesheet" href="./css/style.css">
  </head>
  ```

  

  也可以在style中使用@import 

  ```html
  <style>
      @import 
  </style>    
  ```

  

  可以单个选择元素

  也可以并集选择器

  还有类选择器

  元素选择器

- 外部样式在head里面用link引入

## 二.CSS选择器

- 通用选择器      *{}

  ```html
  *{
  	color:red
  }
  ```

  所有标签里面的颜色都会变成红色

  一般用这个去除外边距，内边距

- 元素选择器      标签名{}

  直接使用标签的名字，那么所有该标签都会使用

  ```html
  div {
  	color:red    
  }
  所有div标签里面的文字颜色都会变成红色
  ```

- 类选择器      .+类名{}     用得最多

  ```html
  <div class="box">
      我是div
  </div>
  
  <style>
      .div{
          color:red
      }
  </style>
  ```

  不同标签，拥有相同的类也可以使用。

  一个标签可以有多个类

- id选择器    #id名{}

  ```html
  <div id="header">
      <div class="he">
          hehe
      </div>
  </div>
  
  <style>
      #header.he{
          color:red
      }
  </style>
  ```

- 属性选择器 [属性名]{}

  ```html
  <div title="div元素">
      我是div元素
  </div>
    
  [title]{
  	//所有含有title属性的标签都会使用
  	color:red
  }
  [title="div元素"]{
  	//title属性值是div元素的标签才会使用
  }
  [title*="元素"]{
  	//title属性值当中包含元素两个字符的标签会使用
  }
  [title^="元素"]{
  	//title属性值当中以元素两个字符开头的标签会使用
  }
  [title$="元素"]{
  	//title属性值当中以元素两个字符结尾的标签会使用
  }
  ~=是包含单词的标签
  ```

  

- 组合选择器（后代选择器）

  ```html
  div span{
  	选择div元素下的span元素（直接子代和间接孙子都有效）
  }
  ```

  子选择器 >

  ```html
  div>span{
  	只能选择直接子代
  }
  ```

  相邻兄弟选择器 + （前后标签必须是兄弟关系）

  ```html
  div+p{
  	选择的是div后面的p标签中的原色
  } 
  ```

  全体兄弟原则器 ~

  ```html
  div~p{
  	//选择的是所有在div标签后面的p标签
  }
  ```

  交集选择器

  ```html
  div.one {
  	选择div中的one类
  }
  ```

  并集选择器

  ```html
  div, .one, [title="test"]{
  //选择三个的并集
  }
  ```

  

- 伪类pseudo-classes

  常见的伪类

  1. 动态伪类

     :link，:visited, :hover, :active, :focus

     例1    a:link(未访问的链接)    a:visited(已访问的链接)   a:hover(鼠标挪到链接上)    a:active(激活状态的链接)

     ```html
     <style>
         a:link{color:red}  //没访问的时候
         a:visited{color:blue} //访问过的时候
         a:hover{color:green} //鼠标放上去的时候
         a:active{color:yellow} //鼠标点击未松手的时候
         
         hover必须放在link 和visited后面才行
         active必须放在hover后面
     </style>
     
     
     <a href='#'>谷歌一下</a>
     ```

     :focus获取焦点的时候

     ```html
     <style>
         input:focus{
             background-color:red
         }
     </style>
     
     <input type=text>
     当输入框选中时候，就会改变背景颜色。a标签也可以使用，要放在hover前面
     ```

     如果想要去除a元素的聚焦状态可以使用

     ```html
     a:focus{
     	outline:none
     }
     ```

     

  2. 目标伪类(不常用)

     :target

     主要是配合锚点一起使用

     ```html
     <a href="#title">点击</a>
     <p id="title">标题1</p>
     
     <style> 
         :target{
             color:red
         }
     </style>
     当点击a标签的时候，a标签和p标签的字体颜色会变成红色
     ```

     

  3. 语言伪类（不常用）

     :lang()

  4. 元素状态伪类（不常用）

     :enabled、:disabled、:checked

     ```html
     <style>
         :disabled{
             //直接选择具有某种属性的标签
             color:red
         }
     </style>
     <button disabled>我是按钮</button>
     ```

  5. 结构伪类

     :nth-child(),:nth-last-child(),:nth-of-type(）,:nth-last-of-type()

     

     :nth-child(1)  选中子类的，数字代表第1个子类

     ```html
     <style>
         :nth-child(3){
             color:red
         }
         
         //交集选择器
         p:nth-child(3){
             //必须是p选择，p元素是子元素中的第三个元素
             color:red
         }
         
     </style>
     
     <div>
         <p>内容1</p>
         <p>内容2</p>
         <p>内容3</p>
         <p>内容4</p>
         <p>内容5</p>
     </div>
     <p>
         <span>文字1</span>
         <span>文字2</span>
         <span>文字3</span>
         <span>文字3</span>
     </p>
     
     内容3，和文字3会变成红色
     ```

     :nth-child(n)代表0，1，2，……的所有子元素

     :nth-child(2n)代表偶数，2n可以替换成even,odd代表奇数

     

     :nth-last-child(3)倒数第三个元素	

     

     p:nth-of-type(3)只计算p元素的个数

     ```html
     p:nth-of-type(3){
     	color;red
     }
     
     
     <div>
         <div>我是div</div>
         <p>文字1</p>
         <p>文字2</p>
         <p>文字3</p>    //变成红色
     </div>
     如果是用:nth-of-type(3)或者p:nth-child(3)那么是文字2变成红色
     ```

     

     

     :first-child,:last-child,:firt-of-type,:last-of-type

     :root,:only-child,:only-of-type,:empty

     ​	:only-child选中的是唯一子元素

     ​	:empty选中的元素内容为空的标签

  6. 否定伪类

     :not(x） x可以是元素选择器，通用选择器，属性选择器，类选择器等。如

     :not(div) 选中除了div之外所有的元素

- 伪元素(使用字体属性，颜色属性，背景属性。其他属性不适用)

  ::first-line(很少用)

  ```html
  p::first-line{
  	font-size:18px//改变p段落中第一行的字体大小
  }
  ```

  ::first-letter（很少用）

  ```html
  p::first-letter{
  	选中p标签中的第一个字符
  }
  ```

  ::before（经常用）在元素前面添加内容，也可以改变margin边距。content后面还可以跟图片，而且content不能少。

  伪元素可以看成是行内元素

  ```html
  <style>
      span::before{
          content: '1';
          //content:url(图片路径)
          color: red;
      }
  </style>
  
  <span>我是span元素</span>
  
  
  >>>1我是span元素     (1显示红色，而且不是在span标签内)
  ```

  

  ::after（经常用）

## 三. 常用的CSS属性

1. color前景色（文字颜色）

   不光是文字，如果设置text-decoration:line-through。线的颜色也会变，包括边框

   所以前景色包括（文字，边框……）

2. font-size

3. background-color背景色

4. width（不适用行内标签）

5. height（不适用行内标签）

Tips：

​	如果想要知道网页的布局，可以使用div的outline属性

![image-20200707181143483](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200707181143483.png)

```html
div{
	outline:2px solid green !import
}
```

## 四. 颜色的表示方式

- 直接使用单词 如red等

- 使用rgb,数值范围在0-255之间

  ```html
  color:rgb(0,0,0)
  ```

- RGBA透明度

```html
color:rgba(0,0,0,0.1s)
```

## 五. 文本属性

- text-decoratioon

  设置文字的装饰线

  包括：none，underline（下划线），overline（上划线），line-through（中划线）

- letter-spacing 设置字母之间的间距10px

- word-spacing 设置单词之间的间距 10px

- text-transform 设置文字大小写转换

  属性值：capitalize(首字母大写)，uppercase（所有字符大写）,lowercase(所有字符小写),none（没有影响）

- text-indent 设置第一行内容缩进

  属性值：16px(取决于字符的fontsize大小)，也可以设置2em，em是相对与文字的字符大写百分比

- text-align 设置元素中的内容（文字以及包括其他标签）在元素中的水平对其方式

  属性值：left,right,center,justify(两端对齐)

  justify对最后一行文本没有效果

## 六.CSS字体

- font-size：

  属性：

  1. 数值+单位（1em代表100%，2em=200%相对父元素的font-size,text-decoration属性是相对于自己的元素）
  2. 百分比，相对父级元素的fontsize

- font-family 

  设置字体的样式（微软雅黑等），取决于操作系统支持的字体，一般存在c/windows/font文件夹下，一般会设置多个字体以防第一个字体找不到。

- font-weight 对字体进行加粗

  属性值：100|200|300~|900，一般使用700.也可以设置normal(400),bold(700)

- font-style

  设置文字的常规，斜体显示

  normal:常规显示

  italic:字体斜体显示（前提是字体支持斜体，有的字体不支持）

  oblique:文本倾斜显示（让文字倾斜）

  像一些标签如：em,i,u,address,var等都默认是italic。i标签经常用来做小图标

- font-variant:很少用

  属性值:small-caps

![image-20200707190946508](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200707190946508.png)

- line=height行高

  每行占据的高度，两行文字基线之间的间距

  ![image-20200707192117438](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200707192117438.png)

  应用：在div中的文字上下居中对齐，一般让line-height = div的height就会让文本居中，为什么呢？视频里有详细解释

  ![image-20200707192633224](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200707192633224.png)

- font缩写属性，后面可以跟多个值

  ```html
  font:italic small-caps bold 30px/50px
  ```

  30px(size)/50px(line-height)  line-height可以省略

## 七.css特性

### 7.1 继承

css中有些属性是可继承的，如font-size，color等。最典型的就是浏览器设置的字体就会被html标签继承。如果要确认属性可否继承，可以查MDN官方文档

可以使用属性:inherit强制继承父标签的元素如width:inherit。

### 7.2 层叠

- 基本层叠：使用了相同的选择器（比如多使用类选择器）

  ​	后面的属性会把前面的相同属性覆盖掉

- 权重层叠：当使用了不同的选择器就要考虑选择器的权重了

  ​	通常设定：  

  ​	 id选择器100

  ​	class选择器10

  ​	元素选择器 1

  ​	!important 为10000

  ​	内联样式为1000

如果写的css属性不好使，可能的原因：

1. 选择器优先级太低

2. 选择器没选中对应的元素

3. css属性使用形式不对

   ​	元素不支持css属性，比如span就不至此width

   ​	浏览器不支持该属性

   ​	被同类css属性覆盖

## 八. 元素类型

- 块级元素（block-level-element）

  哪怕设置了width没有占满屏幕宽度

  独占**父元素**的一行，如：

  div，p,pre,h1-h6,ul,ol,li,dl,dt,dd,table,form,article,aside,footer,header,hgroup,main,nav,section,blockquote,hr

- 行内级元素(inline-level-element)

  多个行内级元素可以在父元素的同一行中显示，如

  span，strong，img，input,a,code,iframe,label,button,canvas,embed,object,video,audio

- 根据元素的内容，html元素还可以分为两类

  - 替换元素，如：img，input，iframe和inline-block类似
  - 非替换元素

### 8.1 display属性

为什么div等会是块级元素，因为所有的浏览器都会给这些元素设置display:block这个属性，其实原本它们都是行内级元素，w3c规定。

像span这些行内级元素，就是因为浏览器没加这个属性。

常见的属性：

- block:可以随意设置宽高，独占父元素一行
- inline 默认元素的属性
- none 把元素隐藏
- inline-block 让元素同时具备行内级和块级元素的特点，比如说让它可以设置宽高，但又可以跟其他元素在同一行

```html
 .header:hover+ul{
            display: block;
        }
可以用来做下拉菜单！！！！！！
```

display取以下值，等同于某些html元素

- table，一个block-level表格
- inline-table, 一个inline-level表格
- table-row>tr
- table-row-group>tbody
- table-footer-group>tfoot
- table-cell>td,th
- table-caption>caption
- list-item>li

### 8.3 visibility

属性值： hidden、visible

display:none  元素在页面中的空间会没有

visibility:hidden 元素在页面中的空间还在，但是看不见

### 8.4 overflow

常用于图片的长宽比父级元素的长宽大的情况

属性值: 

visible（溢出的内容照样可见）默认属性

hidden(超出部分隐藏)

scroll  (超出部分被裁剪，但可以通过滚动查看)

auto （根据内容是否溢出来设置是否使用滚动）



还有两个css属性：overflow-x,overflow-y，只有一个坐标轴会有滚动。但目前有的浏览器还没适配，所以还是使用overflow的多

## 九. 元素之间的空格

行内级元素之间都会产生空格，这是由于每个元素之间，我们使用了换行。所以去除空格的方法就是给元素添加float

## 十. 小知识点

一般来说，块级或者行内块级可以嵌套任何元素。除了p元素下不能签到div

一般来说，行内元素只能嵌套行内元素

## 十一. css盒子模型

每一个元素都可以看成是一个盒子

内容外面是padding，padding外面是border,border外面是margin

![image-20200709200017572](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200709200017572.png)

### 11.1 内容相关的属性

width和height是内容相关的属性

设置min-width就可以让浏览器出现滚动条

min-height可以设置浏览器的最小高度

### 11.2 内边距相关属性

padding: 上 右 下 左

当只有3个值得时候，左得值等于下

当只有2个值得时候，分别是上和右，下跟随上，左跟随右

当只有1个值得时候，上下左右相同

外边距类似

### 11.3 上下margin传递 

如果内外元素的上下边是重叠的，当内元素去设置margin-top/bottom的时候，就会传递给外元素

```html
<head>
	<style>
        .box{
            width: 200px;
            height: 200px;
            background-color: red;
        }
        .box1{
            width: 400px;
            height: 400px;
            background-color: yellow;
        }
        .box2{
            width: 200px;
            height: 200px;
            background-color: green;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <div class="box"></div>
    <div class="box1">
        <div class="box2"></div>
    </div>
</body>
```

![image-20200709205427382](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200709205427382.png)

如何防止传递，只要给父元素设置padding或者触发BFC（相当于是一个结界，block format context）

如何触发BFC：

​	设置一个元素的overflow为非visible

​	使用float

​	只设置父级元素padding

### 11.4 上下margin的折叠

垂直方向上的相邻的两个div的margin有可能会折叠成一个margin,水平方向上的不会出现

如何防止：只设置一个元素的margin

## 十二. 盒子border属性

边框有3类属性，上右下左

边框的宽度

边框的颜色

边框的样式

### 12.1 边框样式的取值

![image-20200709210655136](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200709210655136.png)

### 12.2 边框的使用

![image-20200709211730773](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200709211730773.png)

![image-20200709211740884](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200709211740884.png)

![image-20200709211755556](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200709211755556.png)

![image-20200709211809214](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200709211809214.png)

![image-20200709211951765](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200709211951765.png)

- 以下属性对行内非替换元素不起作用

width,height,margin-top,margin-bottom

- 以下属性对行内非替换元素的效果比较特殊

padding-top,padding-bottom,上下方向的border

比如使用padding-bottm，那么span元素的下面会多出来一块区域，但是不占据空间，如图已经延伸到div元素里去了。但是对于border来说左右方向正常延伸，并且占据空间，border的上下又会出现跟padding一样的情况

![image-20200709212604463](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200709212604463.png)

可以把span元素改成行内块级元素来解决这个问题

### 11.5 border的radius（圆角效果）

四个单独设置，有两个值

border-top-left-radius:55px 25px

55px是水平方向上的值，25是垂直方向上的

一般来说是直接用border-radius：10px直接设置四个角

![image-20200709212755377](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200709212755377.png)

![image-20200709213234336](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200709213234336.png)

## 十三. outline

outline是不占空间的，而且显示在border外面

相关属性：(和border很类似)

- outline-width
- outline-style
- outline-color
- outline:outline-width outline-style outline-color

应用实例

去除a元素，input元素的focus轮廓效果

## 十四. box-shadow

box-shadow = inset(添加之后阴影往里) 5px(水平偏移) 5px(上下偏移) 5px(模糊半径) 5px(像四周增加5px) rbga(设置颜色)

## 十五. text-shadow

和box-shadow的参数设置一样，同样适合::first-line,::first-letter伪元素，但是没有inset属性值

## 十六. box-sizing

默认情况下 box-sizing：content-box，表示设置宽度和高度的时候只代表内容，最终的盒子宽高=内容宽高+padding+border

![image-20200710190355755](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200710190355755.png)

border-box：表示设置宽度和高度时就已经涵盖了内容，padding，和border

![image-20200710190431598](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200710190431598.png)

## 十七. 水平居中的不同类型方式

一般来说，子元素想要在父元素里面居中只要使用text-align就行，一般文本内容、行内元素、图片元素、行内块级元素都只需要用text-align:center就行。但是当子元素是块级元素时，这个就失效了。因为块元素直接占了一行，不用居中。如果这个块级子元素设置了width。想要将内容居中，那外面就要给这个子元素设置 margin：0（上下距离） auto（左右距离）。



margin-left,和margin-right的默认值都是0，如果使用margin-right:auto的话，也可以实现div靠右



## 十八. css背景

- background-image 设置元素的背景图片盖在background-color上面
- backgroud-repeat: repeat(默认是这个值) ，repeat-x(只在X方向平铺)，repeat-y（只在y方向），no-repeat（不平铺）
- backgroud-size: cover(用一张图片撑满内容，会改变图片的原尺寸)，contain（按照图片的原宽高比来拉伸图片，直到先撑满一个方向为止），30% 80%（图片宽占总宽30%，长度占80%），300px 300px(直接设置图片的宽高值)
- backgroud-position:60px 80px （图片的宽距盒子60px，顶边离盒子顶边80px），center center(水平垂直居中)， right top（盒子右上）

怎么让背景一直居中？

```html
.box{
	background-img:url('../img/mhxy.jpg')
	background-position:center center
}
```

- background-attachment（用的比较少）

  属性值：

  scroll: 浏览器滚动的时候，背景图片随元素一起滚动（默认）

  local：背景图片跟随元素以及元素内容一起滚动

  fixed：背景图片想对浏览器固定

- backgroud（背景的所有属性，都可以在里面）

  常用的格式：img position/size repeat attachment color

```html
backgroud:url('imgages/beer.png') center center/150px 250px no-repeat #f00;
```



## 十九. css-sprite

css一种技术，将多张图片放到一张图片里面，好减少http请求次数，加快响应速度。然后利用css背景定位来显示需要的图片。sprite图片一般使用photoshop或者用sprite-generator网站。sprite就是配合backgroud-position使用的

![image-20200710195021353](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200710195021353.png)

## 二十. cursor(光标)

用于设置在元素上面时的显示样式

常见的值：

- auto

  浏览器根据上下文自动设定，比如a连接显示小手，input输入框显示文本输入

- default: 系统设置，就是一个小箭头

- pointer:小手

- text:文本输入

- none

## 二一. 定位

### 21.1 标准流 Normal Flow

默认情况下，都是按照标准流来排布，也可以被称为常规流，文档流

默认情况下，兄弟元素互相之间不存在层叠

![image-20200711080032194](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200711080032194.png)

在标准流里，使用margin,padding对元素进行定位，但是它会影响到其他元素的定位。比如，显示下拉菜单，如果菜单在标准流里面，就会把其他元素的布局打乱。这时候就需要使用定位position，让菜单脱离标准流

position常用的值：

- static:静态定位（默认元素的设置，元素属于标准流），设置此属性的元素，left,right,bottom,top没有任何作用

- relative:相对定位，相对自己原来的位置。如果只设置了position:relative，则元素依然在标准流里占据空间，一旦设置了top,left等，就会脱离标准流相对自己原先进行偏移，但是它原先在标准流里面的空间依然还占据着。

- absolute：绝对定位，会一直往上层找非static属性的父元素，找到了，那么它的属性值（top,left,top,right）就是相对这个非static属性的父元素。如果一直没有找到非static属性的盒子，就会相对视图进行绝对定位，等于fixed了

  子绝父相：绝大多数情况下，子元素的绝对定位是相对于父元素的相对定位，如果希望子元素绝对定位与父元素，又不希望父元素脱标，常用的方案是：

  父元素设置position:relative让父元素成为定位元素

  子元素设置position:absolute

  简称子绝父相

  

-  fixed:相对于浏览器视口（浏览器画布一般都比视口大很多）进行定位，常用来做导航栏，不会随画布滚动。而且元素会脱离标准流，不占据空间

练习：如过要在一个固定宽度的div里面放置一张很宽的图片，要求始终显示图片的中心内容（div缩小也显示中心内容），使用

希望图片向左移动的距离：

= 图片宽度X0.5 -div宽度X0.5



使用left百分比属性是定位元素相对于父元素的，而translate是相对元素本身



## 二二. 脱标元素的特点

能够脱离标准流的元素：position:fixed/absolute,float

特点:

- 可以设置宽度和高度
- 没有设置宽高时候，由内容默认决定
- 不再受标准流的约束
- 父元素不再受它的影响

脱标元素和display的的区别？

脱标的元素一般都是变成块级元素，所以它能设置宽高，因为脱标的元素没有父元素的设定auto的宽高，只能相对本身的内容来设置宽高

## 二三. 绝对定位技巧

绝对定位元素： adsolute或者fixed元素  

对于绝对定位到元素：

定位参照对象的宽度 = left+right+margin-left+margin-right+绝对定位元素的实际占用宽度，高度也一样。

如果要设置绝对定位元素在相对父元素左右上下都居中，那么父元素要设置成相对定位，子元素要设置成绝对定位。并且子元素的left,right,top,bottom要设置成0（默认值是auto），margin要设置成auto（默认是0）



定位元素一般会层叠在非定位元素之上

z-index用来设置定位元素的层叠顺序（仅对定位元素有效）



元素之间的层叠关系

标准元素：标准流种的元素是不存在层叠

定位元素：定位元素会层叠到标准流元素的上面

- 定位元素之间可以z-index
- 前提必须是定位元素 - 非static
- 浮动元素：float

标准元素层叠在浮动元素下面，浮动元素层叠在定位元素下面

![image-20200711160359458](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200711160359458.png)

## 二四. 浮动float

在css中有3种常用的方法对元素进行定位、布局

- normal flow
- absolute positioning
- float

绝对定位和浮动都会让元素脱离标准流，以达到自由布局的效果。

但是浮动元素不能与行内级的内容层叠，行内级内容会被推出

### 24.1 浮动的规则

一.元素一旦浮动后，会脱离标准流，朝着左边或右边移动，直到自己的边界紧贴着包含块（一般是父级元素），或者其他浮动元素的边界位置。

二.浮动元素不能与行内级的内容层叠，行内级内容会被推出

三.行内级元素在浮动后，其顶部将与**所在行**（不会跑到其他行去）的顶部对齐

四. 浮动不能超出父元素的边缘

五. 浮动元素之间不能层叠

六. 浮动元素的顶端不能超过父级元素的顶端，也不能超过之前所有浮动元素的顶端



inline-block水平布局的缺陷：

比如说两个相同大小的div设置成inline-block，div里面没有内容的时候，两个div并排。一旦div里面写了文本或者其他内容，就会在竖直方向上出现错位。而且两个div之间会存在空隙，这个空隙是因为父级元素的空格（字体大小）造成的，所以一般我们使用float来进行布局



### 24.2 float常用的取值

none： 不浮动，默认值

left:	向左浮动

right：	向右浮动

最后一个元素margin取值的技巧：

开发中会碰到很多元素float的情况

![image-20200711170530718](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200711170530718.png)

前面3个元素，我们可以使用margin-left来获得空隙，但是最后一个不方便，所以一般我们会在父级元素和元素之间加一层div，给这个元素设置margin 负值来统一处理

### 24.3 浮动存在的问题

由于脱标，浮动元素的高度不会再向父元素汇报，父元素计算高度时，不会计算浮动元素的高度，这样就会导致高度坍塌的问题。

解决父元素高度坍塌的方法是清浮动，意思就是让父元素计算总高度时，把浮动子元素的高度也计算进去

清浮动的常见方式：

- 写死父元素高度（不推荐）

- 在父元素的下面增加一个空div，使用css属性clear:left/right/both

  left意思是div低于所有左浮动的元素，right/both类似

  但是这个方式会增加很多多余的div。（不推荐） 

- 在父元素的最后增加一个br元素，使用clear="all"，而且父元素还会出现高度（不推荐）

- 直接使用父元素的伪元素::after设置clear=both属性，就可以了（推荐）

  ```html
  .container::after{
  	content:'';      //content在after里面不能省略
  	clear:both;
  	display:block;     //默认伪元素是行内元素，要将它设置成块元素
  }最终效果和使用br一样
  ```

## 二五. transform（形变）

让你对某个元素进行旋转，缩放，倾斜，平移。一般来说是用来做动画的时候会用到，如果光是为了布局，还是用之前的方法

常见的函数transform function有:

平移：translate(x,y)

缩放：scale（x，y）

旋转：rotate(deg)

倾斜：skew（deg,deg）

具体使用：

- translate

```html
.test{
	width:100px
	height:100px;
	background-color:red
}
.test:hover{
	transform:translate(10px,0)
	//也可以使用百分比，参照的是元素本身
}
<div class='test'></div>div>
```

- scale

```html
.test{
	width:100px
	height:100px;
	background-color:red
}
.test:hover{
	transform:scale(2)
	//用的是数字，2代表放大一倍，一个值时代表x，y轴同时缩放，不支持百分比
}
<div class='test'></div>div>
```

- transform-origin

```html
.test{
	width:100px
	height:100px;
	background-color:red;
	transform-origin:center top;
	//这个是为了设置transform原点，默认x,y方向都是center，还可以设置left，right，top,bottom
}
.test:hover{
	transform:scale(2)
}
<div class='test'></div>div>
```

- rotate

  用例ransform:rotate(45deg)，正值代表正方向旋转45°，受transform origin原点影响

- skew:属性值和rotate一样也是角度

## 二六. transition过渡动画

transform是一个属性名称

transition也是一个属性名称，配合transform一起使用，其实它是多个css属性的缩写，包含：

transition-property

​	指定应用过度属性的名称，用all代表所有可动画的属性

​	属性是否支持动画要看文档

transition-duration

​	值过渡动画所需的时间s或ms

transition-timing-function

​	指动画的变化曲线

transition-delay

​	指延迟多久再执行动画

```html
.test{
    height: 200px;
    width: 20px;
    background-color: red;
    margin: 0 auto;

    transition: width linear 2s;
	//width代表就是宽度生效， linear 是变化曲线， 2s是动画时长
}

.test:hover{
    width: 400px;
}

<div class="test"></div>
```

## 二六. vertical-align

它会影响行内级元素在一个行盒中垂直方向的位置

思考一个问题，一个div没有设置高度，但有内容的时候，div高度的本质是什么？因为内容有行高（line-height），撑起了div的高度。为什么行高可以撑起div的高度？因为行盒（line-boxes）的存在，并且行盒有一个特性，包裹每行的inline-level,即每一行就是一个行盒。而其中的文字是有行高的，必须将整个行高包裹进去，才算包裹这个line-level。div的高度就是所有行盒高度的和。

同一行内的内容首先要遵循基线对齐，文字是x字符的底部，图片是自己的底边，没有文本的框也是自己的底边（添加了文本后，就以最后一行文字的基线对齐） 

### 26.1 vertical-align的默认值就是基线（baseline）

文本的基线就是x字符底部

inline-block也就是margin-bottom的底部

inline-block有文本时，就是最后一行文本的x底部

### 26.2 常用的属性

- baseline默认值 

- top 把行内盒子的顶部跟line boxes顶部对齐

  ```html
      <style>
          .test{
  
              width: 1020px;
              background-color: red;
          }
  
          .inner{
              height: 200px;
              width: 100px;
              background-color: blue;
              display: inline-block;
              vertical-align: top;
              //要在子元素里设置
          }
      </style>
  <body>
      <div class="test">
          <div class="inner"></div>
          adfasfaddf
      </div>
  </body>
  ```

  

- middle 行内级盒子的中心点与父盒基线对上x-height一半的线对齐

- bottom 把行盒底部跟line box底部对齐

- percentage ：0%跟baseline一样

- length：ocm跟baseline一样

# 布局方案对比

| 定位方案 | 应用场景 | 实例     |
| -------- | -------- | -------- |
| 标准流   | 垂直布局 | ·        |
| 绝对定位 | 层叠布局 | 下拉菜单 |
| float    | 水平布局 | 布局     |

# HTML5 

## 一.新增语义元素

在html5之前，网站分布层级通常包含(以id的形式表现)：

1. header
2. nav
3. main
4. footer

所以在html5新增了语义化元素：

1. header 头部元素
2. nav 导航元素
3. section 区域元素
4. article 内容元素
5. aside 侧边栏元素
6. footer 尾部元素

还新增了媒体类型元素（在html5之前是通过flash或者其他插件实现的）：

1. audio 让html支持音频播放

   ```html
   <audio src="音频地址"></audio>  也跟video一样拥有一些属性
   ```

2. video 让html支持视频播放

   ```html
   <video src="视频地址" controls autoplay muted></video>
   //controls是为了显示浏览器自带的视频控制栏，可以自定义
   //autoplay自动播放，但存在兼容性问题
   视频都是有格式（封装格式）的：mp4/avi/webm等等，但有的浏览器不一定支持这些格式，如果浏览器不支持上面的格式，还可以在video里嵌套source来给浏览器提供格式的选择
   <video>
       <source src="视频地址1.mp4"></source>
   	<source src="视频地址2.avi"></source>
   	<source src="视频地址3.webm"></source>
   </video>
   //视频格式除了封装格式，还有编码格式
   ```

## 二.input 元素扩展

placeholder, multiple, autofocus

另外，input的type属性值在html5里还有很多扩展：

1. date 使用这个属性后，可以直接出现日期的选框![image-20200715180140717](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200715180140717.png)
2. time
3. number 只能输入数字
4. tel
5. color 会出现调色板，会将颜色的数据提交到后端
6. email
7. 等等……

## 三. flex布局（完全可以代替浮动）

flex布局目前是web开发中使用最多的布局方案，在移动端最适用，目前PC端也越来越多

也被称为Flexible布局，弹性布局

### 3.1两个重要概念

1. 容器盒子需要开启flex布局，这样的元素被叫做flex container
2. flex container里面的元素被叫做flex item，这些items将不再具备块级或者行内级元素的性质

### 3.2 开启flex布局

直接给容器盒子赋予display:flex 样式

```html
<style>
    .box{
        display:flex;      //开启的盒子是块级元素
        display:inline-flex   //开启的是行内元素
    }
</style>
<div class="box"> //flex container
    <div></div>   //flex item
    <div></div>   //flex item
    <div></div>   //flex item
</div>
```

### 3.3 布局模型

![image-20200715182401456](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200715182401456.png)

主轴，和交叉轴的方向是有可能变得

### 3.4 flex相关属性

- 应用在flex container上的css属性

  1. flex-flow 是flex-direction||flex-wrap的简写

  2. flex-direction（决定主轴的方向）

     flex items默认是沿着main axis 从main start 开始往main end排布

     属性值：

     flex-direction:row;默认就是这个

     flex-direction:row-reverse; 主轴方向反转

     flex-direction: column; 主轴方向变为从上往下

     flex-direction: column-reverse; 主轴方向从下往上

  3. flex-wrap 决定了flex container是单行还是多行

     属性值：

     flex-wrap：nowrap（默认值），单行。所有的items都会在同一行显示，哪怕items的总宽度超过了flex盒子的宽度，items会被压缩

     ![image-20200715191910126](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200715191910126.png)

     flex-wrap：wrap，多行，container会被平分

     ![image-20200715192044287](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200715192044287.png)

     flex-wrap：wrap-reverse:多行，cross start 和end相反

     ![image-20200715192111246](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200715192111246.png)

  4. justify-content（决定了items在main axis上的对齐方式）

     属性值：

     justify-content: start;（items默认是紧挨着主轴的起点排布）

     ![image-20200715184247606](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200715184247606.png)

     justify-content: end; （item紧挨着主轴的重点）

     ![image-20200715184301083](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200715184301083.png)

     justify-content: center; （居中对齐）

     ![image-20200715184314381](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200715184314381.png)

     justify-content: space-between; （items之间距离相等。与主轴起点和终点两端对齐）

     ![image-20200715184333434](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200715184333434.png)

     justify-content: space -evenly; （items之间距离相等，并且和起点，终点的距离也相等）

     ![image-20200715184346936](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200715184346936.png)

     justify-content: space-around; （items之间距离相等，和起点，终点的距离是items之间的一半）

     ![image-20200715184402547](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200715184402547.png)

  5. align-items 决定了flex items 在cross axis上的对齐方式

     align-items：normal 默认值，在弹性布局中和stretch一样,items有高度的时候，在交叉轴上顶部对齐

     ![image-20200715190312499](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200715190312499.png)

     align-items：stretch 当flex items在cross axis方向的size为auto（没有设置高度时），会自动拉伸填充flex container

     ![image-20200715190049016](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200715190049016.png)

     align-items：flex-start

     ![image-20200715190312499](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200715190312499.png)

     align-items：flex-end

     ![image-20200715190710222](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200715190710222.png)

     align-items：center

     ![image-20200715190743164](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200715190743164.png)

     align-items：baseline（第一行文本的基线，这个跟行盒里面的不一样）

     ![image-20200715190826889](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200715190826889.png)

  6. align-content 决定了多行flex items在cross axis上的对齐方式，用法与justify-content类似

     属性值

      stretch默认值，

     ![image-20200715193533699](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200715193533699.png)

     flex-start

     ![image-20200715193515459](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200715193515459.png)

     flex-end

     ![image-20200715193553522](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200715193553522.png)

     center

     ![image-20200715193615563](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200715193615563.png)

     space-between

     ![image-20200715193639777](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200715193639777.png)

     space-around

     ![image-20200715193731445](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200715193731445.png)

     space-evenly

     ![image-20200715193704225](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200715193704225.png)

- 应用在flex item上的css属性

  1. flex 是flex-grow|flex-shrink|flex-basis的缩写，可以写1个值，2个或3个

     一个值的情况：

     - 无单位number,被当作flex-grow
     - 有效的宽度值，当作flex-basis
     - 关键字none,auto或initial

     2个值：第一个必须是无单位（代表grow），第二个值以下情况：

     - 无单位数，当作shrink
     - 有效的宽度，basis

     3个：第一个无单位当作grow,第二个无单位当作shrink,第三个有效的宽度当作basis

  2. flex-grow

     任何大于等于0的数

     所有item 的flex-grow之和大于1，那么每个item的size就是按照这个比例来算

     如果items的flex-grow之和不超过1，那么每个item的size就是container剩余的size*flex-grow

     最终size不能大于最大宽度

  3. flex-basis 用来设置flex items在main axis方向上的item size

     auto(默认值)

     具体的宽度数值（100px）

     item选择size大小的优先级

     - max-width/max-height/min-width/min-height
     - flex-basis
     - width\height
     - 内容本身的size

     

  4. flex-shrink 决定了items如何收缩

     可以设置任意非负数字，默认值是1

     当items在主轴的宽度和大于size时，flex-shrink才会生效

  5. order

     给item设定order值（任意整数），那么item就会依照数字大小依次排布

  6. align-self

     auto,stretch,flex-start,flex-end,center,baseline效果跟align-items一致

     单独给item设置一个对齐方式。container里设置align-items:center，item3设置align-self:end

     ![image-20200715194812621](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200715194812621.png)

     

## 四. 关键帧动画

使用@keyframes来制作动画，在animation后面可以跟多个动画，就是identifier1，identifier2

```html
<style>
    .box{
        height: 100px;
        width: 100px;
        background-color: red;
    }

    .box:hover{
        animation: identifier 12s linear;
    }

    @keyframes identifier {
        0%{
            transform: translate(0,0);
        }
        25%{
            transform: translate(200px,0);
        }
        50%{
            transform: translate(200px,200px);
        }
        75%{
            transform: translate(0,200px);
        }
        100%{
            transform: translate(0,0);
        }
    }
</style>
```

有这些属性：

animation-name 执行哪一个关键帧动画

animation-duration 动画的持续时间

animation-time-function: 动画的变化曲线

animation-delay: 延迟执行的时间

animation-iteration-count：指定动画执行的次数，执行infinite表示无限次执行动画

animation-direction:指定方向，normal/reverse

animation-fill-node: none(回到开始的位置)/forwards（动画最后一帧的位置）/backwards(动画第一帧的位置)

## 五. 3D动画

css实现3D动画(很少用，有兼容性问题)：



JS实现3D的库（很适合做3D动画）：three.js