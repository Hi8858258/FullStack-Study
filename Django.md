#  Django

## 一. 常用函数

### 1.1 reverse

reverse只能用来匹配关键字参数，查询字符串（url？后面）不能使用。

```python
#在url中有命名的url
path('login/',views.login,name = "login")
from django.shortcuts import reverse
login_url = reverse('login')
#login_url = reverse('login')+"?next=/" 只能使用这样拼接查询字符串
#url里面如果有参数要求，则后面需要跟参数
path('detail/<article_id>/',views.login,name = "detail")
login_url = reverse('detail',kwargs={'article_id':1})
>>>detail/1/
```

## 二. 模板 DTL（django template language）

### 2.1 配置模板文件搜索路径

在settings文件里面的templates下。

```python
'DIRS':[os.path.join(BASE_DIR,'templates']
'APP_DIRS'：True    #当这个为True的时候，django才会到APP的目录下去找模板
```

先到DIRS里面去找模板，找不到才到APP_DIRS里面去找

### 2.2 模板变量

在html模板里面，用{{变量}}，{{变量.属性}}，如果变量是列表/元组，要通过列表的索引取值，就是{{变量.0}}。如果变量是字典{{变量.key}}

### 2.3 模板标签

{% if  %}

#### 2.3.2 for

{% for item in list %}    {{item}}

在for循环中，可以使用以下变量：

- {{forloop.counter}} 当前循环的下标，以1作为起始
- {{forloop.counter0}}当前循环的下标，以0作为起始
- {{forloop.revcounter}} 当前循环的反向下标，下边倒排，1是最后一个元素的下标
- {{forloop.revcounter0}} 
- forloop.first 判断是否是第一次循环   {% if forloop.first %}
- {{forloop.last}}  
- {{forloop.parentloop}} 如果有多个循环嵌套，那么这个属性代表的是上一级的for循环 

{% for .... in .... empty %} 如果for循环里没有值的话，就会到empty中去

#### 2.3.3 with标签

使用with标签可以定义一些变量，但是自定义变量名，只能在with块里面使用

```python

{% with 自定义变量名=老变量.属性 %}

{{自定义变量名}}

{% endwith %}
也可以使用{% with 自定义变量名 as 老变量.shuxing %}
```

#### 2.3.4 url标签

{% url 'appname:url的name' %}

#### 2.3.5 autoescape自动转义标签

这个标签默认是开启的，如果向在HTML里面关闭

```html
{% autoescape off %}
{% endautoescape %}
```

#### 2.3.6 verbatim 

```html
{% verbatim %}

这里面的代码块都不会被模板解析，比如{{}},和%

{% endverbatim %}
```

### 2.4 模板结构优化

可以使用{% include 'html文件' %}来一个html文件里引入html代码块

### 2.5 加载静态文件

1. 首先确保django.contrib.staticfiles已经在注册的app中

2. 设置STATIC_URL=“/static/”  

   127.0.0.1/static/xxx.jpg   在html里使用这个路径就可以直接加载图片

3. 在app下创建静态文件一定要使用app/static/app/xxx.jpg 的结构目录，不然多个app有相同的静态文件时候，会混淆

4. STATICFILES_DIR = [os.path.join(BASE_DIR，‘static’)] 这是放一些公用的静态文件的地方

5. 在模板中使用load加载static标签，我们才能在html中去使用static标签加载文件，比如要加载根目录下的static文件下的style.css

   ```html
   {% load static %}  #先load static标签
   <link rel="stylesheet" href="{% static 'style.css' %}">
   ```

   也可以直接在html文件中使用完整的静态文件路径来引用，不一定需要使用load

6. 如果不想每次都在模板中加载static标签(将它变成内置的标签)，可以在settings的options里添加 'builtins':['django.templatetags.static']，这样就不用每次都加载了。

7. 如果没有在installed_app中没有添加django.contrib.staticfiles，就需要手动配置url和静态文件的映射（这个其实没什么意义，只要在注册的app中开启django.contrib.staticfiles就可以了）

   ```python
   from django.conf import settings
   from django.conf.urls.static import static
   urlpatterns=[
       
   ]+static(settings.STATIC_URL,document_root=settings.STATICFILES_DIRS[0]) #这个只能映射在根目录下的static文件夹
   ```

   

## 三. 过滤器

可以在django.template中的defaultfilters看到过滤器的源码

django的模板系统可以在html里解析python的对象，甚至是函数如下

```python
#views.py
def greet():
    return "hello"
def index(request):
    context = {
        'greet':greet #这是一个函数对象
    }
    return render(request,'index.html',context)
```

```html
{{greet}}  //但是这个函数不能传参
```

所以可以使用过滤器来传参（但是最多可以传2个参数），比如常用的过滤器:

- add

```python
{{value|add:"2"}}   => add(value,'2')

#add源代码
def add(value,arg):
    try:
        return int(value) + int(arg)
    except (ValueError,TypeError):
        try:
            return value + arg
        except Exception:
            return ''
```

- cut

移除值中指定的字符串，类似replace(args," ") args代表要替换的字符串

```python
#cut 源代码
def cut(value,arg):
    safe = isinstance(value,SafeData)
    value = value.replace(arg,'')
    if safe and arg !=';':
        return mark_safe(value)
    return value
```

- date

将日期按照指定格式转换成字符串

```python
context = {
    'birthday':datetime.now()
}

{{birthday|date:"Y/m/d"}}
```

![image-20200721055944729](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200721055944729.png)

- default

如果变量为false，如空列表,""，None等，可以使用default提供默认值

```python
{{value|default:"nothing"}}
```

default_if_none 只有当value为none时，default才生效

- first

返回列表/元组/字符串中的第一个元素

- last

返回列表/元组/字符串中的最后一个元素

- floatformat:多少为

```python
{{value|floatformat:2}} 保留2位小数
```

用于保留多少位小数

- join

就是python中的join方法，将列表\元组\字符串用指定字符连接

```python
{{value|join:"/"}}
```

- length

获得列表\元组\字符串\字典的长度

- lower/upper

将所有字符转换为小/大写

- random

在给定的列表\元组\字符串中随机选择一个值

- safe

标记一个字符是安全的，就会关掉这个字符串的自动转义。即如果value中是html代码，就会把这个代码直接渲染到页面上（有注入风险）

- slice

类似与切片

```python
{{some_list|slice:"2:"}} #从2开始切片
```

- truncatechars

保留指定位字符，其余的用...来表示

```python
{{value|truncatechars:5}}
```

- truncatechars_html

```python
{{value|truncatechars_html:5}}#会保留html标签
```

### 3.2 自定义模板过滤器

1. 在app目录下创建templatetags文件夹

2. 创建过滤器文件,如my_filter.py

   ```python
   from django import template
   register = template.Library()
   def greet(value,word):    #我们要定义的过滤器，最多只能有两个参数
       return value+word
   
   register.filter("greet",greet)  #第一个参数是过滤的名字，第二个是函数名
   ```

3. 在html文件开头加载过滤器

   ```html
   {% load my_filter %}
   ```


## 四. 数据库操作

### 4.1 使用原生sql

配置好DATABASES后就可以直接在django程序中用原生sql，不需要再import pymysql等驱动引擎，可以查看python文档来了解更多的数据库接口

```python
from django.db import connection
def test(request):
    cursor = connection.cursor()
    cursor.execute("select * from permission.rbac_role")
    rows = cursor.fetchall()
    context = {'rows':rows}
    for row in rows:
        print(row)
    return render(request,'test.html',context)
```

### 4.2 ORM模型

可以在每次使用orm调用connection.queries来看一下执行的SQL语句

```python
from django.db import connection
def ...()
	result = Book.object....
    print(connecion.queries)
```



orm的优势：

