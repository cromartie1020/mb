from django.shortcuts import render
from . models import Post
from django.contrib.auth.models import User

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post/home.html',{'posts':posts})

def post_detail(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'post/post_detail.html',{'post':post})

    