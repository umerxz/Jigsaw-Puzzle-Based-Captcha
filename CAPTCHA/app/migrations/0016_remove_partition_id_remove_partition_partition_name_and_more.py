# Generated by Django 4.2.8 on 2024-01-02 16:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_partition_delete_partitions'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='partition',
            name='id',
        ),
        migrations.RemoveField(
            model_name='partition',
            name='partition_name',
        ),
        migrations.DeleteModel(
            name='Images',
        ),
        migrations.DeleteModel(
            name='Partition',
        ),
    ]