1. 使用orm可以避免SQL注入攻击
2. 易用，减少重复SQL
3. 性能损耗减少，orm转换成底层数据库操作指令的时候确实会有一些开销，但实际损耗很少（不足5%），只要不是对性能严苛的要求。讲究开发效率的话，还是orm更好用
4. 设计灵活，可以写出轻松的写出复杂的查询
5. 可移植性，支持多个数据库引擎，包括mysql,postgresql和sqlite

### 4.3 ORM常用字段

- AutoField：自增长的整形类型
- BigAutoField：64位自增长整形
- BooleanField：接受True/False。数据库里存的是tinyint类型 1/0。默认是none
- CharField：varchar类型，必须定义最大长度
- DateField：数据库中是date类型，只记录年月日。可以使用auto_now=True/False（每次保存这个数据的时候，都使用当前时间），auto_now_add=True/False（第一创建的时候，使用当前时间啊）
- DateTimeField：数据库中是datetime类型，和上面的类似，区别在于多了时间
- TimeField：time类型

```python
#settings里时区的设置
TIME_ZONE = ‘Asia/shanghai’
USE_TZ = True#如果设置成false，就会获取当地时间，但是是一个navie类型的时间，不能够和其他时区互换
```

- EmailField：类似CharField，数据库中是varchar。默认最大长度是254，可以填入任意字符，不一定要求email格式，这个字段是为了再model.Forml表单验证email时候使用的
- UUIDField：只能存储uuid格式的字符串，一般用来作为主键
- TextField：就是longtext类型
- URLField：也可以存储任意字符串，用于表单

### 4.4 字段常用参数

- null = True/False：默认是False，官方建议字符串类型的field不要设为true，因为django会把空字段默认给与一个""空值，如果设置null=True的话，就会有null和空字符串两个空值。如果再表单验证的时候，想要允许这个字符串为空，就设置blank=True
- blank：表单验证的时候是否可以为空，默认是false
- db_column: 字段在数据库中的名字，默认就是字段的名字
- default：默认字段
- primary_key:主键
- unique：唯一键

### 4.5 Meta类中常见的配置

- db_table=‘book’：数据库中的表名
- ordering = ['-字段1'，‘字段2’]

还有很多配置可以官方文档

### 4.6 外键和表关系

Innodb支持外键约束

- ForeignKey(to,on_delete,**options)  一对多

以文章和作者为例，一个作者可以写多篇文章，那么文章中就要有一个作者的外键。

1. on_delete = casecade时候，就是级联操作。意思是被引用的作者被删除的时候，该文章也会被删除。文章删除时作者不受影响
2. on_delete = protect时候,作者不能被删除，因为被一个文章引用了
3. on_delete = set_null时候,作者被删除了，作者引用的文章中的作者字段就会为空，前提是，这个作者字段要设置可以为空
4. on_delete = set_default,类似set_null
5. on_delete = DO_NOTHING:不做任何行为，依赖数据库级的操作
6. on_delete = set（）详细看文档

#### 4.6.1 如果想要引用另一个app中的模型

author = models.ForeignKey(to ="app.模型名",on_delete)

#### 4.6.2 如果想要引用自己（实现多级评论）

comment = models.ForeignKey(to ="self",on_delete)

### 4.7 ForeignKey 一对多

作者要去反向查询文章的时候使用: author.article_set.all()，也可以在article的user字典里面定义一个related_name='articles'，来直接使用author.articles反向查询

在创建某个文章数据的时候

```python
article = Article(title = '111',content= 'sdf')
author = User(user="adsf",pass="asdf")
author.save() #必须要保存author,不然不能给artile赋予author属性
article.author = author
article.save()
```

### 4.8 OneToOneField 一对一

应用场景：用户不常用的信息放到用户扩展表中

```python
class User(models.Model):
    username = models.CharField(max_length=20)

class UserExtension(models.Model):
    birthday = models.DateField(null = True)
    user = models.OneToOneField(to="User",on_delete,related_name="extension") #这个user字段是unique的，如果出现多个userextension指向同一个user就会报错 
```

一对一的反向引用很容易，直接使用user.extension就行了。因为定义了related_name，所以不能使用user.userextension

### 4.9 ManyToManyField 多对多

应用场景：一个文章有多个标签，一个标签可以被多个文章使用

```python
class Article(models.Model):
    title = models.CharField(max_length=20)
    tags = models.ManyToManyField(to = "Tag",related_name = "artile")
class Tag(models.Model):
    name = models.CharField(max_length=20)
```

实际上，数据库会自动给这种多对多的关系额外建立一张中间表，这个中间表分别定义两个外键，引用到article和tags两张表的主键

![image-20200721203705810](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200721203705810.png)

###   4.10 查询操作

如果使用get，就会返回模型中的满足条件的对象。filter返回的是queryset

- exact精确查找

```python
article = Article.objects.get(id__exact = 1)
=>
select ... from article where id =1
```

- lexact:忽略大小的查找

```python
article = Article.objects.get(title__lexact = "hello world")
=>
select ... from article where title like 'hello world'
```

- contains：大小写敏感 类似 like %hello%

- icontains：大小写不敏感

- in: 判断给定的字段值，是否在给定的容器中（list,tuple,或者任何可迭代对象包括queryset）

  ```python
  articles = Article.objects.filter(id__in =[1,2,3])
  =>
  select ... from article where id in (1,2,3)
  #把id为123的文章都找出来
  ```

  如果涉及到一堆多的查询，比如

  ```python
  author = Author.objects.filter(article__id__in = [1,2,3])
  #这根反向引用有点区别，不需要写models_set
  #查找文章id为123的作者
  #author一对多article
  #也可以给foreignkey字段添加一个related_query_name =”articles“来指定查询的名字
  #如:
      author = Author.objects.filter(articles__id__in = [1,2,3])
  ```

  related_name用于反向引用，related_query_name用于反向查询

- gt/gte/lt/lte

  ```python
  articles = Article.objects.filter(id__gt=4)
  =>
  select ... where id > 4
  ```

- startswith

- range 用于判断某个field是否在给定的区间

  ```python
  from django.utils.timezone import make_aware
  from datetime import datetime
  start_date = make_aware(datetime(year = 2008,month=1,day=1))
  end_date = make_aware(datetime(year = 2018,month=1,day=1))
  articles = Article.objects.filter(pub_date__range=(start_date,end_date))
  =>
  select ... from artile where pub_time between 2008-01-01 and 2018-01-01
  ```

- isnull 判断某个字段是否为空

  ```python
  artile = Artiles.objects.filter(pub_date__isnull=False)
  =>
  select .. from article where pub_date is not null
  ```

### 4.11 聚合函数

实例模型：

```python
class Book(models.Model):
    name = models.CharField
    pages = models.IntegerField
    price = models.FloatField
    rating = models.FloatField
    author = models.ForeignKey(to = Publisher)
    
class BookOrder(models.Model):
    price = models.FloatField
    book = models.ForeignKey("Book",on_delete)
    created_time = models.DateTimeField
```

聚合函数不能直接使用，要放在支持这些函数的方法中，比如aggregate/annotate

- Avg：求平均值

  ```python
  from django.db.models import Avg
  result = Book.objects.aggregate(Avg('price'))
  =>{"price_avg":23}#默认是用field_avg来输出结果的键
  #如果想自定义键就将avg函数赋值给一个键
  result = Book.objects.aggregate(may_avg=Avg('price'))
  =>{"may_avg":23}
  ```
  
- Count:计数

  比如可以获得author表中有多少个不同的邮箱，通过count作者的邮箱。可以增加distinct来删除同邮箱

  ```python
  result = Author.objects.aggregate(email_nums=Count("email",distinct=True))
  ```

  统计每本书的销量

  ```python
  result = Book.objects.annotate(book_nums=Count('bookorder__id'))#__id可以省略，因为是主键
  #book_id因为是用来groupby的，所以不能作为聚合函数的条件
  ```

