# Generated by Django 3.2.2 on 2022-05-21 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0008_alter_doctor_full_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='availability',
            field=models.CharField(default='10 A.M-11 A.M', max_length=20),
        ),
    ]