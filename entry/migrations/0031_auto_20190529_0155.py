# Generated by Django 2.2 on 2019-05-29 01:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('entry', '0030_auto_20190528_2101'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='type',
        ),
        migrations.AddField(
            model_name='schedule',
            name='TBA_key',
            field=models.TextField(default='NA', max_length=40),
        ),
        migrations.AddField(
            model_name='schedule',
            name='event',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='entry.Event'),
        ),
        migrations.AlterField(
            model_name='team',
            name='TBA_key',
            field=models.TextField(default='NA', max_length=40),
        ),
    ]