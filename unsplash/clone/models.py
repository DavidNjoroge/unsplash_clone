from django.db import models
from itertools import chain


# Create your models here.
class collections(models.Model):
    name=models.CharField(max_length=50)

    @classmethod
    def get_collections(cls):
        tags=collections.objects.all()
        # print(len(tags))
        return tags

    def __str__(self):
        return self.name

class User(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50,blank =True)

    def __str__(self):
        return self.first_name
class Post(models.Model):
    image=models.ImageField()
    pub_date=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User)
    collection=models.ManyToManyField(collections)

    @classmethod
    def get_tag_posts(cls,tag_id):
        # post=tag.post_set.all()
        # print(len(post))
        posts=Post.objects.filter(collection=tag_id)

        post_par=Post.chunkIt(posts,3)
        return post_par

    @classmethod
    def get_posts(cls):
        posts=Post.objects.all()
        post_par=Post.chunkIt(posts,3)

        return post_par
    @classmethod
    def get_related(cls,post):
        posts_list=[]
        tags=post.collection.all()
        for tag in tags:
            qwerty=tag.post_set.all()
            posts_list.append(qwerty)
        posts=list(set(chain(*posts_list)))
        post_par=Post.chunkIt(posts,3)

        # print(len(results))
        return post_par


    @classmethod
    def chunkIt(cls,seq, num):
        avg = len(seq) / float(num)
        out = []
        last = 0.0

        while last < len(seq):
            out.append(seq[int(last):int(last + avg)])
            last += avg
        return out[::-1]
