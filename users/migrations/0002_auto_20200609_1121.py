# Generated by Django 2.2 on 2020-06-09 08:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='nio',
            new_name='bio',
        ),
    ]
