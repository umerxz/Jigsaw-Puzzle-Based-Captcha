# Generated by Django 4.2.8 on 2023-12-30 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_images_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='img',
            field=models.ImageField(blank=True, max_length=1000000, null=True, upload_to='images/'),
        ),
    ]
