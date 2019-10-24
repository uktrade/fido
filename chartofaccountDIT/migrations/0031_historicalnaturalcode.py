# Generated by Django 2.1.5 on 2019-04-03 12:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0005_remove_financialyear_current_year"),
        ("chartofaccountDIT", "0030_delete_historicalnaturalcode"),
    ]

    operations = [
        migrations.CreateModel(
            name="HistoricalNaturalCode",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("archived", models.DateTimeField(auto_now_add=True)),
                (
                    "natural_account_code_description",
                    models.CharField(max_length=200, verbose_name="NAC Description"),
                ),
                ("used_for_budget", models.BooleanField(default=False)),
                (
                    "natural_account_code",
                    models.IntegerField(verbose_name="PO/Actuals NAC"),
                ),
                (
                    "expenditure_category",
                    models.CharField(max_length=255, verbose_name="Budget Category"),
                ),
                (
                    "NAC_category",
                    models.CharField(max_length=255, verbose_name="Budget Grouping"),
                ),
                (
                    "commercial_category",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="Commercial Category",
                    ),
                ),
                ("account_L5_code", models.BigIntegerField(blank=True, null=True)),
                (
                    "account_L5_description",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "account_L6_budget",
                    models.BigIntegerField(
                        blank=True, null=True, verbose_name="Budget/Forecast NAC"
                    ),
                ),
                (
                    "account_L5_code_upload",
                    models.BigIntegerField(
                        blank=True, null=True, verbose_name="L5 for OSCAR upload"
                    ),
                ),
                (
                    "economic_budget_code",
                    models.CharField(
                        blank=True, max_length=255, verbose_name="Expenditure Type"
                    ),
                ),
                (
                    "financial_year",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="core.FinancialYear",
                    ),
                ),
            ],
            options={
                "verbose_name": "Natural Account Code (NAC)",
                "verbose_name_plural": "Natural Account Codes (NAC)",
                "ordering": ["natural_account_code"],
                "abstract": False,
            },
        )
    ]
