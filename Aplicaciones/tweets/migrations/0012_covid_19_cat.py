# Generated by Django 2.2.3 on 2020-12-01 06:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0011_remove_covid_19_cat'),
    ]

    operations = [
        migrations.AddField(
            model_name='covid_19',
            name='cat',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tweets.Categoria'),
            preserve_default=False,
        ),
    ]