# Generated by Django 3.1.6 on 2021-05-17 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0017_auto_20210517_0708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='like_article',
            field=models.IntegerField(blank=True, max_length=2000, null=True, verbose_name='счётчик лайков'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='like_coment',
            field=models.IntegerField(blank=True, max_length=2000, null=True, verbose_name='счётчик лайков'),
        ),
    ]
