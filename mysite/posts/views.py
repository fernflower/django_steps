from django.utils import timezone
from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.views import generic
from posts.models import Post


class IndexView(generic.ListView):
    template_name = 'posts/index.html'
    context_object_name = 'last_posts'
    paginate_by = 5

    def get_queryset(self):
        objects = Post.objects
        if self.request.user.is_superuser:
            return objects.order_by('-pub_date')
        return objects.filter(pub_date__lte=timezone.now()).\
            order_by('-pub_date')


class DetailView(generic.DetailView):
    model = Post
    template_name = 'posts/detail.html'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context['vk_api_id'] = settings.VK_API_ID
        return context

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Post.objects.all()
        return Post.objects.filter(pub_date__lte=timezone.now())
