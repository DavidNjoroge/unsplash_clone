from django.test import TestCase
from .models import collections,Post,User
from django.contrib.auth.models import User

# Create your tests here.
class PostTestClass(TestCase):
    #setup method
    def setup(self):
        self.david = User(username='davy',password='sdfsdf')
        self.david.save()
        self.new_post=Post(user=self.david)