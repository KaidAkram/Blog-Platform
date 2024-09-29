from django.urls import path 
from django.contrib.auth import views as auth_views
from . import views

urlpatterns =[
    path('register/', views.register_view, name='register'),
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.home_view, name='home'),
    path('<int:post_id>/' , views.post_detail , name='post_detail'),
    path('create_post/' , views.create_post , name='create_post'),
    path('my_posts/' , views.my_posts , name='my_posts')
]