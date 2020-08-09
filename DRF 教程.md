# DRF 教程

## 一. web模式

### 前后端不分离

![image-20200621063732701](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200621063732701.png)

### 前后端分离

![image-20200621063816586](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200621063816586.png)

## 二. restful了解

是统一的接口定义方式，被广大人员认可

### 2.1 设计方法

1. 域名：应该尽量将API部署在专用域名之下

   ```python
   https://api.example.com
   https://exapmle.com/api/                  #如果API简单，不会有进一步扩展，可以放在主域名后面
   ```

2. 版本：

   应该将API的版本号放入URL

   ```python
   http://www.example.com/app/1.0/foo
   ```

   另一种做法是放在http头部信息中，但不如放在URL中方便和直观，Github用的是这样的。不同的版本，可以理解成同一资源的不同表现形式，应该采用同一个URL。版本号在HTTP请求头信息的Accetp字段中进行区分

   ```python
   Accept:vnd.example-com.foo+json;version=1.0
   ```

3. 路径：

   路径又称‘终点’，表示API的具体网站，每个网址代表一种资源（resource）

   1）资源作为网址，只能由名词，不能有动词，而且所有的名词往往与数据库的表名对应

   下面是不好的例子：

   /getProducts

   /listOrders

   /retreiveCilent

   对于一个简洁的结构，应该始终使用名词，此外，利用的HTTP方法可以分离网址中的资源名称的曹祖

   GET /products:返回所有产品清单

   POST/products: 将产品新建到集合

   GET /products/4 获取产品 4

   PATCH(或) PUT /products/4 将更新产品 4

   2）API中的名词应该使用复数。无论子资源或者所有资源

   获取单个产品：域名/AppName/rest/products/1

   获取所有产品：域名/AppName/rest/products

4. HTTP动词

   对于资源的具体操作类型，由HTTP动词表示，常见的动词由以下4个

   1. GET
   2. POST
   3. PUT：更新服务器资源（客户端提供改变后的完整资源）
   4. DELETE

   不常用的由3个：

   1. PATCH: 在服务器更新资源（客户端提供改变的属性）

   2. HEAD：获取资源元数据

   3. OPTIONS：获取信息，关于资源的哪些属性是客户端可以改变的

      ```python
      PUT /zoos/ID:更新某个动物园的全部信息
      PATCH /zoos/ID:更新某个动物园的部分信息
      ```

5. 过滤信息（Filtering）

   如果数据很多，服务器不能将它们同时全部返回给用户，API应该提供参数，过滤返回结果

   常见例子

   ```python
   ?limit =10: 指定返回数量
   ?offset = 10: 偏移量，指定返回记录的开始位置
   ?page=28&per_page=19： 指定第几页，以及每页的记录数
   ?sortby=name&order=asc： 指定排序的属性，以及升序
   ?animal_type_id=1:指定删选条件
   ```

6. 状态码

   ![image-20200621071054624](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200621071054624.png)

7. 错误处理

   如果状态码是4XX，服务器就应该向用户返回出错信息，一般，返回的信息中将error作为键名，出错信息作为值

   ```python
   {
       error:Invalid API key
   }
   ```

8. 返回结果

   针对不同操作，服务器向用户返回的结果应该符合以下规范

   ![image-20200621071420463](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200621071420463.png)

9. 其他

   服务器返回的数据格式，应该尽量使用JSON，避免使用XML

## 三. restful案例

目的：需要能够设置符合restful的接口

案例：图书馆的增删改查

| 功能         | 请求方式 | 请求路径 |
| ------------ | -------- | -------- |
| 获取所有书籍 | GET      | /books   |
| 创建单本书籍 | POST     | /books   |
| 获取单本书籍 | GET      | /books/1 |
| 修改单本     | PUT      | /books/1 |
| 删除单本     | DELETE   | /books/1 |

书籍准备

1. 模型类
2. 迁移
3. 导入数据



可以查看文档项目



## 四. DRF魅力展示（了解）

目的：了解drf的作用，使用流程

作用：比传统的代码相比简单了非常多

​	1.封装路由

​	2.序列化器

​	3.视图

使用流程：

​	1.安装drf     pip install djangorestframework

	2. 注册： rest_framework

## 五. 序列化

