from django.db import models
from teachers.models import Teacher
from department.models import Department
from subjects.models import Subject



class TimeTable(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='timetables')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=10, default='Mon', choices=[
        ('Mon','Monday'),('Tue','Tuesday'),('Wed','Wednesday'),
        ('Thu','Thursday'),('Fri','Friday')
    ])
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.department.name} - {self.subject_name.name} ({self.day_of_week})"


class Holiday(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} ({self.start_date} - {self.end_date})"