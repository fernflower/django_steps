from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from posts.models import Post


def index(request):
    last_10 = Post.objects.order_by('-pub_date')[:10]
    context = {'last_posts': last_10}
    return render(request, 'posts/index.html', context)

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'posts/detail.html', {'post': post})

# Create your views here.
