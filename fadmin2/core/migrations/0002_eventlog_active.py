# Generated by Django 2.0.2 on 2018-08-29 07:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventlog',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
