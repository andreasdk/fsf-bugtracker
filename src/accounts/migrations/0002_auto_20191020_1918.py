# Generated by Django 2.2.6 on 2019-10-20 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to='profile_pics'),
        ),
    ]