将程序中的一个数据结构类型转换为其他格式（字典，json,xml等），例如将django中的模型类对象转换为json字符串，这个过程我们称为序列化

反之，将其他格式转化为语言中的对象称为反序列化。

序列化器有两个作用：序列化，反序列化

![image-20200621135322662](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200621135322662.png)

### 5.1 序列化器定义

目的：能够参考模型类定义序列化器

序列化定义过程：

1. 定义类，继承自serializer
2. 和模型类，字段名字一样(取决于你想序列化字段的个数，可以比模型少)
3. 和模型类，字段类型一样
4. 和模型类，字段选型一样

如下：

```python
#模型类
class BookInfo(models.Model):
    btitle = models.CharField(max_length=20,verbose_name='名称')
    bpub_date = models.DateField(verbose_name='发布日期')
    bread = models.IntegerField(default=0,verbose_name='阅读量')
    bcomment = models.IntegerField(default=0,verbose_name='评论量')
    is_delete = models.BooleanField(default=False,verbose_name='逻辑删除')
    
#序列化器
from rest_framework import serializers
class BookInfoSerializer(serializers.Serializer):
    id = serializers.IntegerField(label="id",read_only=True)    #label 字段说明，类似verbose_name
    btitle = serializers.CharField(max_length=20,label='名称')
    bpub_date = serializers.DateField(label='发布日期')
    bread = serializers.IntegerField(default=0,label='阅读量')
    bcomment = serializers.IntegerField(default=0,label='评论量')
    is_delete = serializers.BooleanField(default=False,label='逻辑删除')
```

### 5.2 序列化单个对象

目的，能够使用序列化器，序列化单个对象

```python
from .serializers import BookInfoSerializer
from booktest.models import BookInfo

#1,获取书籍对象
book = BookInfo.objects.get(id=1)

#2.创建序列化器,instance,表示要序列化的对象
serializer = BookInfoSerializer(instance=book)

#3.转换数据
print(serializer.data)
```

### 5.3 序列化列表

目的：能够将多个对象列表进行序列化操作

```python
#1,获取书籍对象
books = BookInfo.objects.all()

#2.创建序列化器,instance,表示要序列化的对象
serializer = BookInfoSerializer(instance=books,many=True)

#3.转换数据
print(serializer.data)
```

### 5.4 关联对象的序列化（英雄模型里面有外键）

目的：能够序列化英雄的时候，输出英雄关联的书籍显示

操作流程：

1. 定义英雄序列化器

   ```python
   class HeroInfoSerializer(serializers.Serializer):
       GENDER_CHOICE = (
           (0,'female'),
           (1,'male')
       )
       id = serializers.IntegerField(label="id",read_only=True)
       hname = serializers.CharField(max_length=20,label='名称')
       hgender = serializers.ChoiceField(choices=GENDER_CHOICE,required=False,label='性别')
       hcomment = serializers.CharField(max_length=200,allow_null=True, label='描述信息',required=False)
   ```

   

2. 定义序列化字段

   ```python
   #1 关联模型类的主键。外键,在参数中页可以设置read_only = True
   # hbook = serializers.PrimaryKeyRelatedField(read_only=True)
   hbook = serializers.PrimaryKeyRelatedField(queryset = BookInfo.objects.all())
   #2 使用模型类的__str__返回值
   #hbook = serializers.StringRelatedField(read_only=True)
   #3 关联书籍序列化器显示书籍模型的所有信息 
   #hbook = BookInfoSerializer()
   
   ```

### 5.5 书籍序列化器显示英雄

目的：能够序列化书籍的时候，显示英雄的信息

```python
#1 关联英雄，主键
    heroinfo_set = serializers.PrimaryKeyRelatedField(read_only=True,many=True) #如果没有many，会在结果中显示对象，有了many才会显示具体的主键
    # #2 关联英雄，返回str值
    # heroinfo_set = serializers.StringRelatedField(read_only=True,many=True)
    # #3 显示所有的信息
    # heroinfo_set = HeroInfoSerializer()
```

many= True, 用在一对多的时候

## 六. 反序列化

将json反序列化为python对象，反序列化需要反正校验，入库

校验：

