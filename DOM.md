# DOM

dom: 文档对象模型，一个页面就相当于是一个对象，里面的标签都可以看成是可操作的元素。

获取页面中元素的方法：

- 根据ID获取                            getElementById()

  ```javascript
  var element = document.getElementById(‘标签id’)  返回的是一个元素对象
  console.dir(element)    通过这个可以看到js对象的属性和方法
  ```

- 根据标签名

  ```javascript                    
  var elements = document.getElementsByTagName('标签tag（如div/li）')    //如果有多个相同的标签，就会返回标签对象的集合，以伪数组的形式存储
  //使用elements[0]可以获取想要的
  ```

  还可以获取到某个标签里的标签

  ```javascript
  var element = document.getElementById('nav');   //先通过id获取nav 的标签，
  var ss = element.getElementsByTagName('li')     //然后通过这个来获取具体的标签
  ```

- 通过HTML5新增的方法获取（有的浏览器不适配）

  ```javascript
  var elements = document.getElementsByClassName('类名')   //通过类名获取
  ```

  ```javascript
  document.querySelector('选择器')    //根据指定选择器返回第一个元素对象
  var firstBox = document.querySelector('.box') //只能选择第一个
  ```

  ```javascript
  document.querySelectorAll('选择器')   //返回指定选择器的所有标签对象集合
  ```

- 特殊元素获取

  - 获取body元素

    ```javascript
    document.body;
    ```

  - 获取html元素

    ```javascript
    document.documentElement; 
    ```

## 一.事件

事件有3部分组成：事件源，事件类型，事件处理程序

事件源：事件被触发的对象， 就是标签。比如说按钮

```javascript
<button id="btn">唐伯虎</button>
var btn = document.getElementById('btn');
```

事件类型：如何触发，比如鼠标点击（onclick），鼠标hover，键盘敲击

事件处理程序：通过函数赋值的方式完成

```javascript
btn.onclick = function(){
    alert('点秋香')
}
```

## 二. 操作元素

js的dom操作可以改变网页内容，结构，样式

### 2.1 改变元素的内容

```javascript
element.innerText    //从起始位置到终止位置的内容，但它不识别html的标签，同时空格和换行也会去掉
div.innerText('<strong>今天</strong>')   
>>><strong>今天</strong>
```

```javascript
element.innerHTML   //起始位置到终止位置的全部内容，包括html标签，同时保留空格和换行
div.innerHTML('<strong>今天</strong>')
>>>>今天   （加粗的）
```

还可以这两个属性去获取标签里面的内容

```javascript
var p = document.querySelector('p');
console.log(p.innerText)
```

### 2.2 常用元素的属性修改

比如修改input里面的value(还有disabled)

```html
<button>修改</button>
<input type="text" value="输入内容">
<script>
    var btn = document.querySelector('button')
    var inp = document.querySelector('input')
    btn.onclick = function(){
        inp.value = "被修改的内容"
    }
</script>
```

