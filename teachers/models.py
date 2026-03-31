from django.db import models
from home_auth.models import CustomUser 

class Teacher(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    gender = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    qualification = models.CharField(max_length=200)
    experience = models.IntegerField()
    address = models.TextField()

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"