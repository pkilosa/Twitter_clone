# Generated by Django 4.1.2 on 2022-12-16 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.PositiveIntegerField(blank=True, default=0, verbose_name='Likes'),
        ),
    ]
