# Generated by Django 4.2.3 on 2023-08-04 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donation', '0035_adddonationamount_adddonationpaymentmethod'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adddonationamount',
            name='donation_amount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
