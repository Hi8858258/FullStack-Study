from django import forms
from ..forms import FormMixin

class LoginForm(forms.Form, FormMixin):
    telephone = forms.CharField(max_length=11)
    #error_message显示的验证错的信息
    password = forms.CharField(max_length=10,min_length=6,error_messages={"max_length":"密码最多不超过10字符","min_length":"密码最少6字符"})
    remember = forms.IntegerField(required=False)
