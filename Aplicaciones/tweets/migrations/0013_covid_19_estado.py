# Generated by Django 2.2.3 on 2020-12-01 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0012_covid_19_cat'),
    ]

    operations = [
        migrations.AddField(
            model_name='covid_19',
            name='estado',
            field=models.BooleanField(default=True, verbose_name='public/No-public'),
        ),
    ]
