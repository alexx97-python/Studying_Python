from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class Spare (models.Model):
    name = models.CharField(max_length=40)


class Machine (models.Model):
    name = models.CharField(max_length=30)
    spares = models.ManyToManyField(Spare, through='Kit',
                                    through_fields=('machine', 'spare'))


class Kit(models.Model):
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    spare = models.ForeignKey(Spare, on_delete=models.CASCADE)
    count = models.IntegerField()


class Note(models.Model):
    content = models.TextField()
    content_type = models.ForeignKey(ContentType,
                                     on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey(ct_field='content_type',
                                       fk_field='object_id')

