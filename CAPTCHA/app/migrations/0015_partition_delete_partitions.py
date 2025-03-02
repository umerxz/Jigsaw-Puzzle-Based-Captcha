# Generated by Django 4.2.8 on 2024-01-02 15:52

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_rename_part_name_partitions_partition_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Partition',
            fields=[
                ('id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='app.images')),
                ('position', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(4)])),
                ('image_partition', models.ImageField(upload_to='')),
                ('partition_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='part_name', to='app.images', to_field='name')),
            ],
        ),
        migrations.DeleteModel(
            name='Partitions',
        ),
    ]
