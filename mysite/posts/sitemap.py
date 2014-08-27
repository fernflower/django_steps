from django.contrib.sitemaps import Sitemap
from django.utils import timezone
from posts.models import Post


class PostSitemapXML(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Post.objects.filter(pub_date__lte=timezone.localtime(
            timezone.now())).order_by('-pub_date')

    def lastmod(self, post):
        return post.pub_date

    def location(self, post):
        return "/posts/{}".format(post.id)
