# Generated by Django 2.1.5 on 2019-04-03 09:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("chartofaccountDIT", "0024_historicalfcomapping")]

    operations = [
        migrations.RemoveField(
            model_name="historicalfcomapping", name="financial_year"
        ),
        migrations.DeleteModel(name="HistoricalFCOMapping"),
    ]
