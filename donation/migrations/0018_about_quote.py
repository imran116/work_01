# Generated by Django 4.2.3 on 2023-08-01 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donation', '0017_rename_id_or_hef_menu_id_or_href_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='quote',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
