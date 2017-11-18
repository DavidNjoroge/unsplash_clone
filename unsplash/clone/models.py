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
    def get_posts(cls):
        posts=Post.objects.all()
        return list(posts)
    @classmethod
    def get_related(cls,post):
        posts_list=[]
        tags=post.collection.all()
        for tag in tags:
            qwerty=tag.post_set.all()
            posts_list.append(qwerty)
        posts=list(set(chain(*posts_list)))
        # print(len(results))
        return posts
