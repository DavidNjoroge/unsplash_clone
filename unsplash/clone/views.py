from django.shortcuts import render
from .models import Post,collections,User
from django.http import HttpResponse,Http404
from itertools import chain

# Create your views here.
def index(request):
    posts=Post.get_posts()
    tags=collections.get_collections()

    return render(request,'index.html',{"posts":posts,"tags":tags})

def post(request,post_id):
    post=Post.objects.get(id=post_id)
    post_chunks=Post.get_related(post)

    return render(request,'post.html',{"post":post,"posts":post_chunks})

def tag(request,tag_id):
    tag=collections.objects.filter(id=tag_id)
    post_chunks=Post.get_tag_posts(tag_id)

    return render(request,'tag.html',{"tag":tag,"posts":post_chunks})


def search(request):
    if 'search' in request.GET and not request.GET['search']==None:
        search_term=request.GET['search']
        print(search_term)
        posts=Post.search_by_tag(search_term)

    return render (request,'search.html',{'name':search_term,'posts':posts})
