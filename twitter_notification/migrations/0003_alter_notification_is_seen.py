# Generated by Django 3.2.7 on 2021-10-03 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter_notification', '0002_alter_notification_is_seen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='is_seen',
            field=models.BooleanField(default=False),
        ),
    ]