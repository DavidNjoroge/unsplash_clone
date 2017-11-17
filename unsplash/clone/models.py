from django.db import models

# Create your models here.
class collections(models.Model):
    name=models.CharField(max_length=50)

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
        return posts
