# Generated by Django 2.1.5 on 2019-02-22 12:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0020_abakusgroup_show_badge"),
        ("notifications", "0008_auto_20181011_1734"),
    ]

    operations = [
        migrations.AddField(
            model_name="announcement",
            name="from_group",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="from_group",
                to="users.AbakusGroup",
            ),
        )
    ]
