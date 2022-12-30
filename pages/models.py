from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


class ServicesModel(models.Model):
    icon = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    seotitle = models.CharField(max_length=65, default=True)
    altbaslik=models.TextField()
    seodescription = models.CharField(max_length=165, default=True)
    description = RichTextUploadingField()
    
    slug = models.SlugField(unique=True, null=True)


    def __str__(self):
        return self.title


class TeklifFormu(models.Model):
    name = models.CharField(max_length=150, verbose_name='Adı Soyadı')
    company = models.CharField(max_length=150, verbose_name='Şirket Adı')
    work = models.CharField(max_length=150, verbose_name='Faaliyet Alanı')
    email = models.CharField(max_length=150, verbose_name='E mail adresi')
    phone = models.CharField(max_length=150, verbose_name='Telefon Numarası')
    message = models.TextField(verbose_name='Mesajı')


    def __str__(self):
        return self.name
    


