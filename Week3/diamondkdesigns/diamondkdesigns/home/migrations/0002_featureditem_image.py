# Generated by Django 5.0.1 on 2024-02-05 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='featureditem',
            name='image',
            field=models.ImageField(default='featured_items/DiamondK.jpg', upload_to='featured_items'),
        ),
    ]
