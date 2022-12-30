from django.shortcuts import render, get_list_or_404
from .models import Blogs, Category, Tag
from pages.models import ServicesModel

# Create your views here.

def blogs(request):
    services = ServicesModel.objects.all()
    blogs = Blogs.objects.all()
    tags = Tag.objects.all()
    category = Category.objects.all()

    context = {
        'blogs' : blogs,
        'category' : category,
        'tags' : tags,
        'services':services
    }
    return render(request, 'blogs/blogs.html', context )

def blog_detail(request, slug):
    blogs = Blogs.objects.all()
    services = ServicesModel.objects.all()
    blog = Blogs.objects.get(slug=slug)
    category = Category.objects.all()
    tags = Tag.objects.all()


    context = {
        'blog' : blog,
        'category' : category,
        'blogs' : blogs,
        'tags' : tags,
        'services': services,
    }
    return render(request, 'blogs/blog_detail.html', context)


def blogs_by_category(request, slug):
    blogs = Blogs.objects.filter(category__slug=slug)
    blog = Blogs.objects.all()
    category = Category.objects.all()
    tags = Tag.objects.all()


    context = {
        'blogs' : blogs,
        'category' : category,
        'category_selected' : slug,
        'tags' : tags,
        'blog'  : blog
    }
    return render(request, 'blogs/blogs.html', context )

def blogs_by_tags(request, slug):
    blogs = Blogs.objects.filter(tag__slug=slug)
    category = Category.objects.all()
    tags = Tag.objects.all()

    context = {
        'blogs' : blogs,
        'tags' : tags,
        'category' : category
    }

    return render(request, 'blogs/blogs.html', context)

def search(request):
    blogs = Blogs.objects.filter(title__contains = request.GET['search'])
    category = Category.objects.all()
    tags = Tag.objects.all()
    
    context = {
        'blogs' : blogs,
        'category' : category,
        'tags' : tags
    }
    if blogs:
       return render(request, 'blogs/blogs.html', context)
    else:
        return render(request, 'blogs/blogs.html', {'error' : 'Aradığınız kriterlere uygun kayıt bulunamadı.'})