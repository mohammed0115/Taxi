# Generated by Django 2.2.7 on 2019-12-08 05:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('License', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='license',
            old_name='type',
            new_name='License_type',
        ),
    ]