- Max/Min

  求年龄最大和最小的作者

  ```python
  result = Author.objects.aggregate(max=Max('age'),min=Min('age'))
  ```

  获取每本书的最大/最小销售额

  ```python
  result = Book.objects.annotate(max=Max('bookorder__price'),min=Min('bookorder__price'))
  ```

- Sum

  求所有图书的销售总和

  ```python
  result = Bookorder.objects.aggregate(sum=Sum('price'))
  ```

  求每本图书的销售额

  ```python
  result = Book.objects.annotate(sale_total=Sum('bookorder__price'))
  ```

  求2018年度的销售额

  ```python
  result = Bookorder.objects.filter(bookorder__created_time__year=2018).annotate(total =Sum('bookorder__price'))
  #链式调用，先用filter将2018年销售的书查询出来，然后再通过annotate去聚合计算
  #链式调用的前提是Queryset，比如filter返回的结果是queryset，才能使用annotate这个函数
  ```

  求每一本书在2018年的销售额

  ```python
  result = Book.objects.annotate(book_sale_2018=Sum(bookorder.obejcts.filter))
  ```

### 4.12 aggregate和annotate的区别

- 相同：都可以使用聚合函数（avg,sum等）
- 不同：aggregate返回的是聚合函数结果的字典，不会进行分组。annotate返回的是queryset，会进行group by分组

比如要查询每本图书的平均销售价格

使用aggregate只会返回一个字段

```python
def index2(request):
    result = Book.objects.aggregate(avg=Avg('bookorder__price'))
>>> {'avg':91}
```

我们想要的是每本书的的名字，价格，销售数量，平均售价，所以使用annotate

annotate是返回一个在原模型的基础上添加聚合函数字段的结果，并且在使用聚合函数的时候，还会使用当前这个基础模型的主键进行分组（group by）。一（书为基础模型）对多（书的订单为增加的模型）

以sum函数为例，用aggregate返回的就是所有书本的销售总和。annotate就会在每本书后面显示自己的销售额

```python 
def index2(request):
    result = Book.objects.annotate(avg=Avg('bookorder__price'))
>>> queryset#queryset里面就是添加了每本书平均销售额的结果
```

### 4.13 F表达式

F表达式的作用是动态的获取该字段的数据

F和Q表达式可以给orm操作带来很大的遍历，如下

我们想要给每个员工的薪水增加1000元，一般的做法是先从数据库中把所有员工的薪水查询下来保存到内存中，然后遍历增加1000后，再save到数据库中，就是对salay字段中得每一行数据进行操作。如下 

实例1：

```python
employees = Employee.object.all()
for employee in employees:
    employee.salary += 1000
    employee.save()
```

而使用F表达式不需要对字段的每行数据进行+1000，而是可以在SQL层直接执行set语句，一下子更新整个字段

```python
from django.db.models import F
Employee.object.update(salary = F('salary')+1000)
#用F表达式就是标识salary字段
=>update employee set salary = (salary + 1000)
```

实例2：

想要获取在作者表中名字和邮箱相同的

```python
#一般做法
authors = Author.objects.all()
for author in authors:
    if author.name == author.email:
        print author
#F表达式
authors = Author.objects.filter(name = F('email'))#动态获取了email字段的数据
```

### 4.14 Q表达式

如果想要查找所有价格高于100，并且评分在9.0以上的。两个条件都要满足

```python
books = Book.objects.filter(price__gte=100,rating__gte=9)
```

但如果是查找所有价格高于100，或者评分在9以上的书。满足一个条件即可

```python 
books = Book.objects.filter(Q(price__gte=100)|Q(rating__gte=100))
```

Q表达式还能使用其他运算符：&（与），~（非），|（或）等

```python
from django.db.models import Q
#获取id等于3的图书
books = Book.objects.filter(Q(id=3))
#获取id等于3，或者名字中包含“记”的图书
books = Book.objects.filter(Q(id=3)|Q(name__contains="记"))
#获取价格大于100，并且名字包含“记”的图书
books = Book.objects.filter(Q(prince__gte=100)& Q(name__contains="记"))
#获取书名包含“记”,但是id不等3的图书
books = Book.object.filter(Q(name__contains="记")&~ Q(id=3))
```

## 五.QuerySet API

1. all：获取ORM模型的Queryset对象，这个对象没有经过任何修改

2. count：获取数据的个数，比python的len函数要高效，因为len函数会把整个Queryset对象放到内存里，然后一个个去计数。而count是直接使用select count( ) 在数据库层面操作

3. first/last：返回第一个/最后一个数据

4. aggregate：使用聚合函数

5. exists：判断数据是否存在

   ```python
   author = Author.object.filter(name='ll').exists()
   ```

6. bulk_create:可以一次性将数据插入数据库

   ```python
   publisher = Publisher.objects.bulk_create([
       Publisher(name = '123出版社'),
       Publisher(name = '1av出版社'),
       ]
   )
   ```

7. create:创建一条数据，并且保存到数据库当中。效果相当于先创建一个对象，然后对象.save()

8. get_or_create：根据某个条件进行查询，存在就返回，不存在就创建一个

   ```python
   objects,created = Category.object.get_or_created(title='默认分类')
   #object就是查询或者创建的对象，created代表是否创建为布尔值
   ```

   

9. defer('字段'):将字段过滤，不显示在查询结果里。但对id字段无效 

   ```python
   books = Book.objects.defer('name') #结果中没有name字段
   for book in books:
       pirnt(book.name)   #可以查询到，但是要重新去数据库查询
   ```

10. only('字段1','字段2')  只提取字段1和字段2的信息

    ```python
    books = Book.objects.only('name','price') #结果中只有name和price字段
    ```

11. distinct(),去重。使用MySQL不用传任何参数

    ```python
    #获取超过80元的图书并且去重
    books = Book.objects.filter(bookorder__price__gte=80).distinct() 
    ```

12. filter

13. exclude:排除满足条件的数据

    ```python
    Artilce.objects.exclude(title__contains='hello')#获得一个不含有hello标题的queryset
    ```

14. annotate:给queryset中的对象添加一个新的查询表达式（类似添加新字段）,可以使用聚合函数，F\Q表达式，func表达式等

    ```python
    articles = Article.objects.annotate(author_name=F('author__name'))
    ```

15. order_by（‘字段1’，‘字段2’） 先以字段1排序，再用字段2排序

16. get:返回一个模型的对象，不是queryset

17. prefetch_related:用于多对一，或者多对多的关系查询

    ```python
    #比如想要获取标题中带有hello字符的文章，并且它所有的标签
    articles = Article.object.prefetch_related('tag_set').filter(title__contains="hello")
    ```

18. update：可以批量的更新数据

    ```python
    #批量更新
    Book.objects.update(price=F('price')+1000)
    #效率很低的语句
    books = Book.objects.all()
    for book in books:
        book.price+=1000
        book.save
    ```

19. delete:删除满足条件的数据，但要注意on_delete的处理方式

    ```python
    Book.objects.filter(name__contain="书").delete()
    ```

20. values：用于提取指定的字段，而且返回的字典形式

    ```python
    books = book.objects.value('name','title','author__name')
    #values里面是可以用聚合函数以及F/Q表达式的
    #获取图书id,名字，销量
    books = Book.objects.values('id','name',order_count = Count('bookorder__id'))
    ```

21. values_list：和values类似，但返回的不是字典而是元组

## 六. 什么时候会执行SQL语句

1. 迭代Queryset对象的时候
2. 使用步长对queryset做切片操作
3. 调用len函数
4. 调用list函数
5. 判断

## 七. 迁移命令

makemigrations:

- makemigrations app:后面跟一个app或多个app,即指定app生成迁移文件
- --name:给迁移脚本命名
- --empty:生成空的迁移脚本

migrate：

