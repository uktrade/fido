# Generated by Django 2.2.13 on 2020-11-23 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chartofaccountDIT', '0008_auto_20200925_1502'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='archivedexpenditurecategory',
            options={'ordering': ['financial_year', 'expenditurecategory_display_order'], 'verbose_name': 'Archived Budget Category', 'verbose_name_plural': 'Archived Budget Categories'},
        ),
        migrations.AlterModelOptions(
            name='expenditurecategory',
            options={'ordering': ['expenditurecategory_display_order'], 'verbose_name': 'Budget Category', 'verbose_name_plural': 'Budget Categories'},
        ),
        migrations.AddField(
            model_name='archivedexpenditurecategory',
            name='expenditurecategory_display_order',
            field=models.IntegerField(blank=True, default=99, null=True),
        ),
        migrations.AddField(
            model_name='expenditurecategory',
            name='expenditurecategory_display_order',
            field=models.IntegerField(blank=True, default=99, null=True),
        ),
        migrations.AddField(
            model_name='simplehistoryarchivedexpenditurecategory',
            name='expenditurecategory_display_order',
            field=models.IntegerField(blank=True, default=99, null=True),
        ),
        migrations.AddField(
            model_name='simplehistoryexpenditurecategory',
            name='expenditurecategory_display_order',
            field=models.IntegerField(blank=True, default=99, null=True),
        ),
    ]