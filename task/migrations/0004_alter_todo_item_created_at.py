# Generated by Django 4.1.7 on 2023-02-16 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0003_alter_todo_item_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo_item',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
