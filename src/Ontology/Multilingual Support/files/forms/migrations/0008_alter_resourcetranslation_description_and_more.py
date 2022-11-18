# Generated by Django 4.1.3 on 2022-11-12 18:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0007_personname_name_alter_resourcetranslation_pub_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resourcetranslation',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='resourcetranslation',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 12, 18, 18, 19, 49810, tzinfo=datetime.timezone.utc), verbose_name='date published'),
        ),
    ]
