# Generated by Django 4.2.5 on 2023-10-05 07:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meal',
            name='price',
        ),
    ]