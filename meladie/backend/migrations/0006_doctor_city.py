# Generated by Django 3.2.2 on 2022-05-19 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_bookdoctorappointment_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='city',
            field=models.CharField(default='Delhi', max_length=50),
        ),
    ]
