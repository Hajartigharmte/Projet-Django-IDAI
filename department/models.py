from django.db import models
from teachers.models import Teacher


class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    head = models.ForeignKey(
        Teacher,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
       
        related_name='headed_departments'
    )

    teachers = models.ManyToManyField(
        Teacher,
        related_name='departments',
        blank=True
    )

    def __str__(self):
        return self.name