- migrate app,将指定的app做ORM映射
- --fake
- --fake-initial

showmigrations 查看迁移文件

sqlmigrate：映射时候生成的SQL语句

## 八 django限制请求method

常规的请求方式是，get/post等，而一般来说url可以使用get，也可以使用post请求。

而限制请求方法就是限制一个视图函数，只能用一种请求方法访问。如下

```python
from django.views.decorators.http import require_http_methods
@require_http_methods(['GET'])
def my_view(request)
#my_view这个视图函数只能通过GET方法访问
```

```python
from django.views.decorators.http import require_GET
@require_GET
def my_view(request):
    pass
#@require_GET相当于是@require_http_methods(['GET'])的简写
#@require_POST相当于是@require_http_methods(['POST'])的简写
#@require_safe相当于是@require_http_methods(['GET','HEAD'])的简写,我们一般认为get请求是安全的，不会对服务器进行修改
```

## 九. 页面重定向

重定向分为永久重定向和暂时重定向

- 永久重定向：状态码301.用于旧网址废除了要转到一个新的网址，比如京东。输入www.jingdong.com的时候，会被重定向到www.jd.com
- 暂时性重定向：状态码是302，一个网站内页面的跳转，比如说需要权限的页面，如果用户没有登入九会跳转到登陆页面

django中使用rediret（to,*args,permanent = False,**kwargs）。to是一个url，permanent代表是否是永久重定向，默认为false

## 十. WSGI request 对象（HttpRequest）

在视图函数里的参数request其实就是WSGIRequest对象，WSGI request是继承自HttpRequest对象。

django在收到url后，就会创建一个wsgirequest对象，将浏览器发送给服务器的一些数据封装到这个对象里面，这些数据包括请求头的数据可以用request.META来获取，查询字符串的数据可以通过request.GET来获取，表单提交的数据可以通过request.POST来获取。

wsgirequest对象常用的只读属性：

- request.path ：不会显示查询字符串

- request.method:请求的方法

- request.GET:一个diango.HttpRequest.querydict对象，包含了通过查询字符串传递过来的数据

- requeest.POST:同样是一个diango.HttpRequest.querydict对象,包含了表单提交过来的一些数据

- request.FILES：一个diango.http.request.querydict对象，这个属性包含了所有上传的文件数据

- request.COOKIES:一个标准的python字典，包含所有的cookies

- request.session：类似于字典的对象，用来操作服务器的session

- request.META:存储浏览器发过来的请求头中的数据，以下是包含的数据

  ![image-20200723060702333](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200723060702333.png)

  ```python
  #比较靠谱的获取ip地址的方法，可以反向代理或者负载均衡
  if request.META.has_key('HTTP_X_FORWARDED_FOR')：
  	ip = request.META['HTTP_X_FORWARDED_FOR']
  else:
      ip = request.META['HTTP_ADDR']
  ```

![image-20200723061121551](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200723061121551.png)

wsgirequest对象常用方法：

- request.get_full_path():会显示包括查询字符串的路径 
- request.get_raw_uri():会显示包括域名的完整的url
- request.get_host():返回服务器的域名，如果域名商有端口号，还会返回端口号
- request.is_secure():判断是否采用https协议
- request.is_ajax()：是否采用ajax发送请i求，原理是判断请求头中是否存在X-Requested-With:XMLHttpRequest

### 10.1 QueryDict对象

我们使用request.GET和request.POST获得的都是QueryDict对象，这个对象有以下两个方法

- get():QueryDict对象.get('键名'，default = ‘没有找到键就返回的参数’)
- getlist(‘复选框name’):如果浏览器上传过来的key对应的值有多个，那么就需要通过这个方法获取。比如前端的checkbox复选框会通过post过来多个键值（一个name有多个value）信息，用这个就会把复选框的数据都显示出来，不然只会显示一个框的value

## 十一. HttpResponse

django接收到浏览器发过来的请求后，会将提交上来的数据封装成httprequest对象。那么视图函数在处理完相关的逻辑后，也需要返回一个响应给浏览器，这个响应对象就需要返回httpresponsebase或者他的子类对象。Httpresponse是httpresponsebase用的最多的子类

```python
def index(request):
    response = HttpResonse() #创建一个httpresponse对象
    response.content = '返回数据' #给对象属性赋值
    response.status_code=200 #返回的状态码
    return response
```

常用属性：

- content: 返回的内容

- status_code:返回的状态码

- content_type：返回的数据的META类型，默认是text/html。浏览器会根据这个属性，来显示数据。如果是text/html，那么就会解析content内容的字符串（比如content="</h1>哈哈<h1>"，那么就会在浏览器上直接显示一个h1标签的内容），如果是text/plain，就会显示纯文本（一般content="text/plain;charset=utf-8"），常用的content_type如下：

  ![image-20200723063417152](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200723063417152.png)

- 设置请求头中的内容：response['X-Access-Token'] = 'xxxx'，比如response['PASSWORD']='haha‘，那么就会在响应头中包含这个东西，常用于在设置token

  ![image-20200723064236915](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200723064236915.png)

常用的方法：

- set_cookie
- delete_cookie
- write:Httpresponse是一个类文件对象，可以用来写入数据到数据体中

## 十二. JsonResponse 对象

用来对象dump成json字符串，然后将json字符串封装成Response对象返回给浏览器。并且对象的Content-type是application/json。

```python
import json
#以下是通过httpresponse对象传输json数据
def jsonresponse_view(request):
    person = {
        'username':'zhili',
        'age':18
    }
    json_str = json.dump(person)
    response = Httpresponse(json_str,content_type='application/json')
    return response


#可以直接通过jsonresponse来传递数据
def jsonresponse_view(request):
    person = {
        'username':'zhili',
        'age':18
    }
    return jsonresponse(person)
#默认情况下jsonresponse只能对字典进行dump，如果要对非字典进行dump，需要给它额外传递一个参数safe = False
   return jsonresponse(person,safe = False)
```

## 十三. 生成CSV文件

 ```python
import csv
def index(request):
    response = Httpresponse(content_type = 'text/csv')
    response['Content-Disposition'] ="attachment;filename = 'abc.csv'" #不指定这条语句的话。浏览器下载下来的文件就没有格式
    writer = csv.write(response)
    writer.writerow(['username','age'])
    writer.writerow(['zhiliao',18])
    return response
 ```

还可以通过template来直接给模板渲染加载csv文件

```python
from django.template import loader
def template_csv_view(request):
    response = HttpResponse(content_type = 'text/csv')
    response['Content-Disposition'] ="attachment;filename = 'abc.csv'" #不指定这条语句的话。浏览器下载下来的文件就没有格式
    
    template = loader.get_template('abc.txt')#加载这个模板文件里面的内容如下
    '''
    #abc.txt文件里的代码
    
    {% for row in rows%}
    {{row.0}},{{row.1}}
    
    '''
    context = [
        'rows': [
            ['username','age']
            ['ziliao',18]
        ]
    ]
    csv_template = template.render(context)
    response.content = csv_template
    return response
```

上面只适用于小的CSV文件，如果要生成大的CSV文件，那么http连接可能就会超时。这个时候可以用数据流额方式从服务器返回给浏览器，这时候需要用到streamingHttpResponse:这个类是专门用来处理流数据的，它是继承自HttpResponseBase这个类

### 13.1 StreamingHttpResponse

它会启动一个进程来和客户端保持长连接，所以会很消耗资源，尽量少用

类属性：

1. 这个类没有content属性，只有streaming_content
2. 这个类的streaming_content必须是一个可迭代对象
3. 这个类没有write方法

## 十四. 类视图

```python
from django.views import View
class BookDetail(View):
    def get(self,request,*argw,**kwargs):
        return render(request,'detail.html')
    def post(self,request,*argw,**kwargs):
        return render()
    
#urls里面
path('detail/',views.Bookdetail.as_view(),name='detail')
```

