# Generated by Django 4.2 on 2023-05-09 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0007_recipe_image_favorite_recipe_favored_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ImageField(blank=True, upload_to='upload_to'),
        ),
    ]