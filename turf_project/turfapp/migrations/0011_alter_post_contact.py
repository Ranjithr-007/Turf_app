# Generated by Django 4.0.3 on 2022-03-30 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turfapp', '0010_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='contact',
            field=models.CharField(default='', max_length=100),
        ),
    ]
