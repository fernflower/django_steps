from django.contrib.sitemaps import Sitemap
from about.models import Member


class MemberSitemapXML(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Member.objects.all()

    def location(self, member):
        return "/about/{}".format(member.alias)
