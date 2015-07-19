from django.utils import timezone
from django.conf import settings
from django.views import generic
from posts.models import Post
from contacts.models import ContactInfo


# all parameters to be passed to base template are aggregated in this mixin
class GeneralContextMixin(generic.base.ContextMixin):
    def get_context_data(self, **kwargs):
        context = super(GeneralContextMixin, self).get_context_data(**kwargs)
        context['contacts_main'] = ContactInfo.objects.filter(type='main').\
            first()
        context['contacts_friends'] = ContactInfo.objects.filter(type='friends')
        context['vk_api_id'] = settings.VK_API_ID
        return context


class IndexView(generic.ListView, GeneralContextMixin):
    template_name = 'posts/index.html'
    context_object_name = 'last_posts'
    paginate_by = 5

    def get_queryset(self):
        objects = Post.objects
        if self.request.user.is_superuser:
            return objects.order_by('-pub_date')
        return (objects
                .filter(pub_date__lte=timezone.localtime(timezone.now()))
                .filter(is_visible=True).order_by('-pub_date'))


class DetailView(generic.DetailView, GeneralContextMixin):
    model = Post
    template_name = 'posts/detail.html'

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Post.objects.all()
        return (Post.objects
                .filter(pub_date__lte=timezone.localtime(timezone.now()))
                .filter(is_visible=True))


class FavouritePostsView(IndexView):
    model = Post
    template_name = 'posts/favourites.html'

    def get_queryset(self):
        all_favourites = Post.objects.filter(is_favourite=True)
        if self.request.user.is_superuser:
            return all_favourites.order_by('-pub_date')
        return (all_favourites
                .filter(pub_date__lte=timezone.localtime(timezone.now()))
                .filter(is_visible=True)
                .order_by('-pub_date'))
