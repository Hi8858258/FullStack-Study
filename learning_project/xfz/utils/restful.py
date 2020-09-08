from email import message


from django.http import JsonResponse
from django.utils.autoreload import restart_with_reloader

class HttpCode:
    #将code封装起来好调用
    ok = 200
    paramserror = 400
    unauth = 401
    methoderror = 405
    servererror = 500

def result(code=HttpCode.ok,message="",data=None,kwargs=None):
    json_data = {"code":code,"message":message,"data":data}

    if kwargs and isinstance(kwargs,dict) and kwargs.keys():
        #判读那如果kwargs参数中有数据就将其更新到json_data中
        json_data.update(kwargs)

    return JsonResponse(json_data)

#将ok封装起来
#----------------------------------------
def ok():
    return result()

#----------------------------------------

#将错误封装起来
#------------------------------------------
def params_error(message="",data=None):
    return result(code=HttpCode.paramserror,message=message,data=data)

def unauth(message="",data=None):
    return result(code=HttpCode.unauth,message=message,data=data)

def method_error(message="",data=None):
    return result(code=HttpCode.methoderror,message=message,data=data)

def servererror(message="",data=None):
    return result(code=HttpCode.servererror,message=message,data=data)

#------------------------------------------- 

