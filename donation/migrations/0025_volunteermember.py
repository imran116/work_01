# Generated by Django 4.2.3 on 2023-08-02 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donation', '0024_alter_volunteer_volunteer_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='VolunteerMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='volunteer-member/')),
                ('name', models.CharField(max_length=100)),
                ('about', models.TextField()),
            ],
        ),
    ]
