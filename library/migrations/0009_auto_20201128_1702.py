# Generated by Django 3.1.3 on 2020-11-28 12:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0008_auto_20201126_1542'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='received',
            name='returned_at',
            field=models.DateField(default=datetime.datetime(2020, 12, 8, 17, 2, 25, 151783)),
        ),
    ]
