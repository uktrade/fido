# Generated by Django 2.2 on 2019-06-21 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("treasurySS", "0095_auto_20190621_1630")]

    operations = [
        migrations.AlterField(
            model_name="subsegment",
            name="control_budget_detail_code",
            field=models.CharField(
                choices=[
                    ("NON-BUDGET", "NON-BUDGET"),
                    ("DEL", (("DEL ADMIN", "DEL ADMIN"), ("DEL PROG", "DEL PROG"))),
                    (
                        "AME",
                        (("DEPT AME", "DEPT AME"), ("NON-DEPT AME", "NON-DEPT AME")),
                    ),
                ],
                default="NON-BUDGET",
                max_length=50,
                verbose_name="control budget detail code",
            ),
        )
    ]
