# Generated by Django 3.0.8 on 2021-06-20 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp1', '0004_auto_20210620_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='descp',
            field=models.TextField(blank=True, verbose_name='полное_описание'),
        ),
    ]