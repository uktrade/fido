# Generated by Django 2.2 on 2019-07-03 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('costcentre', '0028_auto_20190702_0726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bsceemail',
            name='bsce_email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='BSCE email'),
        ),
    ]
