# Generated by Django 3.2.7 on 2021-10-03 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter_notification', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='is_seen',
            field=models.BooleanField(default=True),
        ),
    ]
