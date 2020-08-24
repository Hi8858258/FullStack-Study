# Python 高级编程

## 一. Python 一切皆是对象

动态语言（python）和静态语言（java）的一个区别在于python面向对象更彻底

动态语言的缺陷：无法在编译时发现错误，只能在运行时才能看出

### 1.1 type、 object 、class 之间的关系

```python
>>> a = 1
>>> type(a)      
<class 'int'>    #a 是 int类的实例对象
>>> type(int)
<class 'type'>   #int 是type类的实例对象
```

他们之间的关系是type—>类—> obj

可以通过       类.\_\_bases\_\_    来看类是从哪里继承来的，所有类的基类都是object

type本身是一个类，但它同时也是一个对象。

```python
>>> type.__bases__
(<class 'object'>,)
#但object也是属于type类
>>> type(object)
<class 'type'>
>>> object.__bases__
()
```

![image-20200613100507770](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200613100507770.png)

 虚线代表实例，实线代表继承。

以list为例，list本身是一个类，所以它能够创建列表实例对象，但list同时也是由type类创建的一个type类实例。所以我们说类其实也是一个对象。

type和object呢就有复杂，从图中可以看出：

- 所有类（包括object，和type自身）都是type的对象（这是python一切皆对象的来源，而对象的属性可以修改，所以这也是python动态语言灵活性的具体体现）
- 所有的类都继承自object

### 1.2 对象的三个特征

- 身份

  通过id（对象）来查看地址—>身份

- 类型

- 值

### 1.3 python内置类型

- None(全局只有一个)，当python解释器启动时，就会直接在内存中生成一个唯一的None类型
- 数值
- 迭代类型
- 序列类型
  - list
  - bytes,bytearray,memoryview
  - range
  - tuple
  - str
  - array

- 映射（dict）
- 集合
  - set
  - frozenst
- 上下文管理类型(with 语句)
- 其他
  - 模块类型
  - class和实例
  - 函数类型
  - 方法类型
  - 代码类型
  - object类型
  - type类型
  - ellipsis类型
  - notimplemented类型

## 二. python 魔法函数

### 2.1什么是魔法函数

以双下划线开头和结尾的东西：

例子1:

```python
class Company:

	def __init__(self,employ_list):
        return self.employee = emloy_list
company = Company(['alibaba','huawei','tencent'])
for i in company.employee:
    print(i)
```

当没有\_\_getitem\_\_魔法函数的时候，我们想要获取company的实例属性，就要具体in 到实例当中的属性

例子2：

```python
class Company:

	def __init__(self,employ_list):
        return self.employee = emloy_list
    def __getitem__(self,position):
        return self.employee[item]
    
company = Company(['alibaba','huawei','tencent'])
for i in company:
    print(i)
```

当有了魔法函数，我们可以直接对company实例进行遍历，但实际上for是首先到类型里面去找迭代器，找不到迭代器后，python才会去找getitem方法

### 2.2 Python的数据模型以及数据模型对python的影响

​	魔法函数会影响python数据类型的使用以及语法的使用

### 2.3 魔法函数

1. 非数学运算相关

   - 字符串表示
     - \_\_repr\_\_
     - \_\_repr\_\_
   - 集合、序列相关
     - \_\_len\_\_
     - \_\_getitem\_\_
     - \_\_setitem\_\_
     - \_\_delitem\_\_
     - \_\_contains\_\_
   - 迭代相关
     - \_\_iter\_\_
     - \_\_next\_\_
   - 可调用
     - \_\_call\_\_
   - with上下文管理器
     - \_\_enter\_\_
     - \_\_exit\_\_
   - 数值转换
     - \_\_abs\_\_
     - \_\_bool\_\_
     - \_\_int\_\_
     - \_\_float\_\_
     - \_\_hash\_\_
     - \_\_index\_\_
   - 元类相关
     - \_\_new_\_
     - \_\_init\_\_
   - 属性相关
     - \_\_getattr\_\_，\_\_setattr\_\_
     - \_\_getattribute\_\_，\_\_setattribute\_\_
     - \_\_dir\_\_
   - 属性描述符
     - \_\_get\_\_，\_\_set\_\_，\_\_delete\_\_
   - 协程
     - \_\_await\_\_，\_\_aiter\_\_，\_\_anext\_\_，\_\_aenter\_\_，\_\_aexit\_\_

