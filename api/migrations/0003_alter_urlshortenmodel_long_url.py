# Generated by Django 4.0.5 on 2022-06-18 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_urlshortenmodel_short_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urlshortenmodel',
            name='long_url',
            field=models.CharField(max_length=500),
        ),
    ]