在使用类视图的时候，其实会先到父类里面去执行dispatch函数做路由的分发，用来判断是get还是post方法.

如果想要禁止用户使用某个方法，可以在类里定义一个http_method_not_allowed方法，如下。如果用户使用了post，就会使用http_method_not_allowed

```python
class AddBookView(View):
    def get(self,request,*args,**kwargs):
        return render(request,'add_book.html')
    def http_method_not_allowed(self,request,*args,**kwargs):
        return HttpResponse('当前方法不支持%s' %request.method)
```



### 14.1 TemplateView

如果渲染的模板不需要传递任何参数（静态页面），可以直接在urls里面使用temlateview，不用再视图函数里写任何的视图函数

```python
from django.views.generic import TemplateView
path('about',TemplateView.as_view(template_name = 'about.html')
```

### 14.2 ListView

在网页开发的时候经常需要用到列出表中的数据，我们可以使用listview来快速实现需求

```python
class ArticleListView(ListView):
    model = Article #指定列表 
    template_name = 'article_list.html' #指定模板
    paginate_by = 10 #代表每页中显示多少条数据
    context_object_name = 'articles' #在前端取数据使用的名字
    ordering = 'created_time'
    page_kwarg = 'page' #查询参数的名字就是url问号后面的查询关键字，默认是？page
    
    def get_context_data(self,'**kwargs'):#获取上下文的数据
        #先通过父类的方法把参数都拿出来，这里面不光有数据，还有paginator等类
        #super(类，self).父类方法()是python2的写法，python3可以直接用super().父类方法()
        context = super(ArticleListView,self).get_context_data(**kwargs)
        #下面是自定义的一些参数
        context['username'] = 'zhizhi'
       
              
    def get_queryset(self): #如果类里没有实现这个方法，那么就会把所有的数据都返回相当于是是使用model.objects.all()。类里重写这个方法，将需要的数据提取出来。
        return Article.objects.filter(id__lte=89)
```

### 14.3 类视图添加装饰器

在开发中给函数添加装饰器很常见，在类上面就不多见了,要用django封装好的method_decorate来装饰类方法

```python
from django.utils.decorators import  method_decorator

#装饰器函数
def login_required(func):
    def wrapper(request,*args,**kwargs):
        #假设在url中有username查询关键字,就允许下面的操作，没有就跳转到登入页面
        username = request.GET.get('username')
        if username:
            return func(request,*args,*kwargs)
        else:
            return redirect(reverse('front:login'))
    return wrapper
class ProfileView(View):
    def get(self,request):
        return HttpResponse('个人中心界面')
    
    #路由分发的时候需要先经过dispath，所以需要可以装饰dispatch来实现一些功能，比如要求登入之后才能操作下面的
    @method_decorator(login_required)
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)
```

也可以直接装饰在类上面，但是要在装饰器里指定装饰哪个方法

```python
@method_decorator(login_required,name='dispatch')
class ProfileView(View):
    def get(self,request):
        return HttpResponse('个人中心界面')
```





## 十五. Paginator 和 Page类

这两个类都是用来做分页的，会直接封装在上面的context里面

Paginator常用属性和方法：

1. count：总共有多少条数据
2. num_page：总共多少页
3. page_range：页面的区间，比如有三页。就是range(1,4)

Page常用属性和方法：

1. has_next：是否还有下一页
2. has_previous：是否还有上一页
3. next_page_number：下一页的页码
4. previous_page_number：上一页的页码
5. number：当前页
6. start_index：当前这一页的第一条数据的索引值
7. end_index：当前这一页的最后一条数据的索引值

```python
class ArticleListView(ListView):
    model = Article #指定列表 
    template_name = 'article_list.html' #指定模板
    paginate_by = 10 #代表每页中显示多少条数据
    context_object_name = 'articles' #在前端取数据使用的名字
    ordering = 'created_time'
    page_kwarg = 'page' #查询参数的名字就是url问号后面的查询关键字，默认是？page
    
    def get_context_data(self,'**kwargs'):
        context = super(ArticleListView,self).get_context_data(**kwargs)
        context['username'] = 'zhizhi'
        #获取context里面的paginator方法
       	paginator = context.get('paginator')
        #下面使用分页器的一些属性和方法
        print(paginator.count)
```



### 15.1 实现分页算法

```python
class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'
    context_object_name = 'articles'
    paginate_by = 10
    ordering = 'created_time'
    page_kwarg = 'p'
    
	def get_pagination_data(self, ):
   		 
```

## 十六.错误处理

### 16.1常见的错误码

- 404：服务器没有指定url
- 403：没有权限
- 405：请求method错误
- 400：bad request，请求参数错误
- 500：服务器内部错误，一般是服务器内部代码出bug，比如出现0的除数等
- 502：部署的时候常见，一般是nginx启动了，然后uwsgi有问题

### 16.2 自定义错误模板

碰到错误的时候直接返回定义的模板，直接在templates下面创建404.html，500.html错误模板，settings里的deburg一定要改成false。其余不需要做什么修改，django会自动跳转。

除了404和500，其他的错误可以使用正常的redirect来使用。

即单独建立一个error的包，在下面和app一样，创建urls，path等。在业务中如果出现错误，就跳转到错误页面

## 十七.表单

### 17.1 django的表单作用

1. 渲染表单模板（在前后端分离的工作中，这部分不涉及）
2. 表单验证数据是否合法

### 17.2 django使用流程

以做一个留言板为例

1. 在app里面建立一个forms.py文件，文件中的表单类要继承自forms.Form

2. 定义一些字段来接收前端提交的字段

   ```python
   from django import forms
   
   class MessageBoardForm(forms.Form):
       title = forms.CharField(max_length=100,min_length=2,label="标题",error_messages="字数要在2-100之间")#label是显示在前端的字段，默认直接用英文title显示，error_messages是数据验证不通过时候在后台显示的信息
       content = forms.CharField(widget=forms.Textarea,label="内容")
       email = forms.EmailField(label="邮箱")
       reply = forms.BooleanField(required=False,label="是否回复")
   ```

   

3. 然后在视图中根据method来决定操作，如果是get就返回一个空表单，如果是post就对数据进行验证

   ```python
   from django.views.generic import View
   from .forms import MessageBoardForm
   # Create your views here.
   class indexView(View):
       def get(self,request):
           form = MessageBoardForm()#定义一个空的表单
           return render(request,'index.html',context={'form':form})
       
       def post(self,request):
           form = MessageBoardForm(request.POST)#将前端提交的数据都取出来了
           if form.is_valid():
               title = form.cleaned_data.get('title') #cleaned_data代表已经验证清理过的数据
               content = form.cleaned_data.get('content')
               email = form.cleaned_data.get('email')
               reply = form.cleaned_data.get('reply')
               print(title)
               return HttpResponse('success')
           else:
               print(form.errors.get_json_data())#form.errors报错了表单验证过程中所有的错误信息
               return HttpResponse('fail')
   
   ```

4. 前端的模板（一般不使用form标签来渲染）

   ```html
   <body>
       <form action="" method="POST">
           <table>
               {{form.as_table}} //as_table表示form以tr一样显示，还可以用as_list等
               <tr>
                   <td>提交</td>
                   <td><input type="submit" value="提交"></td>
               </tr>
           </table>
       </form>
       
   </body>
   ```

### 17.3 表单验证数据

常用的Field：

- CharField：参数，max_length,min_length,required(是否必须),error_message(该字段验证错误时，显示的错误信息)

- EmailField：错误信息的key有required，invalid

- FloatField：参数，max_value,min_value 。错误信息的key有required，invalid,max_value,min_value

  ```python
  price = forms.FloatField(error_messages={"invalid":"请输入浮点数"})
  ```

- IntegerField:参数，max_length,min_length 。错误信息的key有required，invalid,max_value,min_value

