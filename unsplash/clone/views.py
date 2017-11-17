from django.shortcuts import render
from .models import Post,collections,User
# Create your views here.
def index(request):
    posts=Post.get_posts()
    print(len(posts))
    return render(request,'index.html')
