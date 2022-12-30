
from audioop import reverse
from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth import get_user_model
from django.urls import reverse


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=50, unique=True, null=True)

    def __str__ (self):
        return self.name
    
    def get_absolute_url(self):
        return f'/blogs/kategori/{self.slug}/'
    

class Tag(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=50, unique=True, null=True)

    def __str__ (self):
        return self.name

    def get_absolute_url(self):
        return f'/blogs/etiket/{self.slug}/'
    

class Blogs(models.Model):
    image = models.ImageField(upload_to='blogs', verbose_name='Resim 1')
    title = models.CharField(max_length=100, verbose_name='Başlık')
    seotitle = models.CharField(max_length=65, default=True)
    descriptions = models.TextField(verbose_name='Blog Ana Sayfa Açıklama')
    seodescription = models.CharField(max_length=165, default=True)
    descriptions1 = RichTextUploadingField(verbose_name='Blog Detayı Açıklama')
    date = models.DateField(auto_now_add=True, verbose_name='Tarih')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='Yazar')
    category = models.ManyToManyField(Category, verbose_name='Kategori Seçin')
    tag = models.ManyToManyField(Tag, verbose_name='Etiket seçin')
    slug = models.SlugField(max_length=50, unique=True, null=True)


    def __str__(self):
        return self.title

    def get_user_model(self):
        return reverse('blog_detail', args=[str(self.id)])
    
    def get_absolute_url(self):
        return f'/blogs/{self.slug}/'
     

