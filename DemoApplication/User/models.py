from django.db import models
import datetime
# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=50, default = None)
    last_name = models.CharField(max_length=50, default = None)
    email = models.EmailField(max_length=254, default = None)
    password = models.CharField(max_length=20, blank = False)
    username = models.CharField(max_length=50, blank = False)

    def __str__(self):
        return self.username
    

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(default = 'Empty post')
    created_at = models.DateField(auto_now=False, auto_now_add=True)
    updated_at = models.DateField(auto_now=True, auto_now_add=False)


