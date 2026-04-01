from django.db import models
from subjects.models import Subject  
from django.conf import settings

class Exam(models.Model):
    TYPE_CHOICES = [
        ('CC', 'Contrôle Continu'),
        ('EF', 'Examen Final'),
    ]
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name="Matière")
    exam_date = models.DateTimeField(verbose_name="Date et Heure")
    classroom = models.CharField(max_length=50, verbose_name="Salle")
    exam_type = models.CharField(max_length=2, choices=TYPE_CHOICES, default='CC')

    def __str__(self):
        return f"{self.subject.subject_name} - {self.exam_type}"

class Grade(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='grades')
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, limit_choices_to={'groups__name': "Student"})
    score = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Note")

    class Meta:
        unique_together = ('exam', 'student')