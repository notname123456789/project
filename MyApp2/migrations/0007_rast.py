# Generated by Django 3.0.8 on 2022-05-02 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp2', '0006_auto_20220126_2203'),
    ]

    operations = [
        migrations.CreateModel(
            name='rast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('surname', models.CharField(max_length=250)),
                ('desс', models.TextField(blank=True, verbose_name='информация об учинике')),
                ('rt', models.CharField(max_length=250, verbose_name='место в рейтинге')),
            ],
            options={
                'verbose_name': 'ученик',
                'verbose_name_plural': 'ученики',
            },
        ),
    ]
