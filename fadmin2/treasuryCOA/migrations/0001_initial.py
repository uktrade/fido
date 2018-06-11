# Generated by Django 2.0.2 on 2018-06-11 17:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='L1Account',
            fields=[
                ('account_l1_code', models.BigIntegerField(primary_key=True, serialize=False, verbose_name='account l1 code')),
                ('account_l1_long_name', models.CharField(blank=True, max_length=255, verbose_name='account l1 long name')),
                ('account_code', models.CharField(max_length=255, verbose_name='accounts code')),
                ('account_l0_code', models.CharField(max_length=255, verbose_name='account l0 code')),
            ],
            options={
                'verbose_name': 'Treasury Level 1 COA',
            },
        ),
        migrations.CreateModel(
            name='L2Account',
            fields=[
                ('account_l2_code', models.BigIntegerField(primary_key=True, serialize=False, verbose_name='account l2 code')),
                ('account_l2_long_name', models.CharField(blank=True, max_length=255, verbose_name='account l2 long name')),
                ('account_l1_code', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='treasuryCOA.L1Account', verbose_name='account l1 code')),
            ],
            options={
                'verbose_name': 'Treasury Level 2 COA',
            },
        ),
        migrations.CreateModel(
            name='L3Account',
            fields=[
                ('account_l3_code', models.BigIntegerField(primary_key=True, serialize=False, verbose_name='account l3 code')),
                ('account_l3_long_name', models.CharField(blank=True, max_length=255, verbose_name='account l3 long name')),
                ('account_l2Code', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='treasuryCOA.L2Account', verbose_name='account l2 code')),
            ],
            options={
                'verbose_name': 'Treasury Level 3 COA',
            },
        ),
        migrations.CreateModel(
            name='L4Account',
            fields=[
                ('account_l4_code', models.BigIntegerField(primary_key=True, serialize=False, verbose_name='account l4 code')),
                ('account_l4_long_name', models.CharField(blank=True, max_length=255, verbose_name='account l4 long name')),
                ('account_l3_code', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='treasuryCOA.L3Account', verbose_name='account l3 code')),
            ],
            options={
                'verbose_name': 'Treasury Level 4 COA',
            },
        ),
        migrations.CreateModel(
            name='L5Account',
            fields=[
                ('account_l5_code', models.BigIntegerField(primary_key=True, serialize=False, verbose_name='account l5 code')),
                ('account_l5_long_name', models.CharField(blank=True, max_length=255, verbose_name='account l5 long name')),
                ('account_l5Description', models.CharField(blank=True, max_length=2048, verbose_name='account l5 description')),
                ('EconomicBudgetCode', models.CharField(blank=True, max_length=255, verbose_name='economic budget code')),
                ('SectorCode', models.CharField(blank=True, max_length=255, verbose_name='sector code')),
                ('EstimatesColumnCode', models.CharField(choices=[('GROSS', 'GROSS'), ('INCOME', 'INCOME'), ('N/A', 'N/A')], default='N/A', max_length=25, verbose_name='estimates column code')),
                ('UsageCode', models.CharField(blank=True, choices=[('BOTH', 'BOTH'), ('OUTTURN', 'OUTTURN'), ('PLANS', 'PLANS')], default='BOTH', max_length=25, verbose_name='usage code')),
                ('CashIndicatorCode', models.CharField(blank=True, max_length=5, verbose_name='cash indicator code')),
                ('account_l4_code', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='treasuryCOA.L4Account', verbose_name='account l4 code')),
            ],
            options={
                'verbose_name': 'Treasury Level 5 COA',
            },
        ),
    ]