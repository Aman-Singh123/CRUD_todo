# Generated by Django 4.1.7 on 2023-02-16 10:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0006_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo_item',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 2, 16, 15, 37, 58, 287189), editable=False),
        ),
    ]