- URLField: 

### 17.4 常用验证器

在验证某个字段时，可以传递一个validators参数用来指定验证器，进一步对数据进行过滤。一般来说一些字段本身就带有验证器（源码中体现），比如emailfield就是带了EmailValidator验证器

常用的验证器：

- MaxValueValidator

- MinValueValidator

- MaxLengthValidator

- MinLengthValidator

- EmailValidator

- URLValidator

- RegexValidator:比较万能的一个验证器，由正则表达式构成

  使用regex来实现一个手机号码验证器

  ```python
  Tel = forms.CharField(validators=[validators.RegexValidator(r'1[345678]\d{9}',message='请输入正确的手机号码')])
  ```

例如，用charFiedl来实现EmailField

```python
from django import forms
from django.core import validators
class MyForm(forms.Form)
#validators后面跟列表说明，可以不止使用一个验证器，message代表如果不通过邮箱验证器显示的错误信息
	email = forms.CharField(validators=[validators.EmailValidator(message="请输入正确格式的邮箱")])
```

### 17.5 自定义验证器

有时候常用的验证器不一定够用，那就需要我们自定义验证了。比如验证某个字段在数据库里只能存一个，（手机号）

```python
#forms.py
class RegisterForm(forms.Form):
    username = forms.CharField(max_length=100)
    tel = forms.CharField(validators=[validators.RegexValidator(r'1[345678]\d{9}',message='请输入正确的手机号码')])
    pwd1 = forms.CharField(max_length = 16, min_length= 6)
    pwd2 = forms.CharField(max_length = 16, min_length= 6)

    def clean_tel(self):#如果要自定义字段的验证，必须用这个方法名：clean_字段名。当调用form.is_valid的时候，就会自动调用
        telephone = self.cleaned_data.get('tel')#获取前端提交的手机号
        exist = User.objects.filter(tel=telephone).exists() #拿到数据库里去验证是否唯一
        if exist:
            raise forms.ValidationError(message="手机号码已经被注册") #如果存在就通过raise一个错误
        return telephone #验证完后一定要返回拿到的数据，不然view视图中就无法通过form.cleaned_data.get来取到
    
    def clean(self):#这个方法要写在所有字段单独验证的后面，用来同时验证两个或两个以上的字段。比如密码和确认密码是否一致
        cleaned_data = super().clean() #这里重写了clean这个在父类中也存在的方法，如果需要拿到已经验证过的数据，就需要调用父类的clean方法
        pwd1 = cleaned_data.get('pwd1')
        pwd2 = cleaned_data.get('pwd2')
        if pwd1 != pwd2:
            raise forms.ValidationError(message="两次密码不一致")
        return cleaned_data #一定要返回

#views.py
class RegisterView(View):
    def get(self,request):
        form = RegisterForm()
        return render(request,'register.html',context={'form':form})
    def post(self,request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            tel = form.cleaned_data.get('tel') #如果forms中在自定义验证方法中不反回tel，那么这里就取不到tel数据
            print(username,tel)
            return HttpResponse('success')
        else:
            print(form.errors.get_json_data())
            return HttpResponse('fail')
```

### 17.6 错误信息的提取

如果验证失败了，有一些错误信息是需要传给前端的，我们可以通过以下方式实现：

1. form.errors:这个属性的错误信息是包含了html标签的
2. form.errors.get_json_data()：这是获取了一个类字典的错误信息
3. form.as_json()：这个方法是将form.get_json_data()返回的字典dump成json格式的字符串，方便进行传输
4. 上面方法获取的字段的错误值，都是一个比较复杂的数据

如果想把错误信息放在一个列表中，而不是放在一个字典中，我们可以在form类中定义一个方法，把数据重新整理一下

```python
class form(form.Form):
    def get_errors(self):
        errors = self.errors.get_json_data()
        new_errors = {}
        for key,message_dicts in errors.items():
            messages = []
            for message_dict in message_dicts:
                message = message_dict['message']
                messsages.append(message)
            new_errors[key] = messages
        return new_errors
#views.
errors = form.get_errors（）就可以把提交的错误信息比较清晰的展示出来
```

也可以把这个get_errors封装在一个公共类里面比如BaseForm（forms.Form）,然后其他表单类继承这个公共类，表单类就可以直接使用这个方法，而不用在每个表单类里面重新实现

### 17.7 ModelForm

如果表单中的字段和模型中的字段是一样的，而且表单中验证的数据也就是我们模型中需要保存的，那么这时候我们可以将模型中的字段和表单中的字段进行绑定。比如：

```python
class Article(models.Model):
    #在models模型中也可以直接使用验证器
    title = models.CharField(max_length=10,validators=[validators.MinLengthValidator(limit_value=3)])
    content = models.TextField()
    author = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    created_time = models.DateTimeField(auto_now_add=True)
```

这个时候，forms中就很简单了

```python
from django import forms

class MyForm(forms.ModelForm):
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if title > 10:
            raise forms.valudationError('最长不超过10')
        return title
    
    class Meta:
        model = Artile
        fields = "__all__"
        #fields = ['title','content'] 指定字段
        #exclude = ['author'] 排除该字段
        #下面是配置每个字段的报错信息
        error_message={
            'title':{
                'required':'请传入参数'，
            },
            'author':{
                'max_length':'最长位100'
            }
        }
```

### 17.8 ModelForm的save方法

前端提取的数据通过form.is_valid（）验证后，可以直接使用form.save()保存到数据库，不用再取出来单独保存了

```python
form = Form(request.POST)
if form.is_valid():
    form.save()
```

但如果在表单有模型中没有的字段，比如用户模型，只需要一个pwd，但是一般表单提交的时候会有两个pdw用于验证用户的输入是否一致。这时候就需要用下面的方式了

```python
#models.py
class User(models.Model):
    username = models.CharField(max_length=64)
    tel = models.CharField(max_length=11,validators=[validators.RegexValidator(r'1[345678]\d{9}')])
    pwd = models.CharField(max_length=20)

#forms.py
class UserForm(forms.ModelForm):
    pwd1 = forms.CharField(max_length=20) #表单自定义两个pwd字段
    pwd2 = forms.CharField(max_length=20)

    def clean(self):
        cleaned_data = super().clean()
        pwd1 = cleaned_data.get('pwd1')
        pwd2 = cleaned_data.get('pwd2')
        if pwd1 != pwd2:
            raise forms.ValidationError('两次输入不正确')
        else:
            cleaned_data

    class Meta:
        model = User
        exclude = ['pwd'] #将用户模型中的pwd排除
  
#views.py
@require_POST#使用装饰器来限定提交的方法
def register(request):
    form = UserForm(request.POST)
    if form.is_valid():
        user = form.save(commit=False) #使用commit=False，并没有将表单数据save到数据库，而是生成了一个模型对象
        user.pwd = form.cleaned_data.get('pwd1') #将经过验证的pwd赋给模型对象后再保存
        user.save()
        return HttpResponse('suces')
    else:
        print(form.errors.get_json_data)
        return HttpResponse('false')
```

## 十八.文件上传

文件上传分为两部分：

1. 前端页面

   前端页面中需要使用form来提交文件，并且form标签一定要使用enctype='multipart/form-data'属性，不然不能上传文件。form标签中的input标签，要是用type=‘file’,指定name。multipart是为了给文件来编码

   ```html
   <form action="" method="POST" enctype="multipart/form-data">
       <input type="file" name="myfile">
   </form>
   ```

2. 后端处理

   后端是通过reques.FILES.get('myname')来获取

   ```python
   def save_date(file):
       with open('somfile.txt','wb') as fp:
           for chunk in file.chunks():
               fp.write(chunk)
   
   def index(request):
       if request.method == 'GET':
           form = MyForm()
           return render(request,'upload.html',context = {'form':form})
       else:
           file = request.FILES.get('myfile')
           svae_data(file)
           return HttpResponse('success')
   ```

