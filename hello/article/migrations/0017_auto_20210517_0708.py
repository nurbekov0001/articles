# Generated by Django 3.1.6 on 2021-05-17 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0016_auto_20210412_1456'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='like_article',
            field=models.IntegerField(blank=True, max_length=20000, null=True, verbose_name='счётчик лайков'),
        ),
        migrations.AddField(
            model_name='comment',
            name='like_coment',
            field=models.IntegerField(blank=True, max_length=20000, null=True, verbose_name='счётчик лайков'),
        ),
    ]