1. 字段类型校验

   目的：理解序列化器中的字段，对数据进行校验的过程

   ```python
   #1. 准备数据
   book_dict = {
       "btitle":"金瓶X",
       "bpub_date":"1990-1-1",
       "bread":10,
       "bcomment":5
   }
   #2. 创建序列化器
   serializer = BookInfoSerializer(data=book_dict)
   #获得一个序列化器后，必须要校验数据之后，才能入库
   serializer.is_valid()
   # serializer.is_valid(raise_exception=True) 校验不通过可以直接报错
   print(serializer.data)
   #3. 输出
   ```

   

2. 字段属性（选项）校验

   目的：知道序列化器中字段选项的校验操作

   常见的选项：

   1. max_length:
   2. min_length:
   3. required:默认就是true，必须要传递一个值。除非设置default | false | read_only
   4. read_only:只序列化，不进行反序列化。json转模型对象的额时候不需要它。对象转json时，一定要

3. 单字段，校验（方法）

   目的：能够定义单字段校验

   ```python
   def validate_btitle(self,value): #value就是字段里面的值
       if "金瓶" not in value:
           raise serializers.ValidationError('书籍名必须包含金瓶')
       return value
   
   ```

   注意格式：validate_字段名

4. 多字段，校验（方法）

   目的：定义多字段校验方法对数据校验

   ```python
   def validate(self, attrs):
       '''
       :param attrs:就是外界传进来的book_dict
       :return 
        '''
       #1. 获取阅读，评论量
       bread = attrs['bread']
       bcomment = attrs['bcomment']
       #2. 判断
       if bcomment > bread:
           raise serializers.ValidationError('评论大于阅读量')
           #3. 返回
       return attrs
   ```

   其实可以在多字段校验中对单字段进行。

   注意：当校验不通过的时候，一定要抛出异常

5. 自定义，校验方法（没什么用）

6. create新的数据入库

   目的：能够重写create方法实现代码入库

   在views中只要完成验证，就可以使用serializer.save()进行入库。（但是序列化器中一定要定义create方法，实现数据保存）

   ```python
   #1. 准备数据
   book_dict = {
       "btitle":"金瓶X",
       "bpub_date":"1990-1-1",
       "bread":10,
       "bcomment":5
   }
   #2. 创建序列化器
   serializer = BookInfoSerializer(data=book_dict)
   #获得一个序列化器后，必须要校验数据之后，才能入库
   #sserializer.is_valid()
   serializer.is_valid(raise_exception=True) 校验不通过可以直接报错
   #3. 入库
   serializer.save()
   ```

   序列化器中实现的create方法

   ```python
   def create(self,validated_data): #validated_data是校验成功后的值
           #1.创建book模型对象。设置属性,入库
           book = BookInfo.objects.create(**validated_data)
           #3. 返回
           return book
   ```

7. update新的数据

   views中要实现的

   ```python
   book_dict = {
       "btitle":"金瓶X",
       "bpub_date":"1990-1-1",
       "bread":10,
       "bcomment":5
   }
   book = BookInfo.objects.all(id=1)
   serializer = BookInfoSerializer(instance = book ,data=book_dict)
   serializer.is_valid(raise_exception=True) #校验不通过可以直接报错
   serializer.save()
   ```

   当序列化器中传递了两个属性（instance,和data）一旦调用save，序列化器就会去调用updata（）

   ```python
   def update(self,instance, validated_data):
       #1.更新数据
       instance.btitle = validated_data['btitle']
       instance.bcomment = validated_data['bcomment']
       instance.bpub_data = validated_data['bpub_data']
       instance.bread = validated_data['bread']
       #2.入库
       instance.save()
       return instance
   ```

## 七. ModelSerializer

### 7.1 使用方式

目的:可以使用ModelSerializer根据模型类生成字段，避免使用那么多的字段

作用：

