# Generated by Django 2.2.7 on 2019-12-09 06:04

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APIKEY', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apikey',
            name='User',
            field=models.ForeignKey(on_delete=None, to=settings.AUTH_USER_MODEL),
        ),
    ]