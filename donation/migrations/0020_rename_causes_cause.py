# Generated by Django 4.2.3 on 2023-08-01 19:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('donation', '0019_causes'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Causes',
            new_name='Cause',
        ),
    ]
