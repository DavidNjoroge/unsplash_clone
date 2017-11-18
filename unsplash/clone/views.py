from django.shortcuts import render
from .models import Post,collections,User
from django.http import HttpResponse,Http404
from itertools import chain

# Create your views here.
def index(request):
    posts=Post.get_posts()
    tags=collections.get_collections()
    print(len(tags))
    return render(request,'index.html',{"posts":posts,"tags":tags})
def post(request,post_id):

    post=Post.objects.get(id=post_id)
    related_posts=Post.get_related(post)
    return render(request,'post.html',{"post":post,"posts":related_posts})
