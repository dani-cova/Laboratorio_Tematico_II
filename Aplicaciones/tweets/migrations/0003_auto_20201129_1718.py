# Generated by Django 2.2.3 on 2020-11-29 23:18

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0002_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='cotenido',
            field=ckeditor.fields.RichTextField(),
        ),
    ]