# Generated by Django 2.0.2 on 2018-09-06 13:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('payroll', '0001_initial'),
        ('costcentre', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='directorate',
            name='director',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='payroll.DITPeople'),
        ),
        migrations.AddField(
            model_name='directorate',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='costcentre.DepartmentalGroup'),
        ),
        migrations.AddField(
            model_name='departmentalgroup',
            name='director_general',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='payroll.DITPeople'),
        ),
        migrations.AddField(
            model_name='costcentre',
            name='business_partner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='business_partner', to='payroll.DITPeople', verbose_name='Finance Business Partner'),
        ),
        migrations.AddField(
            model_name='costcentre',
            name='deputy_director',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='deputy_director', to='payroll.DITPeople'),
        ),
        migrations.AddField(
            model_name='costcentre',
            name='directorate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='costcentre.Directorate'),
        ),
    ]
