# Generated by Django 5.1.1 on 2024-10-15 03:45

import Petstagram.photos.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_alter_photo_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.ImageField(upload_to='media/', validators=[Petstagram.photos.validators.validate_photos]),
        ),
    ]
