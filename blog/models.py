from turtle import title
from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models
from django.db import timezone

class Post(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name="blog_post")
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True,null=True)
    
    
    def publish(self):
        self.published_date