from email import message
from django.shortcuts import render,HttpResponse
from django.contrib.auth import login,logout,authenticate
from django.views.decorators.http import require_POST
from .forms import LoginForm
from django.http import JsonResponse
from utils import restful
# Create your views here.

#因为通过ajax来登入，所以不涉及到跳转到模板页面，只会有post请求

def index(request):
    return HttpResponse('helo')

@require_POST
def login_view(request):
    form = LoginForm(request.POST)
    if form.is_valid():
        telephone = form.cleaned_data.get('telephone')
        password = form.cleaned_data.get('password')
        remember = form.cleaned_data.get('remember')
        user = authenticate(request,username = telephone, password = password)
        if user:
            if user.is_active:
                login(request,user)
                if remember:
                    # 选择了remember，session就会使用默认的时长2星期
                    request.session.set_expiry(None)
                else:
                    #不选择，remember。就会在关闭浏览器的时候就删除
                    request.session.set_expiry(0)
                    #message和data可以为空
                return restful.ok()
            else:
                #用户没有active
                return restful.unauth(message="账号已被冻结")
            #用户验证失败
            return restful.params_error(message="账号或密码错误")
    else:
        #表单验证失败
        errors = form.get_errors()
        return restful.params_error(message=errors)