2. 数学运算相关

   - 一元运算符

     - \_\_neg_\_(-)
     - \_\_pos_\_(+)
     - \_\_abs_\_

   - 二元运算符

     - \_\_lt_\_(<)
     - \_\_le_\_(<=)
     - \_\_eq_\_(==)
     - \_\_ne_\_(!=)
     - \_\_gt_\_(>)
     - \_\_ge_\_(>=)

   - 算数运算符

     - \_\_add_\_ +
     - \_\_sub_\_ -
     - \_\_mul_\_ *
     - \_\_truediv_\_ /
     - \_\_floordiv_\_ //
     - \_\_mod_\_ %

     ......

   - 反向算数运算

     - \_\_radd_\_ 

     ......

   - 增量赋值运算

     - \_\_iadd_\_  +=
     - \_\_isub_\_  -=

     ......

   - 位运算符

     - \_\_invert_\_  ~
     - \_\_lshift_\_  <<
     - \_\_rshift_\_ >>
     - \_\_and_\_  &.
     - \_\_or_\_     |
     - \_\_xor_\_  ^

   - 反向位运算符

     ......

   - 增量赋值位运算符

     - \_\_ilshift_\_  

     ......

#### 2.3.1 \_\_repr\_\_，\_\_str\_\_

```python
class Company:

	def __init__(self,employ_list):
        return self.employee = emloy_list
    def __str__(self):
        return ','.join(self.employee)
    def __repr__(self):
        return ','.join(self.employee)
    
company = Company(['ss','yy'])
#print(实际上是调用str函数)
print(company)
>>>ss,yy
#str和repr的区别在于，str必须使用print函数调用才能打印出想要的东西
#repr可以是让我们直接使用company就可以看到，下面的代码如果没有repr魔法函数实现，那么就会显示__main__.Company 
company
>>>ss,yy
```

这两个魔法函数对应的所调用的内置函数有不一样，一个是str，另一个是repr。

len()方法对内置的类型如list，dict使用的使用，它的性能会非常好。因为这些类型是c语言直接写的额，在类型内部有一个长度属性。len可以直接去取它

## 三.深入理解类和对象

### 3.1 鸭子类型和多态

​	动态语言是实现鸭子类型的典型。

​	鸭子类型配合魔法函数就构成了python中的协议

```python
class Cat:
    def say(self):
        print('im a cat')
        
class Dog:
    def say(self):
        print('im a dog')
        
class Duck:
    def say(self):
        print('im a duck')
        
animal_list = [Cat,Dog,Duck]
for animal in animal_list:
    animal().say()
```

在java中，如过想要实现多态，那么多有的类必须要继承同一个父类。但是Python却不用，只要所有类都实现同一个方法，那么我们可以实现多态

### 3.2 抽象基类（abc模块）

- ​	抽象基类是什么：可以理解成接口，不能实例化。

- ​	具体的实现是，在抽象基类里面设定一些方法，所有继承这个基类的类都需要把这些方法覆盖到，抽象基类不能实例化。

- ​	为什么有了协议后还需要有抽象基类？

  1.  我们去检查某个类是否有某种方法

  ```python
  class Company:
      def __init__(self, employee_list)
      	self.employee = employee_list
      def __len__(self)
      	return len(self.employee)
  com = Company(['bobby','booy'])
  ```

  第一种方法： 

  print(hasattr(com, "\_\_len\_\_"))

​		第二种方法：在某些情况下希望判定某个对象的类型

```from collections.abc import Sized```

```isinstance(com, Sized)```

​	   当我们需要强制某个子类必须实现某些方法，比如django框架，集成cache（redis, cache,memorychache）,需要设计一个抽象基类

- 如何去模拟一个抽象基类

```python
class CacheBase:
    def get(self):
        raise NotImplementedError
    def set(self, key, value):
        raise NotImplementedError
         
class RedisCache(CacheBase):
    pass

redis_cache = RedisCache()
redis_cache.set('ley','values')
>>>会报错 NotImplementedError
如果在子类中实现了set方法，就不会抛异常，实际这里是使用子类重写父类方法的方式，不算真的抽象基类，真正的抽象基类在子类实例化的时候就会抛出异常。
```

- 实现真正的抽象基类

