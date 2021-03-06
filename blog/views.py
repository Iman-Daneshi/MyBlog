from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Post, Tag, Review

# Create your views here.


def index_view(request):
    posts = Post.objects.filter(status=1)
    paginator = Paginator(posts, 2)
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)
    context = {
        'page_object': page_object,
    }
    return render(request,'index.html', context)

def single_post(request, id):
    posts = Post.objects.filter(status=1)
    post = get_object_or_404(posts, id=id)
    reviews = Review.objects.filter(post=post.id)
    context = {
        'post': post,
        'reviews': reviews,
        }
    return render(request,'single-post.html', context)
    

