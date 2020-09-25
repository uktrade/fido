# Generated by Django 2.2.13 on 2020-09-24 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chartofaccountDIT', '0006_auto_20200916_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archivedanalysis1',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='archivedanalysis2',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='archivedcommercialcategory',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='archivedexpenditurecategory',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='archivedfcomapping',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='archivedinterentity',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='archivednaturalcode',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='archivedprogrammecode',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='archivedprojectcode',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='simplehistoryarchivedanalysis1',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='simplehistoryarchivedanalysis2',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='simplehistoryarchivedcommercialcategory',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='simplehistoryarchivedexpenditurecategory',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='simplehistoryarchivedfcomapping',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='simplehistoryarchivedinterentity',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='simplehistoryarchivednaturalcode',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='simplehistoryarchivedprogrammecode',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='simplehistoryarchivedprojectcode',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