```python
import abc
class CacheBase(metaclass = abc.ABCMeta):
    @abc.abcstractmethod
    def get(self, key):
    	pass
    @abc.abcstractmethod
    def set(self,key,value):
        pass

class Redis(CacheBase):
    #下面必须实现get和set方法，不然实例化的时候会报错
```

### 3.3 isinstance和type的区别

​	isinstance会去检查类的继承链，而type只能找到父类，不能找到更上层的继承，所以使用isinstance去判断类

```python
class A:
    pass
class B(A):
    pass
b = B()
print(isinstance(b,B))    >>>True
print(isinstance(b,A))    >>>True
print(type(b) is B)       >>>True
print(type(b) is A)       >>>False
```

### 3.4 类属性和实例属性以及查找顺序

类属性：定义在类内部的变量及方法

实例顺序：定义在实例内部的变量及方法

查找顺序（MRO算法）：由下而上从实例对象出发

多继承查找顺序

![image-20200613144523271](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200613144523271.png)

DFS：深度优先算法在下面这张图里就不合适，如果C中有一个方法是用来重写D中的方法，如果使用深度优先我们就会找不到C中的那个方法

![image-20200613144807216](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200613144807216.png)

BFS：广度优先算法，但是BFS对于第一张图又不适用了，原因同样

![image-20200613145033593](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200613145033593.png)

python2.3之后，就改成C3算法。

可以通过   类.\_\_mro\_\_来查看类的属性继承顺序

### 3.5 静态方法，类方法，对象方法及采数

```python
class Data:
    #构造函数
    def __init__(self, year, month ,day):
        self.year = year
        self.month = month
        self.day = day
    
    def tomorrow(self):
        self.day += 1
        
    @staticmethod
    def parse_from_string(data_str):
        year,month,day = tuple(data_str.split("-"))
        return Data(int(year),int(month),int(day))
    
    @staticmethod
    def valid_str(data_str):
        year,month,day = tuple(data_str.split("-"))
        if int(year)>0 and (int(month)>0 and int(month)<12) and (int(day)>0 and int(day) <= 31):
            return True
        else:
            return False
        
    @classmethod
    def from_string(cls, date):
        year,month,day = tuple(data_str.split("-"))
        return cls(int(year),int(month),int(day))
    
    def __str__(self):
        return "{year}/{month}/{day}".format(year = self.year, month = self.month, day = self.day)
```

静态方法和类方法的区别在于，静态方法不需要传递类或者实例参数，但是它只能通过硬编码的方法来放回一个值如上面的 Data(....) ， Data就是类名而类方法，最后返回值的时候可以直接用cls来避免硬编码。那为什么还要有staticmethod呢，因为当方法中不需要返回值的时候，我们就可以用它了，如上面的 valid_str方法。

### 3.6 数据封装和私有属性

```python
import Data
class User:
    def __init__(self,birthday):
        self.__birthday = birthday
    
    def get_age(self):
        #返回年龄
        return 2018 - self.birthday.year
if __name__=='__main__':
    user = User(Data(1990,2,1))
    print(User.get_age())
```

通过双下滑线完成属性的私有化，封装。用户就取不到这个属性了，但它并不是真正的私有化，可以通过user._User__birthday来获取。

### 3.7 Python对象的自省机制（dir，\_\_dict\_\_）

- 可以通过\_\_dict\_\_来查询对象的属性，但是它不会找到父类的类属性

- 可以通过给\_\_dict\_\_来给对象增加属性：

  - ```python
    user = Student('haa')   #Student类里只有一个属性
    user.__dict__['school_addr'] ='北京市'
    ```

dir可以列出对象的所有属性，比dict要强大很多

### 3.8 super函数

```python
class A:
    def __init__(self):
        print('A')
        
class B(A):
    def __init__(self):
        print('B')
        super().__init__()     #调用父类的构造方法
```

- 既然我们重写B的函数，为什么还要去调用super？

因为可以重用’父类‘中的代码：

```python
class B(A):
    def __init__(self,name,user):
        self.user = user
        super().__init__(name = name) #加入父类A中的构造函数有name这个参数，并且会对name进行处理，那么我们就可以直接使用super函数来宠用A中的代码
```

- super执行顺序是什么样的？多继承上

  其实并不是调用父类，而是按照MRO顺序

### 3.9 with语句（上下文管理器）

```python
def exe_try():
    try:
        print('code started')
        raise KeyError
        return 1
    except KeyError as e:
        print('key error')
        return 2
    else:
        print('other error')
        return 3
    finally:
        print('finally')
        return 4
    
result = ext_try()
print(result)
>>>code started
>>>KeyError
>>>finally
>>>4
```

