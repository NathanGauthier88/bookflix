# Generated by Django 4.1.2 on 2022-10-12 01:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_remove_album_profile_profile_album_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='album',
            new_name='albums',
        ),
    ]