1. 自动生成模型类的字段，还可以自己定义新的字段

   ```python
   #1. 定义数据模型类序列化器
   from rest_framework import serializers
   from .models import BookInfo
   class BookModelSerialzier(serializers.ModelSerializer): #这个ModelSerializer牛逼，可以省略我们自己写字段的过程
       mobile = serializers.CharField(max_length =11,min_length=11,label='手机号') #这里可以定义比模型类额外的字段
       class Meta:
           model = BookInfo   #这里就直接将BookInfo模型中的字段参考过来
           fields = "__all__" #all代表所有的字段都拷贝
   ```

   在views中进行逻辑判断时候

   ```python
   #====使用模型类序列化器，测试序列化，返序列化
   from .models import BookInfo
   from .serialzier import BookModelSerialzier
   #1.获取模型类对象
   book = BookInfo.objects.get(id =1 )
   book.mobile = "15462154" #因为在序列化器中有mobile这个字段，所以在这里一定要添加这个属性，不然会报错,也可以通过在序列化器中添加默认值解决，或者write_only = True代表只支持反序列化
   #2.创建序列化对象
   serializer = BookModelSerialzier(instance=book)
   #3.输出结果
   serializer.data
   ```

2. 在序列化器可以不用写create方法，就可以直接调用save

   ```python
   #1. 准备字典数据
   book_dict = {
       "btitle":"鹿鼎记",
       "bpub_date":"1999-01-01",
       "bread":10,
       "bcomment":5
   }
   #2. 序列化器对象创建
   serializer = BookModelSerialzier(data=book_dict)
   #3. 校验，入库
   serializer.validate(raise_exception = True)
   serializer.save()
   ```

3. 使用模型类序列化器，更新数据。也不用写updata方法

   ```python
   book_dict = {
       "btitle":"鹿鼎记2",
       "bpub_date":"1999-01-01",
       "bread":10,
       "bcomment":5
   }
   book = BookInfo.objects.get(id=1)
   #2. 序列化器对象创建
   serializer = BookModelSerialzier(instance=book,data=book_dict)
   #3. 校验，入库
   serializer.validate(raise_exception = True)
   serializer.save()
   ```

4. fields

   如果指向生成指定的，可以写成如下

   ```python
   from rest_framework import serializers
   from .models import BookInfo
   class BookModelSerialzier(serializers.ModelSerializer): #这个ModelSerializer牛逼，可以省略我们自己写字段的过程
       mobile = serializers.CharField(max_length =11,min_length=11,label='手机号') #这里可以定义比模型类额外的字段
       class Meta:
           model = BookInfo   #这里就直接将BookInfo模型中的字段参考过来
           #生成指定字段
           fields = ["id","btitle"]
   ```

5. read_only_fields设置只读字段

   ```python
       class Meta:
           model = BookInfo   #这里就直接将BookInfo模型中的字段参考过来
           #生成指定字段
           fields = ["id","btitle"]
           read_only_fields = ["btitle"]
   ```

6. extra_kwargs

   目的：可以给生成的字段添加约束

   ```python
       class Meta:
           model = BookInfo   #这里就直接将BookInfo模型中的字段参考过来
           #生成指定字段
           fields = "__all__"
           extra_kwargs = {
               "bread":{
                 "max_value":100,
                 "min_value":0
               },
               "bcomment":{
                   "max_value":100,
                 	"min_value":0
               }
           }
   ```

## 八.APIView

### 8.1 request

目的：知道APIView的特点，并且可以通过request获取参数

特点：

- 继承自View
- 提供了自己的request对象，而不是django中的httprequest
- 并且提供了认证，权限，限流的功能

操作流程

```python
from rest_framework.views import APIView
from django.http import HttpResponse
class BookAPIView(APIView):
    def get(self,request):
        """
        View获取数据方式
            GET：
                request.GET
            POST:
                request.POST
                request.body
        
        APIView获取方式
            GET:
                request.query_params
            POST:
                request.data
        """
        #1. 获取APIView中的get请求参数(url中以？后面的查询参数)
        print(request.query_params)
    def post(self,request):
        #2. 获取APIView中的POST请求参数，而且可以获取json，表单，等数据都可以
        print(request.data)
        return HttpResponse('POST方法')
```

### 8.2 response

以前返回数据有httpresponse, jsonresponse。API中的Response既可以返回文本，又可以返回json。还可以直接在里面添加状态码。

目的：

​	使用一个类就可以代替之前很多的response

​	可以配合status状态码使用

```python
class BookAPIView(APIView):
    def get(self,request):
        print(request.query_params)
       	return Response('GET方法',status=status.HTTP_404_NOT_FOUND) #这个status需要导进来
```

### 8.3 APIView实现列表视图

