# Generated by Django 3.2.2 on 2022-05-07 14:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0008_heartpatient_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='diabetespatient',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2022, 5, 7, 14, 12, 53, 699067, tzinfo=utc)),
            preserve_default=False,
        ),
    ]