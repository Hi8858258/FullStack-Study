from django.urls import path
from . import views

app_name = 'xfzauth'

urlpatterns = [
    path('ll/',views.index,name ="index"),
    path('login/', views.login_view, name = 'login_view')
]