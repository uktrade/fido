# Generated by Django 2.2 on 2019-06-18 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('costcentre', '0023_auto_20190514_1432'),
    ]

    operations = [
        migrations.AddField(
            model_name='costcentre',
            name='used_for_travel',
            field=models.BooleanField(default='False', verbose_name='Used for Travel'),
        ),
    ]