也可以在模型中定义一个file类型字段来简化上面的处理，如下

```python
#models.py
class Upload(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    file_obj = models.FileField(upload_to="files") #upload_to到指定的文件路径，一般这里是项目下的files文件夹

#views.py
def upload(request):
    if request.method == 'GET':
        return render(request,'upload.html')
    else:
        title = request.POST.get('title')
        content = request.POST.get('content') 
        file_obj = request.FILES.get('myfile') #这里注意一定要用request.FILES.get。不然获取不到文件对象
        new_obj = Upload(title=title,content=content,file_obj=file_obj)
        print(title,content,file_obj)
        new_obj.save()
        return HttpResponse('suce')
```

### 18.1 指定MEDIA_ROOT和MEDIA_URL

上面是我们指定了一个files文件夹然后upload_to到里面去存储，如果我们指定了media_root，那么就不要在filefield字段中指定upload_to，它会自动将文件上传到MEDIA_ROOT

```python 
MEDIA_ROOT = os.path.join(BASE_DIR,'media')#具体的路径
MEDIA_URL = '/media/'#访问时候用的url，比如127.0.0.1:800/media/aa.txt
```

然后我们在urls.py 中添加MEDIA_ROOT目录下的访问路径，这是为了通过url去访问静态文件时候配置的，一般如果不需要访问静态文件，不需要配置

```python
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('...')
] + static(settings.MEDIA_ULR,document_root=settings.MEDIA_ROOT)
```

如果同时指定了MEDIA_ROOT和upload_to，那么文件就会上传到MEDIA_root下的upload_to下的文件夹里

```python
models.FileField(upload_to='%Y/%m/%d')
#这样会子啊media文件夹下自动生成一个年月日的文件夹，将文件保存到里面
```

### 18.2 限制上传文件类型

可以在模型中使用验证器来限制上传的文件类型

```python
models.FileField(upload_to='%Y/%m/%d',validators=[validators.FileExtensionValidator(['txt'],message="必须上传txt格式的文件")])
#这个message可以在模型里面的验证器里写，也可以在表单里统一写error_message
```

### 18.3 上传图片

上传图片有一个单独的字段:ImageField,这个字段实在filefield的基础上增加了一些文件类型的验证.注意这个字段必须要安装pillow库

## 十九.memcached

这是一个内存级别的缓存系统软件，高性能分布式的内存对象缓存系统。简单来说就是把数据直接存在内存里，它是通过在内存里维护一个统一的巨大的hash表，它能存储各种各样的数据，包括图像视频文件以及数据库检索的结果，但一般来说不会去存图像视频。

### 19.1 使用memcached的情况

存储验证码（图形验证码、短信验证码）、session等不是重要的数据 

### 19.2 安装

## 二十. session和cookie

- cookie:在web中，http请求是无状态的，也就是说每一次客户端和服务器连接都是全新的，cookie的出现就是解决了这个问题，第一次登入服务器后，会返回一些cookie给浏览器，然后浏览器就保存在本地。当第二次请求时就带上这个cookie，那么服务器就通过这个cookie可以判断当前用户是谁了。

  但是cookie能存储的数据有限，而且不同浏览器有不同的存储大小。一般不超过4k,所以cookie只能存储一些小数据。

- session:类似cookie，也是为了存用户相关的数据。不同的是，session是存在服务器，不同的服务器，框架，语言有不同的实现，session主要是为了解决数据不安全的问题
- cookie和session结合使用：
  - 存储在服务端：通过cookie存储一个sessionid，具体的数据是保存在session中。如果用户已经登入，服务器会在cookie中保存一个sessionid，下次浏览器再请求时候，就会携带这个sessionid。服务器根据sessionid到数据库中去找用户的session数据。就可以知道session是谁了，以及之前存的状态信息。这种方式叫做server side session
  - 将session数据加密，然后存在cookie中。这种方式叫client side session。flask框架采用的就是这种方式

### 20.1 django操作cookie和session:

- cookie是设置给浏览器的，所以需要通过response来传输这个数据，所以通过response.set_cookie来设置，相关参数：
  - key：cookie的key
  - value:cookie的值
  - max_age：cookie有效时间，单位是s
  - expires：过期时间，具体的日期，datetime。如果同时设置了max_age和expires,那么会采用expires的值
  - path：对域名下哪些路径有效，默认是域名下全部有效
    - path = '/路径/'
  - domain：针对哪个域名有效。默认是针对主域名下都有效，如果要针对子域名，那就可以设置这个属性
  - secure：是否是安全，如果设置为True，那就只能再https协议下才能使用
  - httponly:默认是false，如果为true，那就在客户端不能通过javascript进行操作

- 删除cookie：

  - 通过delete_cookie即可删除cookie,实际上删除cookie就是将指定的cookie值设为空字符串，过期时间设为0，也就是浏览器关闭就过期

- 获取cookie：获取是通过request来获取的，返回的是一个字典

  - ```python
    cookies = request.COOKIES
    for cookie_key,cookie_value in cookies.items():
        print(cookie_key,cookie_value)
    ```

- 操作  session,request.session.get('username')

  - request.session['username'] = 'zhiliao' 设置session数据，这些数据会存到django_session表中，这个表模型已经在默认的app中存在了，所以只要完成迁移就可以直接使用，不用我们再建模型
  - get:用来从session中获取指定值
  - pop(字段):用来从session中删除一个值
  - keys()：从session中获取所有键
  - items()：从session中获取所有值
  - clear():删除session并且删除在浏览器中存储的session_id，注销时候用得比较多.flush()方法会把所有的清空
  - set_expiry(value)L设置过期时间
    - 整形：多少秒
    - 0：浏览器关闭就过期
    - None：使用全局中setting.py里设置的SESSION_COOKIE_AGE来配置全局过期时间，默认是2周
  - clear_expired:清楚过期的session。django不会自动清除过期的session，需要定期手动清除，或者是在终端shell，使用 python manage.py clearsession来清除过期session

### 20.2 修改session的存储机制

session 默认是存在数据库中的django_session表，也可以存到其他地方。通过设置SESSION_ENGINE来指定存储位置，有以下几种方案：

1. django.contrib.sessions.backends.db：默认数据库
2. django.contrib.sessions.backends.file:使用文件来存
3. django.contrib.sessions.backends.cacher：使用缓存来存储，前提是必须要在setting里设置号caches,并且需要用memcached，而不能使用纯内存作为缓存
4. django.contrib.sessions.backends.cached_db：既使用缓存，也使用数据库。存数据时，先存到缓存，再存到数据库。这样可以保证缓存系统出现问题，session数据也不会丢失，还存在数据库里。当取数据时，先到缓存里去找，找不到再到数据找
5. django.contrib.sessions.backends.signed_cookies：将session信息加密后存到浏览器的cookies中，这种方式不一定安全，建议设置SESSION_COOKIE_HTTPONLY=True，就不能通过js来获取session数据，并且还需要对setttings中的secret_key进行保密，别人一旦知道这个key，就可以用来解密。数据大小不能超过4k

## 二一.上下文处理器

上下文处理器可以返回一些数据，在全局中使用，比如用户登入的用户信息，在很多页面中都可以使用，就是因为用户信息存在上下文处理器中了。所以我们把公用的数据放在上下文中，就没必要再每个视图函数中返回这个数据。

案例：

```tex
比如登入功能，正常的网站只要登入了，那么在导航栏这些位置原本的登入按钮就会显示用户信息。这个功能就是通过session+上下文处理器来实现的
```

```python
#根本的做法是在每个视图函数中都需要取一次session
def index(request):
    user_id = request.session.get('user_id')#前提是在登入时候，已经通过request.session['user_id']=变量在django_session中建立了一个信息
    context = {}
    try:
        user = User.objects.get(pk = user_id)
        context['front_user'] = user
    except：
    	pass
    return render(request,'index.html'.context)
```

