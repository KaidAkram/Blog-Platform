from django.shortcuts import render  , get_object_or_404 , redirect
from .models import Post , Comment
from .forms import CommentForm , PostForm ,RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate , logout
from django.contrib.auth.models import User




def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    
    return render(request, 'registration/register.html', {'form': form})


def login_view(request):
    error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(f"Username: {username}, Password: {password}")  # For debugging
        password_exists = User.objects.filter(password = password).first()  
        print (f"Password exists: {password_exists}")
        user = authenticate(request , username = username , password = password)
        print(f"User: {user}")
        if user is not None:
            login(request , user)
            return redirect('home')
        else:
            error = 'wrong username or password'
    return render(request , 'registration/login.html' , {'error' : error})


def logout_view(request):
    
    if request.method == 'POST': 
        logout(request)
        return redirect('login')
    else:
        return render(request , 'registration/logout.html')


def home_view(request):
    posts = Post.objects.all()
    return render (request ,'blog/home.html',{'posts': posts})



def post_detail(request , post_id):
    post = get_object_or_404(Post , id = post_id)
    comments = Comment.objects.filter(post = post)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail' , post_id = post_id)
    else:
        form = CommentForm()

    return render(request , 'blog/post_detail.html' , {'post': post , 'comments': comments , 'form': form})


@login_required
def create_post(request):
    if request.method== 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit = False)
            post.author = request.user
            post.save()
            return redirect('post_detail' , post_id = post.id)
    else:
        form = PostForm()

    return render(request , 'blog/create_post.html' , {'form': form})


def my_posts(request):
    posts = Post.objects.filter(author = request.user)
    return render(request , 'blog/my_posts.html' , {'posts': posts})