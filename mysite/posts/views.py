import json

import django.http

from django.core.urlresolvers import reverse
from django.contrib.admin import actions, site
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.utils import timezone
from django.views import generic

from posts import utils
from posts.models import Post


@utils.check_auth
def delete_multiple(request):
    ids = request.POST.getlist('ids[]')
    for post_id in ids:
        post = get_object_or_404(Post, pk=post_id)
        post.delete()
    return django.http.HttpResponseRedirect(reverse('admin:index'))


@utils.check_sadmin
def destroy(request):
    if request.GET.get('no_confirm'):
        Post.objects.all().delete()
    else:
        # FIXME not an optimal way to delete one-by-one, but helps to ease the
        # pain and reuse existing admin method
        # FIXME an easier way to get modeladmin?
        modeladmin = site._registry[Post]
        all_posts = Post.objects.all()
        response = actions.delete_selected(modeladmin, request, all_posts)
        if response:
            # show confirmation
            return response
    return django.http.HttpResponseRedirect(reverse('admin:index'))


def about_author(request):
    return render_to_response(
        'posts/about_clean.html', context_instance=RequestContext(request))


@utils.check_auth
def update(request, pk):
    data = request.body.decode('utf-8')
    json_data = json.loads(data)
    is_visible = json_data.get('is_visible')
    is_favourite = json_data.get('is_favourite')
    post = get_object_or_404(Post, pk=pk)
    if is_visible is not None:
        post.is_visible = is_visible
    if is_favourite is not None:
        post.is_favourite = is_favourite
    post.save()
    return django.http.HttpResponse()


@utils.check_auth
def preview(request):
    data = request.body.decode('utf-8')
    json_data = json.loads(data)
    posts = [get_object_or_404(Post, pk=post_id)
             for post_id in json_data["visible"]]
    return render_to_response('posts/index_clean.html', {"last_posts": posts},
                              context_instance=RequestContext(request))


class IndexView(generic.ListView):
    template_name = 'posts/index_clean.html'
    context_object_name = 'last_posts'
    paginate_by = 5

    def get_queryset(self):
        objects = Post.objects
        as_user = self.request.GET.get('as_user', False)
        if self.request.user.is_staff and not as_user:
            return objects.order_by('-pub_date')
        return (objects
                .filter(pub_date__lte=timezone.localtime(timezone.now()))
                .filter(is_visible=True).order_by('-pub_date'))


class DetailView(generic.DetailView):
    model = Post
    template_name = 'posts/detail_clean.html'

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Post.objects.all()
        return (Post.objects
                .filter(pub_date__lte=timezone.localtime(timezone.now()))
                .filter(is_visible=True))
