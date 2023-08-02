# Generated by Django 4.2.3 on 2023-08-02 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donation', '0027_newscategory_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_1', models.ImageField(upload_to='news/')),
                ('image_2', models.ImageField(upload_to='news/')),
                ('image_3', models.ImageField(upload_to='news/')),
                ('news_title', models.CharField(max_length=250)),
                ('news_description', models.TextField()),
                ('news_quote', models.CharField(max_length=200)),
                ('news_author_name', models.CharField(max_length=100)),
                ('datetime', models.DateTimeField(auto_now=True)),
                ('is_draft', models.BooleanField(default=False)),
                ('category', models.ManyToManyField(to='donation.newscategory')),
                ('tags', models.ManyToManyField(to='donation.tag')),
            ],
        ),
    ]