目的：可以使用序列化器和APIView对列表视图进行改写

```python
class BookAPIView(APIView):
    def get(self,request):
        #1 获取数据
        books = BookInfo.objects.all()
        #2 创建序列化对象
        serializer = BookModelSerialzier(instance=books,many=True)
        #3 返回响应
        return Response(serializer.data)
    def post(self,request):
        #1. 获取前端的POST请求参树
        data_dict = request.data
        #2. 创建序列化器
        serializer = BookModelSerialzier(data= data_dict)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
```

### 8.4 APIView实现详情视图

目的：可以使用模型类序列化器和APIView改写

```python
class BookDetailView(APIView):
    def get(self,request,book_id):
        #1获取数据
        book = BookInfo.objects.get(id = book_id)
        #2创建序列化对象
        serializer = BookModelSerialzier(instance=book)
        return Response(serializer.data)
    
    def put(self,request,book_id):
        #1获取前端的数据
        book_dict = request.data
        book = BookInfo.objects.get(id = book_id)
        #2
        serializer = BookModelSerialzier(data=book_dict,instance=book)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data)
    
    def delete(self,request,book_id):
        BookInfo.objects.get(id = book_id).delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 
```

### 8.5 二级视图，实现列表视图

GenericAPIView继承自REST框架的APIVIew类，封装了标准列表和详细信息视图通常需要的属性和方法，提供的每个具体的通用视图可以和多个或一个mixin类组合而构建

```python
class BookListGenericAPIView(GenericAPIView):
    #1 提供公共的属性
    queryset = BookInfo.objects.all()
    serializer_class = BookModelSerialzier
    def get(self,request):
        #1 查询所有书籍
        # books = self.queryset
        books = self.get_queryset()   #与上面那条查询用法向同
        #2 将对象转换成字典列表
        # serializer = BookModelSerialzier(instance=books,many=True)
        # serializer = self.serializer_class(instance=books,many=True)
        # serializer = self.get_serializer_class(instance=books,many=True)
        serializer = self.get_serializer(instance=books,many=True)
        #3 返回响应
        return Response(serializer.data)
    def post(self,request):
        #1. 获取前端的POST请求参树
        data_dict = request.data
        #2. 创建序列化器
        serializer = self.get_serializer(data= data_dict)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
```

以后可以直接改属性里面的queryset，和serializer_class来是实现通用 

### 8.6 二级视图，实现详情视图

需要注意的是，传递的主键一定要用pk来命名（包括路由里面），因为在GenericAPIView里面的 lookup_field = 'pk'。当然也可以通过设定lookup_url_kwarg = "id"属性来设定这个

```python
class BookDetailGenericView(GenericAPIView):
    queryset = BookInfo.objects.all()
    serializer_class = BookModelSerialzier
    #lookup_url_kwarg = "id" #使用id就需要将下面的pk全部改掉了
    #lookup_field = "id" 也可以达到相同的效果
    def get(self,request,pk):
        #1获取数据
        book = self.get_object()#这里根据book_id直接从queryset属性里面去取单个对象
        serializer = self.get_serializer(instance = book)
        return Response(serializer.data)
    def put(self,request,pk):
        #1获取前端的数据
        book_dict = request.data
        book = self.get_object()
        #2
        serializer = BookModelSerialzier(data=book_dict,instance=book)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data)
    
    def delete(self,request,pk):
        self.get_object().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
```

### 8.7 get_object()

目的：理解get_object如何根据pk在queryset获取单个对象

### 8.8 和mixin类配合使用

配合二级视图使用，提供了列表视图，和详情视图的基本行为，可以将get,put,delete方法封装起来

作用：提供通用的增删改查功能

| 类名称             | 提供方法 | 功能         |
| ------------------ | -------- | ------------ |
| ListModelMixin     | list     | 查询所有数据 |
| CreateModelMixin   | create   | 创建单个对象 |
| RetrieveModelMixin | retrieve | 获取单个对象 |
| UpdateModelMixin   | update   | 更新单个对象 |
| DestroyModelMixin  | destroy  | 删除单个对象 |

minxin类和GenericAPIView实现列表视图

