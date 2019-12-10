# Generated by Django 2.2.4 on 2019-12-09 16:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_delete_admininfo'),
        ('forecast', '0037_auto_20191209_1155'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='monthlyfigure',
            unique_together={('financial_code', 'financial_year', 'financial_period')},
        ),
        migrations.RemoveField(
            model_name='monthlyfigure',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='monthlyfigure',
            name='version',
        ),
        migrations.CreateModel(
            name='MonthlyFigureAmount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=False)),
                ('amount', models.BigIntegerField(default=0)),
                ('version', models.IntegerField(default=1)),
                ('monthly_figure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='monthly_figure_amounts', to='forecast.MonthlyFigure')),
            ],
            options={
                'unique_together': {('monthly_figure', 'version')},
            },
        ),
    ]
