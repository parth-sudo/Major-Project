# Generated by Django 3.2.2 on 2022-05-05 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_auto_20220505_1439'),
    ]

    operations = [
        migrations.AddField(
            model_name='heartpatient',
            name='age',
            field=models.CharField(default=50, max_length=3),
        ),
    ]
