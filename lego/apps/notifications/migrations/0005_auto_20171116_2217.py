# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-16 22:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("notifications", "0004_auto_20171021_1758")]

    operations = [
        migrations.AlterField(
            model_name="notificationsetting",
            name="notification_type",
            field=models.CharField(
                choices=[
                    ("weekly_mail", "weekly_mail"),
                    ("event_bump", "event_bump"),
                    ("event_admin_registration", "event_admin_registration"),
                    ("event_admin_unregistration", "event_admin_unregistration"),
                    ("event_payment_overdue", "event_payment_overdue"),
                    ("event_payment_overdue_creator", "event_payment_overdue_creator"),
                    ("meeting_invite", "meeting_invite"),
                    ("penalty_creation", "penalty_creation"),
                    ("restricted_mail_sent", "restricted_mail_sent"),
                    ("company_interest_created", "company_interest_created"),
                    ("comment", "comment"),
                    ("comment_reply", "comment_reply"),
                    ("announcement", "announcement"),
                ],
                max_length=64,
            ),
        )
    ]
