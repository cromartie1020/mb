from django.shortcuts import render,reverse,redirect
from . models import Post
from django.contrib.auth.models import User
from .forms import PostForm

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post/home.html',{'posts':posts})

def post_detail(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'post/post_detail.html',{'post':post})

def post_form(request):
    if request.method==('POST' or None):
        form= PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm()
    context= {
        'form':form
    }

    return render(request, 'post/post_new.html', context)
    
def post_edit(request, id):
    post= Post.objects.get(id=id)
   
    form = PostForm(request.POST or None, instance = post)
    if form.is_valid():    
        post=form.save(commit=False)
        post.save()
        return redirect('home')

    

    context = {
        'form':form,
        'post':post
    }  
   
    return render(request, 'post/post_edit.html', context)    

def post_delete(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect('home')