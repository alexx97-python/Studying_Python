# Generated by Django 3.0.3 on 2020-07-22 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_task_progress'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='deadline',
        ),
        migrations.AlterField(
            model_name='task',
            name='completed',
            field=models.BooleanField(default=False, verbose_name='Completed'),
        ),
        migrations.AlterField(
            model_name='task',
            name='progress',
            field=models.CharField(choices=[(None, 'Chose you progress'), ('s', 'Started working'), ('c', 'Currently working'), ('f', 'Almost finished')], default=None, max_length=1, verbose_name='Progress'),
        ),
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Task'),
        ),
    ]
