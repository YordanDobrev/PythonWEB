# Generated by Django 5.1.3 on 2024-11-21 06:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workshops', '0003_alter_workshop_options_alter_workshop_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workshopregistration',
            name='attended',
        ),
        migrations.RemoveField(
            model_name='workshopregistration',
            name='payment_status',
        ),
    ]