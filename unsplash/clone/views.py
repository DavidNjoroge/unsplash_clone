from django.shortcuts import render
from .models import Post,collections,User
from django.http import HttpResponse,Http404
from itertools import chain
# result = list(chain(*docs))

# Create your views here.
def index(request):
    posts=Post.get_posts()
    tags=collections.get_collections()
    print(len(tags))
    return render(request,'index.html',{"posts":posts,"tags":tags})
def post(request,post_id):
    # try:

    post=Post.objects.get(id=post_id)
    posts_list=[]
    tags=post.collection.all()
    for tag in tags:
        # other_posts=collections.objects.filter(collection=1)
        qwerty=tag.post_set.all()
        posts_list.append(qwerty)
    results=list(chain(*posts_list))
    print(len(results))
        # posts_list=posts_list+qwerty
        # print(len(other_posts))
    # other_posts=Post.objects.get(collection=post.collection).distinct()
    # print(len(posts_list))
    # except DoesNotExist:
    #     raise Http404()
    return render(request,'post.html',{"post":post,"posts":results})
