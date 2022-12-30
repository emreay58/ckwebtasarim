from django.contrib import admin
from .models import Blogs, Category, Tag

# Register your models here.
@admin.register(Blogs)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title', 'description',)
    prepopulated_fields={'slug':('title',)}

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    prepopulated_fields={'slug':('name',)}

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    prepopulated_fields={'slug':('name',)}