```python
#Generica配合mixin实现列表视图
class BookListMixinGenericAPIView(GenericAPIView,ListModelMixin,CreateModelMixin):
    #提供公共的属性
    queryset = BookInfo.objects.all()
    serializer_class = BookModelSerialzier
    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)
```

mixin实现详情视图

```python
class BookDetailMixinGenericView(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset = BookInfo.objects.all()
    serializer_class = BookModelSerialzier
    lookup_url_kwarg = "book_id"
    def get(self,request,book_id):
        return self.retrieve(request)
    def put(self,request,book_id):
        return self.update(request)
    def delete(self,request,book_id):
        return self.destroy(request)
```

## 九.三级视图

如果没有大量的自定义行为（都是标准的增删改查）,那么就可以使用通用的三级视图来解决	

其实，三级视图就是将通用视图和mixin封装起来了，不用我们自己再写

常见的三级视图

| 类名称          | 父类                              | 提供方法 | 作用         |
| --------------- | --------------------------------- | -------- | ------------ |
| CreateAPIView   | GenericAPIView,CreateModelMixin   | post     | 创建单个对象 |
| ListAPIView     | GenericAPIView,ListModelMixin     | get      | 查询所有数据 |
| RetrieveAPIView | GenericAPIView,RetrieveModelMixin | get      | 查询单个数据 |
| DetroyAPPIView  | GenericAPIView,DestroyModelMixin  | delete   | 删除单个对象 |
| UpdateAPIView   | GenericAPIView,UpdateModelMixin   | pust     | 更新单个对象 |
| ……              |                                   |          |              |

### 9.1 使用三级视图实现列表，和详情视图

```python
#三级视图实现，列表视图
class BookListThirdAPIView(ListAPIView,CreateAPIView):
    queryset = BookInfo.objects.all()
    serializer_class = BookModelSerialzier
#三级视图实现详情视图
class BookDetailThirdAPIView(RetrieveAPIView,DestroyAPIView,UpdateAPIView):
    queryset = BookInfo.objects.all()
    serializer_class = BookModelSerialzier
    lookup_url_kwarg = "book_id"
```

### 9.2 视图集

将详情视图，和列表视图集合在一起实现。

1.将一组相关的操作，放在一个类里面实现

2.不提供get,post方法，而是list，retrieve

3.可以将标准的请求方法(get,post,put,delete)，和mixin中的方法做映射

| 类名称               | 父类                                             | 作用                                                        |
| -------------------- | ------------------------------------------------ | ----------------------------------------------------------- |
| ViewSet              | APIView,ViewSetMixin                             | 可以做路由映射(ViewSetMixin提供)                            |
| GenericViewSet       | GenericAPIView,ViewSetMixin                      | 可以做路由映射(ViewSetMixin提供),可以使用三个属性，三个方法 |
| ModelViewSet         | GenericAPIView,5个mixin类                        | 所有的增删改查功能，可以使用三个属性，三个方法              |
| ReadOnlyModelViewSet | GenericAPIView,RetrieveModelMixin,ListModelMixin | 获取单个，所有数据，可以使用三个属性，三个方法              |

#### 9.2.1 ViewSet

目的：可以使用viewset实现获取所有，单个数据

```python
class BookViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving Book.
    """
    def list(self, request):
        queryset = BookInfo.objects.all()
        serializer = BookInfoSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = BookInfo.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = BookInfoSerializer(user)
        return Response(serializer.data)
```

在路由里面要做映射

```python
booklist = BookInfoViewSet.as_view({'get': 'list'})
bookdetail = BookInfoViewSet.as_view({'get': 'retrieve'})
```

#### 9.2.2 ReadOnlyModelViewSet实现获取单个和所有

```python
class BooksReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing accounts.
    """
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoModelSerializer
```

路由

```python
BookReadOnlyViewSet.as_view({'get': 'list'})
pk(路由里面要传递),BookReadOnlyViewSet.as_view({'get': 'retrieve'})
```

#### 9.2.2 ModelViewSet实现列表视图，详情视图的所有功能

```python
class BooksModelOnlyViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing accounts.
    """
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoModelSerializer
```

```python
BooksModelViewSet.as_view({'get': 'list','post':'create'})
pk(路由里面要传递),BooksModelViewSet.as_view({'get': 'retrieve','put':'update','delete':'destroy'})
```

