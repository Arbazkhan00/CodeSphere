from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.
def index(request):
    posts= Post.objects.all()
    return render(request, 'index.html',{'posts':posts})
def post(request,id):
    post=Post.objects.get(id=id)
    return render(request,'post.html',{'posts':post})