# Generated by Django 4.1.5 on 2023-01-19 18:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ToDoTask', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='task_endtime',
        ),
    ]
