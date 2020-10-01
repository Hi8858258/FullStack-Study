# prototype属性

1. 每个函数都有一个prototype属性，它默认指向一个object空对象（即：原型对象）

2. 原型对象中有一个属性constructor，它指向函数对象。实例对象中也有一个constructor，它指向对应的构造函数

3. 给原型对象添加属性（一般添加方法）

   作用：函数所有的实例对象自动拥有原型中的属性（方法）

```javascript
console.log(Date.prototype)
>>>会显示一堆的方法，这是因为Date是内置函数，本身有很多方法，包括constructor。其实这些方法都是通过prototype赋予的

function fun(){}

console.log(fun.prototype)
>>>只会显示constructor对象和__proto__属性

console.log(Date.prototype.constructor === Date)
>>>True

//prototype
function Fun(){}
Fun.prototype.test = function(){
	console.log('haha')
}

var fun = new Fun()
fun.test()
```

# 显示原型与隐式原型

```js
function Fn(){
}

var fn = new Fn()
//每个函数对象都有一个prototype，即显式原型
console.log(Fn.prototype)
//每个实例对象也有一个隐式原型
console.log(fn.__proto__)

Fn.prototype === fn.__proto__ >>true
```

可以把原型对象理解成一个基类，函数对象（继承基类的类）和实例对象可以理解成这个基类的两个实例，所以通过Fn.prototype给原型对象添加方法的时候，实例对象也能获得这个方法

# 原型链

1. 访问一个对象的属性时，会现在自身中找，如果自己没有会沿着隐式proto向上，直到找到object的原型对象，也就是原型链的尽头

   ![image-20201001060459444](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201001060459444.png)

2. 所有函数都是Function实例，包括它自身。因为本质上所有函数都是Function函数对象new出来的

   ```js
   function Foo(){} 等于 var foo = new Function(){}
   ```

   所有函数都有隐式原型和显示原型，而且隐式原型proto 都是一样的，都是new function产生的  。可以由instanceof 来判断

3. Object的原型对象式原型链的终点，Object.prototype.__proto__ ===null

# 属性

通过原型对象增加的属性或者方法，对于实例对象来说其实都是在实例对象的内存中生成了一个属性，所以不会去原型链中找

```js
function Fun(){

}
Fun.prototype.a = 1
var fn1 = new Fun()
console.log(fn1.a)
var fn2 = new Fun()
fn2.a  = 2
console.log(fn2.a,fn1.a)  >>>2,1
//这里fn2的a属性是通过设置的，所以在fn2对象中会直接生成一个a属性，不会去到原型链中找
//但是fn1的a属性是通过原型链添加的，而fn1对象本身没有这个属性，要到原型链中去找
```

注意：一般我们不会在原型链中添加属性，都是在对象本身上添加，而方法会通过原型链去添加，这样就可以让方法给所有实例对象通用

```js
function Person(name,age){
    //每次生成的实例，都会在对象中生成name和age属性
    this.name = name 
    this.age = age
}

Person.prototype.setName = function(name){
    this.name = name
}
```

# instanceof

1. 判断左边的对象是不是右边的实例

   表达式：A instanceof B

   如果B函数的显示原型对象在A对象的原型链上，返回true，否则返回false

   ```js
   console.log(Object instanceof Function) >>>true
   console.log(Object instanceof Object) >>>true
   console.log(Object.prototype instanceof Object) >>>False,object的原型对象是原型链尽头
   console.log(Function instanceof Function) >>>true
   console.log(Function instanceof object) >>>true
   ```

   

2. Funtion是通过new自己产生的实例，所以

```js

function foo(){}
var f1 = new Foo()
```

