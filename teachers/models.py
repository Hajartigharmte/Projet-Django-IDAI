from django.db import models
from home_auth.models import CustomUser

class Teacher(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True)
    teacher_id = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    
   
    photo = models.ImageField(upload_to='teacher_photos/', null=True, blank=True)
    city = models.CharField(max_length=100, verbose_name="Ville")
    diploma = models.CharField(max_length=200, verbose_name="Diplôme")
    parcours = models.TextField(null=True, blank=True, verbose_name="Parcours Professionnel")
    
  
    qualification = models.CharField(max_length=200)
    experience = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=20)
    
   
    def __str__(self):
        return f"{self.first_name} {self.last_name}"