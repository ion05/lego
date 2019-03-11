# Generated by Django 2.1.7 on 2019-03-11 19:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("events", "0021_auto_20190302_1448")]

    operations = [
        migrations.AddField(
            model_name="event",
            name="youtube_url",
            field=models.URLField(
                default="",
                validators=[
                    django.core.validators.RegexValidator(
                        regex="^(?:https?://)?(?:www[.])?(?:youtube[.]com/watch[?]v=|youtu[.]be/)([^&]{11})"
                    )
                ],
            ),
        )
    ]