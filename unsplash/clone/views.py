from django.shortcuts import render
from .models import Post,collections,User
from django.http import HttpResponse,Http404
from itertools import chain

# Create your views here.
def index(request):
    posts=Post.get_posts()
    tags=collections.get_collections()
    def chunkIt(seq, num):
        avg = len(seq) / float(num)
        out = []
        last = 0.0

        while last < len(seq):
            out.append(seq[int(last):int(last + avg)])
            last += avg
        return out

    # post_chunks=chunkIt(posts,3)
    # print(len(post_chunks))
    return render(request,'index.html',{"posts":posts,"tags":tags})

def post(request,post_id):
    post=Post.objects.get(id=post_id)
    post_chunks=Post.get_related(post)

    return render(request,'post.html',{"post":post,"posts":post_chunks})

def tag(request,tag_id):
    tag=collections.objects.filter(id=tag_id)
    post_chunks=Post.get_tag_posts(tag_id)

    return render(request,'tag.html',{"tag":tag,"posts":post_chunks})
