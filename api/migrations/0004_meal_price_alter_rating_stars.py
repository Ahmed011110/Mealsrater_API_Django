# Generated by Django 4.2.5 on 2023-10-05 09:32

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_meal_description_alter_rating_stars'),
    ]

    operations = [
        migrations.AddField(
            model_name='meal',
            name='price',
            field=models.CharField(default=django.utils.timezone.now, max_length=40),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='rating',
            name='stars',
            field=models.IntegerField(validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator(5)]),
        ),
    ]
