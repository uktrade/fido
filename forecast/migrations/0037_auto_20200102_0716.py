# Generated by Django 2.2.4 on 2020-01-02 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forecast', '0036_auto_20191231_1226'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='financialcode',
            options={'permissions': [('can_view_forecasts', 'Can view forecast'), ('can_upload_files', 'Can upload files')]},
        ),
    ]