理论上应该没有finally和4,而是直接返回2。在python语句中，return会被压入到栈当中，如果finally 中也有返回值，那么就会将finally中的出栈返回4。如果把return 4注释掉，就会返回2了。

with语法就是为了简化try，finally

#### 3.9.1 上下文管理器协议

实现了\_\_enter\_\_，和\_\_exit\_\_两个协议的类，可以用with语句来使用

```python
class Sample:
    def __enter__(self):
        print('enter')
    def __exit__(self):
        print('exit')
    def do_something(self):
		print('do something')
        
 with Sample() as sample:
    sample.do_something()
>>> enter 
>>> doing something
>>> exit
```

​    在enter里面获取资源，在exit里释放资源

- 如何通过contextlib来简化上下文管理器

```python
import contextlib

@contextlib.contextmanager   #装饰的生成器函数就可以当作上下文管理器来用
def file_open(file_name):
    print("file open")
    yield {}
    print('file end')

with file_open('body.txt') as f_open:
    print('processing')
    
>>> file open
>>> processing
>>> file end
```

yield之前就是enter，之后是exit。contextmanager利用了生成器的特点

## 四. 自定义序列类

### 4.1 序列类型的分类

- 容器序列
  - list、tuple、deque
- 扁平序列
  - str、bytes、bytearray、array.array
- 可变序列
  - list、deque、bytearray、array
- 不可变序列
  - str、tuple、bytes

### 4.2 序列的abc继承关系

```python
from collections import abc #和容器相关的数据结构抽象基类都是在里面
```

序列类型的基类是Sequence，Sequence从Sized等基类继承而来，而MutableSequence是从Sequence继承而来。

### 4.3 序列的+，+= 和extend的区别

- +，+= 第一个区别是+= 是就地加
- 第二个区别

```python
a = [1,2]
a = a + (3,4)   #报错
a += (3,4) >>> [1,2,3,4] #在源码选中__iadd__方法条用extend方法，extend方法的参数是一个可迭代对象
a.append((3,4)) >>> [1,2,(3,4)]
```

### 4.4 实现可切片的对象

```python
import numbers
class Group:#不可修改序列
	#下面是所有不可变序列所要求的方法，如果只是想要类型支持切片，只需要完成是实现getitem就行
    def __init__(self, group_name, company_name, staffs):
        self.group_name = group_name
        self.company_name = company_name
        self.staffs = staffs
        
   	def __reversed__(self):
        self.staffs.reverse()
    
    def __getitem__(self,item):
       # return self.staffs[item] 
       #如果只是实现这句话，那么切片出来的东西就不是Group,而是列表。如果想要切片出来的还是group类，那么就需要弄明白item是什么。在使用group[:2]是，[:2]会被当成是slice(none,2,none)传给item。当group[2]是，item得到的值就是整形2
       #--------------下面是真正的切片-----
    	cls = type(self)
        if isinstance(item,slice):
            return cls(group_name = slef.group_name, company_name = self.company_name,staffs = self.staffs[item])
        elif isinstance(item, numbers.Intergral):
            return cls(group_name = slef.group_name, company_name = self.company_name,staffs = [self.staffs[item]])
    
    def __len__(self):
        return len(self.staffs)
    
    def __iter__(self):
        return iter(self.staffs)
    
    def __contains__(self,item):
        if item in self.staffs:
            return True
        else:
            return False

staffs = ['bob1','bob2','bob3']
group = Group(company_name = 'immo',group_name ='user',staffs = staffs)
group[:2]
```

### 4.5 bisect 序列

当项目中需要维护好一个排序的序列，用这个包会很方便

bisect是用来处理已排序的序列，用来维持已排序的序列，升序

二分查找

```python
import bisect
inter_list = []
bisect.insort(inter_list,3)
bisect.insort(inter_list,2)
bisect.insort(inter_list,5)
bisect.insort(inter_list,1)
bisect.insort(inter_list,6)
bisect.insort(inter_list,7)
print(inter_list)
>>>[1,2,3,5,6,7]
print(bisect.bisect(inter_list,3))  #插找3这个元素的右边是哪个位置,默认bisect是用bisect_right
>>> 3
print(bisect.bisect(inter_right,3))
>>> 2
```

