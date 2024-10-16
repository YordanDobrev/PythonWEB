# Generated by Django 5.1.1 on 2024-10-12 08:15

import Artonia.products.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_artpainting_created_at_macrame_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artpainting',
            name='description',
            field=models.TextField(validators=[Artonia.products.validators.bad_words]),
        ),
        migrations.AlterField(
            model_name='macrame',
            name='description',
            field=models.TextField(validators=[Artonia.products.validators.bad_words]),
        ),
    ]
