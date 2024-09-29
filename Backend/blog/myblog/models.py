from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Post(models.Model):
    CATEGORY_CHOICES = [
        ('tech', 'Technology'),
        ('life', 'Lifestyle'),
        ('edu', 'Education'),
        ('ent', 'Entertainment'),
    ]
    
    title = models.CharField(max_length=100)
    content = models.TextField()
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default='tech')
    author = models.ForeignKey(User, on_delete = models.CASCADE , default=1)

    def __str__(self):
        return self.title


    
   
    

class Comment(models.Model):
    post = models.ForeignKey(Post , on_delete = models.CASCADE , related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    author = models.ForeignKey(User, on_delete = models.CASCADE , default=1)
    