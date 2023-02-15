# Generated by Django 3.0.8 on 2021-06-23 18:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp1', '0007_auto_20210620_1536'),
    ]

    operations = [
        migrations.CreateModel(
            name='cust',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('surname', models.CharField(max_length=250)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('password', models.CharField(max_length=250, validators=[django.core.validators.MinLengthValidator(8)])),
            ],
            options={
                'verbose_name': 'клиент',
                'verbose_name_plural': 'клиенты',
            },
        ),
    ]
