# Generated by Django 4.0.4 on 2022-10-10 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_servicesmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicesmodel',
            name='icon',
            field=models.CharField(max_length=50),
        ),
    ]
