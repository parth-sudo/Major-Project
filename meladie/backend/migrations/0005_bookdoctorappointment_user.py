# Generated by Django 3.2.2 on 2022-05-17 09:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('backend', '0004_bookdoctorappointment'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookdoctorappointment',
            name='user',
            field=models.ForeignKey(default=7, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]