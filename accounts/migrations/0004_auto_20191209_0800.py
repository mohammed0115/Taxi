# Generated by Django 2.2.7 on 2019-12-09 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='License',
            field=models.ForeignKey(blank=True, null=True, on_delete=None, to='License.License'),
        ),
        migrations.AlterField(
            model_name='user',
            name='Vehicle',
            field=models.ForeignKey(blank=True, null=True, on_delete=None, to='Vehicle.Vehicle'),
        ),
    ]
