# Generated by Django 2.2.13 on 2020-08-27 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_data_20200810'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicaluser',
            name='sso_user_id',
            field=models.CharField(db_index=True, default='2020-08-27 11:10:19.594376', max_length=36, verbose_name='SSO user id'),
        ),
    ]