#### 9.2.3 视图集额外方法

目的：可以给视图集添加额外的方法

```python
class BookInfoModelViewSet(ModelViewSet):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoModelSerializer

    #获取阅读量大于20的数据，需要自定义
    def bread_book(self,request):
        #1获取指定书籍
        books = BookInfo.objects.filter(bread__gt = 20)
        #2创建序列化器对象
        serialzer = self.get_serializer(instance = books,many =True)
        return Response(serialzer.data)
    
```

在路由里面添加映射关系

```python
path('books/bread/',views.BookInfoModelViewSet.as_view({'get':'bread_book'})),
```

#### 9.2.4 partial

目的：给视图集添加额外方法的时候添加参数，并且局部更新

```python
def update_book(self,request,pk):
    book = self.get_object()
    data = request.data
    print (data)
    serializer = self.get_serializer(instance = book,data = data, partial=True)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data,status=201)

```



## 十. 路由router

目的：可以通过DefaultRouter 和SimpleRouter两个类自动生成路由

#### 10.1 DefaultRouter

```python
from rest_framework.routers import SimpleRouter,DefaultRouter
urlpatterns=[

]

#1 创建路由对象
router = DefaultRouter()
#2 注册视图集
router.register('books',views.BookInfoModelViewSet)
urlpatterns +=router.urls

#3 输出结果
print(urlpatterns)
```

urlpatterns下面的输出

- 列表路由
- 详情路由
- 根路由

```python
[
 <URLPattern '^books/$' [name='bookinfo-list']>, 
 <URLPattern '^books\.(?P<format>[a-z0-9]+)/?$' [name='bookinfo-list']>, #可以使用books.json/返回json格式数据
    
 <URLPattern '^books/(?P<pk>[^/.]+)/$' [name='bookinfo-detail']>, 
 <URLPattern '^books/(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$' [name='bookinfo-detail']>, 
 <URLPattern '^$' [name='api-root']>, 
 <URLPattern '^\.(?P<format>[a-z0-9]+)/?$' [name='api-root']>
]
```

使用drf可以根据前端需要的数据类型，返回对应的格式

#### 10.2 SimpleRouter

忽略了数据格式接口，和根路径接口

```python
urlpatterns=[
]

#1 创建路由对象
router = SimpleRouter()
#2 注册视图集
router.register('books',views.BookInfoModelViewSet)
urlpatterns +=router.urls

#3 输出结果
print(urlpatterns)
```

输出下面

```python
[
 <URLPattern '^books/$' [name='bookinfo-list']>, 
 <URLPattern '^books/(?P<pk>[^/.]+)/$' [name='bookinfo-detail']>
]
```

#### 10.2 自定义方法也在路由生成里面

使用action去装饰

生成路由的规则是路由前缀+方法名，如：books/bread_book

```python
from rest_framework.decorators import action
@action(methods = ['GET'],detail = False)
def bread_book(self,request):
    books = BookInfo.objects.filter(bread__gt = 20)
    serialzer = self.get_serializer(instance = books,many =True)
    return Response(serialzer.data)

@action(methods = ['PUT'],detail = True)          #methods代表要替换的默认方法，detail表示有么有参数过来
def update_book(self,request,pk):
    book = self.get_object()
    data = request.data
    serializer = self.get_serializer(instance = book,data = data, partial=True)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data,status=201)
```

```python
[#装饰bread_book得到
 <URLPattern '^books/$' [name='bookinfo-list']>, 
 <URLPattern '^books/bread_book/$' [name='bookinfo-bread-book']>, 
 <URLPattern '^books/(?P<pk>[^/.]+)/$' [name='bookinfo-detail']>
]
```

```python
[#装饰update_book得到的
 <URLPattern '^books/$' [name='bookinfo-list']>, 
 <URLPattern '^books/bread_book/$' [name='bookinfo-bread-book']>, 
 <URLPattern '^books/(?P<pk>[^/.]+)/$' [name='bookinfo-detail']>,
 <URLPattern '^books/(?P<pk>[^/.]+)/update_book/$' [name='bookinfo-update-book']>
]
```

## 十一. drf认证authentication

详细看官方文档

## 十二. 权限Permissions

## 十三. 限流ThrottlIng