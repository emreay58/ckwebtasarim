# Generated by Django 4.0.4 on 2022-11-19 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0006_blogs_seodescription_blogs_seotitle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='seodescription',
            field=models.CharField(default=True, max_length=165),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='seotitle',
            field=models.CharField(default=True, max_length=65),
        ),
    ]
