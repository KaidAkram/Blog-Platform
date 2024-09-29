from django import forms
from django.contrib.auth.models import User
from .models import Post , Comment
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
            'username',
            'password1',
            'password2'
        ]
      
class CommentForm(forms.ModelForm):
    class Meta :
        model = Comment
        fields = ['content']
        


class PostForm(forms.ModelForm):
   
    class Meta : 
        model=Post
        fields = ['title' , 'content' , 'category']