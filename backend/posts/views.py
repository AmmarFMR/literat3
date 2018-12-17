from django.shortcuts import render
from .models import Posts
from django.contrib.auth.models import User
# from django.http import HttpResponse

# Create your views here.

def index(request):
    # return HttpResponse('Hello from Posts!')
    posts = Posts.objects.all()[:10:-1]
    context = {
        'title': 'Latest Posts',
        'posts': posts
    }
    return render(request, 'posts/posts.html', context)

def details(request, id):
    post = Posts.objects.get(id=id)
    context = {'post': post}
    return render(request, 'posts/details.html', context)

def user_details(request, id):
    user = User.objects.filter(id=id).first()
    posts = user.posts_set.all()[:10]
    context = {
        'title': f'Posts by {user.username}',
        'posts': posts
    }
    return render(request, 'posts/user_details.html', context)
