from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    post_list = Post.objects.filter(published = True)
    paginator = Paginator(post_list, 4)
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)

    category = request.GET.get("category")
    if category:
        posts = posts.filter(category=category)

    return render(request, 'blog/index.html',{'posts':posts, 'category':category})

def post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post.html',{'post':post})


# Create your views here.
