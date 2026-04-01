from django.db import models
from teachers.models import Teacher
from department.models import Department

class Subject(models.Model):
    subject_name = models.CharField(max_length=255)
    
    # Relation avec le professeur (déjà terminé)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='subjects')
    
    
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    
    # Dates de création (toujours utile pour un projet pro)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject_name