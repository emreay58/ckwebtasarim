from django.contrib.sitemaps import Sitemap
from blogs.models import Blogs, Category, Tag

class BlogViewsSitemap(Sitemap):

    def items(self):
        return Blogs.objects.all()

class TagViewsSitamp(Sitemap):

    def items(self):
        return Tag.objects.all()

class CategoryViewsSitamp(Sitemap):

    def items(self):
        return Category.objects.all()

    