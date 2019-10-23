# Generated by Django 2.2.4 on 2019-10-11 18:11

from django.db import migrations


def create_forecast_expenditure_types(apps, schema_editor):
    ForecastExpenditureType = apps.get_model('forecast', 'ForecastExpenditureType')
    CalForecastExpenditureType = apps.get_model('forecast', 'CalcForecastExpenditureType')
    BudgetType = apps.get_model('chartofaccountDIT', 'BudgetType')

    forecast_capital = ForecastExpenditureType.objects.create(
        forecast_expenditure_type_name='Capital',
        forecast_expenditure_type_description='Capital',
        forecast_expenditure_type_display_order=3
    )
    del_type = BudgetType.objects.get(budget_type_key='DEL')
    ame_type = BudgetType.objects.get(budget_type_key='AME')
    admin_type = BudgetType.objects.get(budget_type_key='ADMIN')
    CalForecastExpenditureType.objects.create(
        nac_economic_budget_code='CAPITAL',
        programme_budget_type=del_type,
        forecast_expenditure_type_fk=forecast_capital
    )
    CalForecastExpenditureType.objects.create(
        nac_economic_budget_code='CAPITAL',
        programme_budget_type=ame_type,
        forecast_expenditure_type_fk=forecast_capital
    )
    CalForecastExpenditureType.objects.create(
        nac_economic_budget_code='CAPITAL',
        programme_budget_type=admin_type,
        forecast_expenditure_type_fk=forecast_capital
    )

    forecast_programme = ForecastExpenditureType.objects.create(
        forecast_expenditure_type_name='Programme',
        forecast_expenditure_type_description='Resource Programme',
        forecast_expenditure_type_display_order=2
    )

    CalForecastExpenditureType.objects.create(
        nac_economic_budget_code='RESOURCE',
        programme_budget_type=del_type,
        forecast_expenditure_type_fk=forecast_programme
    )
    CalForecastExpenditureType.objects.create(
        nac_economic_budget_code='RESOURCE',
        programme_budget_type=ame_type,
        forecast_expenditure_type_fk=forecast_programme
    )

    forecast_admin = ForecastExpenditureType.objects.create(
        forecast_expenditure_type_name='Admin',
        forecast_expenditure_type_description='Resource Admin',
        forecast_expenditure_type_display_order=1
    )

    CalForecastExpenditureType.objects.create(
        nac_economic_budget_code='RESOURCE',
        programme_budget_type=admin_type,
        forecast_expenditure_type_fk=forecast_admin
    )


class Migration(migrations.Migration):
    dependencies = [
        ('forecast', '0022_calcforecastexpendituretype'),
    ]

    operations = [
        migrations.RunPython(create_forecast_expenditure_types),
    ]
