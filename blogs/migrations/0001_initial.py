# Generated by Django 4.0.4 on 2022-04-16 08:58

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('slug', models.SlugField(blank=True, editable=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('slug', models.SlugField(blank=True, editable=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='blogs', verbose_name='Resim 1')),
                ('title', models.CharField(max_length=100, verbose_name='Başlık')),
                ('descriptions', models.TextField(verbose_name='Blog Ana Sayfa Açıklama')),
                ('descriptions1', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Blog Detayı Açıklama')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Tarih')),
                ('slug', models.SlugField(blank=True, editable=False, unique=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Yazar')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogs.category', verbose_name='Kategori')),
                ('tag', models.ManyToManyField(to='blogs.tag')),
            ],
        ),
    ]