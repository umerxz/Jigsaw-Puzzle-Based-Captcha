# Generated by Django 4.2.8 on 2024-01-02 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_alter_images_img_alter_partition_image_partition_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partition',
            name='image_partition',
            field=models.ImageField(blank=True, max_length=100000, null=True, upload_to=''),
        ),
    ]
