from django.urls import path
from . import views

urlpatterns = [
    path('', views.blogs, name='blogs'),
    path('kategori/<slug:slug>/', views.blogs_by_category, name='blogs_by_category'),
    path('etiket/<slug:slug>/', views.blogs_by_tags, name='blogs_by_tags'),
    path('<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('ara/', views.search, name="search"),
]
