# Generated by Django 2.2 on 2020-03-30 15:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entry', '0005_auto_20200327_0012'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pits',
            name='images',
        ),
    ]