更好的做法是使用上下文处理器，就不需要在每个函数中再取了，下面是自定义上下文处理的步骤

1. 在app目录下创建一个context_processors.py文件

   ```python
   def app_user(request):
       user_id = request.session.get('user_id')
       context = {}
       if user_id:
           try:
               user = User.objects.get(pk = user_id)
               context['front_user'] = user
           except:pass
       return context
   ```

2. 在setttings.py的templates    opptions中加入

   ```python
   'OPTIONS': {
       'context_processors': [
           'django.template.context_processors.debug',
           'django.template.context_processors.request',
           'django.contrib.auth.context_processors.auth',
           'django.contrib.messages.context_processors.messages',
           'front.context_processors.app_user'
       ],
   ```

3. 在模板中可以直接使用front_user这个对象，就不需要在每个视图函数中写一遍

### 21.1 内置的上下文处理器，模板变量

在setting.TEMPLATES.OPTIONS.context_processors中，有许多内置的上下文处理器。这些处理器的作用如下：

- django.template.context_processors.debug:增加一个debug和sql_requires变量，在模板中可以通过他来看一些数据库查询

  - ```python
    def debug(request):
        """
        Return context variables helpful for debugging.
        """
        context_extras = {}
        if settings.DEBUG and request.META.get('REMOTE_ADDR') in settings.INTERNAL_IPS:
            context_extras['debug'] = True
            from django.db import connections
            # Return a lazy reference that computes connection.queries on access,
            # to ensure it contains queries triggered after this function runs.
            context_extras['sql_queries'] = lazy(
                lambda: list(itertools.chain.from_iterable(connections[x].queries for x in connections)),
                list
            )
        return context_extras
    ```

  - 源码意思是只要deburg开启并且在内部ip池里，那么我们就可以在模板中使用deburg和sql_queries（在视图函数里面有了查询操作才能使用这个变量）

- django.template.context_processors.request:增加一个request变量。这个request变量也就是在视图函数的第一个参数。

- django.template.context_processors.auth：Djangon内置的用户系统，增加一个user对象

- django.template.context_processors.messages：增加一个messagges变量

  1. 现在视图函数中使用message

     ```python
     from django.contrib import messages
     def index(request):
         messages.info(request,'需要传的消息') #这个message不需要用context通过render返回，可以直接在模板中使用，因为上下文处理器的存在
         return render(request,)
     ```

     ```html
     {% for message in messages %}
     {{message}}
     {% endfor %}
     ```

- django.template.context_processors.media：在模板中可以读取MEDIA_URL,比如想要在模板中使用上传的文件，那么这时候就需要使用settings.py中设置的MEDIA_URL来凭借url，

  ```html
  <img src="{{MEDIA_URL}}{{user.avatar}}" /> user.avator里面是相对media的相对路径
  ```

- django.template.context_processors.static:使用STATIC_URL

- django.template.context_processors.csfr：使用csrf_token来生成一个csrf令牌，主要在表单中使用。

  - ```html
    <input type="hidden" name="csrfmiddlewaretoken"  value = "{{csrf_token}}">
    ```

  - 也可以用{% csrf_token %} ，这个标签就是生成了一个上面的input标签（可以在前端页面看到），这个token不一定在form中产生，还可能在head中使用。这个时候就必须要使用{{ csrf_token }}变量，不能使用{% csrf_token %}这个标签了。

## 二二.中间件

中间件是request和response处理过程中的一个插件，比如在request到达视图函数之前，我们可以使用中间件来做一些相关事情，比如可以判断当前用户有没有登入，如果登入了，就绑定一个user对象到request上。也可以在response到达浏览器之前，做一些相关的处理，比如要统一在response上设置一些cookie信息等

### 22.1 自定义中间件

中间件所处的位置没有规定。只要是放到项目当中即可，一般分为两种情况，如果中间件是属于某个app的，那么可以在这个app下创建一个python文件来放这个中间件。也可以专门创建一个python包，用来存放所有的中间件。中间件有两种方式，一种是函数，一种是类

### 22.2 使用函数的中间件

- 在app下写一个middlewares.py文件

```python
#中间件函数
def user_middleware(get_response):
    print('user_middleware') #这是在django启动时候就会运行的初始化代码
    def middleware(request):
        print('request到达view函数之前运行')
        user_id= request.session.get['user_id']
        if user_id:
            try:
				user = User.objects.get(pk = user_id)
                request.front_user = user   #将user作为request的一个对象，这样就可以就可以在view函数通过request来直接使用登入用户的信息了
            except:
                request.front_user = None
        else:
            request.front_user = None
        #下面是response对象到达浏览器之前执行的代码    
        response = get_response(request)
        return reponse
        
```

- 然后在settings.py中将这个中间件写入

### 22.2 使用类的中间件

```python
class UserMidder:
    def __init__(self,get_response):
        #初始化代码
        self.get_response = get_response
        
    def __call__(self,requst):
        print('request到达view函数之前运行')
        user_id= request.session.get['user_id']
        if user_id:
            try:
				user = User.objects.get(pk = user_id)
                request.front_user = user   #将user作为request的一个对象，这样就可以就可以在view函数通过request来直接使用登入用户的信息了
            except:
                request.front_user = None
        else:
            request.front_user = None
        #下面是response对象到达浏览器之前执行的代码    
        response = self.get_response(request)
        return reponse
```

然后再settings.py中注册

### 22.3内置中间件

- django.middleware.common.CommonMiddleware:用于当浏览器中的url不规范（没有/时），通过301重定向的方式到规范的url里。也可以用于防爬虫，处理user-agent

  - ```python
    #在setttings中配置
    import re
    DISALLOWED_USER_AGENTS=[
        re.compile(r'^\s$|^$'),
        re.compile(r'.*PhantomJS.*')
    ]
    #这段代码是用于防爬虫，伪造User-agent
    ```

  - 可以直接到.CommonMiddleware源码去看

- gzip中间件，可以压缩页面的字节数量，response的content_type也会变成gzip格式

- django.middleware.security.SecurityMiddleware：做了一些安全处理，比如设置xss防御的请求头，比如一个网站有https协议，那么当用户使用http协议的时候就会自动转https协议。

- django.contrib.sessions.middleware.SessionMiddleware：给request添加一个处理好的session对象

- django.contrib.auth.middleware.AuthenticationMiddleware：给request添加一个user对象

- django.middleware.clickjacking.XFrameOptionsMiddleware：在响应头中添加一个属性response['X-Frame-Option']，让网页不能被其他网站使用iframe标签引用

### 22.4 中间件放置位置

没有依然其他中间件的要放在前面，存在依赖关系的就要注意位置顺序

## 二三. 安全

### 23.1 CSRF攻击

CSRF（cross site request forgery，跨站域请求伪造）是一种网络的攻击方式

原理：网站是通过cookie来实现登陆功能的，而cookie只要存在浏览器中，那么浏览器在访问这个cookie的服务器时，就会自动携带cookie信息到服务器上。有些病毒网站可以在网页源代码中插入js代码，使用js代码给其他服务器发送请求（比如银行的转账请求）。因为在发送请求的时候，浏览器会自动的把cookie发送给服务器，这时候银行的网站就不知道这个请求时伪造的，就会在用户不知情的 情况下，发生转账

### 23.2 XSS攻击 

- 原理：利用网站的漏洞，比如在评论里面提交了一些script语言（<script>alert('hello world')</script>）,浏览器就会跳出一个弹窗。可以利用类似的漏洞在网站页面上插入广告，破坏html的结构
- 防御：如果不需要显示富文本，那么在渲染用户提交的数据时候，一定要使用转义（django默认开启转义，使用|safe是关闭转义）