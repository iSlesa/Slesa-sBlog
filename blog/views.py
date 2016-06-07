from django.shortcuts import render, get_object_or_404
from blog.models import Post

def index(request):
    posts = Post.objects.filter(published = True)

    category = request.GET.get("category")
    if category:
        posts = posts.filter(category=category)

    return render(request, 'blog/index.html',{'posts':posts, 'category':category})

def post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post.html',{'post':post})


# Create your views here.
