# Generated by Django 4.2.5 on 2023-10-05 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_meal_price_alter_rating_stars'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='stars',
            field=models.CharField(max_length=50),
        ),
    ]
