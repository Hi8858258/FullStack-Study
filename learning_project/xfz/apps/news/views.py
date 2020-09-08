from django.shortcuts import render,HttpResponse
from django.template.context_processors import request

# Create your views here.
def index(request):
    return render(request,'news/index.html')

def news_detail(request,news_id):
    return HttpResponse(news_id)

def search(request):
    pass