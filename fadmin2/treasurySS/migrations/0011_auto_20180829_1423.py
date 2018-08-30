# Generated by Django 2.0.2 on 2018-08-29 14:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('treasurySS', '0010_auto_20180829_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subsegment',
            name='control_budget_detail_code',
            field=models.CharField(choices=[('AME', (('DEPT AME', 'DEPT AME'), ('NON-DEPT AME', 'NON-DEPT AME'))),
                                            ('DEL', (('DEL ADMIN', 'DEL ADMIN'), ('DEL PROG', 'DEL PROG'))),
                                            ('NON-BUDGET', 'NON-BUDGET')], default='NON-BUDGET', max_length=50,
                                   verbose_name='control budget detail code'),
        ),
    ]
