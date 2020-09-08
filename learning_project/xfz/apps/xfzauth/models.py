from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin,BaseUserManager, UserManager,User
from shortuuidfield import ShortUUIDField
from django.db import models

class UserManager(BaseUserManager):
    def __create_user(self, telephone, username, password, **kwargs):
        if not telephone:
            raise ValueError('请输入手机号')
        if not username:
            raise ValueError('请输入用户名')
        if not password:
            raise ValueError('请输入密码')
        
        user = self.model(telephone=telephone,username=username,**kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, telephone, username, password, **kwargs):
        kwargs['is_superuser'] = False
        return self.__create_user(telephone, username, password, **kwargs)

    def create_superuser(self, telephone, username, password, **kwargs):
        kwargs['is_superuser'] = True
        return self.__create_user(telephone, username, password, **kwargs)

# Create your models here.
class User(AbstractBaseUser,PermissionsMixin):
    #一般公司开发不会使用默认的自增长主键，而是使用uuid
    #但是uuid比较长，所以我们使用shortuuid。这就需要使用第三方包shortuuid
    uid = ShortUUIDField( primary_key = True)
    telephone = models.CharField(max_length=11,unique=True)
    # password = models.CharField(max_length=200) 不用这个password，因为基类中有了，不用重写
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    data_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'telephone'  #默认使用username作为唯一验证，但国内使用telphone
    REQUIRED_FIELDS = ['username'] #当使用cmd创建用户的时候，会提示输入的信息，username_field的也会提示
    EMAIL_FIELD = 'email'

    objects = UserManager()

    def get_full_name(self):
        return self.username
    
    def get_short_name(self):
        return self.username
