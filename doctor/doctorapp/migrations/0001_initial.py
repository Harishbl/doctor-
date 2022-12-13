# Generated by Django 4.0.5 on 2022-12-13 06:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('specialization', models.CharField(max_length=100)),
                ('qualification', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('birth_year', models.DateField(max_length=10)),
                ('gender', models.CharField(max_length=50)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctorapp.doctor')),
            ],
        ),
    ]
