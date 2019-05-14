# Generated by Django 2.2 on 2019-05-14 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chartofaccountDIT', '0036_auto_20190410_0748'),
    ]

    operations = [
        migrations.CreateModel(
            name='OperatingDeliveryCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=False)),
                ('operating_delivery_description', models.CharField(max_length=255, unique=True, verbose_name='Operating Delivery Plan Category')),
            ],
            options={
                'verbose_name': 'Operating Delivery Plan Category',
                'verbose_name_plural': 'Operating Delivery Plan Categories',
                'ordering': ['operating_delivery_description'],
            },
        ),
        migrations.AddField(
            model_name='expenditurecategory',
            name='op_del_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='chartofaccountDIT.OperatingDeliveryCategory', verbose_name='Operating Delivery Plan'),
        ),
    ]
