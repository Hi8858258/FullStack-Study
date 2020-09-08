from django.shortcuts import render,HttpResponse

# Create your views here.
def login_view(request):
    return render(request,'cms/login.html')