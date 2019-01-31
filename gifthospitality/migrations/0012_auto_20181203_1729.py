# Generated by Django 2.1.2 on 2018-12-03 17:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('gifthospitality', '0011_auto_20181203_1723'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='giftandhospitalitycategory',
            options={'ordering': ['sequence_no'], 'verbose_name': 'Gift and Hospitality Category',
                     'verbose_name_plural': 'Gift and Hospitality Categories'},
        ),
        migrations.AlterModelOptions(
            name='giftandhospitalityclassification',
            options={'ordering': ['sequence_no'],
                     'verbose_name': 'Gift and Hospitality Classification',
                     'verbose_name_plural': 'Gift and Hospitality Classifications'},
        ),
        migrations.AlterModelOptions(
            name='giftandhospitalitycompany',
            options={'ordering': ['sequence_no'], 'verbose_name': 'Gift and Hospitality Company',
                     'verbose_name_plural': 'Gift and Hospitality Companies'},
        ),
        migrations.AddField(
            model_name='giftandhospitalitycategory',
            name='sequence_no',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='giftandhospitalityclassification',
            name='sequence_no',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='giftandhospitalitycompany',
            name='sequence_no',
            field=models.IntegerField(null=True),
        ),
    ]