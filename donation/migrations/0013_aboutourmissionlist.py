# Generated by Django 4.2.3 on 2023-08-01 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donation', '0012_remove_about_start_about_total_donations_unit'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutOurMissionList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mission_name', models.CharField(max_length=50)),
            ],
        ),
    ]