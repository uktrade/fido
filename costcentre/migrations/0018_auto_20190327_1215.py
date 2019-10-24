# Generated by Django 2.1.5 on 2019-03-27 12:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("costcentre", "0017_auto_20190325_1655")]

    operations = [
        migrations.RenameField(
            model_name="historiccostcentre", old_name="created", new_name="archived"
        ),
        migrations.AddField(
            model_name="historiccostcentre",
            name="active",
            field=models.BooleanField(default="True"),
        ),
        migrations.AddField(
            model_name="historiccostcentre",
            name="bsce_email",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="costcentre.BSCEEmail",
                verbose_name="BSCE Email",
            ),
        ),
        migrations.AddField(
            model_name="historiccostcentre",
            name="business_partner_fullname",
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name="historiccostcentre",
            name="deputy_director_fullname",
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name="historiccostcentre",
            name="dg_fullname",
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name="historiccostcentre",
            name="director_fullname",
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name="historiccostcentre",
            name="disabled_with_actual",
            field=models.BooleanField(
                default="False", verbose_name="Disabled (Actuals to be cleared)"
            ),
        ),
    ]
