# Generated by Django 5.1.3 on 2024-11-30 14:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('art_painting', '0002_artpainting_is_public_artpainting_likes_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artpainting',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='artpainting',
            name='views_count',
        ),
    ]