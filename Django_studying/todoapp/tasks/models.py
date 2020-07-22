from django.db import models
import datetime


class Task(models.Model):
    PROGRESS = (
        (None, 'Chose you progress'),
        ('s', 'Started working'),
        ('c', 'Currently working'),
        ('f', 'Almost finished'),
    )

    title = models.CharField(max_length=200, verbose_name='Task')
    progress = models.CharField(max_length=1, default=None, choices=PROGRESS, verbose_name='Progress')
    completed = models.BooleanField(default=False, verbose_name='Completed')

    def __str__(self):
        return self.title

