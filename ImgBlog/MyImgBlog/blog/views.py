from django.shortcuts import render
from .models import Post
from .forms import PostForm

def post_list(request):
    posts=Post.objects.all()
    return render(request,'post_list.html', {'posts':posts})