### 4.6 什么时候不该用列表

array，deque

array就是数组，只能存放指定的数据类型，因为它内部是连续存放

### 4.7 列表推导式，生成器表达式，字典推导式

## 五. 深入理解set和dict

### 5.1 dict常用方法

dict在builtins里可以看到源码

两个比较中要的方法：

- dict.setdefault() 如果字典里没有指定的键，就生成这个键
- update():增加字典中的键值对
  - old_dict.update({'home':'lie'})等效于下面
  - old_dict.update(home = 'lie')
  - old_dict.update([('home','lie')])

### 5.2 dict子类

不建议自己去继承dict，非要继承可以继承collections 模块中的UserDict

### 5.3 set集合 fronzenset（不可变集合)

特点：无序，不重复

fronzentset不能给它添加值，不可变类型。无add方法，可以作为dict的key

#### 5.3.1 向set添加数据

- set.add()
- set.update()        another_set = set('def')   s = {'b','c'}    s.update(another_set) = {'b','c','d','e','f'}

### 5.4 dict和set实现原理

哈希

1. dict的key或者set的值，都必须是可hash的
2. 不可变对象才可以hash，如str，frozentset，tuple，自己实现的类
3. dict的内存花销比较大， 但是查询很块
4. dict的存储顺序和元素添加顺序有关
5. 添加数据有可能改变已有数据的顺序（当散列表的空间只剩下1/3的时候，会重新申请空间并搬迁数据，这时候会造成数据顺序的改变）

## 六. 对象引用、可变性、垃圾回收

python变量是实际上一个指针，大小基本上是固定的

对于小整数：  a = 1, b = 1       a is  b， 对于大整数就不行

## 七. 元类编程

### 7.1 property 动态属性

![image-20200614070618500](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200614070618500.png)

可以把动态改变实例属性（详见第43课）



### 7.2 \_\_getattr\_\_和\_\_getattribute\_\_ 魔法函数

\_\_getattr\_\_：在查找不到属性的时候调用（如果类当中没有想要的属性，一般情况是报错no attr，当我们在类当中实现了\_\_getattr\_\_魔法函数的时候，它就不会报错，并且会执行该函数当中的代码）

\_\_getattribute\_\_ ：首先优先级比\_\_getattr\_\_高，尽量不要去动它



### 7.3 属性描述符和属性查找过程 

需要回顾视频！！！



### 7.4 \_\_new\_\_和\_\_init\_\_的区别

```python
class User:
    def __new__(cls,*args,**kwargs):#new第一参数是class
        pass
    def __init__(self):
        pass
```

new函数只有在新式类中才有，第一个参数是class，允许我们在生成对象之前加逻辑。new是类的生成过程，也用来控制对象的生成过程，init是用来完善对象。如果new不返回对象，则不会调用init函数



## 八. 迭代器和生成器

迭代器是什么？

迭代器是访问集合内元素的一种方式一般用来遍历数据

迭代器和以下标的访问方式不一样，迭代器不能返回，迭代器提供一种惰性访问数据的方式（访问数据的时候才会生成数据）。



下标的方式背后原理是\_\_getitem\_\_

迭代协议：可迭代对象是实现了\_\_iter_\_，而迭代器是实现了\_\_iter_\_，和\_\_next\_\_方法。list等只是可迭代对象，但是实现了iter方法，可以返回一个迭代器

### 8.1 迭代协议

## 九. Python socket编程

### 9.1 弄懂HTTP、SOCKET、TCP概念

socket是处在应用层和传输层之间的一层，socket可以使得应用和TCP直接打交道

9.2 client 和server实现通信

![image-20200614140546926](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200614140546926.png)

##  十. 多线程，多进程

### 10.1 GIL

GIL：global interpreter lock全局解释器锁

python中一个线程对应于c语言中的一个线程，GIL使得同一时刻只有一个线程运行在一个cpu上执行字节码，无法将多个线程映射到多个cpu上。



GIL 在一个线程中运行到一定阶段会释放给另一个线程，但是这样就导致了有时候它是不安全的如下实例，每次运行下面的代码都会得到不同的结果。

GIL释放的情况：

1. ​	根据执行的字节码行数，以及时间片释放
2. ​    遇到IO操作的时候释放

