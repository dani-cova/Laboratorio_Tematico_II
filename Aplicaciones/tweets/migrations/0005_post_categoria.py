# Generated by Django 2.2.3 on 2020-11-30 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0004_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='categoria',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.CASCADE, to='tweets.Categoria'),
            preserve_default=False,
        ),
    ]
