# Generated by Django 2.2.7 on 2019-12-30 09:13

import accounts.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('License', '0002_auto_20191208_0755'),
        ('Vehicle', '0002_auto_20191209_0801'),
        ('accounts', '0005_auto_20191230_1012'),
    ]

    operations = [
        migrations.CreateModel(
            name='client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(max_length=90)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('address', models.CharField(max_length=90, null=True)),
                ('email', models.EmailField(blank=True, db_index=True, max_length=254, null=True, unique=True, verbose_name='email address')),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('gender', models.IntegerField(blank=True, choices=[(0, 'Female'), (1, 'Male')], null=True)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', accounts.models.UserManager()),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='License',
        ),
        migrations.RemoveField(
            model_name='user',
            name='Vehicle',
        ),
        migrations.RemoveField(
            model_name='user',
            name='bloodClass',
        ),
        migrations.RemoveField(
            model_name='user',
            name='lat',
        ),
        migrations.RemoveField(
            model_name='user',
            name='lon',
        ),
        migrations.RemoveField(
            model_name='user',
            name='status',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_type',
        ),
        migrations.CreateModel(
            name='driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(max_length=90)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('address', models.CharField(max_length=90, null=True)),
                ('email', models.EmailField(blank=True, db_index=True, max_length=254, null=True, unique=True, verbose_name='email address')),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('gender', models.IntegerField(blank=True, choices=[(0, 'Female'), (1, 'Male')], null=True)),
                ('lat', models.FloatField(max_length=20, null=True)),
                ('lon', models.FloatField(max_length=20, null=True)),
                ('status', models.IntegerField(blank=True, choices=[(0, 'ACTIVE'), (1, 'UNACTIVE')], null=True)),
                ('bloodClass', models.CharField(max_length=5, null=True)),
                ('License', models.ForeignKey(blank=True, null=True, on_delete=None, to='License.License')),
                ('Vehicle', models.ForeignKey(blank=True, null=True, on_delete=None, to='Vehicle.Vehicle')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', accounts.models.UserManager()),
            ],
        ),
    ]
