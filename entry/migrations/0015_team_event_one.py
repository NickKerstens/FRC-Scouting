# Generated by Django 2.2 on 2019-05-22 23:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('entry', '0014_auto_20190522_2340'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='event_one',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='entry.Event'),
        ),
    ]
