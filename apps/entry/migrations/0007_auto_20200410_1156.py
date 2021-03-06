# Generated by Django 2.2 on 2020-04-10 15:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entry', '0006_remove_pits_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='climb',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='match',
            name='wheel_score',
            field=models.SmallIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)]),
        ),
    ]
