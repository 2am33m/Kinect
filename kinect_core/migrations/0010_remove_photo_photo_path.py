# Generated by Django 4.2.6 on 2024-07-02 15:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kinect_core', '0009_rename_photo_photo_photo_path'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='photo_path',
        ),
    ]
