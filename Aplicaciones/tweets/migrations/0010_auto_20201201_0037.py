# Generated by Django 2.2.3 on 2020-12-01 06:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0009_covid_19_categoria'),
    ]

    operations = [
        migrations.RenameField(
            model_name='covid_19',
            old_name='categoria',
            new_name='cat',
        ),
    ]
