from django import forms
from .models import Grade
from .models import Exam

class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ['student', 'score']
        widgets = {
            # On ajoute des classes CSS 'form-control' pour que ça soit joli avec Bootstrap
            'student': forms.Select(attrs={'class': 'form-control'}),
            'score': forms.NumberInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Note sur 20',
                'step': '0.25', 
                'min': '0', 
                'max': '20'
            }),
        }
        labels = {
            'student': 'Nom de l\'étudiant',
            'score': 'Note obtenue',
        }
       
class ExamForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = ['subject', 'exam_date', 'classroom', 'exam_type']
        widgets = {
            'exam_date': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'subject': forms.Select(attrs={'class': 'form-control'}),
            'classroom': forms.TextInput(attrs={'class': 'form-control'}),
            'exam_type': forms.Select(attrs={'class': 'form-control'}),
        }