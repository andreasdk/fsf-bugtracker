# Generated by Django 2.2.6 on 2019-10-14 10:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='featurecomment',
            old_name='bug',
            new_name='feature',
        ),
        migrations.RenameField(
            model_name='featurevotes',
            old_name='bug',
            new_name='feature',
        ),
    ]