```python
import threading

total = 0
def add():
    global total
    for i in range(1000000):
        total += 1

def desc():
    global total
    for i in range(1000000):
        total -= 1

thread1 = threading.Thread(target=add)
thread2 = threading.Thread(target=desc)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(total)
```

### 10.2 Threading

对于IO操作来说，多线程和多进程的性能差别不大。

### 10.2.1 针对简单的多线程编程写法

```python
import threading
import time
def get_detail_html(url):
    print("get_detail_html started")
    time.sleep(2)
    print("get_detail_html end")

def get_detail_url(url):
    print("get url sttarted")
    time.sleep(2)
    print("get url end")

if __name__ == "__main__":
    thread1 = threading.Thread(target=get_detail_html,args=('',))
    thread2 = threading.Thread(target=get_detail_url,args=('',))
    #thread1.setDaemon(True)  #守护线程，当主线程退出时，子线程也会退出
    #thread2.setDaemon(True)
    start_time = time.time()
    thread1.start()
    thread2.start()
	#thread1.join()    线程阻塞，只有等到线程结束，主线程才会退出 
    #thread2.join()
    print("last time {}".format(time.time()-start_time))
    
>>>get_detail_html started
>>>get url sttarted
>>>last time 0.000997304916381836
>>>get url end
>>>get_detail_html end
```

以上其实有3个线程，有一个是主线程，如果主线程想要最后结束，可以用thread.

### 10.2.3 通过继承threading来多线程编程

大部分情况使用继承类的方式比较好，可以处理更多的逻辑

```python
import threading
import time
class GetDetailHtml(threading.Thread):
    def __init__(self,name):
        super().__init__(name = name)

    def run(self): #重载run方法
        print("get_detail_html started")
        time.sleep(2)
        print("get_detail_html end")

class GetDetailUrl(threading.Thread):
    def __init__(self,name):
        super().__init__(name = name)

    def run(self):
        print("get url sttarted")
        time.sleep(2)
        print("get url end")


if __name__ == "__main__":
    thread1 = GetDetailHtml("get_detal_html")
    thread2 = GetDetailUrl("get_detal_url")
    # thread1.setDaemon(True)
    # thread2.setDaemon(True)
    start_time = time.time()
    thread1.start()
    thread2.start()
    #thread1.join()
   # thread2.join()
    print("lasttime{}".format(time.time()-start_time))
```

### 10.2.4 线程间的通信

通信方式：

1. 共享变量（全局变量，并不推荐，需要配合锁才能将共享变量用好，详见上面计算total值每次不一样的例子）

```python
import threading
import time

detail_url_list = [] #全局变量
def get_detail_html(detail_url_list):
    #global detail_url_list    如果函数的参数时这个值就不需要全局变量
    url = detail_url_list.pop()
    #获取文章详情页
    print("get_detail_html started")
    time.sleep(2)
    print("get_detail_html end")

def get_detail_url(detail_url_list):
    #爬取文章列表页
    #global detail_url_list
    print("get url sttarted")
    time.sleep(2)
    for i in range(20)：
  		get_detail_list.append("http：//p.com/{id}".format(id = i))
    print("get url end")
    
if __name__ == '__main__':
    thread_detail_url = threading.Thread(target = get_detail_url)
    for i in range(10):
    	html_thread= threading.Thread(target = get_detail_html)
        html_thread.start()
	start_time = time.time()
```

上面时伪代码，不能真正实现，只作为逻辑参考



2. 通过queue的方式进行线程间同步

```python
from queue import Queue

import threading
import time

def get_detail_html(queue):
    while True:
        url = queue.get()    #queue 是线程安全的，多个线程
        #获取文章详情页
        print("get_detail_html started")
        time.sleep(2)
        print("get_detail_html end")

def get_detail_url(queue):
	while True:
        print("get url sttarted")
        time.sleep(2)
        for i in range(20)：
            queue.put("http：//p.com/{id}".format(id = i))
        print("get url end")
    
if __name__ == '__main__':
    detail_url_queue = Queue(maxize = 1000)
    thread_detail_url = threading.Thread(target = get_detail_url)
    for i in range(10):
    	Queue.
	start_time = time.time()
```

### 10.2.5 线程同步（Lock）

用lock.aquire一定要lock.release

1. Lock会影响性能（必然）
2. Lock会产生死锁
   1. 连续上了两把锁， 之间没有释放

### 10.2.6 条件变量（condition）

条件变量是用于复杂线程间同步

