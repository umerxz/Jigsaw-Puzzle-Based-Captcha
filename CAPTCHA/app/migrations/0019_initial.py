# Generated by Django 4.2.8 on 2024-01-02 19:37

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app', '0018_remove_partition_id_remove_partition_partition_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(max_length=1000001, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Partition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(4)])),
                ('image_partition', models.ImageField(upload_to='')),
                ('partition_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.images')),
            ],
        ),
    ]
