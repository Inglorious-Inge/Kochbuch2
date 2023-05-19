# Generated by Django 4.2 on 2023-05-16 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0012_alter_search_preparation_time_in_minutes_max_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='level',
            field=models.CharField(choices=[('easy', 'leicht'), ('medium', 'mittel'), ('hard', 'schwer')], default=0, max_length=6),
            preserve_default=False,
        ),
    ]