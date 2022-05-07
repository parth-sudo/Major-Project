# Generated by Django 3.2.2 on 2022-05-06 15:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_auto_20220506_1124'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiabetesPatient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('glucose', models.CharField(max_length=3)),
                ('blood_pressuse', models.CharField(max_length=3)),
                ('insulin', models.CharField(max_length=3)),
                ('body_mass_index', models.CharField(max_length=4)),
                ('age', models.CharField(max_length=3)),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.profile')),
            ],
        ),
    ]