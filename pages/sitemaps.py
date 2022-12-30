from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse


class StaticViewsSitemap(Sitemap):

    def items(self):
        return ['index', 'about', 'contact', 'pricing', 'referans','teklif',]

    def location(self,item):
        return reverse(item)