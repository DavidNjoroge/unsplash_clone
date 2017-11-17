from django.shortcuts import render
from .models import Post,collections,User
# Create your views here.
def index(request):
    posts=Post.get_posts()
    tags=collections.get_collections()
    print(len(tags))
    return render(request,'index.html',{"posts":posts,"tags":tags})
