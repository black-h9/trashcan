# Generated by Django 3.0.3 on 2020-02-29 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trashcan', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ashbin',
            name='modified_time',
        ),
        migrations.AlterField(
            model_name='ashbin',
            name='created_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
